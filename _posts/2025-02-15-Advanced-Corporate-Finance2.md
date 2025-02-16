---
title: Advanced Corporate Finance - NPV & IRR applications, cash flows & WACC
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-15   19:21:00 -0500
# image:
# path:
media_subpath: /assets/media
---
# **NVP & IRR in practice**
## **The Pros and Cons of NPV and IRR**
- Pros and Cons of NPV:
  - Pros of NPV: **Direct Measurement**: NPV provides a direct measure of the expected increase in firm value attributable to the investment.
  - Cons of NPV: **Investment Size Ignored**: NPV does not consider the size of the investment, which can skew comparisons when evaluating projects of different scales.

- Pros and cons of IRR
  - Pros of IRR: **Percentage Profitability**: IRR captures profitability as a percentage, making it easy to understand how far a project stands from achieving a negative NPV.
  - Cons of IRR: **Consistency Issues**: Project IRR ranking is not always consistent with NPV and can yield multiple values in cases of sporadic cash flows, complicating decision-making.

- Bottom Line
  - **NPV as a Guide**: For accept/reject investment decisions, follow the NPV. The NPV criterion is economically sound and accurately reflects the goal of maximizing firm value.

## Positive NPV & Attractive IRR

Even if a project has a **positive NPV and an attractive IRR**, management may choose not to proceed due to several factors:
- **Risk Factors**: Higher than accounted risks might deter progress despite attractive financial figures.
- **Resource Allocation**: Limited resources might be better allocated to projects with even higher returns or strategic value.
- **External Conditions**: Market volatility, economic downturns, or changes in consumer behavior could affect project viability post-evaluation.
- **Regulatory and Social Impact**: Potential regulatory changes and negative social impacts can also prevent project initiation.

## How NPV Analysis May Go Astray

- Failing to Incorporate All Economic Response
  - **Overlooking Externalities**: Not including all economic impacts can lead to inaccurate NPVs.

- Abusing Templates
  - **Misunderstanding Templates**: Ensure understanding of the financial model's assumptions, especially around terminal value calculations and growth rates.

- Ethics and Office Politics
  - **Subjective Influences**: Be wary of projects that are favored due to political reasons rather than solid financial justification.

- Mixing Real and Nominal Terms
  - **Discount Rate Confusion**: Always match the type of cash flow (real vs nominal) with the appropriate discount rate to avoid miscalculations.

- Cash Flow Blunders
  - **Double Counting**: For complex projects, ensure that cash flows are not counted more than once or overlooked.

- Sunk Costs vs. Incremental Costs
  - **Ignoring Sunk Costs**: Do not include costs that have already been incurred and cannot be recovered.

- Misestimating Overhead Costs
  - **Overhead Costs**: Include only incremental overhead costs related to management time and IT support, which are often difficult to quantify accurately.

## **What methods do CFOs use?**
![Graph](CFO.png)

## **What prevents firms from pursuing all positive NPV projects?**
![Graph](NPV2.png)

# **Calculating after-tax cash flows**

## Steps to Calculate After-Tax CFs
1. **Initial Outlay**
   - Includes fixed capital investment (e.g., new plant, equipment) and working capital investment (changes in net working capital).
2. **Operating Cash Flow Over the Project’s Life**
   - Consider revenues, expenses, and tax effects.
3. **Terminal-Year After-Tax Cash Flow**
   - Consider salvage value and any working capital recoveries.

## **1. Initial Outlay**
* **Initial outlay = Fixed capital investment + working capital investment**
  - **Fixed capital investment**: investment in new plant, equipment, etc.
  - **Working capital investment**: investment in net working capital (NWC)
    - Must be included when making investment decisions
    - **NWC investment** = Change in non-cash current assets – Change in non-debt current liabilities
    - If NWC investment (i.e., change in NWC) is positive, this means that additional financing is necessary!
  - Add positive NWC to positive up-front fixed cost
  - Then, put a negative sign in front of the sum in the NPV calculation as the initial outlay is cash flow **leaving** the firm


> ## **Example: After-tax CF calculation, NPV, & IRR Part1**
> * Analyze a project with the following cash flow forecasts:
>   - **3-year project**
>   - **Projected unit sales** = 1500 per year
>   - **Sale price** = $50 per unit
>   - **Variable cost** = $20 per unit
>   - **Fixed cost** = $5,000 per year
>   - **Up-front installation costs** = $60,000
>   - **NWC initial costs** = $15,000
>   - **Salvage value** = $10,000
>   - **Marginal tax rate** = 40%
>   - **Cost of capital** = 15%
>   - Assume straight-line depreciation to $0_
> * What is the **initial outlay?**

