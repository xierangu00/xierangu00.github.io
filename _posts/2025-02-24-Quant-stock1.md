---
title: Quant strategies for Stocks - Stock market indices and ETFs
description: Quant stock modeling using python
categories: [Python, project]
tags: [note]
math: true
date: 2025-02-24   15:12:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
## Active vs. Passive Strategies
- Passive Strategies:
  - Track benchmark: Market Indices
- Active strategies
  - Beat the benchmark
- Quant Models – An example, JP Morgan Q model

## Stock Market Indices
- Market indices are used to gauge market-wide price movements
- Popular Indices
- Types of indexes
  - Price-weighted index
  - Market cap-weighted index (aka. value-weighted)
  - Equal-weighted index

## Calculation 1 - Stock Market indice normal case
![graph](indice.png)
  - Price-Weighted Index – e.g. DJIA
  - Day 0 Index Value = $\frac{\text{Sum of prices}}{\text{Divisor}} = \frac{20+30+50}{1} = 100$
    - 分母上的1 指的是divisor arbitrarily chosen on day 0
  - Day 1 Index Value = $\frac{18+32+46}{1} = 96$
  - Index Return = $\frac{96}{100} - 1 = -0.04$ or $-4\%$

## Calculation 2 - Price-Weighted Index – Stock Splits
![graph](split.png)
- If no adjustment to index computation: Day 1 Index Value = $\frac{9+32+46}{1} = 87$
- **Q. Does the index=87 truly reflect market movement?** ➜ *change the divisor, should not change the index*
- Choose new divisor so that $\frac{9+32+46}{d_{\text{new}}} = 96 \Rightarrow d_{\text{new}} = .91$
- Post-split Index = $\frac{9+32+46}{.91} = 96$



## Dow Jones Industrial Average (DJIA) 
- Price-weighted index of 30 large stocks
- Divisor adjusted when  (?)
  - Intel added Nvida, they add 1 stock does not mean the divisor will go down
- What is the adjustment to the index made following regular dividends?
- Implications?
- DJIA divisor = **0.16268413**

## DIA
- ![graph](DIA.png)
- Portfolio: https://www.zacks.com/funds/etf/DIA/holding


## ETF portfolios
- Question: Suppose you manage a fund that tracks the Dow Jones Index. How will you construct the fund portfolio?

## Tracking a Price-weighted index
- ![graph](track.png)
- Weight for stock i = $W_i = \frac{\text{Dollar value in stock i}}{\text{Total portfolio value}}$


## Dividends
- Dow Jones does not adjust divisor for regular dividends
- What are the implications?
- Special dividends exceeding 10% of stock price would result in corresponding adjustment to the divisor
- Q. At the end of one year will the return you earn from this portfolio exactly the same as the return on the DJIA for that year?

## DJIA vs. DIA
![graph](DJIA vs DIA.png)

## Calculations
- DJIA trades at 42,638 points. DJIA divisor = 0.163
- ![graph](DIAcal.png)
- **DJIA old= sum of prices/Divisor**
- **DJIA new = old + 1/divisor**
- 1% price increase in AAPL will increase S&P 500 by:
  - (a) 32.15 points
  - **(b) 14.85 points**
  - (c) 7.80 points
  - (d) 5.13 points

- 1% price increase in UNH will increase S&P 500 by:
  - **(a) 32.15 points**
  - (b) 14.85 points
  - (c) 7.80 points
  - (d) 5.13 points

- $1 price increase in KO will increase S&P 500 by:
  - (a) 1.31 points
  - (b) 2.40 points
  - (c) 3.80 points
  - **(d) 6.13 points**

- Suppose UNH declares a stock split. Ex-split, S&P 500 divisor will be:
  - (a) bigger
  - **(b) smaller**
  - (c) the same
  - (d) depends

## Net Asset Value
- Net Asset Value (NAV) = $\frac{\text{Total Asset Value}}{\text{Number of Units}}$
- Market Price = Price at which investors trade
- Should Market Price = NAV?
- **Price (sum) / New Divisor = DJIA old**
- **New divisor = Price (sum) / DJIA old

## DIA Premium/Discount
![graph](DIApremium.png)
- **Premium/Discount ≡ Market Price/NAV - 1**

## Market Price Vs. NAV
- Q.  Why do the market prices closely track the NAV? 
- ETFs have agreements with selected brokerages to act as Authorized participants (APs) to create new ETF shares or redeem existing shares. 
- Creation: APs deliver underlying portfolio to the ETF sponsor and the sponsor issues to the APs the corresponding new shares 
- Redemption: APs deliver ETF shares the sponsor and the sponsor redeems them and delivers the underlying portfolio of individual stocks to the APs. 

## ETF Arbitrage
- When actions would APs take is the ETF trades at a premium?
  - Short ETF and long stock baskets
- When actions would APs take is the ETF trades at a discount?
- Does DJIA have any shortcomings as a market index ?
  - DJIA --> 30 stocks, not the reflection 

## Market Cap or Market Value-Weighted Index - e.g. S&P500
![graph](marketcap.png)
- **Day 0 Value** = Total market Cap of N stocks / Divisor = (Σ from i=1 to N of Price_i * Shares_i) / d = 20,000 / 200 = 100
- **Day 1 Index Value** = 20,560 / 200 = 102.8
- **Index Return** = 102.8 / 100 - 1 = .028 or 2.8%
`divisor arbitrarily chosen on day 0`
![graph](SPY.png)
- Portfolio : https://www.zacks.com/funds/etf/SPY/holding
![graph](investment.png)

## Market Value-Weighted Indexes
- S&P 500 
  - Index of 500 large cap stocks selected by Standard and Poor’s
- Russell 1000
  - Index of 1000 largest stocks. Reconstituted at the end of June every year
- Wilshire 5000
  - All publicly traded stocks
  - It started with about 5000 stocks but now has about 3400 stocks. 
- Divisor adjusted when
  - Stocks in the index change
  - Stocks declare dividend greater than 10% of price
- No adjustment to the index for regular dividends
- Q. Would the divisor change for stock splits?
