---
title: Investment and Portfolio - Types of Stock Positions
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Investment Portfolio]
tags: [note]
math: true
date: 2025-03-02 18:06:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
# Active Stock Selection II

## Technical Analysis vs. Momentum
* the most-used signal (by far) in technical analysis is a **stock’s price trend**
* **Buy stocks trending up** and **sell or short stocks trending down**
* Trend is closely related to price momentum
  * A sort based on momentum will usually identify up-trending long candidates and down-trending short candidates
    * Can confirm this with a Bloomberg screen
  * Momentum emphasizes return sorts based on the past 6 to 12 months, whereas technical analysis trend indicators are more ambiguous on timing 该策略与趋势相关，但侧重于股票价格在中期（6到12个月）内的移动。

## Short-term Reversals

* On average, stock returns over one-week to one-month periods reverse 平均而言，表现良好的股票在一周到一个月后往往表现不佳，反之亦然。
  * Past winners underperfor
  * Past losers outperform
* Opposite of momentum effect
* Sort based on much more recent returns

## ST Reversal Performance

![Graph](STreversal.png)

> ## Question

> 1. **Question 1: Based on the VW returns, what is the historical return of a long-only reversal strategy that invests in 20% of the stock universe and with a leverage ratio of 1?**

> - Answer: From previous slides, we saw historical data indicating the performance of "losers" and "winners" under equal weight (EW) and value weight (VW) strategies. Specifically, under the VW (Value Weighted) strategy, the worst-performing stocks (the lowest 20%) have an average return of 18.64%. Therefore, if employing a long-only reversal strategy that invests only in the worst-performing 20% of the stock universe, the historical return, based on past data, would be 18.64%. Given that the leverage ratio is 1, it means there's no borrowing of additional funds for investment, so the return doesn't require any adjustments for leverage.
> - 从前面的幻灯片中，我们看到历史数据显示"输家"和"赢家"在等权重和价值权重中的表现。特别地，VW（价值权重）策略下，最差表现的股票（排名最低的20%）的平均回报率为18.64%。因此，如果采用长期只买入策略，并且只投资股票宇宙中表现最差的20%，那么根据历史数据，这种策略的历史收益为18.64%。此处假设杠杆比率为1，意味着没有借贷额外资金进行投资，所以收益率不需要进行任何调整。

> 2. **Question 2: Based on a long-only short-term reversals portfolio, which three stocks would you buy?**

> - Answer: From a short-term reversal standpoint, the ideal choices would be those stocks that have recently performed the worst but are poised for a potential reversal. Since specific historical performance data for the stocks isn't provided in the screenshots, the usual approach would be to analyze recent return rates of these stocks and choose the three with the lowest recent returns. Additional financial metrics and market conditions could also be considered for a more comprehensive decision-making process.
> - 从短期反转的角度出发，理想的选择是挑选那些最近表现最差，但有可能出现反转的股票。由于具体的股票历史表现数据在截图中没有给出，通常的做法是分析这些股票最近的回报率，并选择那些最近回报率最低的三只股票。此外，还可以考虑其他财务指标和市场情况来做出更全面的决策。

> 3. **Question 3: Based on the data in MonthlyReturns.xlsx, for a market neutral short-term reversals portfolio that consists of 4 stocks total, what are the holdings as of January 2024?**

> - Answer: typically, a market-neutral short-term reversals portfolio would select the two worst and the two best-performing stocks. The worst-performing stocks are chosen for a long position (buying), and the best-performing stocks might be chosen for short selling.
> - 通常情况下，市场中性短期反转投资组合会选择两只表现最差和两只表现最好的股票。选择最差的股票是为了长期持有（买入），而选择最好的股票则可能是为了卖空。

## Reversals

- **Caveats**
  - Skewed toward small market cap stocks with low price-to-book ratios 市场偏差: 指出短期反转策略往往偏向于小市值股票，这些股票的账面价值比较低。
  - High turnover 高交易量: 短期反转策略通常涉及高交易量，因为需要频繁买卖股票以利用价格的短期波动。
  - High transaction costs 高交易成本: 高交易量导致交易成本增加，这可能会侵蚀投资回报。


## Long-term Reversals
- **Also evidence of reversal when sorting based on three- to five-year returns** 
  - Long the losers (and potentially short the winners)
  - 提议长期持有表现不佳的股票（long the losers），并可能做空表现良好的股票（short the winners）。
- ![Graph](LTreversal.png)
  - 显示了等权重（EW）和价值权重（VW）下的股票表现。在等权重策略中，表现最差的股票组的回报高达29.13%，而在价值权重策略中，这一组的回报为18.03%。此外，赢家组的回报显著低于输家组。


## Question
1. **Question: Would a long-term reversal strategy be more likely to long Apple Computer than to short Apple Computer?**
长期反转策略是否更可能长期持有苹果电脑而不是做空苹果电脑？
- Answer: False
- Explanation: 
  - A long-term reversal strategy typically focuses on selecting stocks that have underperformed over an extended period, with the expectation that they will eventually rebound. Apple Inc., known for its sustained positive performance and consistent growth in stock value, generally does not fit the criteria for a long position under this strategy.
  长期反转策略通常是基于股票历史表现的极端情况，选择长期表现不佳的股票买入，而对于长期表现优异的股票则可能选择做空。苹果电脑（Apple Inc.）作为一个长期表现优秀的公司，其股票价格多年来一直呈上升趋势，这使得它通常不符合长期反转策略中选择买入的条件。
  - The rationale behind a long-term reversal strategy is to invest in stocks that the market has undervalued and that have shown poor returns over several years, anticipating a turnaround. Conversely, stocks like Apple, which have demonstrated long-term success and significant market value appreciation, are often considered for short positions if the strategy predicts an eventual pullback. Therefore, in the context of a long-term reversal strategy, it would be more likely to consider shorting Apple rather than taking a long position, especially when the stock is perceived to be overvalued.
  长期反转策略着眼于那些过去几年表现不佳，被市场低估的股票，预期这些股票将会反弹。相反，对于长期表现良好，市值持续增长的公司，如苹果，使用长期反转策略更可能考虑做空，尤其是在其股票价格高估时。因此，如果考虑长期反转策略，对于苹果电脑而言，更可能是选择做空而不是买入。


