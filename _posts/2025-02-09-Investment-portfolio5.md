---
title: Investment and Portfolio - Active Stock Selection I
description: Course review for Spring course in MAF program at Emory.
categories: [Finance,Course]
tags: [note]
math: true
date: 2025-02-09   02:14:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
## **Active Stock Selection**主动选股

- We focus on several strategies shown to **outperform**, on average, across the past ~100 years, including:过去 约 100 年 来，以下几种投资策略被证明能带来 超额回报
  - **Value** --> 购买被低估的股票，即当前股价低于其内在价值的股票
  - **Growth** --> 关注那些 未来有高增长潜力 的公司，通常具备快速增长的收入或利润
  - **Momentum** --> 选择最近表现 较好的股票，认为趋势会持续
  - **Reversals** --> 关注那些 近期涨幅过高或跌幅过大 的股票，押注它们将回归均值
- Understanding and following these strategies gives an investor an **"edge"**, a performance advantage relative to the average investor.
  - 通过理解并运用这些策略，投资者可以获得比 普通市场参与者更高的收益，从而实现 超额回报（Alpha）
- **Cyclical nature to strategies**
  - Sometimes they work great for long time periods, and other times they don’t work well (but they work well on average across time). 没有一种策略可以在所有市场环境下都有效

## **Alternative Measures of Value**

- Stock price divided by a proxy for its worth, e.g.,
  - **Price / Earnings** --> P/E 反映了投资者愿意为每 1 美元的收益支付多少倍的价格
    - Forward or trailing earnings
    - 前瞻 P/E (**Forward P/E**): 以未来预测的收益计算
    - 滞后 P/E (**Trailing P/E**): 以过去 12 个月的收益计算
    - High P/E: 表明投资者对公司未来增长预期较高，可能代表成长型公司（如科技股）
    - Low P/E：可能表示市场对公司增长缺乏信心，或股票被低估，通常出现在价值股中
  - **Price / Book Value** --> 反映股票价格相对于公司净资产（股东权益）的溢价或折价
    - Book Value 代表公司资产扣除负债后的净值
    - P/B < 1：股票可能被低估，公司资产价值可能高于市场价格
    - P/B > 1：市场对公司品牌价值、增长潜力或无形资产（如专利、品牌）给予较高溢价
  - **Price / Cash Flow** --> 反映市场对公司现金流创造能力的估值
    - Low P/CF：可能意味着股票被低估，公司现金流强劲
    - High P/CF: 投资者愿意支付更多价格获取公司的现金流，通常出现在增长型公司
  - **Price / Sales** --> 反映公司市值相对于收入的水平
    - High P/S：可能表明公司销售额较高，但市场定价较低，可能存在投资机会。
    - Low P/S：市场预期公司未来增长较快，但需要进一步评估盈利能力。


| Ratio | Measure                                                                                      | Typical Interpretation                                    |
| ------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| P/E   | 反映了投资者愿意为每 1 美元的收益支付多少倍的价格<br />Stock price relative to earnings      | High P/E = strong growth potential, Low P/E = value stock |
| P/B   | 反映股票价格相对于公司净资产（股东权益）的溢价或折价<br />Stock price relative to net assets | P/B < 1 may indicate undervaluation                       |
| P/CF  | 反映市场对公司现金流创造能力的估值                                                           | Low P/CF = stable cash flow                               |
| P/S   | 反映公司市值相对于收入的水平                                                                 | Low P/S may indicate an investment opportunity            |

## **General Test Procedure**

- For any quant strategy (i.e., based on a “quantifiable” sorting measure), including value:
  - **Sort stocks according to the chosen measure**排序股票
    - Use a comprehensive database of stocks that includes up-to-date, quality data
  - **Compute the future return**计算未来收益 (i.e., after the sort measure was known) of top and/or bottom group of stocks to examine whether a relationship exists between the criteria and future performance
    - E.g., sort into 10 buckets based on P/E at time *t* and examine the average return of each bucket at time **t+1** 将股票按P/E分成10个组，并计算每组在下一个时间周期的平均收益
- **➡️ 回测策略: This is one of the back test variations available using the EQS function in Bloomberg** 使用Bloomberg EQS等工具测试不同的投资方法

## **General Approach**

- Another name for investing according to quantitative measures combined with rules (like “buy stocks in the lowest 10th percentile based on P/E”) is **algorithmic trading**算法交易 --> 即按照固定规则买入或卖出股票
  - “买入P/E最低10%的股票”就是一种算法交易策略
  - In addition to a stock’s value measure, **quant/algorithmic trading** encompasses many other variables that correlate with a stock’s future return and a wide range of rules. 除了P/E，量化交易还可能包括其他因素（如动量、波动率等）来预测股票的未来表现
