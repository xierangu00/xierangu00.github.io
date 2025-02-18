---
title: Advanced Corporate Finance - Valuation using multiples
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-15   22:40:00 -0500
# image:
# path:
media_subpath: /assets/media
---
# Multiples, ratios, and comparables

## **Multiples: An alternative valuation method**

- **Multiples** are an alternative valuation method
  - Used extensively by equity research analysts and investment bankers for the valuation of whole companies
  - Used less commonly for individual investment project valuation
- **Basic idea**: "Simplify" the valuation by estimating a **"value per unit"** of something crucial to value creation_
  - In practice, use comparable firms or projects
  - For example, for whole company valuation, the method of **comparables** uses a **price multiple** of a similar firm or the average price multiple of a portfolio of firms as a **benchmark**
  - 在同一个行业中，相似公司的每一美元收益的价值应当相同。这种假设是基于市场在估值方面的效率和同质性，即市场参与者对相似资产的价值判断应当一致
- **The economic argument for comparables**:
  The value of a dollar of earnings should be the same across similar firms in the same industry

## **The basic idea behind multiples**

- We want to know the value of firm A, which we don’t observe

  - We know some performance measure \( X \) (e.g., earnings) for firm A
- We also know _both_ the value and performance measure for firm B
- 假设一个美元的收益在公司A和B中具有相似的价值。这意味着这两家公司的市盈率应当相似
- So, if the value of a dollar of earnings is similar for A and B, then

  $$
  \frac{Value(A)}{X(A)} = \frac{Value(B)}{X(B)}

  $$
- So, we can then estimate

  $$
  Value(A) = X(A) \times \frac{Value(B)}{X(B)}

  $$
- **Multiple** is represented as:

  $$
  \frac{Value(B)}{X(B)}

  $$

  - This ratio is used to estimate the value of another firm based on a comparable firm's observed value and performance measure.市盈率，表示每单位绩效指标X的市场价值
- In practice, we base the multiple on several comparable firms

## Most used multiple: the P/E ratio

The **Price-to-Earnings (P/E) ratio** is one of the most commonly used valuation multiples:

$$
P/E \ ratio = \frac{\text{Market price per share}}{\text{Earnings per share}}

$$

where **Earnings per share (EPS)** is given by:

$$
EPS = \frac{\text{Net income}}{\text{Shares outstanding}}

$$

#### Key Insights:

- The P/E ratio represents the dollar amount an investor must invest to receive $1 of the company's earnings.
- **Variations of the P/E ratio** (ensure consistency in comparisons):
  - **Price**: Can be based on the current price, average price over the past 6 months, or past year.
  - **EPS**: Can be derived from the most recent quarterly EPS, the average of the most recent four quarterly EPS, or forecasted next year's EPS.

## **P/E ratio’s many variations**

- We usually use the **current price** in the numerator.
- However, there are many different measures of **EPS**:
  - **Current P/E**: Uses EPS from the most recent financial year.
  - **Quarterly P/E**: Uses EPS from the most recent financial quarter.
  - **Trailing P/E**: Uses EPS from the past 4 quarters' earnings.
  - **Forward P/E**: Uses forecasted one-year earnings.

### General trend:

- **Will the current P/E or forward P/E be greater?**
  - Since **EPS generally increases over time**, forward P/E is typically lower than current P/E.

## **Fundamentals of P/E ratio**

- Let’s decompose the P/E ratio to understand how it links to fundamentals.
- Use a stable growth (DCF) dividend model for equity value.
- Start with the numerator: market price.

$$
P_0 = \frac{DPS_1}{r_E - g} = \frac{DPS_0 \times (1 + g)}{r_E - g} = \frac{EPS_0 \times b \times (1 + g)}{r_E - g}

$$

> - $ P_0 $ = price at time 0
> - $ DPS_1 $ = dividends per share (i.e., payout) at time 1
> - $ DPS_0 $ = dividends per share (i.e., payout) at time 0
> - $ r_E $ = required rate of return on equity
> - $ g $ = sustainable long-term growth rate
> - $ b $ = dividend payout ratio

- Divide both sides by EPS:

$$
P_0 = \frac{EPS_0 \times b \times (1 + g)}{r_E - g} \Rightarrow \frac{P_0}{EPS_0} = \left(\frac{EPS_0}{EPS_0}\right) \frac{b \times (1 + g)}{r_E - g}

