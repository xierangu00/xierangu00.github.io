---
title: Investment and Portfolio - Risk Management
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Investment Portfolio]
tags: [note]
math: true
date: 2025-03-04 03:06:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
# Risk Management风险管理

## Risk Management 风险管理概述

- Both the money management firm and the firm’s clients want:

  - Good performance 良好的表现
  - Without excessive risk 避免过度风险
    - Excessive risk could lead to a blowout 过度风险可能导致爆仓
    - "There are old traders, and there are bold traders, but there are no old, bold traders."
      “市场上有老交易员，也有大胆的交易员，但没有年老且大胆的交易员。”

---

## Risk Measures 风险衡量指标

- **Beta** 贝塔系数
- **Standard deviation** 标准差
- **Maximum drawdown** 最大回撤
- **Calmar ratio** 卡尔玛比率
- **VaR (Value at Risk)** 在险价值

---

## Beta 贝塔系数

Beta is used to measure a fund's exposure to market risk.
**Beta 用于衡量基金对市场风险的敞口。**

### Formula 公式：

$r_p - r_f = \alpha_p + \beta_p (r_m - r_f) + \varepsilon$
where:

- \( r_p \) = portfolio return 组合收益
- \( r_f \) = risk-free rate 无风险收益率
- \( \alpha_p \) = alpha 阿尔法（超额收益）
- \( \beta_p \) = beta 贝塔系数
- \( r_m \) = market return 市场收益
- \( \varepsilon \) = error term 误差项

### Interpretation 解释：

- During a positive market (e.g., 10% for the year), if a fund has high total return (e.g., 20% for the year), it is difficult to distinguish between:

  - A normal level of beta (around 1) and high alpha (10%)
  - High beta (e.g., 2) and low alpha (0%)
    **在市场向好时（例如年增长10%），如果一个基金的总回报率为20%，我们难以区分它是因为正常的 Beta (约1) 并具有高 Alpha (10%)，还是因为高 Beta (2) 且低 Alpha (0%)。**
- "Only when the tide goes out do you discover who’s been swimming naked."**“只有当潮水退去，你才知道谁在裸泳。”**— Warren Buffett

  - A fund reliant on high beta risk to generate high returns does poorly when the market return is negative.
    **依赖高 Beta 风险来获得高收益的基金，在市场下跌时表现较差。**
- Beta can be measured with a time series of past returns or holdings.
  **Beta 可以通过过去的收益或持仓数据计算。**

---

## Risk Measures 风险衡量

### Standard deviation 标准差

- Measures past standard deviation with historical returns
  **用历史收益计算过去的标准差**

### Maximum drawdown 最大回撤

- The largest drop from a peak to a bottom in a certain time period
  **在特定时期内从最高点到最低点的最大跌幅**

### Diversification 分散投资

- Reduces firm-specific risk
  **可以降低个股风险**

---

## Maximum Drawdown

![Graph](maxdrawdown.png)

- Represents the absolute value of the worst possible return for a buy followed by a sell

### Question

![Graph](drawdownq.png)

#### **What is the max drawdown (in percentage) in the below plot?**

- To calculate the maximum drawdown in the provided plot, we need to identify the largest peak-to-trough decline in the value of the portfolio over the given time period. Let's go through the steps:

##### Steps to Calculate Maximum Drawdown:

1. **Identify Peaks and Troughs** : Start by finding the highest and lowest points in the dataset from each local peak to the subsequent trough.
2. **Calculate Drawdowns** : For each identified peak, calculate the percentage drop to the next trough. This is done by:

$$
\text{Drawdown} = \left( \frac{\text{Peak Value} - \text{Trough Value}}{\text{Peak Value}} \right) \times 100\%

$$

3. **Identify Maximum Drawdown** : The maximum drawdown is the largest of these values.

##### Detailed Calculation:

From the visual inspection of the plot and using the provided data points, we would perform the following:

* **Find the Local Peaks and Troughs** : We look at the data where there are local maxima and subsequent minima.
* **Calculate the Drawdowns Between These Points** : For each peak-trough pair, calculate the drawdown percentage as described above.

Let's manually identify the highest visible peak and the lowest subsequent trough from the plot to approximate the maximum drawdown. For instance, suppose the highest peak is around 237.23 on January 1, 2022, and the lowest trough follows at around 153.87 on April 11, 2022.

* **Calculate the Maximum Drawdown** :

$$
\text{Max Drawdown} = \left( \frac{\text{237.23} - \text{153.87}}{\text{237.23}} \right) \times 100\%

