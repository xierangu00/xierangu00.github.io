---
title: Investment and Portfolio - Bloomberg Back Testing
description: Course review for Spring course in MAF program at Emory.
categories: [Finance,Course]
tags: [note]
math: true
date: 2025-02-08   15:06:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
# Bloomberg Back Testing

## **Equity Screening**
- Back test via the “Equity Screening” function (EQS)
- ![Bloomberg Interface](bloomberg.png)
- **Equity Screening (EQS)**: 这是 Bloomberg 提供的一个功能，允许用户根据自定的财务、经济和市场标准筛选股票。用户可以设置筛选条件如市值、盈利能力、股息率等，进行深入的股票分析。
- **Backtesting** ：通过模拟历史数据，评估一个交易策略或金融模型在过去的表现，预测未来的效果。这涉及到使用历史数据（如价格、交易量、市场指标），策略逻辑（买卖信号、资金管理规则），和模拟交易的过程。


## **Screening Criteria**
- Select screening criteria
  - E.g., narrow to stocks in S&P 500 (“Indices” = SPX) or “Country/Territory of Domicile” = United States
- Add additional screening criteria by typing in orange box to select criteria, such as **P/E**, and then modifying criteria, e.g., **P/E in bottom 50th percentile**
- Select “Backtest” and then modify parameters, including:
  - **“Analysis Period”** and **“Rebalance Frequency”**
  - Select **“Use Benchmark” = SPX**

## **Results**
- Then **“Run Model”** and see **EQBT** for progress
  - EQBT 代表 "Equity Backtest"，允许用户通过模拟历史数据来测试特定的股票或股票组合策略的表现。
- Click on magnifying glass for detailed results
  - **“Counts”** shows number of stocks and turnover
  - **Security analysis** shows stocks in portfolio during each rebalance period
- Detailed results (cont.)
  - Overview includes cumulative return plot vs. benchmark and statistics including:
    - Total return
    - Min and max period return
    - Standard deviation
    - Sharpe ratio
    - Alpha
    - Beta
    - Correlation vs. benchmark