- **Value: Earnings / Price**
- ![Graph](ValueEarnings.png)
  - 这张表格显示了按照 Earnings-to-Price (E/P) Ratio 进行分组后的股票回报率，分别采用了 EW（Equal-Weighted, 等权重） 和 VW（Value-Weighted, 市值加权） 的方式计算收益
  - E/P 越高，收益越高
    - EW 方式：低 E/P 组的收益率为 13.17%，而高 E/P 组的收益率为 22.09%，表现出一个明显的正相关趋势
    - VW 方式：低 E/P 组的收益率为 12.40%，而高 E/P 组的收益率为 18.22%，趋势相同但收益率稍低
  - 等权重（EW）收益比市值加权（VW）更高
    - 在每个分组中，EW 收益率都高于 VW，这表明在小市值股票上，E/P 选股策略可能更有效（因为等权重方法会赋予小市值股票更大的权重）
    - 说明小市值高 E/P 股票的收益更高，而大市值股票的收益较低，使得 VW 的整体收益偏低
  - 低 E/P 组表现较差
    - EW = 13.17%，VW = 12.40%，说明低 E/P 股票的收益相对较低
    - 这与价值投资理论一致，即 低 E/P（高 P/E）股票往往是成长股，价格昂贵，但未来回报不一定高
  - 高 E/P 组收益最高
    - EW = 22.09%，VW = 18.22%，显示高 E/P（低 P/E）股票的收益最高
    - 这支持价值投资策略，即 低估值股票（高 E/P，低 P/E）在长期内可能获得更好的回报
  - 结论
    - 价值投资策略有效：高 E/P（低 P/E）股票在历史回测中表现较好，符合价值投资逻辑。
    - 小市值股票收益更高：EW（等权重）收益普遍高于 VW（市值加权），表明高 E/P 策略在小市值股票上表现更好。
    - 成长股（低 E/P）回报较低：低 E/P 组的收益最低，说明高估值的成长股可能面临回报下降的风险。

## **Leveraged Ratio**

- **Leveraged stock portfolios have stock exposure greater than the value of the account**.杠杆比率（Leverage Ratio） 衡量投资组合的股票敞口相对于账户净值的大小
- $$
  Leverage\ ratio = \frac{Long\ position\ value + |Short\ position\ value|}{Account\ value}

  $$

  - Account value（账户价值）：投资者的总资金
- **Suppose you have $100K in your brokerage account**

  - If you long $100K, your leverage ratio is **1.0**
    - $$
      Leverage\ ratio = \frac{100K + |0K|}{100K} = 1.0

      $$
    - 解释：投资者仅用自有资金投资，并未使用杠杆
  - If you long $130K and short $30K, your leverage ratio is **1.6**
    - $$
      Leverage\ ratio = \frac{130K + |30K|}{100K} = 1.6

      $$
    - 总敞口（多头+空头）$160K，比账户净值 $100K 更大，因此杠杆比率 > 1
- 结论

  - 杠杆比率越高，投资者承担的风险越大，因为：
    - 市场波动放大：上涨时收益增加，下跌时损失加剧
    - 保证金要求增加：如果市场反向波动过大，可能会触发追加保证金（margin call），投资者需要追加资金
  - Leverage ratio：
    - Leverage ratio = 1.0 --> 表示投资组合的总风险敞口等于账户的本金(即没有使用杠杆)
    - Leverage ratio > 1.0 --> 表示投资组合的总风险敞口大于账户本金，即投资者使用了杠杆
    - Leverage ratio < 1.0 --> (极少见), 表示投资组合的总风险敞口小于账户本金，即投资者持有部分现金或低风险资产，没有将全部资金用于市场敞口, 这通常意味着投资者采取了更加保守的策略，以降低市场风险或保留流动性

> ## 根据这张图计算：
>
> - ![Graph](ValueEarnings.png)
>
> ### **Question 1**:
>
> - What is the return of a long-short portfolio that is long the 10% highest E/P stocks and short the 10% lowest E/P stocks based on EW returns assuming no margin (i.e., leverage ratio = 1) is used?

- **8.92%**
- **4.46%**
- **None of the above**

