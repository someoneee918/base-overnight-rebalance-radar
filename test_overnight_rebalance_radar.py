#!/usr/bin/env python3
"""
Unit Tests for Base Overnight.fi USD+ & ETS Rebalance Arbitrage Radar
"""

import unittest
from overnight_rebalance_radar import (
    calculate_usd_plus_collateral_health,
    calculate_ets_delta_neutral_drift,
    calculate_dex_discount_basis_arbitrage,
    calculate_keeper_rebalance_bounty,
    generate_vip_sentinel_script,
    BASE_RECEIVE_ADDRESS,
    SOL_RECEIVE_ADDRESS
)

class TestOvernightRebalanceRadar(unittest.TestCase):

    def test_usd_plus_collateral_health(self):
        # Case 1: Over-collateralized pristine state ($10.05M reserves backing $10M USD+)
        pristine = calculate_usd_plus_collateral_health(10050000.0, 10000000.0)
        self.assertTrue(pristine["is_fully_backed"])
        self.assertEqual(pristine["status"], "PRISTINE")
        self.assertAlmostEqual(pristine["backing_ratio"], 1.005, places=4)
        self.assertEqual(pristine["reserve_surplus_usd"], 50000.0)
        
        # Case 2: Under-collateralized state ($9.95M reserves backing $10M USD+)
        deficit = calculate_usd_plus_collateral_health(9950000.0, 10000000.0)
        self.assertFalse(deficit["is_fully_backed"])
        self.assertEqual(deficit["status"], "UNDER_COLLATERALIZED_RISK")
        self.assertAlmostEqual(deficit["backing_ratio"], 0.995, places=4)

    def test_ets_delta_neutral_drift(self):
        # $50,000 spot LP, $50,000 short hedge (zero initial net delta)
        # Spot drops 5% (-0.05), short gains 5% (+0.05) -> net drift = 0.
        # Daily funding rate 0.04% (14.6% APR)
        ets = calculate_ets_delta_neutral_drift(
            spot_exposure_usd=50000.0,
            short_hedge_usd=50000.0,
            spot_price_delta_pct=-0.05,
            funding_rate_daily_pct=0.0004
        )
        self.assertEqual(ets["net_delta_usd"], 0.0)
        self.assertEqual(ets["net_drift_usd"], 0.0)
        self.assertEqual(ets["daily_funding_earned_usd"], 20.0)
        self.assertEqual(ets["annualized_funding_apr_pct"], 14.6)
        self.assertEqual(ets["net_strategy_daily_usd"], 20.0)

    def test_dex_discount_basis_arbitrage(self):
        # USD+ trading at $0.994 on Aerodrome (60 bps discount)
        # Canonical redeem fee: 0.2% (20 bps)
        # Capital: $10,000 -> buys 10,000 / 0.994 = 10,060.36 USD+
        # Canonical redeem at 0.998 = $10,040.24 USDC.
        # Gross profit: $40.24. Base gas: $0.03 -> Net profit: $40.21.
        arb = calculate_dex_discount_basis_arbitrage(
            market_price_usd_plus=0.994,
            redeem_fee_pct=0.002,
            capital_usd=10000.0,
            base_gas_usd=0.03
        )
        self.assertTrue(arb["is_profitable"])
        self.assertEqual(arb["discount_bps"], 60.0)
        self.assertAlmostEqual(arb["gross_profit_usd"], 40.2414, places=2)
        self.assertAlmostEqual(arb["net_profit_usd"], 40.2114, places=2)
        self.assertAlmostEqual(arb["roi_pct"], 0.4021, places=2)

    def test_keeper_rebalance_bounty(self):
        # $25,000 pool imbalance, 10 bps bounty = $25.00 gross. Base gas $0.04 -> $24.96 net.
        keeper = calculate_keeper_rebalance_bounty(
            pool_imbalance_usd=25000.0,
            bounty_bps=10.0,
            base_gas_usd=0.04
        )
        self.assertEqual(keeper["gross_bounty_usd"], 25.0)
        self.assertEqual(keeper["net_bounty_usd"], 24.96)
        self.assertTrue(keeper["is_executable"])

    def test_generate_vip_script(self):
        script = generate_vip_sentinel_script(BASE_RECEIVE_ADDRESS, SOL_RECEIVE_ADDRESS)
        self.assertIn("Overnight Radar", script)
        self.assertIn(BASE_RECEIVE_ADDRESS, script)
        self.assertIn(SOL_RECEIVE_ADDRESS, script)
        self.assertIn("Exchange.redeem", script)

if __name__ == "__main__":
    unittest.main()
