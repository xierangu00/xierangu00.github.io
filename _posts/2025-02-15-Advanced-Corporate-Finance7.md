---
title: Advanced Corporate Finance -  Adjusted Present Value (APV)
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-16   17:50:00 -0500
# image:
# path:
media_subpath: /assets/media
---
#  Adjusted Present Value (APV)

## **Different investment valuation methods**
1. **Weighted average cost of capital (WACC) approach**
   - NPV calculations where one discounts the free cash flows of a target firm or investment project with WACC  
   - $ Value = \sum_{t=0}^{\infty} \frac{FCF_t}{(1 + WACC)^t} $
2. **Multiples and comparable firm approach**
3. **Adjusted Present Value (APV)**
   - Discount cash flows as if the firm was funded with equity only  
   - Then, add the present value of tax shield and other “financial side effects” of debt

## **APV: The fundamental idea**
- ![Graph](APV.png)
- APV unbundles components of value and analyzes each one separately
- (Whereas WACC bundles all financing side effects into the discount rate)

## **Different investment valuation methods**
1. **Weighted average cost of capital (WACC) approach**
   - NPV calculations where one discounts the free cashflows of a target firm or investment project with WACC
   - $$ Value = \sum_{t=0}^{\infty} \frac{FCF_t}{(1 + WACC)^t} $$
2. **Multiples and comparable firm approach**
3. **Adjusted Present Value (APV)**
   - Discount cash flows as if the firm was funded with equity only
   - Then, add the present value of tax shield and other “financial side effects” of debt

---
## **APV consists of 3 steps**
1. **Calculate NPV of a project or target firm assuming it is financed with equity only**
   - Being financed with only equity implies always using the “cost of unlevered equity,” $r_U$, for discounting  
   - *Note: This is often called the “base-case NPV”*
2. **Calculate NPV of each financing item**
   - For example, the present value of an interest tax shield  
   - *Note: These are often called “side effects”*
3. **Add the base-case NPV and the NPV of each financing item together to get APV**

---

## **APV in formulas**

$$ APV = V_{Levered} = V_{Unlevered} + PV(SideEffects) $$
- $V_{Levered}$ = value accounting for how project is financed
  - i.e., what mix of equity and debt is used
- $V_{Unlevered}$ = value *not* accounting for how project is financed
  - But rather assuming all equity financing
  - “Base-case NPV” (or “base-line NPV”)
- $PV(SideEffects)$ = present value of financing side effects
  - E.g., interest tax shields

---

## **Step 1: Calculate $V_{Unlevered}$**

$$ V_{Unlevered} = \sum_{t=0}^{\infty} \frac{FCF_t}{(1 + r_U)^t} $$

- $r_U$ = the unlevered cost of equity
  - If the firm has no debt (i.e., it is unlevered) $\Rightarrow$ all equity financed and so $r_U = r_E$

**Note:** Do **not** use the WACC for calculating the base-case NPV in the APV method!

---

## **Step 2: Calculate $PV(SideEffects)$**

- The most common financial side effect is the **interest tax shield**
- To calculate the value of the interest tax shield:
  1. First, calculate how much expected cashflows the firm saves on taxes each year because of interest expenses
     - If debt = $D$, this is given by $r_D \times D \times \tau_c$ (where $r_D \times D$ are interest payments and $\tau_c$ is the tax rate)
  2. Second, these savings need to be discounted to present value
     - Discount tax savings by $r_D$. Why?
       - The appropriate discount rate is the rate associated with the debt (i.e., $r_D$)
       - $r_D$ better captures the riskiness of debt (recall, we want to discount to reflect similar risk level)

---

## **Calculating debt and interest payments**

- When structuring a loan, some firms like to have equal debt payments over the life of a loan
  - This is often referred to as a **"standard amortizing loan"**
- With this approach, a large percentage of a firm’s payments are applied to interest in the early years of the loan
  - In the later years, the outstanding balance slowly declines, and so more and more of each payment is applied to paying down the balance (i.e., the principal amount)
