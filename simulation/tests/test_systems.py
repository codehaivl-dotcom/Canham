import copy
import unittest
from simulation.systems import (Economy, Site, Treatment, RewardLedger, PvpWorld,
                                Claim, FIXTURE, fit_cargo, run_all, Pity)


def economy(**kwargs):
    stock=copy.deepcopy(FIXTURE["economy"]["start"]);pop=stock.pop("population")
    return Economy(stock,population=pop,**kwargs)


class OfflineTests(unittest.TestCase):
    def test_partition_across_battery_storage_treatment_and_collection(self):
        a=economy(generator_integrity=0,battery=1,sites=[Site()],treatment=Treatment(20,3))
        a.stock["food"]=250
        b=copy.deepcopy(a);a.advance_offline(28800)
        for now in (17,59,500,3600,7201,18000,28800):b.advance_offline(now)
        for r in a.stock:self.assertAlmostEqual(a.stock[r],b.stock[r])
        self.assertAlmostEqual(a.battery,b.battery)
        self.assertAlmostEqual(a.treatment.progress,b.treatment.progress)
        self.assertEqual(a.sites[0].collections,b.sites[0].collections)

    def test_no_skipped_time_debt_or_reconnect_mint(self):
        a=economy(sites=[Site()]);a.advance_offline(57600)
        before=copy.deepcopy(a.stock);self.assertEqual(a.advance_offline(57600),0)
        self.assertEqual(a.stock,before);self.assertAlmostEqual(a.sites[0].produced["scrap"],144)

    def test_full_storage_does_not_stop_consumption_or_refill(self):
        a=economy();a.stock["food"]=250;a.production["food"]=2
        a.advance(3600);self.assertAlmostEqual(a.stock["food"],246)
        b=economy();b.stock["food"]=250;b.advance(3600)
        self.assertAlmostEqual(b.stock["food"],250)

    def test_empty_survival_stays_recoverable(self):
        a=economy(generator_integrity=0);a.stock.update(food=0,water=0,supply=0)
        a.advance(28800);self.assertEqual(a.stock["food"],0);self.assertTrue(a.emergency)
        self.assertTrue(a.restart());a.advance(300);self.assertEqual(a.generation,24)
        a.advance(3600);self.assertGreater(a.stock["water"],0)
        self.assertFalse(a.restart())

    def test_emergency_hunger_reset_at_ten_minutes_no_resource_mint(self):
        a=economy(generator_integrity=0);a.stock.update(food=0,water=0)
        a.hunger={"food":14400,"water":14400}
        a.advance(599);self.assertEqual(a.hunger["water"],14400)
        a.advance(1);self.assertEqual(a.hunger["water"],0)
        self.assertEqual(a.stock["food"],0)

    def test_treatment_debit_once_pause_and_resume(self):
        stock={"chemicals":3};t=Treatment(20,3,1.2)
        t.advance(500,stock);t.advance(999,stock,powered=False);t.advance(500,stock)
        self.assertTrue(t.complete);self.assertEqual(stock["chemicals"],0)
        t.advance(1000,stock);self.assertEqual(stock["chemicals"],0)


class TransactionTests(unittest.TestCase):
    def test_failed_pickup_retry_then_replay(self):
        ledger=RewardLedger();loot={"unique":{"scrap":100}}
        ledger.settle("f",False,loot,"node",knowledge=["crawler"])
        self.assertFalse(ledger.banked);self.assertFalse(ledger.first_clears)
        ledger.settle("ok",True,loot,"node")
        for _ in range(10):ledger.settle("ok",True,loot,"node")
        ledger.settle("new-run",True,loot,"node")
        self.assertEqual(ledger.inventory["scrap"],100)
        self.assertEqual(ledger.knowledge,{"crawler"})

    def test_seeded_cache_and_partial_inbox_claim(self):
        ledger=RewardLedger(8);cards=ledger.cache("x",{"a":1,"b":2})
        self.assertEqual(cards,ledger.cache("x",{"different":99}))
        inbox={"scrap":50};self.assertEqual(ledger.claim("one","scrap",20,inbox),20)
        self.assertEqual(ledger.claim("one","scrap",20,inbox),20)
        self.assertEqual(inbox["scrap"],30)
        ledger.claim("two","scrap",999,inbox);self.assertEqual(ledger.inventory["scrap"],50)

    def test_pity_only_success_and_once_per_event(self):
        p=Pity()
        for i in range(10):self.assertEqual(p.settle("failed"+str(i),"std",False,False),0)
        self.assertEqual(p.settle("one","std",True,False),0)
        self.assertEqual(p.settle("two","std",True,False),0)
        self.assertEqual(p.settle("three","std",True,False),1)
        self.assertEqual(p.settle("three","std",True,False),1)
        self.assertEqual(p.dry["std"],0)
        p.settle("four","std",True,False);p.settle("natural","std",True,True)
        self.assertEqual(p.dry["std"],0)

    def test_claim_refunds_once_and_success_does_not_refund(self):
        stock={"scrap":100,"components":20,"supply":30,"claim_beacon":2};initial=stock.copy();c=Claim(stock)
        c.begin("fail",6);c.settle("fail",False);c.settle("fail",False);self.assertEqual(stock,initial)
        c.begin("ok",6);c.settle("ok",True);c.settle("ok",False)
        self.assertEqual(stock["claim_beacon"],1);self.assertEqual(stock["scrap"],75)
        with self.assertRaises(ValueError):c.begin("contested",6,private=False,opted=True)

    def test_cargo_never_splits_gear_or_exceeds_capacity(self):
        result=fit_cargo([("heavy",3),("body",2),("food",1)],4)
        self.assertEqual(result["kept"],["heavy","food"]);self.assertEqual(result["used"],4)


