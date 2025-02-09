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
## **Active Stock Selection**
- We focus on several strategies shown to outperform, on average, across the past ~100 years, including:
  - **Value**
  - **Growth**
  - **Momentum**
  - **Reversals**
- Understanding and following these strategies gives an investor an **"edge,"** a performance advantage relative to the average investor.
- **Cyclical nature to strategies**
  - Sometimes they work great for long time periods, and other times they don’t work well (but they work well on average across time).

## **Alternative Measures of Value**
- Stock price divided by a proxy for its worth, e.g.,
  - **Price / Earnings**
    - Forward or trailing earnings
  - **Price / Book Value**
  - **Price / Cash Flow**
  - **Price / Sales**


## **General Test Procedure**
- For any quant strategy (i.e., based on a “quantifiable” sorting measure), including value:
  - **Sort stocks according to the chosen measure**
    - Use a comprehensive database of stocks that includes up-to-date, quality data
  - **Compute the future return** (i.e., after the sort measure was known) of top and/or bottom group of stocks to examine whether a relationship exists between the criteria and future performance
    - E.g., sort into 10 buckets based on P/E at time *t* and examine the average return of each bucket at time **t+1**
- **➡️ This is one of the back test variations available using the EQS function in Bloomberg**

## **General Approach**
- Another name for investing according to quantitative measures combined with rules (like “buy stocks in the lowest 10th percentile based on P/E”) is **algorithmic trading**  
  - In addition to a stock’s value measure, **quant/algorithmic trading** encompasses many other variables that correlate with a stock’s future return and a wide range of rules.
- **Value: Earnings / Price**
- ![Graph](ValueEarnings.png)

## **Leveraged Ratio**
- Leveraged stock portfolios have stock exposure greater than the value of the account.
$$
Leverage\ ratio = \frac{Long\ position\ value + |Short\ position\ value|}{Account\ value}
$$
- **Suppose you have $100K in your brokerage account**  
  - If you long $100K, your leverage ratio is **1.0**  
  - If you long $130K and short $30K, your leverage ratio is **1.6**


## **Question**:
What is the return of a long-short portfolio that is long the 10% highest E/P stocks and short the 10% lowest E/P stocks based on EW returns assuming no margin (i.e., leverage ratio = 1) is used?
- **8.92%**
- **4.46%**
- **None of the above**
#### Answer:
- **8.92%**
#### Explanation:
- A long-short portfolio that is long the 10% highest earnings-to-price (E/P) stocks and short the 10% lowest E/P stocks is constructed to exploit value investing principles. Historically, stocks with higher E/P ratios (value stocks) tend to outperform those with lower E/P ratios (growth stocks). The expected return is derived from the difference in performance between these two groups. Given the conditions specified in the question (equal-weighted returns and no leverage), the correct return calculation leads to **8.92%**, making it the correct choice.


## **Additional Examples**
*(based on slide “Value: Earnings / Price”)*
- VW returns, leverage ratio = 1, long-only top 10%  
  - Return = _18.22%_
- VW returns, leverage ratio = 2, long top 10%, short bottom 10%  
  - Return = 18.22% - 12.40% = _5.82%_
- VW returns, leverage ratio = 1, long-only top 20%  
  - Return = (18.22% + 17.15%) / 2 = _17.685%_
- ![Graph](BookMarket.png)
- ![Graph](CashflowPrice.png)


## **Value**
- Sorting on a value ratio may miss important relationships between value and certain groups of stocks
  - E.g., tech sector stocks trade at higher P/Es, on average, than other stocks
  - To account for sector-related tendencies, could sort based on value ratio relative to value ratios of same sector stocks
- Similarly, certain stocks consistently trade at relatively high P/Es (e.g., Amazon)
  - Could sort stocks based on their current value ratios relative to their historical value ratios
    - E.g., Even if Amazon has a high P/E compared to the universe of stocks, could consider buying Amazon when its P/E is low relative to Amazon’s long-term average P/E ratio
    - Doesn’t appear to be an option on Bloomberg’s back tester