- In Excel, you can use the **PMT** function to calculate the periodic payment for a standard amortizing loan
  - `=PMT(interest rate, # of periods, loan amount)`

- When structuring a loan, some firms like to only make interest payments in the early periods and pay off the entire principal of the loan at the end
  - This is often referred to as a **"bullet loan"**
- With this approach, the payment is constant through the initial years and equal to the interest rate on the loan; the final period payment is interest plus principal


## **Example: calculating debt and interest payments**

- First Motor Corp. is financing its new investment with a \$10 million bank loan at an interest of 12% over 6 years.
- The loan is structured so that the firm makes equal payments each period.
- **Q:** Calculate the portion of the payment that goes towards principal and interest each period.

- In Excel, find the periodic payment (standard amortization):
  - `=PMT(interest rate, # of periods, loan amount)`
  - `=PMT(12%, 6, 10,000,000) = $2,432,257.18`

- At the beginning of year 1, the full \$10 million is outstanding:
  - Interest on that is $12\% \times 10$ million $= 1.2$ million
  - Principal repayment = total payment made - interest paid  
    $= 2.432$ mil $- 1.2$ mil $= 1.232$ mil

- At the beginning of year 2:
  - Loan outstanding = $10$ mil $- 1.232$ mil $= 8.768$ mil
  - Interest on that is $12\% \times 8.768$ mil $= 1.052$ mil
  - Principal payment = $2.432$ mil $- 1.052$ mil $= 1.380$ mil

- At the beginning of year 3:
  - Loan outstanding = $8.768$ mil $- 1.380$ mil $= 7.387$ mil
  - Interest on that is $12\% \times 7.387$ mil $= 0.887$ mil
  - Principal payment = $2.432$ mil $- 0.887$ mil $= 1.545$ mil

- ![Example](debtinterestrate.png)
---

## **Example: PV(financing effects)**

- First Motor Corp. would like to know the benefits of a potential financing arrangement.
- Using the debt and interest payments that you just calculated, what would be the PV(financing effects) if:
  - The firm’s cost of equity is 15%.
  - Cost of debt is 12%.
  - The marginal tax rate is 30%.
  - Leverage is 25%.

- The key financing side effect here is the interest tax shield:
  - $PV(\text{tax shield}) = r_D \times D \times \tau_c$, discounted at the cost of debt.
  - $r_D \times D$ are the interest payments.

- $PV(\text{Year 1 interest}) = \frac{12\% \times 10\text{ mil} \times 30\%}{(1+12\%)^1} = 321,428.57$

- ![Example](discountedtaxpayment.png)
---

## **Comparing NPV and APV**
- ![Example](NPV bs APV.png)

- NPV and APV produce equivalent values:
  - Both subtract initial outlays.
- NPV requires recalculating the WACC each period to account for any changes in financing:
  - NPV begins with after-tax cash flows, discounts them period-by-period using the WACC.
  - This method incorporates the benefits of debt through the discount rate.
- APV starts with unlevered cash flows (i.e., equity-financed cash flows):
  - Discounts unlevered cash flows at the unlevered cost of equity.
  - PV of side effects are calculated separately and added to the “unlevered NPV.”
  - This method incorporates the benefits of debt through the side effect calculation.


## **When to use APV over NPV**

- **APV** is often an easier calculation for decisions with **large fluctuations in the firm’s leverage**
  - **Example: the project**
    - Needs an initial outlay that can be financed internally
    - But will need a large outlay in 5 years that will need to be funded with long-term debt that will have a long-term impact on the firm’s leverage
    - Should be evaluated using APV, as APV only requires debt outstanding year-by-year

- **APV is also commonly used for LBO valuations**
  - A **leveraged buyout (LBO)** is an acquisition by a financial sponsor, financed using significant amounts of debt
  - Typically, there will be high debt initially but expectations that it will be paid down over time, leading to variations in a firm’s leverage


## **Example: APV of Sun, Inc.**