> ### **Step 1: Calculate initial outlays**
> ![Graph](Initial Outlay.png)
> Key insights:
>  - Because NWC increased (likely because you had to purchase inventory), it is considered an outlay.
>  - If you had reduced inventory by $15,000 instead, then the initial outlay would have been negative $45,000.
>  - If you had done a feasibility study with consultants first, this would not be included in the initial outlay (sunk cost).

## **2. Operating Cash Flow Over Project Life**
* After-tax operating cash flows are the incremental inflows over the capital asset's economic life.
  - **Formula**:
    - $$CF = (Sale - Exp - Depr)(1 - tc) + Depr - CapEx - ΔNWC$$
    - $$CF = (Sale - Exp)(1 - tc) + tcDepr - CapEx - ΔNWC$$
* **Where**:
  - **Sale** = sales (or "revenue")
  - **Exp** = operating expenses
  - **Depr** = depreciation expenses
  - **tc** = marginal tax rate
  - **CapEx** = capital expenditures
  - **ΔNWC** = change in net working capital


## **Depreciation**
* Depreciation is a **non-cash expense**
  - Yet, it is a **critical part** of cash flow because it **reduces the taxes paid by the firm**.
* **Key intuition for depreciation**:
  - Higher depreciation expense → Higher tax savings, higher after-tax cash flow.
* **Accelerated depreciation methods** lead to higher depreciation expenses earlier in the life of the project.
  - When compared to straight-line depreciation (i.e., an equal percent depreciation in each year).
* Which type leads to a higher NPV, all else equal?

## **An aside: Interest & Cash Flows**
* We include depreciation in the operating cash flow over the life of the project because it has a **tax advantage**.
  - What about interest rates? Interest also has a tax advantage!
* **Do not include interest in after-tax cash flows**
  - Interest is **already incorporated** into the cost of capital (or discount rate) used to analyze if the investments' return surpasses the required rate of return.
* **Summary**:
  - **Depreciation affects cash flows**
  - **Interest affects discount rates**



> ## **Example: After-tax CF calculation, NPV, & IRR Part 2**
> * Analyze a project with the following cash flow forecasts:
>   - **3-year project**
>   - **Projected unit sales** = 1500 per year
>   - **Sale price** = $50 per unit
>   - **Variable cost** = $20 per unit
>   - **Fixed cost** = $5,000 per year
>   - **Up-front installation costs** = $60,000
>   - **NWC initial costs** = $15,000
>   - **Salvage value** = $10,000
>   - **Marginal tax rate** = 40%
>   - **Cost of capital** = 15%
>   - Assume straight-line depreciation to $0_
> * What are the **operating cash flows?**

> ### **Step 2: Calculate cash flows**
> ![Graph](CashFlow.png)
> Key insights:
  > - Operating expenses include variable and fixed cost
  > - Subtract depreciation first to get to operating income, then add it back to get cash flows
  > - Sales are just projections; make sure the forecasts are reasonable (e.g., if the economy is slumping, are sales growth of 25% reasonable?)


## 3. Terminal Value Calculations
* Main idea: even if at the end of the project the new plant is no longer of use to your firm, it may be of use to some other firm → they will buy it from you!
  - **Formula**:
    - $$TV = Price_T - 𝜏_c(Price_T - BookValue_T) + ΔNWC$$
* **Where**:
  - **TV** = terminal value
  - **Price_T** = sale price (e.g., of plant) in terminal period T
  - **BookValue_T** = book value (e.g., of plant) in terminal period T
    - Non-zero only if you don’t fully depreciate the asset; if you fully depreciate it, then BookValue_T=0 by definition
  - **ΔNWC** = unwinding net working capital (NWC balance at end of project must equal 0)
  - **𝜏_c** = marginal tax rate


> ## **Example: After-tax CF calculation, NPV, & IRR Part 3**
> * Analyze a project with the following cash flow forecasts:
>   - **3-year project**
>   - **Projected unit sales** = 1500 per year
>   - **Sale price** = $50 per unit
>   - **Variable cost** = $20 per unit
>   - **Fixed cost** = $5,000 per year
>   - **Up-front installation costs** = $60,000
>   - **NWC initial costs** = $15,000
>   - **Salvage value** = $10,000
>   - **Marginal tax rate** = 40%
>   - **Cost of capital** = 15%
>   - Assume straight-line depreciation to $0_
> * What are the **terminal flows?**

