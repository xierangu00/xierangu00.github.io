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
    - **再平衡频率（Rebalance Frequency）** ：选择 **月度、季度或年度** 调整投资组合。
  - Select **“Use Benchmark” = SPX**
    - **基准选择（Benchmark Selection）** ：将投资策略与基准指数对比（如 S&P 500）。

## **Results**

- Then **“Run Model”** and see **EQBT** for progress
  - EQBT 代表 "Equity Backtest"，允许用户通过模拟历史数据来测试特定的股票或股票组合策略的表现。
- Click on magnifying glass for detailed results
  - **“Counts”** shows number of stocks and turnover
    - 显示 **每个再平衡周期内选中的股票数量** 。
    - 计算 **换手率（Turnover Rate）** ，衡量投资组合中股票更换的频率
  - **Security analysis** shows stocks in portfolio during each rebalance period
    - 列出 **每次再平衡时选入的具体股票**
    - 帮助观察 **投资组合的变化情况**
- Detailed results (cont.)
  - Overview includes cumulative return plot vs. benchmark and statistics including:

    - Total return --> 策略在回测期间的总回报率
    - Min and max period return --> 历史上 **最好的** 和 **最差的** 投资时期
    - Standard deviation --> 衡量 **投资组合的波动性（风险）**
    - Sharpe ratio --> **每单位风险的超额回报** （值越高越好）
    - Alpha --> 超额回报（与基准相比）
    - Beta --> 投资组合对市场的敏感度
    - Correlation vs. benchmark
      - **相关性 = 1** ：完全与市场同步；
      - **相关性 = -1** ：完全逆市场波动；
      - **相关性 ≈ 0** ：无明显关系。