$$

$$
\frac{P_0}{EPS_0} = \frac{b \times (1 + g)}{r_E - g} \Rightarrow \mathbf{PE \ ratio} = \frac{b \times (1 + g)}{r_E - g}

$$

- Shows how P/E ratios link to fundamentals $(b, g, r_E)$
- **Note**: This is a “current” P/E (denominator is $EPS_0$)
  - In the case of a **forward** P/E, divide by $EPS_1$ instead.
  - Or, equivalently, divide by $EPS_0 \times (1 + g)$

## **Fundamentals of P/E ratio: Propositions**

$$
PE \ ratio = \frac{b \times (1 + g)}{r_E - g}

$$

- **Proposition 1**: Other things held equal, higher growth firms will have higher P/E ratios than lower growth firms. 在其他因素不变的情况下，预期增长速度更快的公司将拥有比增长预期较低的公司更高的市盈率。
  - 这是因为投资者愿意为未来可能更高的收益增长支付更多。
- **Proposition 2**: Other things held equal, higher-risk firms will have lower P/E ratios than lower-risk firms.高风险公司的市盈率通常较低。
  - 较低的市盈率表示在股票投资上要求更高的回报，这是因为高风险意味着未来现金流的不确定性更大，投资者需要更多的潜在收益来补偿这种风险。
- **Proposition 3**: Other things held equal, firms with lower reinvestment needs will have higher P/E ratios than firms with higher reinvestment needs. 如果公司的再投资需求较低，它们通常会有更高的市盈率。
  - 较低的再投资需求意味着公司可以将更多的利润返还给股东或用于其他高回报投资，从而提高股东价值。

## **EPS timing matters**


| **Industry**      | **# Firms** | **Current P/E** | **Trailing P/E** | **Forward P/E** |
| ------------------- | ------------- | ----------------- | ------------------ | ----------------- |
| Entertainment     | 118         | 1157.13         | 908.12           | 58.16           |
| Utility (General) | 16          | 18.73           | 20.24            | 18.25           |
| Restaurants       | 79          | 58.91           | 70.43            | 1610.21         |