- **Sun, Inc. produces solar heaters**
  - FCF will be **$1.8 million per year for 10 years**
  - The firm has **$5 million in debt**
  - $ r_D = 10\% $, risk-free debt will be paid in equal installments over the next $10$ years
  - $ \tau_c = 46\% $, tax rate
  - $ r_U = 12\% $, unlevered cost of equity

- **Q: What is the value of the firm? (Calculate using APV)**

- **Steps:**
  1. Calculate **PV of FCFs** (\$1.8 mil per year)
     - What discount rate should we use?
  2. Calculate the **PV of tax savings**
     - What are the tax savings each period?
     - How do we calculate interest each period?
     - What discount rate should we use?

- Recall that **APV equals the sum of two parts**:
  1. **Valuation of base-case discounted at the unlevered cost of equity**
  2. **Valuation of financing side effects discounted at the cost of debt**

| Base-case value | Value of all financing side effects |
|---------------|-----------------------------|
| **APV** = value of the project as if it were financed entirely with equity | + interest tax shields |
|  | + costs of financial distress |
|  | + subsidies |
|  | + hedges |
|  | + issue costs |
|  | + other costs |

- **APV unbundles components of value and analyzes each one separately**, whereas the WACC **bundles all financing side effects into the discount rate**.


- **Step 1: Calculate base-case NPVs**
  - You are already given the **FCFs**
  - You need to choose the **correct discount rate**
    - The correct discount rate is the **unlevered cost of equity** = **12%**
  - No initial outlays, so nothing needs to be subtracted in period 0
- ![example](sun.png)


- **Step 2: PV(side effects)**
  - First, determine the **equal debt payments across 10 periods**
    - Using the “PMT” function in Excel, **payment = $813,727$**
  - Next, what portion of the **$813,727$** goes toward interest each period?
    - $ (D \times \text{interest rate}) $ goes towards interest, where $ D $ is the outstanding principal
    - Anything that remains goes towards paying down the principal
  - **Period 1**: $ 5 \text{ mil} \times 10\% = 500,000 $ goes towards interest
    - The remaining **$313,727$** goes towards paying down the principal
    - In **period 2**, the outstanding debt is **$ 5 \text{ mil} - 313,727 = 4.69 \text{ mil} $**

  - **PV(interest tax shield)**:
    $$
    PV = r_D \times D \times \tau_C, \text{ discounted at rate } r_D
    $$
  
  - **Tax shield calculation:**
    $$
    \text{Period 1} = \frac{10\% \times 5 \text{ mil} \times 46\%}{1+10\%}, \quad
    \text{Period 2} = \frac{10\% \times 4.69 \text{ mil} \times 46\%}{(1+10\%)^2}, \dots
    $$

- ![example](sun2.png)
- The final APV = base-case NPV + PV(side effects) = $11.16

## **Project valuation with APV**

- Just like the calculation of firm values with APV, you can calculate the APV of projects.
- We follow a similar approach to the NPV estimation:
  - But break apart into base-case NPV and PV(side effects).
- **Note:** for projects, there may be additional side effects:
  - *E.g., issuance costs*.

## Example: Project value with APV

- Your firm is evaluating a potential project:
  - Requires a **$10 million** investment.
  - Offers after-tax cash flows of **$1.8 million/year** for **10 years**.
  - The firm has a **30% target debt-to-equity ratio**:
    - I.e., the firm will use **30% ($3 million) debt** to **70% ($7 million) equity** to finance the project.
  - Unlevered cost of equity is **12%**.
  - The firm can obtain a **bullet loan at a rate of 8%**:
    - Debt issuance costs are **1.5%** of face value.
  - The tax rate is **20%**.

**Q:** *What is the project's APV?*

- There are three differences conceptually between the previous problem and this problem:
  1. **The debt repayment schedule is different**:
     - Instead of fixed payments, this has a **balloon payment** after the end of the project.
     - Interest payments are **constant** throughout the project.
  2. **This is a “project”**, so it will have an **initial outlay**.
  3. **This has an additional side effect**: **issuance costs**.
     - How does this affect calculations?


- ![example](APVex.png)