> #### Answer:
>
> - **8.92%**
>
> #### Explanation
>
> - Understanding the Question
>   - Goes long (buys) the top 10% of E/P stocks.
>   - Goes short (sells) the bottom 10% of E/P stocks.
>   - Uses EW (Equally Weighted) returns.
>   - Assumes no margin (leverage ratio = 1).
> - Step 1: Identify the Relevant Returns
>   - From the E/P table, we extract the EW (Equally Weighted) returns:
>   - High E/P (Top 10%): 22.09% (this is the long portfolio return).
>   - Low E/P (Bottom 10%): 13.17% (this is the short portfolio return).
> - Step 2: Calculate the Long-Short Return
>   - The return of a long-short portfolio is calculated as:
>   - $$
>     Return = Return of Long Portfolio − Return of Short Portfolio = 22.09% − 13.17% =8.92%
>
>     $$

> ## **Additional Questions**
>
> 这些计算是基于收益/价格（E/P）比率，用来分析市场中不同E/P区间的表现。数据区分了等权重（EW）收益和价值加权（VW）收益
>
> - *(based on slide **“Value: Earnings / Price”**)*
> - **VW returns, leverage ratio = 1, long-only top 10%**
>   - Return = _18.22%_
>   - 这个数值直接来自表格中VW 列 "High E/P" 的数据
> - **VW returns, leverage ratio = 2, long top 10%, short bottom 10%**
>   - Return = 18.22% - 12.40% = _5.82%_
> - **VW returns, leverage ratio = 1, long top 10%, short bottom 10%**
>   - Return = (18.22% - 12.40%) / 2 = _2.91%_
> - **VW returns, leverage ratio = 1, long-only top 20%**
>   - Return = (18.22% + 17.15%) / 2 = _17.685%_

## **Book/Market**

- ![Graph](BookMarket.png)
  - 收益随着 B/M 的上升而提高，说明 高 B/M（价值股）相较于低 B/M（成长股）收益更高
  - B/M 低 代表市值相较于账面价值较高，这通常是成长股的特征，市场对其未来增长预期较高，因此估值溢价较高
  - B/M 高 代表市值相较于账面价值较低，这通常是价值股的特征，意味着市场对其增长预期较低，但可能被低估，导致未来收益较高

## **Cash flow/Price**

- ![Graph](CashflowPrice.png)
  - 收益随着 CF/P 的上升而提高，说明 高 CF/P（高现金流回报股票）相较于低 CF/P（低现金流回报股票）收益更高
  - CF/P 低 代表现金流相对较低，通常是成长型企业，其大部分现金流用于再投资，盈利能力较弱
  - CF/P 高 代表现金流相对较高，通常是成熟企业，稳定产生现金流，并可能派发股息，因此未来收益更稳健

## **Value**

- Sorting on a value ratio may miss important relationships between value and certain groups of stocks 基于价值比率的排序可能会忽略特定股票类别的价值关系
  - E.g., tech sector stocks trade at higher P/Es, on average, than other stocks科技股通常具有较高的市盈率 (P/E)
  - To account for sector-related tendencies, could sort based on **value ratio relative** to **value ratios of same sector stocks** 可以基于行业内的相对 P/E 进行排序，而不是绝对 P/E
- Similarly, certain stocks consistently trade at relatively high P/Es (e.g., Amazon)某些股票（如亚马逊）长期保持较高 P/E
  - Could sort stocks based on their current value ratios relative to their historical value ratios 对于这类股票，可以根据它们相对于自身历史 P/E 的高低来决定是否买入，而不是和整个市场比较
    - E.g., Even if Amazon has a high P/E compared to the universe of stocks, could consider buying Amazon when its P/E is low relative to Amazon’s long-term average P/E ratio 即使亚马逊的 P/E 在整个市场范围内较高，但当它的 P/E 低于其历史均值时，可能是买入机会
    - Doesn’t appear to be an option on Bloomberg’s back tester 在 Bloomberg 回测工具中，可能无法直接使用这种方法进行筛选

## **Market Capitalization**

- Can define **small cap** as less than **$2 billion market capitalization** 小盘股的定义 --> 市值小于 20 亿美元 的公司
- Small cap stocks are typically classified as **growth stocks**, rather than value stocks 小盘股通常被归类为成长股，而非价值股
  - **Stock valuation multiples** (such as P/E) for small cap stocks typically **higher** than for value stocks 小盘股的估值指标（如 P/E）通常较高，因为市场预期其未来收益和收入增长较快
    - Due to expected earnings and/or revenue growth