### **Step 3: Calculate Terminal Flow**
> ![Graph](Terminal Value.png)


## Sensitivity Analysis
* Sensitivity analysis involves changing an input (e.g., projected sales) to see what effect this change has on a project’s NPV or IRR.
  - If the NPV or IRR changes a lot (i.e., is sensitive) when the input changes, we should think carefully about how confident we are about the input before making an investment decision.
* **Key**: only change one factor at a time (hold all other factors constant).
* Rule of thumb: change the factor by a fixed percentage (e.g., what if sales were 5% lower), and compare it to the base case NPV and IRR calculations.


> ## **Example: Sensitivity analysis**
> ![Graph](Sensitivity analysis2.png)
> Which inputs are the NPV and IRR most and least sensitive to?


# Discount rates (WACC)

## **What Discount Rate Should Firms Use?**
* The **discount rate** should be the rate a firm expects to pay all its security holders (equityholders and debtholders) to finance its assets.
* A discount rate that accounts for both debt and equity is:
  - **The weighted average cost of capital (WACC)**
  - Often referred to simply as the cost of capital.
* The WACC formula is a weighted average of the cost of equity and the after-tax cost of debt.
  - By looking at the after-tax cost of debt when calculating the WACC, we incorporate the tax savings of interest into the discount rate.


## **WACC, Discount, and Hurdle Rates**
* Most firms use the WACC as their discount rate and hurdle rate.
  - **Hurdle rate**: the minimum rate of return required on a project or investment.
* **Why?**
  - Because firms can **buy back their shares** as an alternative to making new investments.
  - Investing in their shares (earning their WACC) is the **opportunity cost** of alternative investments.
* Therefore, the WACC is the required rate of return investors demand.
  - It is the discount rate.
  - Any project the company invests in should have a return greater or equal than the WACC.

## **Accounting for Risk**
* In practice, firms often add a **risk premium** to the WACC.
  - We call the resulting rate the **hurdle rate**.
  - Example: If the company is US-based but the investment is in a less-developed (riskier) country, firms may add a few percentage points to the WACC and use that as their hurdle rate for investments.

## **WACC Formula and Example**
* **WACC Formula**:
  - $$WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D$$
* **Where**:
  - **E** = amount of equity
  - **D** = amount of debt
  - **r_E** = cost of equity
  - **r_D** = before-tax cost of debt
  - **𝜏_c** = marginal tax rate
* **Example**:
  - Suppose a firm has 60% debt and 40% equity. Its before-tax cost of debt is 10%, its cost of equity is 14%, and its marginal tax rate is 40%. Then:
    - WACC = 40%(14%) + 60%(1 - 40%)(10%) = 9.2%

## **The WACC Computation**
* **Leverage (D/(D + E))**
  - Book values or market values?
  - How have market fluctuations affected value?
* **Cost of Debt**
  - Expected, current, or historical rate of debt issuances?
  - Marginal or effective tax rate?
* **Cost of Equity**
  - Investment horizon?
  - Risk-free rate (match investment horizon? Expected, current, or historical rate?)
  - Equity market premium (how much data to include? What frequency?)
  - Firm’s beta (how much data to include?)
* **Risk Adjustment**
  - Comparable firms vs. gut feeling?
* **WACC Formula**:
  - $$WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D$$

## **Appropriate WACC Debt Assumptions**
* **The cost of debt** should be estimated with the expected rate on debt issuances and the marginal tax rate.
  - What proxies for the expected debt rate?
    - The market rate of a firm’s debt.
    - The yield to maturity (YTM) on current debt captures this market rate.
    - This is the relevant rate because it represents the **cost of debt that will be available for the firm to finance the project**.
* **Cost of Equity Inputs**:
  1. **Investment horizon**
     - Match investment horizon? 
     - Expected, current, or historical rate?
  2. **Risk-free rate, \( r_F \)**
     - How does it match the investment horizon?
     - Is it based on expected, current, or historical rates?
  3. **Equity market premium, \( r_M - r_F \)**
     - How much data to include?
     - What equity index is appropriate?
  4. **Firm’s beta, \( \beta_E \)**
     - Beta is a measure of systematic risk.
     - How much data to include for calculating beta?
* **Cost of equity based on CAPM model**:
  - $$ r_E = r_F + \beta_E (r_M - r_F) $$


## **The Risk-Free Interest Rate \( r_F \)**

* Use the risk-free rate on the day of the valuation.
  - Example: if your final analysis for a 5-year project is on Jan 20, 2018, use the 5-year US Treasury rate for Jan 20, 2018.

