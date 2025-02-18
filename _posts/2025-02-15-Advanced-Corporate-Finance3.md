---
title: Advanced Corporate Finance - Investment valuation & DCF
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-15   21:58:00 -0500
# image:
# path:
media_subpath: /assets/media
---
# Discount rates in practice

## **Discount rates in practice**

- In practice, estimating the WACC is part science, part art!
- Firms differ widely in the assumptions built into the models that they use to evaluate investment opportunities
  - For example, in a 2012 survey by the Association of Financial Professionals, across 1000+ professionals, no question about WACC assumptions received the same answer from the respondents!

# Recap of WACC, NPV, and investment decisions

## **Bringing together all our concepts so far**

- **Example: Startcorp is a startup company that will operate for 4 years**
  - Initial investment in equipment of $400K
    - Straight-line depreciated over 4-years to $0
    - The salvage value of the equipment is $10K
  - Marginal tax rate: 30%
  - The company has leverage of 50%
  - The current YTM of the debt is 6%; the interest rate on debt is 4%; the cost of equity is 19.8%
  - Expected annual sales are $400K, $450K, $450K, and $400K
  - Annual fixed costs are $40K per year; annual production costs are $150K when sales are $400K and $175K when sales are $450K

## - **What are the after-tax cash flows, WACC, and NPV?**

- ### **Step 1: Calculate the initial outlay**

  - The only outlay in this project is the initial investment in equipment of $400K
  - **初始投资** ：设备投资为40万美元，使用四年直线折旧法折旧至0，第四年末的残值为1万美元。
- ### **Step 2: Calculation of the after-tax Cash Flows**

  - **Cash flow formula:**
  - ![Formula](CF formula.png)
  - **Project details:**

    - Initial investment = $400K
      - Straight-line depreciation over 4 years to $0
      - Salvage value = $10K
    - Marginal tax rate = 30%
    - Leverage = 50%
      - YTM on debt = 6%; interest rate = 4%; cost of equity = 19.8%
    - [Sales] = $400K, $450K, $450K, $400K
    - Fixed costs = $40K per year
    - Production costs = $150K for $400K in sales, $175K for $450K in sales
      - **加回折旧** ：由于折旧是非现金支出，需将其加回到税后营业收入中，得到税后经营现金流。
- ### **Step 3: Calculate the Terminal Value**

  - We now have two potential formulas
  - Since the project will *not* continue into infinity, we want to select the formula      that uses the sale price (i.e., salvage value)
  - **Option 1:**

    $$
    TV = Price_T - \tau_c (Price_T - BookValue_T) + \Delta NWC

    $$

    - **TV** = terminal value
    - **Price_T** = sale price (e.g., of plant) in terminal period **T**
    - **BookValue_T** = book value (e.g., of plant) in terminal period **T**
      - Non-zero only if you don’t fully depreciate asset; if you fully depreciate it, then        **BookValue_T = 0** by definition
    - **ΔNWC** = unwinding net working capital (**NWC** balance at end of project must equal 0)
    - **τ_c** = marginal tax rate
  - **Option 2:**

    $$
    TV = \frac{(CF_n)(1+g)}{(r-g)} \times \frac{1}{(1+r)^n}

    $$

    - Initial investment = $400K
    - Straight-line depreciation over 4 years to $0
    - Salvage value = $10K
    - Marginal tax rate = 30%
- ### **Step 4: Calculate the WACC**

$$
WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D

$$

- **Leverage** = $ \frac{D}{D+E} = 50\% \Rightarrow \frac{E}{D+E} = 50\% $
- $ \tau_c = 30\% $
- $ r_D = 6\% $ (always choose the market rate!, i.e., the YTM)
- $ r_E = 19.8\% $

$$
WACC = 50\%(19.8\%) + 50\%(1 - 30\%)6\% = 12\%

$$

## **The numbers**

![Graph](Numbers.png)
![Graph](Numbers2.png)
![Graph](Numbers3.png)

> ## **Reminder: Useful Formulas**
>
> - **PV of an annuity:**
>   $$
>   PV_0 = \frac{C}{r} \left(1 - \frac{1}{(1+r)^T} \right)
>   $$
> - **PV of an annuity with growth:**
>   $$
>   PV_0 = \frac{C}{r - g} \left(1 - \left( \frac{1+g}{1+r} \right)^T \right)
>   $$
> - **PV of a perpetuity:**
>   $$
>   PV_0 = \frac{C}{r}
>   $$
> - **PV of a perpetuity with growth:**
>   $$
>   PV_0 = \frac{C}{r - g}
>   $$
> - *Note:* **C** are the payments, **r** is the discount rate, **g** is the growth rate of the payments, and **T** is the number of payments of the annuity.

## **Discounted cash flow (DCF) analysis**

- Estimating the NPV of a potential investment is one form of the more general idea of **DCF analysis**.
- Any asset can be valued as:

  $$
  \text{Value of asset} = \sum_{t=1}^{T} \frac{E(CF_t)}{(1 + r)^t}

  $$