- Small cap stocks have **outperformed** large cap stocks on average 小盘股的长期回报通常优于大盘股 --> 这是因为小盘股往往具有更高的增长潜力，同时在市场低效时容易被低估，从而带来超额收益。
- ![Graph](SmallCapPerf.png)
  - EW (Equal-Weighted, 等权重)：对每个股票给予相同的权重，计算平均回报率。
  - VW (Value-Weighted, 市值加权)：根据公司市值给予不同权重，较大公司对指数影响更大
  - 小盘股整体表现优于大盘股：
    - 这是符合小盘股的长期高回报特性，投资者可以考虑在组合中配置一定比例的小盘股。
  - 等权 (EW) 小盘股回报更高：
    - 25.47% (EW) > 18.35% (VW) 说明，小盘股中的小型公司可能有更高的增长潜力，而市值加权会被大盘股的影响稀释收益。
  - 分位数下降趋势：
    - 说明在小盘股内部，规模较小的公司回报更高，这可能是由于市场低估、成长潜力更大等原因。

> ### **Question 2**
>
> 根据这张图计算：
>
> - ![Graph](SmallCapPerf.png)
> - 问题：**Based on the EW returns, what is the historical performance of a long-short small cap strategy (i.e., long small, short big) based on a total of 20% of the stock universe with leverage ratio = 2?**
>
> ### Answer
>
> - The historical performance depends on the excess return of small-cap stocks relative to large-cap stocks. Assuming:
> - **Small-cap EW return = 25.47%**
> - **Large-cap EW return = 11.45%**
> - **Leverage Ratio = 2**
>
> ### Return Calculation
>
> - **Return = (Small Cap Return - Large Cap Return) × Leverage Ratio  = (25.47% - 11.45%) × 2 = 28.04%**

> - Thus, the estimated historical performance is **28.04%**.
>
> ### Explanation
>
> - 杠杆比率 = 2 表示投资者管理的 资金规模是自己的 2 倍，也就是说，投资组合的总回报应该放大 2 倍。
> - 如果杠杆比率是 0.5，我们才会 乘以 0.5（或等价于除以 2），表示投资规模只有原来的 一半。

## **Small Cap Features**

- **High transaction costs**高交易成本
  - Bid-ask spread 买卖价差
    - 小盘股的流动性较低，买入和卖出之间的价格差距更大，导致投资者可能需要支付更高的成本
  - Depth of liquidity 市场深度
    - Implications regarding whether the strategy is scalable
    - 流动性较低意味着大额交易可能会影响股价。这对投资策略的可扩展性提出了挑战
  - Price impact价格影响
    - 由于市场深度有限，大额交易可能导致股价较大波动
- **Scarcity of information**

## **图表分析**

- ![Graph](SMTranCost1.png)
- ![Graph](SMTranCost2.png)
- ![Graph](TranCost.png)
  - 该图展示了 CRSP 小盘股（CRSP Small Stocks）与 DFA 小盘股基金（DFA Small Stock Fund）的回报比较。
  - 交易成本可能是导致这两类股票回报差异的一个重要因素。
  - 在某些年份，DFA 基金的回报明显高于 CRSP 小盘股，可能是因为 DFA 采用了更优化的交易策略来降低交易成本。
  - 小盘股的交易成本较高，可能会侵蚀实际收益。
  - 量化交易或主动管理策略需要考虑如何减少交易成本的影响，例如使用算法交易、分散交易时机等方法。
- ![Graph](SmallCapStockInfo.png)
  - 该图显示了不同规模股票的分析师覆盖率（Analyst Coverage）。
  - 大盘股（Large-Cap） 通常有 100% 覆盖率，并且平均分析师数量最多（超过 20 位）。
  - 中盘股（Mid-Cap） 分析师覆盖减少，但仍有较高覆盖率。
  - 小盘股（Small-Cap） 分析师覆盖度更低，研究报告相对较少。
  - 微盘股（Micro-Cap） 覆盖率最低，几乎没有分析师研究这些股票。
  - 由于信息稀缺，小盘股的定价可能比大盘股更容易出现失误，导致潜在的市场无效性（Market Inefficiency）。
  - 投资者如果能够获取到独特的信息，可能更容易在小盘股市场找到未被市场发现的投资机会（信息优势）。

> ### **Question 3**
>
> - **Which fund outperformed, Fidelity Value or Fidelity Growth Strategies?**
>
> #### Answer
>
> - **Fidelity Growth Strategies outperformed Fidelity Value.**
>
> #### Explanation
>
> - Historically, growth strategies tend to outperform value strategies during periods of economic expansion and low-interest-rate environments, while value strategies typically perform better during market recoveries and high-inflation periods.
> - Over the past decade, many growth stocks, particularly in the technology sector, have delivered higher returns compared to value stocks.
> - **如果市场处于扩张期或牛市，Fidelity Growth Strategies 可能表现更好**
> - **如果市场处于衰退期或利率上升，Fidelity Value 可能更具优势**

## **Price Momentum**

