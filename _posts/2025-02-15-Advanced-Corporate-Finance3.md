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
- **Step 1: Calculate the initial outlay**
    - The only outlay in this project is the initial investment in equipment of $400K
- **Step 2: Calculation of the after-tax Cash Flows**
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

- **Step 3: Calculate the Terminal Value**
     - We now have two potential formulas
     - Since the project will *not* continue into infinity, we want to select the formula      that uses the sale price (i.e., salvage value)

  - **Option 1:**
    $$TV = Price_T - \tau_c (Price_T - BookValue_T) + \Delta NWC$$
       - **TV** = terminal value
       - **Price_T** = sale price (e.g., of plant) in terminal period **T**
       - **BookValue_T** = book value (e.g., of plant) in terminal period **T**
         - Non-zero only if you don’t fully depreciate asset; if you fully depreciate it, then        **BookValue_T = 0** by definition
       - **ΔNWC** = unwinding net working capital (**NWC** balance at end of project must equal 0)
       - **τ_c** = marginal tax rate

  - **Option 2:**
    $$TV = \frac{(CF_n)(1+g)}{(r-g)} \times \frac{1}{(1+r)^n}$$
       - Initial investment = $400K
       - Straight-line depreciation over 4 years to $0
       - Salvage value = $10K
       - Marginal tax rate = 30%

- **Step 4: Calculate the WACC** 
$$WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D$$
- **Leverage** = $ \frac{D}{D+E} = 50\% \Rightarrow \frac{E}{D+E} = 50\% $
- $ \tau_c = 30\% $
- $ r_D = 6\% $ (always choose the market rate!, i.e., the YTM)
- $ r_E = 19.8\% $


$$WACC = 50\%(19.8\%) + 50\%(1 - 30\%)6\% = 12\%$$

## **The numbers**
![Graph](Numbers.png)
![Graph](Numbers2.png)
![Graph](Numbers3.png)

> ## **Reminder: Useful Formulas**
  > - **PV of an annuity:** $$PV_0 = \frac{C}{r} \left(1 - \frac{1}{(1+r)^T} \right)$$
  > - **PV of an annuity with growth:** $$PV_0 = \frac{C}{r - g} \left(1 - \left( \frac{1+g}{1+r} \right)^T \right)$$
  > - **PV of a perpetuity:** $$PV_0 = \frac{C}{r}$$
  > - **PV of a perpetuity with growth:** $$PV_0 = \frac{C}{r - g}$$
  > - *Note:* **C** are the payments, **r** is the discount rate, **g** is the growth rate of the payments, and **T** is the number of payments of the annuity.


## **Discounted cash flow (DCF) analysis**
- Estimating the NPV of a potential investment is one form of the more general idea of **DCF analysis**.
- Any asset can be valued as:

  $$ \text{Value of asset} = \sum_{t=1}^{T} \frac{E(CF_t)}{(1 + r)^t} $$
## Where:
- The asset has a life of *T* years.
- *r* is the discount rate that reflects both the **riskiness** of the cash flows and the **financing mix** used to acquire the asset.


# Link between DCF and share price

## **Using DCF to get to share price**
- A firm is a **portfolio of assets**, so we can use the logic of DCF to value a firm.
- For a firm, the DCF approach considers:
  - the **expected CFs** to the firm **over the firm’s life**, and
  - a **discount rate** that reflects the **collective risk** of the firm’s assets.
- Now we’ll consider:
  1. DCF in the firm context.
  2. Choosing the right inputs (i.e., cash flows, discount rate).
  3. How these concepts can be used to get the share price.

# Firm vs. equity valuation

### Value of firm:
$${Value-of-firm} = \sum_{t=1}^{T} \frac{E(CF \ to \ firm_t)}{(1 + WACC)^t}$$

- E(CF to firm_t) is the expected cash flows to the **firm**  
  - i.e., the residual cash flows after meeting all operating expenses, tax obligations, and reinvestment needs,  
    _but prior to debt payments_
