---
title: Investment and Portfolio - Performance Analysis
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Investment Portfolio]
tags: [note]
math: true
date: 2025-03-04 01:06:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
# Performance Analysis

## Key Performance Metrics

Performance statistics are crucial for analyzing and reporting the effectiveness of investment portfolios or individual assets. Commonly used metrics include:

- **Return**: This is a fundamental measure of the increase in value of an investment over a given time period, expressed as a percentage.
- **Regression Statistics**:
  - **Alpha**: Represents the excess return of an investment relative to the return of a benchmark index.
  - **Beta**: Measures the volatility of an investment relative to the market.
  - **R-squared**: Indicates the percentage of an investment's movements that are explained by movements in its benchmark index.
- **Sharpe Ratio**: Used to understand the return of an investment compared to its risk.

## Visual Tools for Performance

![graph](heatmap.png)

- **Heat Maps**: These provide a visual summary of stock performance across different industries and market cap sizes, helping quickly highlight areas of strength and weakness within the market.

## Calculation of Returns

Returns can be calculated using different methods depending on the requirement:

- **Arithmetic Average**:

  - Formula: $ r_a = \frac{\sum_{t=1}^{N} r_t}{N} $
  - Example: If the returns over 12 months are 2%, 3%, -1%, ..., the arithmetic average return is calculated by summing all monthly returns and dividing by 12.
- **Geometric Average**:

  - Formula: $ r_g = \left(\prod_{t=1}^{N} (1 + r_t)\right)^{\frac{1}{N}} - 1 $
  - This method accounts for the compounding effects over time and is usually less than the arithmetic average unless all returns are equal.

## Returns

- Raw returns are often monthly or daily frequency
  - Performance is often summarized via annualized returns
    - E.g., easier for many to relate to 10% annual returns rather than 0.8% monthly or 0.04% daily returns

## Annualizing Returns

### Arithmetic Average

To annualize, multiply by the number of return periods per year:为了将回报率年化，请乘以每年的回报期数：

- Monthly 每月:
  - N = 12
  - $r_a,annualized = 12 * r_a,m$
- Daily 每日:
  - N ≈ 250 (52 weeks per year, 5 trading days per week, minus holidays 每年52周，每周5个交易日，扣除假期)
  - $r_a,annualized = 250 * r_a,d$

### Geometric Average 几何平均值

Annualize by compounding 年化通过复合计算:

- Monthly 每月:
  - N = 12
  - $r_g,annualized = (1 + r_g,m)^{12} - 1$
- Daily 每日:
  - N ≈ 250
  - $r_g,annualized = (1 + r_g,d)^{250} - 1$

Annualizing via geometric average (rather than arithmetic average) is convention:

- Consistent with buy and hold performance, which benefits from the compounding effect
  通过几何平均数（而不是算术平均数）进行年化是常规做法，这与买入并持有的表现一致，受益于复合效应。

When total return `r_T` encompasses N months, use:

- $r_{\text{annualized}} = (1 + r_T)^{\frac{12}{N}} - 1$

For example, if total return across 2 years (or 24 months) is 20%:

- $r_g,annualized = 1.2^{0.5} - 1 = 0.0954 = 9.54%$

## Practical Example with FINVIZ

Using tools like FINVIZ, investors can visualize performance metrics such as return, beta, and alpha across various market segments, helping in strategic decision-making.

## Calculating Annualized Return

To find the annualized return for a stock that increases from $100 to $300 over three years, apply the geometric average formula:

**Formula**:

$$
r_{g,annualized} = (\frac{Final Price} {Initial Price})^{1 / Years} - 1

$$

**Given**:

- Initial Price: $100
- Final Price: $300
- Years: 3

**Calculation**:

1. Compute the growth factor:
   - $Growth Factor = 300 / 100 = 3$
2. Calculate the annualized return:
   - $r_{g,annualized} = 3^{1/3} - 1$
   - $r_{g,annualized} = 1.44224957 - 1$
   - $r_{g,annualized} = 0.44224957$

Thus, the annualized return is approximately 44.22%.

## Returns (回报率)

In performance reports, returns are shown in several ways:

- Hedge funds may show monthly and annual returns since inception in a table.
- Trailing cumulative returns over 1, 3, and 12 months.
- Cumulative buy-and-hold total or annualized returns over long periods, like the past 10 years.
- Returns are often compared to a benchmark, such as the S&P 500.