- Where:

  - The asset has a life of *T* years.
  - *r* is the discount rate that reflects both the **riskiness** of the cash flows and the **financing mix** used to acquire the asset. **r** 是折现率，反映了现金流的风险性和用于获取资产的融资组合

# Link between DCF and share price

## **Using DCF to get to share price**

- A firm is a **portfolio of assets**, so we can use the logic of DCF to value a firm.
- For a firm, the DCF approach considers:
  - the **expected CFs** to the firm **over the firm’s life**, and **

    - 确定现金流** ：分析和预测公司未来每一年的自由现金流。这通常基于公司的财务预测，包括收入、成本、资本支出和营运资本的变化。
  - a **discount rate** that reflects the **collective risk** of the firm’s assets.

    - **选择折现率** ：选择一个适当的折现率，反映投资者对公司整体资产风险的评估。这个率可能基于加权平均资本成本（WACC）来计算
- Now we’ll consider:
  1. DCF in the firm context.
  2. Choosing the right inputs (i.e., cash flows, discount rate).
  3. How these concepts can be used to get the share price.

# Firm vs. equity valuation

### Value of firm:

$$
{Value-of-firm} = \sum_{t=1}^{T} \frac{E(CF \ to \ firm_t)}{(1 + WACC)^t}

$$

- E(CF to firm_t) is the expected cash flows to the **firm**
  - i.e., the residual cash flows after meeting all operating expenses, tax obligations, and reinvestment needs,
    _but prior to debt payments_
- \(WACC\) is the weighted average cost of capital
  - 加权平均资本成本（WACC）是股权和债务成本的加权平均，反映了公司资本结构中不同资金来源的成本。使用WACC作为折现率，能够代表公司整体资产的风险和融资组合

### Value of equity:

$$
{Value-of-equity} = \sum_{t=1}^{T} \frac{E(CF \ to \ equity_t)}{(1 + r_e)^t}

$$

- E(CF \ to \ equity_t) is the expected cash flows to **equity**

  - i.e., the residual cash flows after meeting all operating expenses, tax obligations, reinvestments needs, interest and debt payments_
- r_e is the cost of equity

  - 反映了股东投资的风险性。不同于WACC，股本成本只考虑了股东承担的风险
- ### 两者区别
- **现金流来源** ：公司估值考虑的现金流是在支付运营成本后、支付债务利息之前的现金流；股本估值则是在支付所有费用包括债务后的现金流。
- **风险和折现率** ：公司估值使用WACC包含了债务和股本的风险，而股本估值只考虑股本的风险，因此使用更高的股本成本来折现。
- **评估目标** ：公司估值提供企业总体价值的视角，适用于并购、合伙或整体出售的情况；股本估值则更专注于股东的角度，适用于股票投资分析和股权估价。

## **Choosing the right inputs**

- In terms of cash flows, we have three choices:
  1. **FCFF (free cash flow to firm) for firm valuation** 自由现金流至企业

     $$FCFF = EBIT(1 - \tau_c) - (Capex - Depr.) - \Delta NWC$$

     * FCFF 是公司在满足运营支出、税务义务和资本支出后，但在考虑任何债务融资（即利息和债务偿还）之前的剩余现金流
  2. **FCFE (free cash flow to equity) for equity valuation** 自由现金流至股权

     $$
     FCFE = Net\ Income - (Capex - Depr.) - \Delta NWC + (New\ Debt\ Issued - Repayments)

     $$

     - FCFE 是公司在支付了所有运营费用、税务、资本支出和债务服务后（包括新债务发行和债务偿还），归属于股东的剩余现金流
  3. **Dividends for equity valuation**股利

     - Dividends are cash payments to a firm’s shareholders
     - 股利是公司支付给股东的现金分红，通常基于公司的净利润和派息政策
