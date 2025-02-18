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
# Adjusted Present Value (APV)

## **Different investment valuation methods**

1. **Weighted average cost of capital (WACC) approach**
   - NPV calculations where one discounts the free cash flows of a target firm or investment project with WACC
   - $ Value = \sum_{t=0}^{\infty} \frac{FCF_t}{(1 + WACC)^t} $
2. **Multiples and comparable firm approach**
3. **Adjusted Present Value (APV)**-->调整现值法（Adjusted Present Value, APV）是一种投资估值方法，主要用于评估融资方式对项目价值的影响。
   - Discount cash flows as if the firm was funded with equity only
   - Then, add the present value of tax shield and other “financial side effects” of debt

## **APV: The fundamental idea**

- ![Graph](APV.png)
- APV unbundles components of value and analyzes each one separately
- (Whereas WACC bundles all financing side effects into the discount rate)

* **基准情况的价值（Base-case value）** ：假设项目完全由权益资本融资计算出的价值。
* **融资的影响（Financing side effects）** ：包括税盾、金融困境成本、补贴、对冲、发行成本等因素的影响。

## **APV consists of 3 steps**

1. **Calculate NPV of a project or target firm assuming it is financed with equity only** 计算假设**无债务融资** 情况下的NPV，使用无杠杆权益成本（rU）折现
   - Being financed with only equity implies always using the “cost of unlevered equity,” $r_U$, for discounting
   - *Note: This is often called the “base-case NPV”*
2. **Calculate NPV of each financing item**
   - For example, the present value of an interest tax shield
   - *Note: These are often called “side effects”*
3. **Add the base-case NPV and the NPV of each financing item together to get APV**

---

## **APV in formulas**

$$
APV = V_{Levered} = V_{Unlevered} + PV(SideEffects)

$$

- $V_{Levered}$ = value accounting for how project is financed 考虑资本结构后的项目价值
  - i.e., what mix of equity and debt is used
- $V_{Unlevered}$ = value *not* accounting for how project is financed 假设完全由权益资本融资的价值
  - But rather assuming all equity financing
  - “Base-case NPV” (or “base-line NPV”)
- $PV(SideEffects)$ = present value of financing side effects融资带来的税盾、金融困境成本等现值
  - E.g., interest tax shields

---

## **Step 1: Calculate $V_{Unlevered}$**

$$
V_{Unlevered} = \sum_{t=0}^{\infty} \frac{FCF_t}{(1 + r_U)^t}

$$

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

## **Calculating debt and interest payments** 债务结构和利息支付方式

- When structuring a loan, some firms like to have equal debt payments over the life of a loan

  - This is often referred to as a **"standard amortizing loan"**
- With this approach, a large percentage of a firm’s payments are applied to interest in the early years of the loan

  - In the later years, the outstanding balance slowly declines, and so more and more of each payment is applied to paying down the balance (i.e., the principal amount)
  - 在贷款的整个生命周期内，每期偿还的总金额（本金+利息）是相等的。
  - 这种方法适用于希望均衡偿还贷款的公司。
  - **利息与本金的关系：**
    - 在早期，大部分还款用于支付利息，而本金偿还较少。
    - 随着时间推移，本金余额减少，每期的利息支付也随之减少，因此更多的付款用于偿还本金。
- In Excel, you can use the **PMT** function to calculate the periodic payment for a standard amortizing loan

  - `=PMT(interest rate, # of periods, loan amount)`
- When structuring a loan, some firms like to only make interest payments in the early periods and pay off the entire principal of the loan at the end

  - This is often referred to as a **"bullet loan"** 子弹贷款
  - 只需在贷款期间支付利息，而本金在最后一期一次性偿还。
  - 适用于需要前期现金流自由度较高的公司，例如项目融资、债券融资等。
- With this approach, the payment is constant through the initial years and equal to the interest rate on the loan; the final period payment is interest plus principal

  - 前期：仅支付贷款利息，不偿还本金。
  - 最后一笔付款：包括所有未偿还的本金 + 最后一期的利息。

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
- 总结
- **1. 两种方法的共同点**

  - **NPV 和 APV 计算的最终价值是等效的**
  - 都需要扣除初始投资
- **2.NPV（净现值）方法**

  - NPV 需要每期重新计算 WACC，以考虑融资结构的变化：
  - 以税后现金流为基础
  - 通过 WACC（加权平均资本成本） 进行贴现
  - 债务的好处（如税盾）被内嵌到 WACC 中，减少贴现率
- **3.APV（调整现值）方法**

  - APV 以无杠杆现金流（即假设全部由股权融资）为基础
  - 使用 无杠杆股权成本（Unlevered cost of equity） 进行贴现
  - 单独计算融资的副作用（如税盾），并将其加回无杠杆 NPV
  - 这种方法明确地分离了融资对项目价值的影响
- **4.关键区别**

  - NPV 方法 将债务带来的收益（如税盾）包含在WACC 贴现率中，而不直接计算融资副作用。
  - APV 方法 先计算无杠杆 NPV，再单独计算债务带来的副作用（如税盾、补贴等），然后加总。
- **5.适用场景**

  - NPV 适用于融资结构稳定的公司，因为 WACC 在长期保持不变，计算简单。
  - APV适用于融资结构可能发生变化的情况（如杠杆收购、项目融资等），因为它分开计算融资副作用，更加灵活。

## **When to use APV over NPV**

- **APV** is often an easier calculation for decisions with **large fluctuations in the firm’s leverage** APV 适用于 公司杠杆率发生大幅波动的决策，相比 NPV 更易于计算。

  - **Example: the project**

    - Needs an initial outlay that can be financed internally
    - But will need a large outlay in 5 years that will need to be funded with long-term debt that will have a long-term impact on the firm’s leverage
    - Should be evaluated using APV, as APV only requires debt outstanding year-by-year
  - APV适用于杠杆率变化较大的项目
    - 需要一笔 **初始投资** ，可通过内部融资解决，5年后需要一笔大额支出** ，需要通过长期债务融资，会影响公司的长期杠杆率，由于杠杆率变化较大，**使用 APV 更合适** ，因为APV **只需考虑逐年变化的债务** ，不需要像NPV 那样反复调整WACC
- **APV is also commonly used for LBO valuations**

  - A **leveraged buyout (LBO)** is an acquisition by a financial sponsor, financed using significant amounts of debt
  - Typically, there will be high debt initially but expectations that it will be paid down over time, leading to variations in a firm’s leverage

  - APV **适用于杠杆收购（** **LBO** **）估** **值**
    - **LBO（Leveraged Buyout）** 是由金融机构通过大量债务融资进行的收购。
    - **特点**
      - 初期**债务水平很高** 
      - 未来 **杠杆率会逐渐下降** ，因为企业通常会用盈利偿还部分债务。
      - **杠杆率变化显著** ，因此使用APV 更适合，因为APV **能够逐年单独计算债务的影响** ，而NPV 方法需要不断调整WACC 来适应杠杆变化。

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


| Base-case value                                                            | Value of all financing side effects |
| ---------------------------------------------------------------------------- | ------------------------------------- |
| **APV** = value of the project as if it were financed entirely with equity | + interest tax shields              |
|                                                                            | + costs of financial distress       |
|                                                                            | + subsidies                         |
|                                                                            | + hedges                            |
|                                                                            | + issue costs                       |
|                                                                            | + other costs                       |

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