$$

##### Conclusion:

The maximum drawdown, based on this approximation and the visible data points, would be around 35.14%. This calculation involves a manual identification process, which is susceptible to errors if not every data point is visible or accurately read from the chart. For precise analysis, it's recommended to use the raw numerical data in a computing environment to automate peak and trough identification and subsequent calculations.

---

## Risk Management

**Important to keep drawdowns small**
![Graph](small.png)

这张图展示了在投资管理中，保持最小化回撤的重要性。图表列出了不同初始亏损百分比（Initial loss）所需要的盈利百分比（Break even）来恢复到原始投资价值。

##### 图表解释：

* **Initial Loss** ：代表投资组合价值下降的百分比。
* **Break Even** ：为了抵消这种亏损并回到初始投资金额，所需要实现的回报率百分比。

##### 详细解读：

* **10%的亏损** 需要11.1%的盈利来弥补。
* **20%的亏损** 需要25%的盈利来弥补。
* **30%的亏损** 需要42.9%的盈利来弥补。
* **40%的亏损** 需要66.7%的盈利来弥补。
* **50%的亏损** 需要100%的盈利来弥补。
* **60%的亏损** 需要150%的盈利来弥补。

##### 重要性：

这说明了为什么在风险管理中必须努力最小化回撤。亏损越大，未来要通过盈利回到初始投资水平所需的回报率越高。这种非线性关系强调了保护资本的重要性，因为亏损的影响是累积且放大的。从长远来看，这种策略有助于确保投资组合的稳健和持续增长。

---

## Calmar Ratio 卡尔玛比率

- Ratio of return to max drawdown
  **收益与最大回撤的比率**
- Formula 公式：
  $$
  \text{Calmar Ratio} = \frac{\text{Geometric Annualized Return}}{\text{Max Drawdown}}

  $$
- **计算方法：过去36个月的几何年化收益率 / 同期最大回撤**

##### Explanation of the Calmar Ratio

The Calmar Ratio is a performance measurement for investments that considers the relationship between annualized return and the maximum drawdown. It helps investors evaluate the risk-adjusted returns of investment strategies or funds.卡尔马比率是一种投资绩效测量方法，它考虑了年化回报与最大回撤之间的关系。这有助于投资者评估投资策略或基金的风险调整后回报。

##### **Key Components** :

* **Calmar Ratio** : It is calculated as the ratio of the annualized return of a portfolio over a specified time period to the maximum drawdown during the same period.**卡尔马比率** ：它的计算方法是在指定时间内，投资组合的年化回报与同期的最大回撤之比。
* **Maximum Drawdown** : This represents the largest single drop from peak to trough in the value of a portfolio, before a new peak is achieved. It is expressed as an absolute value.**最大回撤** ：这代表在达到新高之前，投资组合价值从峰值到谷底的最大单次下跌。它以绝对值表示。
* **Annualized Return** : This is typically calculated as the geometric mean of the investment returns, compounded annually.**年化回报** ：通常计算为投资回报的几何平均值，按年复合计算。

##### **Importance** :

* A higher Calmar Ratio indicates a better performance relative to the risk (as measured by the maximum drawdown) an investor has taken on.较高的卡尔马比率表示相对于投资者所承担的风险（通过最大回撤测量），获得了更好的表现。
* The ratio is especially useful for comparing the risk-adjusted returns of investment funds or strategies that may experience significant fluctuations.该比率特别适用于比较可能经历重大波动的投资基金或策略的风险调整后回报

#### Graph Explanation and Calmar Ratio Calculation

![Graph](calmar.png)
The provided graph titled "Calmar Ratio" plots the Calmar Ratio of an investment over time, showing how the ratio has evolved from December 2019 through December 2022.

#### **Steps to Calculate the Calmar Ratio** :

To calculate the Calmar Ratio for the graph provided, follow these steps:

1. **Identify the Maximum Drawdown** : Look for the largest peak-to-trough decline within the period displayed. This can be done visually or by calculating the percentage drop from each high to subsequent lows.
2. **Calculate the Annualized Return** : Calculate the Compound Annual Growth Rate (CAGR) for the entire period. This can be done using the formula:
   $$
   \text{CAGR} = \left(\frac{\text{End Value}}{\text{Start Value}}\right)^{\frac{1}{\text{Number of Years}}} - 1

   $$

Given the plot shows values from December 2019 to December 2022, and assuming the values represent some form of financial metric that can be measured in monetary terms (like fund value), let's say the value in December 2019 is 100 and in December 2022 is 170. This can be visually estimated based on the graph. The time period is 3 years.