- For valuing equity, dividends (#3) and FCFE (#2) are the same
  - We’ll use this equivalence to get to share price
- 三种方法的区别与联系
  1. FCFF vs. FCFE
  - 主要区别：FCFF 是公司视角下未扣除负债成本之前的现金流量，适用于评估公司整体价值，包括债权人和股东的权益。FCFE 则是扣除了所有负债成本后归股东的现金流，直接反映了股东的权益价值。
  - 风险与折现率：FCFF 通常使用WACC来折现，因为它包含了公司的整体资本结构风险。FCFE 使用股本成本（𝑟𝑒）来折现，因为它只涉及股东权益的部分，反映了股东所承担的风险。
  2. FCFE vs. 股利
  - 联系：在不考虑资本结构调整（如发行或偿还债务）的情况下，FCFE 有时可以近似等于公司的股利支付，特别是当公司的所有自由现金流最终都用于支付股利时。
  - 使用情景：如果公司有规律的股利支付政策，而且股利支付与FCFE接近时，可以直接使用股利进行估值。如果公司的资本结构复杂或股利支付政策不稳定，使用FCFE进行估值可能更准确。



## **Income statement vs. CF formula**

![Graph](IS vs CF.png)

- Notice subtle differences: 
- **overhead-type expenses and interest are in I/S only**
- I/S: last line = Net Income (often called “earnings” or “profit”)
- On I/S: EBIT is often used interchangeably with “operating income” or “operating profit”
  - But this is only true if non-operating income = $0
- EBIT = revenue – all operating expenses + non-operating income
- EBIT = net income + interest + taxes
- EBIT的用法：在损益表中，EBIT常用于表示营业利润（Operating Income），但这仅在非营业收入为零时有效。在现金流量表中，EBIT用来计算税后现金流，进而得出自由现金流。
- EBIT的定义：EBIT是从总收入中减去所有运营费用和非运营收入后得到的。而在损益表中，它还需要加上利息和税费，以得到净收入。


## **Getting to share price**

- There are a few ways of getting the share price:

  **1. Estimate the present value of all future dividends**估计所有未来分红的现值

  $$
  \text{Value per share of stock} = \sum_{t=1}^{\infty} \frac{E(DPS_t)}{(1 + r_e)^t}

  $$
- However, estimating dividends (DPS) to infinity (\(\infty\)) is a challenge!
- So, we make the simplifying assumption that the value of a stock has two parts:
  (similar idea to the two parts of an investment decision)

  - **Part 1**: *the growth period* (i.e., incremental cash flows)成长期：预计股票在初期会有不同程度的增长
  - **Part 2**: *stable growth period* (i.e., terminal value)稳定期：股票进入成熟期，增长率𝑔稳定

  $$
  \text{Value per share of stock} = 
  \sum_{t=1}^{N} \frac{E(DPS_t)}{(1 + r_e)^t} + 
  \frac{DPS_N(1+g)}{(r_e - g)} \times \frac{1}{(1 + r_e)^N}

  $$
- Alternative ways:
- **2. Substitute FCFE for DPS, in the previous slide** 使用自由现金流至股东（FCFE）

  - FCFE = free cash flow to equity
  - Discount by 𝑟𝑒
- **3. Estimate the value of the whole firm, using FCFF and discounting by WACC** 首先使用自由现金流至企业（FCFF）和加权平均资本成本（WACC）来估算公司的总价值。
  - Then subtract out value the of debt 从公司总价值中扣除负债，得到股权价值，然后除以股票数量，得到每股价值
  - Note: if the firm has other forms of financing (e.g., preferred stock), we would also need to account for this

## **Easier calculations for stable growth firms**

- In many cases, we do easier calculations:

  - Most stocks aren’t young tech or biotech firms.
  - Most stocks aren’t in high-growth periods.
  - For firms that are not in the high-growth phase, it is common to simplify the calculation:
    - Drop Part 1: growth period (i.e., incremental CFs).
    - Only use Part 2: stable growth period (i.e., terminal value).

  $$
  \text{Value per share of stock in stable growth} = \frac{E(DPS \text{ next year})}{(r_e - g)}

  $$

  $$
  \text{Value of firm in stable growth} = \frac{E(FCFF \text{ next year})}{(WACC - g)}

  $$
- **Note**: always make sure your denominators are consistent!

  - If the numerator is a CF to equity, then the denominator must be \( r_e \).
  - If the numerator is a CF to the firm, then the denominator must be the **WACC**.

> ## Example: stable growth valuation
>
> Consider the following stable firm:
>
> - Next year, FCFF for the firm will be **$30 million**.
> - Expected growth rate = **5%**.
> - Debt-to-equity ratio = **33.33%**.
> - Beta = **1.3**.
> - Cost of debt = **10%**.
> - Estimated equity premium = **7%**.
> - The current risk-free rate is **2.9%**.
> - The marginal tax rate is **40%**.
>
> **What is the firm’s value?**
>
> - To value a *firm*, you need **FCFF** and **WACC**.
> - To value *equity*, you need **DPS** (or **FCFE**) and cost of equity ($r_e$).
> - Here, we’re valuing a firm:
>   1. **Calculate** $r_e$, which is a component of the WACC:
>      - $$r_e = r_F + \beta_E (r_M - r_F) = 2.9\% + 1.3(7\%) = 12\%$$
>   2. **Determine** the debt and equity weights for WACC:
>      - $$\text{Debt-to-equity ratio of } 33.33\% = \frac{1}{3} \Rightarrow D = 1, E = 3 \Rightarrow \frac{E}{D+E} = \frac{3}{4}, \quad \frac{D}{D+E} = \frac{1}{4}$$
>   3. **Calculate the WACC**:
>      - $$WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D = \frac{3}{4} (12\%) + \frac{1}{4} (1 - 40\%) (10\%) = 10.5\%$$
>   4. **Calculate firm value**:
>      - $$\text{Value of firm in stable growth} = \frac{E(FCFF \text{ next year})}{WACC - g}= \frac{30}{10.5\% - 5\%} = 545.45 \text{ million}$$