## Variance (方差)

- The returns for a stock portfolio are considered nearly **"independent"** over time, implying **no correlation from one period to the next**.
- Mathematically, if returns are independent, the variance of returns scales with the time period.
  - Annualize variance by multiplying by the number of periods per year

## Annualizing Standard Deviation (年化标准差)

- Monthly: With 12 observations per year, the annualized standard deviation is calculated by:
  $$ \sigma_{\text{annualized}} = \sqrt{12} \times \sigma_m $$
- Daily: With approximately 250 trading days per year, it is calculated by:
  $$\sigma_{\text{annualized}} = \sqrt{250} \times \sigma_d $$

## Sharpe Ratio (夏普比率)

- This ratio is a measure of excess return per unit of risk and is annualized for comparison across different timeframes:
- annualize Monthly:
  $$ S_{p,\text{annualized}} = \sqrt{12} \times S_{p,m} $$
- annualize Daily:
  $$ S_{p,\text{annualized}} = \sqrt{250} \times S_{p,d} $$

## Regression Statistics (回归统计)

- CAPM model is used to determine the alpha and beta of a portfolio relative to a benchmark:
  $$ r_p - r_f = \alpha_p + \beta_p (r_m - r_f) + \epsilon $$
- Alpha and beta are annualized for consistency over different time periods.
- To annualize alpha
  - Monthly (N = 12): $a_{p,\text{annualized}} = {12} \times a_{p,m}$
  - Daily (N ≈ 250): $a_{p,\text{annualized}} = {250} \times a_{p,d}$

## Sortino Ratio (索提诺比率)

- This ratio measures returns relative to downside risk, differing from Sharpe by only considering negative volatility:

$$ \text{Sortino}_p = \frac{r_p - \text{MAR}}{\text{downside risk}}$$

- Ratio of reward to downside risk
- Downside risk = downside semi-variance
- For N returns below the MAR, compute：

$$ \text{downside risk} = \sqrt{\frac{1}{N} \sum_{i=1}^N (r_{pi} - \text{MAR})^2 \text{ for } r_{pi} < \text{MAR}} $$

- For **returns below a threshold (MAR)**, the downside risk is calculated and used in the Sortino ratio formula.

## Holdings (持股情况)

- Performance reports may detail the number and types of holdings, often visualized using tools like the Morningstar style box.
- Morningstar style box:
![Graph](holding.png)
  - Number of holdings
  - Top-10 holdings
  - Commonly reported for mutual funds, but not commonly reported for hedge funds

## Attribution Analysis (归因分析)

- This analysis helps in understanding how much of the performance can be attributed to selecting the right industries versus picking the right stocks within those industries.
- Alpha captures overall performance of stock holdings relative to the market
- Can decompose performance into that which is attributable to:

  - Industry selection: The ability to pick stocks in strong industries
    - E.g., allocating assets to energy stocks when the energy sector outperforms the market
  - Stock selection: The ability to pick stocks that outperform other stocks in the same industry
    - E.g., picking Energy stock A when stock A outperforms other energy stocks
- Total performance = Industry skill + Stock skill
- Return vs. benchmark is the sum of:

  1. the return contribution of the specific set of industries (or sectors) vs. the benchmark return, plus
  2. the return of stocks in those industries vs. the index return of those industries
- The basic formula used is:

  $$ \text{Performance} = \sum \left( w_{\text{active},i} - w_{\text{benchmark},i} \right) \left( r_{\text{industry},i} - r_{\text{benchmark}} \right) + \sum w_{\text{active},i} \left( r_{\text{active},i} - r_{\text{industry},i} \right) $$

  This sums the industry and stock selection skills to determine total performance.

## Attribution Analysis Example

![example](ex222.png)

### Question:
Which of the following changes in the fund's industry weights would result in a negative industry selection for industry A?

### Options

- [ ] A's weight = 0
- [ ] A's weight > 0.35
- [ ] A's weight < 0.20
- [ ] Answers A and C
- [ ] None of the above

### Explanation

The industry selection effect becomes negative when the fund's weight in an industry is less than the benchmark's weight, assuming the fund's return from that industry is higher than the benchmark's return. Reducing Industry A's weight below the benchmark weight of 0.20 would lead to a negative industry selection effect.

根据提供的表格，我们需要确定哪些情况下对于行业A的选择权重将导致负面的行业选择贡献（Industry Selection）。