class PvpTests(unittest.TestCase):
    def world(self):
        w=PvpWorld();w.add("a");w.add("b");w.add("d");return w

    def test_concurrent_silo_site_lock_and_failed_extraction(self):
        w=self.world();w.begin("r","a","d",0)
        with self.assertRaises(ValueError):w.begin("s","b","d",0,asset="site",site_stock={"scrap":144},output={"scrap":18})
        result=w.settle("r",100,False,{"scrap":999})
        self.assertEqual(result["stolen"]["scrap"],0)
        self.assertEqual(w.accounts["d"].stock["scrap"],1000)
        self.assertFalse(w.accounts["d"].reserved)

    def test_cap_reserve_commit_replay_rolling_boundary(self):
        w=self.world();d=w.accounts["d"];d.losses=[(-82800,{"scrap":40})]
        self.assertEqual(w.begin("r","a","d",0)["exposure"]["scrap"],20)
        w.settle("r",100,True,{"scrap":999});w.settle("r",100,True,{"scrap":999})
        self.assertEqual(d.stock["scrap"],980)
        self.assertEqual(w.remaining(d,"scrap",3599),0)
        self.assertEqual(w.remaining(d,"scrap",3600),40)

    def test_spending_cannot_use_theft_reserved_stock(self):
        w=self.world();w.begin("r","a","d",0)
        with self.assertRaises(ValueError):w.spend("d",{"scrap":950})
        w.spend("d",{"scrap":900});w.settle("r",10,True,{"scrap":60})
        self.assertEqual(w.accounts["d"].stock["scrap"],40)

    def test_expiry_not_extended_by_reconnect(self):
        w=self.world();w.begin("r","a","d",0);w.expire(899)
        self.assertEqual(w.accounts["d"].active_incoming,"r")
        w.expire(900);self.assertIsNone(w.accounts["d"].active_incoming)
        self.assertFalse(w.raids["r"]["result"]["successful"])

    def test_timeout_at_cleared_exit_and_shield(self):
        w=self.world();w.begin("r","a","d",0)
        w.settle("r",900,False,{"scrap":10},at_exit=True)
        self.assertEqual(w.accounts["d"].stock["scrap"],990)
        with self.assertRaises(ValueError):w.begin("s","b","d",901)

    def test_private_optin_ccl_disjoint_and_charge_regen(self):
        for kwargs in ({"private":True},{"roster_overlap":True}):
            w=self.world()
            with self.assertRaises(ValueError):w.begin("r","a","d",0,**kwargs)
            self.assertEqual(w.accounts["a"].charges,3)
        for changes in ({"ccl":7},{"opted":False}):
            w=self.world()
            for k,v in changes.items():setattr(w.accounts["d"],k,v)
            with self.assertRaises(ValueError):w.begin("r","a","d",0)
        w=self.world();w.begin("r","a","d",0);self.assertEqual(w.accounts["a"].charges,2)
        w.regenerate(w.accounts["a"],14400);self.assertEqual(w.accounts["a"].charges,3)

    def test_site_stolen_stock_does_not_debit_silo(self):
        w=self.world();buffer={"scrap":144,"alien_material":999}
        r=w.begin("r","a","d",0,asset="site",site_stock=buffer,output={"scrap":18})
        self.assertEqual(r["exposure"]["scrap"],14)
        w.settle("r",100,True,{"scrap":14,"alien_material":999})
        self.assertEqual(buffer["scrap"],130);self.assertEqual(buffer["alien_material"],999)
        self.assertEqual(w.accounts["d"].stock["scrap"],1000)


class BatchTests(unittest.TestCase):
    def test_all_scenarios_execute_and_are_deterministic(self):
        a=run_all(8);b=run_all(8)
        self.assertEqual(a,b);self.assertEqual(a["summary"]["failed"],0,a["checks"])


if __name__=="__main__":unittest.main()
