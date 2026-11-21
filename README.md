# Base Overnight.fi USD+ & ETS Delta-Neutral Rebalance Arbitrage Radar

[![Python Unit Tests](https://img.shields.io/badge/Unit%20Tests-5%2F5%20Passing-brightgreen.svg)]()
[![Base L2](https://img.shields.io/badge/Network-Base%20Mainnet-blue.svg)]()
[![Overnight.fi](https://img.shields.io/badge/Protocol-Overnight.fi%20USD%2B-emerald.svg)]()
[![Live Visualizer](https://img.shields.io/badge/Live%20Dashboard-GitHub%20Pages-blue.svg)](https://someoneee918.github.io/base-overnight-rebalance-radar/)

Commercial DeFi intelligence engine analyzing:
1. **USD+ Collateral Reserve Backing Ratio & De-peg Boundaries on Base L2**
2. **Exchange-Traded Strategies (ETS) Delta-Neutral Basis Drift & Funding Carry Yield**
3. **Secondary DEX (Aerodrome / Slipstream) Discount Mint-and-Redeem Basis Arbitrage**
4. **Keeper Rebalance Auction Bounty Economics on Base**
5. **Non-Custodial VIP Sentinel License Generator (5 Base USDC / 0.03 SOL)**

---

## Live Interactive Dashboard
🌐 **Access the live dashboard at**: [https://someoneee918.github.io/base-overnight-rebalance-radar/](https://someoneee918.github.io/base-overnight-rebalance-radar/)

---

## Key Mathematical Models

### 1. DEX Discount Basis Arbitrage
When USD+ trades below $1.00 on secondary DEXes (Aerodrome, Slipstream), an arbitrageur purchases USD+ and redeems it canonically for USDC:
$$T_{bought} = \frac{C}{P_{market}}$$
$$\text{Proceeds} = T_{bought} \times (1 - \text{Fee}_{redeem})$$
$$\Pi_{net} = \text{Proceeds} - C - \text{Gas}_{Base}$$

For $C = \$10,000$, $P_{market} = \$0.9940$ (60 bps discount), and $\text{Fee}_{redeem} = 0.20\%$:
- Tokens Bought: $10,060.36\text{ USD+}$
- Redemption Proceeds: $\$10,040.24\text{ USDC}$
- Base Gas: $\$0.03$
- **Net Profit: $+\$40.21\text{ USD}$ ($+0.402\%$ Instant ROI).**

### 2. ETS Delta-Neutral Hedging Basis Drift
$$\Delta_{net} = \text{Spot}_{LP} - \text{Short}_{hedge}$$
$$\text{Yield}_{daily} = \text{Short}_{hedge} \times R_{funding} + \Delta_{drift}$$

When delta is properly balanced ($\Delta_{net} \approx 0$), basis drift is 0.00% and the strategy captures clean annualized funding carry ($~14.6\%\text{ APR}$).

---

## Unit Test Verification
Run the 5/5 unit test suite:
```bash
python3 -m unittest test_overnight_rebalance_radar.py
```

---

## Non-Custodial VIP Sentinel License
Unlock automated ethers.js flash swap & canonical redeem keeper scripts by sending **5 Base USDC** or **0.03 SOL** to our verified receive addresses:
- **Base EVM:** `0xF0E0D361bBE899F3089f0a968506eF2B97693c01`
- **Solana:** `DW2MdHEq3qZ6nh9b5YFUoaPnBuuxC8Gz2785kwbbjSAM`
