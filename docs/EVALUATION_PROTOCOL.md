# Continuous research protocol — decision gates

## Immutable experiment record
Each hypothesis must record:
- experiment ID; idea and competing null hypothesis
- exact code/model revision and prompt/skill revisions
- dataset origin, license, permitted use, data checksum, date range and timezone
- market, capital, exposure, execution timing, fees, spreads, slippage and order handling
- training / validation / held-out partitions frozen BEFORE test
- primary economic objective, auxiliary risk metrics, confidence calibration and failure threshold
- every trial and parameter sweep, runtime, tool invocations, compute and budget
- results including non-finite/failed runs, missed opportunities and avoided losses
- independent evaluation signature, adoption/rollback reasoning and versioned memory changes

## Comparison gates
G0 pipeline runs offline with 100% synthetic origin and deterministic replay.
G1 real historical comparison only after dataset license and legal use are verified.
G2 all controls have identical comparable assumptions; 100%-invested passive case is a SEPARATE benchmark, never averaged with 10%-capped controls.
G3 no lookahead, test contamination or accidental training on held-out observations.
G4 out-of-sample net returns, realized round trips, mark-to-market open positions, max drawdown, volatility, tail risks, fees, missed gains and avoided losses.
G5 robustness under three additional preregistered single-factor volatility/market-regime challenges.
G6 reproduce champion on fresh untouched market conditions; calculate uncertainty and multiple testing cost.
G7 forward-only paper/live-demo for an observation period set by the risk committee.
G8 separate manual founder approval for broker credentials and any live order handling. Risk governor has veto and manual kill switch.

## Stable live return claim
Never use the wording "stable 5%" without a precisely fixed timeframe and a track record. Five percent is a target to challenge, not a deployment gate that forces the model to take risk. If expected net edge is negative, the correct action may be no trade.

## Difference between teaching and learning
Skills teach engineers procedures. Genesis only learns when model/memory adaptation is implemented, tested and shown to outperform independent baselines. Store true/false hypotheses with provenance and confidence decay, and re-evaluate after distribution shifts.