- \(WACC\) is the weighted average cost of capital

### Value of equity:
$${Value-of-equity} = \sum_{t=1}^{T} \frac{E(CF \ to \ equity_t)}{(1 + r_e)^t}$$
- E(CF \ to \ equity_t) is the expected cash flows to **equity**  
  - i.e., the residual cash flows after meeting all operating expenses, tax obligations, reinvestments needs, interest and debt payments_
- r_e is the cost of equity


## **Choosing the right inputs**
- In terms of cash flows, we have three choices:
  1. **FCFF (free cash flow to firm) for firm valuation**
     $$
     FCFF = EBIT(1 - \tau_c) - (Capex - Depr.) - \Delta NWC
     $$
  2. **FCFE (free cash flow to equity) for equity valuation**
     $$
     FCFE = Net\ Income - (Capex - Depr.) - \Delta NWC + (New\ Debt\ Issued - Repayments)
     $$
  3. **Dividends for equity valuation**
     - Dividends are cash payments to a firm’s shareholders
- For valuing equity, dividends (#3) and FCFE (#2) are the same
  - We’ll use this equivalence to get to share price

## **Income statement vs. CF formula**
![Graph](IS vs CF.png)
- Notice subtle differences: overhead-type expenses and interest are in I/S only
- I/S: last line = Net Income (often called “earnings” or “profit”)
- On I/S: EBIT is often used interchangeably with “operating income” or “operating profit”
  - But this is only true if non-operating income = $0
- EBIT = revenue – all operating expenses + non-operating income
- EBIT = net income + interest + taxes

## **Getting to share price**

- There are a few ways of getting the share price:

  **1. Estimate the present value of all future dividends**

  $$
  \text{Value per share of stock} = \sum_{t=1}^{\infty} \frac{E(DPS_t)}{(1 + r_e)^t}
  $$

- However, estimating dividends (DPS) to infinity (\(\infty\)) is a challenge!
- So, we make the simplifying assumption that the value of a stock has two parts: 
  (similar idea to the two parts of an investment decision)
  - **Part 1**: *the growth period* (i.e., incremental cash flows)
  - **Part 2**: *stable growth period* (i.e., terminal value)
  $$
  \text{Value per share of stock} = 
  \sum_{t=1}^{N} \frac{E(DPS_t)}{(1 + r_e)^t} + 
  \frac{DPS_N(1+g)}{(r_e - g)} \times \frac{1}{(1 + r_e)^N}
  $$
- Alternative ways:
  **2. Substitute FCFE for DPS, in the previous slide**
    - FCFE = free cash flow to equity
    - Discount by 𝑟 𝑒
  **3. Estimate the value of the whole firm, using FCFF and discounting by WACC**
    - Then subtract out value the of debt
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
> - To value a *firm*, you need **FCFF** and **WACC**.
> - To value *equity*, you need **DPS** (or **FCFE**) and cost of equity ($r_e$).
> - Here, we’re valuing a firm:
>   1. **Calculate** $r_e$, which is a component of the WACC:
>      $$
>      r_e = r_F + \beta_E (r_M - r_F) = 2.9\% + 1.3(7\%) = 12\%
>      $$
>   2. **Determine** the debt and equity weights for WACC:
>      $$
>      \text{Debt-to-equity ratio of } 33.33\% = \frac{1}{3} \Rightarrow D = 1, E = 3 \Rightarrow \frac{E}{D+E} = \frac{3}{4}, \quad \frac{D}{D+E} = \frac{1}{4}
>      $$
>   3. **Calculate the WACC**:
>      $$
>      WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D = \frac{3}{4} (12\%) + \frac{1}{4} (1 - 40\%) (10\%) = 10.5\%
>      $$
>   4. **Calculate firm value**:
>      $$
>      \text{Value of firm in stable growth} = \frac{E(FCFF \text{ next year})}{WACC - g}= \frac{30}{10.5\% - 5\%} = 545.45 \text{ million}
>      $$