## **Market Capitalization**
- Can define small cap as less than $2 billion market capitalization
- Small cap stocks are typically classified as growth, rather than value, stocks
  - Stock valuation multiples (such as P/E) for small cap stocks typically higher than for value stocks
    - Due to expected earnings and/or revenue growth
- Small cap stocks have outperformed large cap stocks on average
- ![Graph](SmallCapPerf.png)


> ### Question
> - **Based on the EW returns, what is the historical performance of a long-short small cap strategy (i.e., long small, short big) based on a total of 20% of the stock universe with leverage ratio = 2?**
> ### Answer
> - The historical performance depends on the excess return of small-cap stocks relative to large-cap stocks. Assuming:
  > - **Small-cap EW return = 10%**
  > - **Large-cap EW return = 5%**
  > - **Leverage Ratio = 2**
> ### Return Calculation
**Return = (Small Cap Return - Large Cap Return) × Leverage Ratio  = (10% - 5%) × 2 = 10%**
  > - Thus, the estimated historical performance is **10%**.
> ### Explanation
  > - Small-cap stocks historically outperform large-cap stocks on average.
  > - A long-short strategy benefits from this excess return.
  > - Leverage amplifies the return by a factor of 2.


## **Small Cap Features**
- **High transaction costs**
  - Bid-ask spread
  - Depth of liquidity
    - Implications regarding whether the strategy is scalable
  - Price impact
- **Scarcity of information**
- ![Graph](SMTranCost1.png)
- ![Graph](SMTranCost2.png)
- ![Graph](TranCost.png)
- ![Graph](SmallCapStockInfo.png)


> ### **Question**
  > - **Which fund outperformed, Fidelity Value or Fidelity Growth Strategies?**
> #### Answer
  > - **Fidelity Growth Strategies outperformed Fidelity Value.**
> #### Explanation
  > - Historically, growth strategies tend to outperform value strategies during periods of economic expansion and low-interest-rate environments, while value strategies typically perform better during market recoveries and high-inflation periods. 
  > - Over the past decade, many growth stocks, particularly in the technology sector, have delivered higher returns compared to value stocks.


## **Price Momentum**
- **Jegadeesh and Titman** (*Journal of Finance*, 1993)
  - Sort based on past return over:
    - 6 months
    - 12 months
  - Hold portfolios for **1 month or longer**
  - Repeat
  - ![Graph](PriceMomentum.png)
  - ![Graph](MomentumRisk.png)


> ### Question 1:
  > - **Based on a long-only momentum portfolio, which three stocks would you buy?**
> #### Answer:
  > - **RMCF (9 votes)**
  > - **JJSF (6 votes)**
  > - **PLXS (5 votes) or MSFT (5 votes) (tie-breaker needed)**
> #### Reasoning:
  > - The selection is based on a long-only momentum strategy, which implies choosing stocks with the strongest past performance. In the given poll, RMCF received the highest votes (9), followed by JJSF (6), and a tie between PLXS and MSFT (5). If only three stocks are allowed, additional criteria, such as recent price trends or market conditions, could determine the tie-breaker.

> ### Question 2:
  > - **What would be the holdings of a market-neutral momentum portfolio that consists of 4 stocks total?**
> #### Answer:
  > - A market-neutral momentum portfolio typically consists of:
  > - **2 long positions in high-momentum stocks** (best-performing stocks)
  > - **2 short positions in low-momentum stocks** (worst-performing stocks)
> - Based on the given voting results:
  > - **Long positions:** **RMCF (9 votes), JJSF (6 votes)**
  > - **Short positions:** **ELA (0 votes), ADX (0 votes) or AADR (0 votes)**
> #### Reasoning:
  > - A market-neutral strategy aims to capture the relative outperformance of strong momentum stocks while hedging against underperformance by shorting weak momentum stocks. The long selections are based on the highest votes (RMCF and JJSF), while the short positions are selected from stocks with the lowest votes (ELA, ADX, and AADR, which all received 0 votes). This ensures the portfolio remains neutral to overall market movements while profiting from momentum effects.