3. **Calculate the Calmar Ratio** : Divide the annualized return by the maximum drawdown (both in absolute values). The formula for the Calmar Ratio is:
   $$
   \text{Calmar Ratio} = \frac{\text{CAGR}}{\text{Maximum Drawdown}}

   $$

##### Example Calculation

* **Start Value (Dec 2019)** : 100
* **End Value (Dec 2022)** : 170
* **Period** : 3 years

**Step 1: Calculate CAGR**

$$
\text{CAGR} = \left(\frac{170}{100}\right)^{\frac{1}{3}} - 1 \approx 0.1974 \text{ or } 19.74\%

$$

**Step 2: Estimate Maximum Drawdown**

* Assume the maximum drawdown, visually estimating from the graph, occurs from about 150 down to 110 between February 2021 and July 2021.
  $$
  \text{Maximum Drawdown} = \frac{150 - 110}{150} = \frac{40}{150} \approx 0.2667 \text{ or } 26.67\%

  $$

**Step 3: Calculate Calmar Ratio**

$$
\text{Calmar Ratio} = \frac{0.1974}{0.2667} \approx 0.74

$$

## Value at Risk (VaR) 在险价值

- Defines the likelihood that a portfolio’s losses will exceed a certain amount under normal market conditions over a given period.
  **衡量在正常市场条件下，投资组合损失超过特定金额的可能性。**
- Based on the probability distribution for a portfolio’s market value, using historical returns.
  **基于投资组合市场价值的概率分布，使用历史回报数据计算。**
- Confidence levels: **95% or 99%**

#### **Value at Risk (VaR)**定义

Value at Risk (VaR) quantifies the potential loss in value of a risky asset or portfolio over a defined period for a given confidence interval. It provides a statistical measure of the risk level associated with an investment. 风险价值（VaR）量化了在给定置信区间内，一个风险资产或投资组合在定义的时间段内可能的价值损失。它提供了一个统计量度，用于评估投资相关的风险水平。

* **Definition:** VaR is the maximum expected loss over a specified time period, given a certain level of confidence. **定义：** VaR 是在指定时间期间内，给定一定置信水平下的最大预期损失。
* **Example:** If a portfolio has a one-day 95% VaR of $8 million, it means there is a 95% chance that the portfolio will not lose more than $8 million in a single day. 如果一个投资组合的单日95%VaR为800万美元，这意味着有95%的概率表明该组合在一天之内的损失不会超过800万美元
* **Computation:** VaR is typically calculated by determining the point on the loss distribution past which lies 5% (for a 95% confidence level) of the outcomes. This is based on the probability distribution of potential returns, which can be modeled using historical data.**计算：** VaR 通常通过确定损失分布图上的一个点来计算，该点的右侧覆盖了5%（对于95%置信水平）的结果。这基于潜在回报的概率分布，可以使用历史数据进行建模

##### Example 例子：

A $50 million portfolio with a one-day VaR of $8 million at the 95% confidence level:**一个价值5000万美元的投资组合，1天的95%置信水平VaR = 800万美元**

- This means there is a **5% probability** that the portfolio’s value will decrease by **$8 million or more** in one day.
  **意味着有5%的可能性，该组合在一天内损失800万美元或更多。**
- Calculation:

  $$
  -8M = 1.645 \times \sigma

  $$
- With a probability of 95%, the value of the portfolio will decrease by $8 million or less during one day

  - $8 million is 1.645 standard deviations below the mean daily dollar return, though VaR is typically expressed as an absolute value, e.g., a VaR of $8 million

##### 图表解释

![Graph](VaR.png)

随附的图形直观展示了VaR：

* **横轴：** 代表投资组合的可能价值。
* **垂直线（$42m - $50m)：** 这条线标记了95%置信水平下的VaR。这条线左侧的曲线下面积，以蓝色阴影表示，代表了最坏情况的5%。
* **曲线下面积：** 阴影区域指示的是结果与VaR同样糟糕或更糟的范围，发生概率为5%。

这种图形表示帮助投资者理解损失的潜力及这些损失超过某一阈值的可能性，强调了通过量化潜在损失来进行风险管理的重要性。

---

## Software 交易软件

- Sophisticated tools can help measure past risk and identify areas of concern.**专业工具可以帮助衡量过去的风险并识别潜在问题**
  - Example 例子：
    - **Bloomberg**
    - **FactSet**