表格中显示行业A的基金权重是0.35，基准权重是0.20。根据表格计算，行业选择贡献为正值（0.20%），这表明当前的权重选择对基金性能是有益的。因为这是通过（基金权重 - 基准权重）×（基金回报 - 基准回报）计算得出，当前为 (0.35 - 0.20) × (11% - 10%) = 0.20%。

现在我们要评估的是哪种情况下行业选择贡献会变成负数。这会发生在基金权重低于基准权重的情况下，因为基金的回报是高于基准回报的。所以，如果行业A的权重降低到低于基准权重0.20以下，计算结果将是负数，即：

##### Industry Selection Contribution Formula
- Industry Selection Contribution = (Fund Weight - Benchmark Weight) × (Fund Return - Benchmark Return)
- Industry Selection Contribution = (Fund Weight < 0.20 - 0.20) × (11% - 10%) < 0

所以，正确的答案是选项中的“A's weight < 0.20”。这表示如果行业A的基金权重降低到低于0.20，行业选择贡献将变为负。

---
## Factor Analysis因子分析
- **Factor Analysis**
  - When holdings data are not available (e.g., for hedge funds), factor analysis can provide insight into a portfolio's return exposures.当持有数据不可用时（例如，对于对冲基金），因子分析可以提供对投资组合回报暴露的见解
  - Examples:
    - Is it a value fund or a growth fund?
    - What market cap stocks does it focus on?
  - Running a multi-factor regression and analyzing the factor coefficients is an example of basic factor analysis.运行多因子回归并分析因子系数是基础因子分析的一个例子

- **Question: In which cell in the style box would the "Mystery Fund" likely be located?**
  - Options:
    - Large cap value
    - Large cap growth
    - Mid cap blend
    - Small cap value
    - Small cap growth
- **Answer:** Without specific data on the "Mystery Fund's" investment focus and market capitalization range, it's not possible to accurately place it in a style box. A factor analysis could reveal whether it leans more towards value or growth and the size of the companies it invests in, but without that data, we cannot specify its location in the style box.
如果没有“神秘基金”的投资重点和市值范围的具体数据，我们无法准确地将其定位在风格框中。因子分析可以揭示它是更倾向于价值还是增长，以及它投资的公司的大小，但没有那些数据，我们无法确定其在风格框中的位置。

---

## Portfolio Turnover投资组合周转率
- **Portfolio Turnover**
  - Captures the degree to which the portfolio changes annually.表示投资组合年度变动的程度
  - A 100% turnover implies the portfolio completely changes, on average, annually.100%的周转率意味着投资组合平均每年完全更换一次
    - For example, holdings as of December 31 are completely sold and replaced by the next December 31.例如，12月31日的持仓到下一个12月31日前会被完全卖出并替换

---

## Fund Stats
- **Fund Stats**
  - Asset allocation
    - E.g., percent of fund invested in stocks vs. cash
  - Fund size

## Fee Information
- **Fee Information**
  - Fees are annually deducted (e.g., the expense ratio for a mutual fund)费用每年扣除（例如，共同基金的费用比率）
  - Sales load (for a mutual fund), if applicable销售负担（如果适用于共同基金）
  - Performance incentive fee for a hedge fund对冲基金的绩效激励费
  - Fees are expressed in percentage费用以百分比表示

---

## Performance Data表现数据
- **Performance Data**
  - In the U.S., investment funds provide performance data to the Securities Exchange Commission (SEC) (required by regulation).在美国，投资基金必须向证券交易委员会（SEC）提供表现数据（法规要求）。
  - Mutual funds are required to provide more detailed information than hedge funds.共同基金比对冲基金需要提供更详细的信息
  - Investors can acquire data from:
    - The SEC证券交易委员会
    - Fund companies
    - Fund data providers, such as Morningstar

---

## Performance Analysis绩效分析
- **Performance Analysis**
  - Two perspectives:
    - From the money manager’s perspective, the goal is to sell the fund.从资金管理者的角度看，目标是销售基金
      - Present the most favorable picture of performance.
      - Lots of discretion for hedge funds; less for mutual funds.对冲基金有较大的自由度；共同基金较少
    - From the potential client’s perspective, the goal is to objectively analyze the fund’s performance.从潜在客户的角度看，目标是客观分析基金的表现
      - To the extent possible, make apples-to-apples comparisons across funds.尽可能地进行基金间的公平比较