* The Federal Reserve has current and historical risk-free rates:
  - [Federal Reserve Historical Data](https://www.federalreserve.gov/releases/h15/)
  - Note: if a 6-year project, take the average of the 5- and 7-year rates, etc.
* ![Graph](IR.png)

## **The Equity Market Premium \( r_M - r_F \)**
* The equity market premium is the excess return that the overall stock market provides over the risk-free rate.
  - Also called the **equity risk premium** (higher risk, higher reward).
  - Compensates investors for taking on the relatively high risk of the equity market.
* For example: if the average return on the stock market over some period is 11% and the risk-free rate over the same period is 5% → equity market premium = 6%.

## **Everyone Uses Historical Premiums \( r_M - r_F \)**
* The historical premium is the premium that stocks have historically earned over risk-free securities.
* But practitioners rarely agree on the premium! Sensitive to:
  - How far back you go in history.
  - Whether you use T-bills or T-bonds (i.e., short or long-term risk-free).
  - Whether you use arithmetic or geometric mean.
    - Arithmetic mean: $${am} = \frac{a_1 + a_2 + ... + a_n}{n} $$
    - Geometric mean: $${gm} = \sqrt[n]{a_1 \times a_2 \times ... \times a_n} $$
* For example, for the US:
  * ![Graph](StockTbill.png)


## **Arguments for Using Lots of Historical Data \( r_M - r_F \)**

* When using historical premiums, go back as far as possible. Why?
  - A risk premium comes with a standard error (it's an estimate).
  - If the annual standard deviation of stock prices is 25%
  - So, the standard error of a historical premium estimated over 25 years is:
    - $$ SE = \frac{25\%}{\sqrt{25 \text{ years}}} = 5\% $$
* In other words, adding more years makes our estimate more precise.
* Some practitioners prefer the geometric mean over the arithmetic mean:
  - Because geometric is how investors think about risk over long periods.
  - However, the arithmetic (or simple mean) is more commonly used.

## **The Firm’s Beta**
* We use the **CAPM** (Capital Asset Pricing Model) to determine a firm’s beta.
  - CAPM: an idealized portrayal of how financial markets price securities and thus determine expected returns on capital investments.
* **Review of CAPM**:
  - Risk is separated into systematic and unsystematic:
    - **Unsystematic (i.e., firm-specific) risk** can be diversified away.
    - **Systematic (i.e., market) risk** cannot.
  - A diversified investor is:
    - Compensated for taking on systematic risk.
    - Not compensated for taking on unsystematic risk.
* For our purposes of using beta to help evaluate an investment decision, beta is an appropriate measure of investment risk.


## **The Basic CAPM Formula**
* The CAPM formula is used to determine the expected return of an asset:
  - $$ E(R_i) = R_F + \beta_i [E(R_M) - R_F] $$
    - \( E(R_i) \) = expected return of the asset (e.g., firm stock)
    - \( R_F \) = risk-free rate
    - \( 𝛽_i \) = sensitivity to market
    - \( E(R_M) \) = expected return of the market
    - \( [E(R_M) - R_F] \) = the price of risk
* In a statistical analysis, the firm’s beta (\( \beta_i \)) is calculated as:
  - $$\beta_i = \frac{\text{cov}(R_i, R_M)}{\text{var}(R_M)} = \frac{\sigma_{iM}}{\sigma^2_M} $$
    - This captures how much the return of asset \( i \) moves with the market return.
* The formula helps capture the relationship between an asset's returns and the market returns, emphasizing the role of risk.


## **Where and how do you get beta?**
- Almost every financial data provider (Yahoo! Finance, Bloomberg, Capital IQ, etc.) provides an estimate of firm-specific betas
  - Using these betas is OK, but be sure to know *how* they are calculated and that the assumptions of the calculation hold
  - Example: Yahoo! Finance provides a 5-year beta, with the S&P 500 as the benchmark index
  - If your project is shorter or longer than 5 years, you may want to consider manually calculating beta

## **How do you manually calculate beta? It’s a 3-step process...**
### Step 1: Obtain adjusted close historical prices
- Why adjusted close?
  - We don’t want to have to deal with dividends and splits; adjusted close adjusts for them
- What frequency?
  - Daily is noisy, so weekly may be better. Monthly is less noisy but requires many years.

### Step 2: Calculate returns
- ![Graph](Returns.png)

### Step 3: Calculate beta
- ![Graph](beta.png)
- What does a beta lower than 1 mean?