## Additional Quant Signals
### **Investment**
指公司在资本支出（capex）和研发（R&D）上的支出。这些被考虑在内以评估公司的成长潜力。
  - Market tends to **overvalue companies that invest a lot** (e.g., on cap ex, R&D)市场估值：市场往往会高估那些在资本支出和研发上投资较多的公司，期望这些投资将产生未来增长。
    - These companies subsequently disappoint, relative to market expectations 然而，这些公司往往未能满足这些高期望。
  - High investment correlates with relatively low future returns
    - 高投资水平与较低的未来回报相关。这可能是因为更多的资本被以较低的回报率投入，或因为未能满足乐观的市场预期。
  - ![Graph](investment6.png)
    - 该图表按投资水平（从低到高）显示回报，采用等权重（EW）和价值权重（VW）两种不同的加权方案。数据显示，投资较少的公司往往产生更高的回报，表明过度投资可能是未来表现不佳的一个警告信号。
### **Accruals**
应计项目：代表收益中的非现金部分，如应收账款的变动。
  - Accruals relate to the non-cash component of earnings
    - 应计项目是指在企业收益中的非现金部分。这包括由企业运营产生的现金流（如销售收入）以及非现金组成部分（如应收账款的变动）。这些非现金项目影响了公司报告的净收益，但它们不涉及实际的现金交换。
    - Earnings reflect cash flows generated by the business (e.g., sales revenue) plus non-cash components like change in receivables
      - 当公司展示高应计项目时，可能表明公司在财务报表中采用了一定的会计处理方式，以显示较高的公认会计原则（GAAP）收益，但这些收益可能并不代表公司的真实经营实力。
    - If a company shows high accruals, it can suggest manipulation in the financial statements to show relatively high GAAP earnings that is not representative of the company’s genuine business strength 高应计项目可以暗示收益操纵，人为夸大报告的利润，因此不真实反映现金流。
  - High accruals correlates with relatively low future returns 高应计水平通常与较低的未来股票回报相关，因为这些收益可能不可持续，或不反映实际的财务健康。
  - ![Graph](accruals.png)
    - 回报按应计水平组织。趋势显示，应计项目较低的公司表现更好，支持高应计项目（可能掩盖真实经济表现）在市场上被负面看待的观点。
  - 应计项目的定义
    - 应计项目是指在企业收益中的非现金部分。这包括由企业运营产生的现金流（如销售收入）以及非现金组成部分（如应收账款的变动）。这些非现金项目影响了公司报告的净收益，但它们不涉及实际的现金交换。
  - 应计项目的含义与影响
    - 当公司展示高应计项目时，可能表明公司在财务报表中采用了一定的会计处理方式，以显示较高的公认会计原则（GAAP）收益，但这些收益可能并不代表公司的真实经营实力。
    - 高应计项目可能涉及收益管理或操纵，企图通过调整非现金账目项目来美化财务报告。例如，通过推迟确认费用或提前确认收入，公司可以临时提高其收益。
  - 应计项目与未来回报的关联
    - 研究发现高应计项目与较低的未来回报相关联。这是因为高应计项目可能掩盖了公司面临的财务问题或业绩不佳，而当这些问题最终显现时，可能会对股票价格产生负面影响。
    - 投资者和分析师经常会审视应计项目的水平，作为评估公司财务透明度和质量的一个重要指标。通常情况下，较低的应计项目水平被视为公司财务健康和持续盈利能力的正面信号。

### **Market Beta**
市场Beta值：衡量股票相对于整体市场的波动性
  - As theory predicts, stocks with high beta have higher returns, on average, than stocks with low beta
    - 根据金融理论，高Beta值的股票预期有更高的回报，因为风险更高。然而，它们常常没有产生更高的风险调整后回报（Alpha）
  - However, on a risk-adjusted basis (e.g., based on alpha), stocks with low beta outperform
    - Low beta stocks have higher alpha, on average, compared to high beta stocks
    - 虽然波动性较低，但低Beta股票在风险调整基础上往往表现更好，表明它们可能提供更好的风险回报比。
### **Net Share Issuance**
净股票发行：观察公司发行的股票数量，这可以表明内部人士对股票估值的看法。
  - Companies issue stock when they perceive their stock price to be high relative to fundamentals
  - High net issuance is associated with relatively low future performance
  - 公司通常在认为其股票相对于基本面高估时发行更多股票，这是筹集资本的好时机。高净发行量与较低的未来表现相关，可能由于稀释和可能是内部人士对过高估值的信号。
  - ![Graph](Net Share Issuance.png)
    - 该图表根据净股票发行量的不同水平列出回报。结果显示，净发行量较低的公司表现更好，再次强调高发行量可能是一个负面信号。


## Other Quant Signal
- **Other quant signals have been documented, but performance is not as robust**
  - Operating profitability
    - 营运盈利能力：衡量公司经营其核心业务的盈利能力。
  - Daily return variance
    - 日收益率方差：表示股票价格的日波动性。
  - Daily residual variance
    - 日剩余方差：衡量股票回报中未被市场运动解释的方差部分。