- **Jegadeesh and Titman** (*Journal of Finance*, 1993)

  - Sort based on past return over:
    - 6 months
    - 12 months
    - 计算股票在过去 6个月或12个月 内的收益率。选取过去表现最好的股票作为**买入（long）标的，表现最差的股票作为卖出（short）**标的。
  - Hold portfolios for **1 month or longer** 该策略要求投资者持有这些选定的股票至少 1个月或更长时间。
  - Repeat --> 这个过程是一个动态更新的交易策略，每过一个周期（比如每月）就重新计算，调整持仓。

  ## **图表分析**


  - ![Graph](PriceMomentum.png)
  - ![Graph](MomentumReturns.png)
    - 动量策略有效：高动量股票（Winners）的未来收益 > 低动量股票（Losers）。
    - **Return EW > Return VW**，表明小盘股的动量效应更强。
    - 这与经典的Jegadeesh & Titman（1993）研究一致，即动量策略在长期有效，并且小盘股中表现更好。

> ### Question 4:
>
> - **Based on a long-only momentum portfolio, which three stocks would you buy?**
>
> #### Answer:
>
> - **RMCF (9 votes)**
> - **JJSF (6 votes)**
> - **PLXS (5 votes) or MSFT (5 votes) (tie-breaker needed)**

> ### Question 5:
>
> - **What would be the holdings of a market-neutral momentum portfolio that consists of 4 stocks total?**
>
> #### Answer:
>
> - A market-neutral momentum portfolio typically consists of:
>
>   - **2 long positions in high-momentum stocks** (best-performing stocks)
>   - **2 short positions in low-momentum stocks** (worst-performing stocks)
> - Based on the given voting results:
>
>   - **Long positions:** **RMCF (9 votes), JJSF (6 votes)**
>   - **Short positions:** **ELA (0 votes), ADX (0 votes) or AADR (0 votes)**
> - 一个市场中性（market neutral）的动量投资组合通常包含等量的多头（long）和空头（short）股票，以消除市场整体波动的影响，仅依赖个股的相对表现获利。
> - 如果该投资组合由4 只股票组成，那么：
>
>   - 2 只股票属于动量最高（winners）组 → 做多（long）
>   - 2 只股票属于动量最低（losers）组 → 做空（short）
>
> #### Reasoning:
>
> - 解题思路：
>
>   - 从最近的动量回报表中（例如"Momentum Returns"表），找到过去一段时间（如6个月或12个月）表现最好的股票（winners）。
>   - 找到表现最差的股票（losers），这些股票可能经历了负收益或表现低迷。
>   - 选出2 只收益最高的股票（long），并选出2 只收益最低的股票（short）。
>   - 权重均衡分配，即：
>     > - 做多赢家股票 50%（每只 25%）
>     > - 做空输家股票 50%（每只 -25%）
>     > - 这样整体市场敞口为0，实现市场中性策略。
>     >
> - 总结
>
>   - 市场中性动量投资组合的构建方法是做多高动量股票、做空低动量股票，并确保整体市场敞口接近于零。
>   - 选取2只最高收益率股票做多，2只最低收益率股票做空，均衡分配权重。
>   - 这样可以剔除市场整体的影响，仅依赖个股相对表现获利。
>   - 计算预期回报时，用赢家组的平均收益减去输家组的平均收益，即(Long Winners Avg. - Short Losers Avg.)。

## **图表分析**

- ![Graph](MomentumRisk.png)
- 高波动性:
- - 动量策略的年度回报率波动较大，有的年份高达**+40%或更高**，而有的年份则出现**-60%甚至更低**的回报。**
  - **这种高波动性反映了动量策略的风险特性，即收益高度依赖市场趋势。**
- **极端负回报年份:**
  - **在某些年份（如2009年金融危机期间），动量策略的回报跌至接近**-100%**。这可能是因为市场的急剧反转导致之前表现强劲的股票迅速贬值，而表现弱的股票快速回升。
    长期平均正回报:
  - 尽管存在短期的极端波动，动量策略在长期内的回报大多为正（在大部分年份中，回报高于0%）。
    这表明动量策略在统计上有效，但投资者需要应对可能出现的极端负回报。
- 策略失效期:
  - 某些阶段（如上世纪30年代大萧条或2000年代经济危机），动量策略可能会表现较差，甚至产生持续的负回报。
- 总结
  - 这张图表清楚地揭示了动量策略的收益特性——高回报伴随高风险。虽然动量策略在长期中通常能带来超额收益，但投资者需要应对市场反转带来的重大风险以及年度收益的不确定性。这也是为何动量策略在实际投资中需要谨慎运用，并结合其他策略以实现风险控制。