Data used as of January 2021.Source: [NYU Stern](https://pages.stern.nyu.edu/~adamodar/)

- **Current P/E**:

  $$
  \text{Current P/E} = \frac{P}{\text{EPS over most recent financial year}}

  $$
- **Trailing P/E**:

  $$
  \text{Trailing P/E} = \frac{P}{\text{EPS over last 4 years}}

  $$
- **Forward P/E**:

  $$
  \text{Forward P/E} = \frac{P}{\text{EPS over next year}}

  $$

## **Undervaluation: Utopian world vs. real world**

- In a **utopian world**, if you were looking for the perfect undervalued asset, it would have the following characteristics:
  - **Low P/E ratio** (i.e., cheap)
  - **High expected growth in earnings**
  - **Low risk** (and low **cost of equity**)
  - **High return on equity**
  - That is, cheap with **no good reason** for being cheap
- In the **real world**, most assets that **look cheap** _deserve_ to be cheap.

## **Shortcomings of the P/E ratio**

1. **Earnings can be negative**, which yields a meaningless **P/E ratio**.
2. **Earnings can be volatile and transitory**, which makes **P/E interpretation non-uniform**.
   - Especially if you only consider earnings over a **short period** (e.g., one year).
3. **Reported earnings may not be very comparable**.
   - **Management discretion** within allowed accounting practices can **distort reported earnings**.
   - This makes **comparing P/E ratios across firms difficult**.

## **Market value vs. enterprise value (EV)**

- **Enterprise value**: a measure of a company’s total value.

  $$
  \text{Enterprise value} = \text{equity market value} + \text{debt} - \text{cash}

  $$

  where:

  $$
  \text{Equity market value} = \text{Share price} \times \text{Shares outstanding}

  $$
- Often used as an alternative to **equity market capitalization**.
- **Basic idea**: can think of **EV** as the theoretical _takeover price_ if the company were to be bought.

  - Acquirer would have to **take on the company’s debt**, but would **pocket the company’s cash** for itself.

## **Another multiple: Value/earnings ratios**

- **P/E ratio**: market value of equity relative to earnings.
- Next financial ratio we’ll consider: **value-to-earnings**.
- Recall from last class: **equity value vs. firm value**.

  - What form of earnings has the closest match to enterprise cash flows rather than equity cash flows?

    $$
    EBITDA \times (1 - \tau_c) + (Depr \times \tau_c) - Capex - \Delta NWC

    $$
  - **In practice**: simplify to just **EBITDA** (earnings before interest, taxes, depreciation, and amortization).
- **Most common “value-to-earnings” multiple**: **EV/EBITDA**.

  - **Enterprise value/earnings**.
  - **Often in the range of 6.0x to 18.0x**.

## **Link between EV/EBITDA and DCF**

- **Value of a stable-growth firm’s assets** can be written as:
  $$
  EV_o = \frac{CF_1}{WACC - g}
  $$
- **Best estimate** of cash flows:
  $$
  EBITDA \times (1 - \tau_c) + (Depr \times \tau_c) - Capex - \Delta NWC
  $$
- **Divide both sides by EBITDA**:
  $$
  \frac{EV}{EBITDA} = \frac{(1 - \tau_c)}{WACC - g} + \frac{(Depr \times \tau_c) - Capex - \Delta NWC}{(EBITDA)(WACC - g)}
  $$
- **Reinvestment in firm is**:
  $$
  Capex - Depr + \Delta NWC
  $$

## **EV/EBITDA Propositions**

- From the previous slide, the determinants of EV/EBITDA are:
  - Cost of capital ( WACC )
  - Expected growth rate ( g ）
  - Tax rate (\( \tau_c \))
  - ~Reinvestment rate
- **Proposition:** Holding all else equal, then the following increase the EV/EBITDA multiple:
  - **Lower reinvestment** (via higher depreciation or lower capex)
  - **High earnings**
  - **Low taxes**
  - **Low risk**

## **Simple Example: EV/EBITDA**

- Calculate the EV/EBITDA for a firm:

  - The firm has $100$ million shares outstanding, with shares trading for $12.50$.
  - The firm has debt of $500$ million, cash of $200$ million, and short-term investments that can be viewed as cash equivalents of $50$ million.
  - The firm’s EBITDA is $130$ million.
- **Enterprise value calculation**:

  $$
  \text{Enterprise value} = \text{equity market value} + \text{debt} - \text{cash}

  $$

  where

  $$
  \text{Equity market value} = \text{Share price} \times \text{Shares outstanding}

  $$
- **Thus**:

  $$
  EV = (12.50 \times 100 \text{ million}) + 500 \text{ million} - (200 \text{ million} + 50 \text{ million})

  $$

  $$
  = 1250 + 500 - 250 \text{ million} = 1500 \text{ million}

  $$

  $$
  \frac{EV}{EBITDA} = \frac{1500}{130} = 11.54

  $$

## **Another multiple: Price-to-book**

- Price/book value multiple: ratio of market value of equity to the book value of equity
  - Book value = measure of shareholders’ equity on balance sheet
  - 这是公司在其资产负债表上记录的股东权益的值，通常是公司总资产减去总负债后的余额
- Price/book varies by region, industry, firm life cycle, …

## **Simple Example: P/B Ratio**

- Consider two recent IPOs with the potential for significant growth:


| **Company**  | **Sales (m)** | **Book value of equity ($m)** | **Outstanding shares (m)** | **Price ($)** |
| -------------- | --------------- | ------------------------------- | ---------------------------- | --------------- |
| Warby Parker | 393.72        | 308.41                        | 92.5                       | 54.05         |
| Poshmark     | 262.08        | 56.39                         | 40.29                      | 24.09         |

- **Warby Parker**:

  $$
  \frac{\text{Book Value}}{\text{Share}} = \frac{308.41}{92.5} = 3.33

  $$

  $$
  PB = \frac{54.05}{3.33} = 16.21

  $$
- **Poshmark**:

  $$
  \frac{\text{Book Value}}{\text{Share}} = \frac{56.39}{40.29} = 1.40

  $$

  $$
  PB = \frac{24.09}{1.40} = 17.21

  $$

## **More Multiples (Based on Sales)**

- Two other commonly used multiples:
  - **Price to Sales (P/S)**
  - **Enterprise Value to Sales (EV/S)**
- But, in the consistency test, the price/sales ratio fails!
  - The market value of *equity* is divided by the total revenues of the *firm*
    - Recall: We need to compare apples to apples!
  - Analysts have historically gotten away with this inconsistency because the price to sales ratio is:
    - Used in sectors with no debt (e.g., technology)
    - Used in sectors where financial leverage stays in a tight range (e.g., retail)
- A key determinant of the P/S ratio is the **profit margin**:
  - Lower profit margin → lower P/S ratio (direct)
  - Lower profit margin → sometimes lower growth, which lowers P/S

## Using Multiples for Valuations

- We discussed a bunch of multiples...What do we do with them?
- **Estimate the value of a firm**

##### **Approach #1**

1. Find many comparable firms (in terms of industry, technology, clientele, size, leverage, etc.).**寻找可比公司** ：选择与目标公司在行业、技术、客户群、规模和财务杠杆等方面相似的公司
2. Choose several scaling bases (i.e., earnings, sales, EBITDA).**选择多个基准** ：例如利润、销售额、EBITDA等不同的基准，用于评估和比较
3. Calculate the average multiple for each scaling factor for comparable firms.**计算平均倍数** ：对每个基准的倍数计算平均值，得到一组可比的市场倍数
4. Use various multiples and projections to get the valuation.应用不同的倍数和预测** ：利用这些倍数和未来的财务预测来估算目标公司的市场价值。
   - **Note:** Valuation often varies wildly for different multiples – think about which multiple is the *“best”* multiple.**注意，不同的倍数可能会得到不同的估值结果，因此选择最适合的倍数非常重要

##### **Approach #2**

1. Compare firms’ multiples directly. **直接比较法** ：直接比较目标公司与类似公司的倍数。这种方法较为简单，但可能受到市场情绪和临时因素的影响，使得结果出现波动

> ## Example: Delta
>
> - Let’s value Delta Airlines
>   - What comparable companies would you use?
>   - What multiples would you use?
>   - Calculations
> - **Step 1:** Since you’re trying to value Delta Airlines, you decide that the two best comparable companies are United Airlines (UA) and American Airlines (AA).
> - **Step 2:** You select sales and EBITDA as your two scaling factors, and you want to relate them to enterprise value (EV).
> - **Step 3:** What is the value of Delta? Suppose:
>   - UA’s debt plus equity is $1B; UA has no cash.
>   - AA’s debt plus equity is $2.2B; AA has $0.2B cash.
>   - UA’s sales are $1.5B; AA’s sales are $1.25B.
>   - UA’s EBITDA is $0.5B; AA’s EBITDA is $0.75B.
>   - Delta’s sales are $2B; Delta’s EBITDA is $0.75B.
> - **Multiples using sales:**
>   - UA: $EV/Sales = \frac{1 - 0}{1.5} = 0.67$
>   - AA: $EV/Sales = \frac{2.2 - 0.2}{1.25} = 1.6$
>   - **Average = 1.13**
> - **Multiples using EBITDA:**
>   - UA: $EV/EBITDA = \frac{1 - 0}{0.5} = 2$
>   - AA: $EV/EBITDA = \frac{2.2 - 0.2}{0.75} = 2.67$
>   - **Average = 2.33**
> - **Step 4: Get a valuation of Delta**
>   - **Using "sales" multiple**:
>      - Valuation = (Avg EV/Sales) × Delta sales = 1.13 × 2 = 2.26 Billion
>   - **Using "EBITDA" multiple**:
>      - Valuation = (Avg EV/EBITDA) × Delta EBITDA = 2.33 × 0.75 = 1.75 Billion
> - 在选择最终估值时，你可以考虑哪个倍数更符合公司的特性和市场环境。例如，如果市场更注重公司的收入增长能力，那么使用基于EBITDA的倍数可能更合适。反之，如果市场更关注公司的销售规模和市场占有率，那么使用基于销售额的倍数可能更恰当。
> - 在这个例子中，可以分别考虑使用销售额和EBITDA两种倍数得到的估值，然后决定哪一个更能准确反映Delta Airlines的市场价值。也可以考虑取两者的平均值来得到一个综合估值，以平衡不同指标带来的影响。最终的选择取决于你的分析目的和对市场情况的理解。

