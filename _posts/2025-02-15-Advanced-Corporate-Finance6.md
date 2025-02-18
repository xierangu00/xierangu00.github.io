---
title: Advanced Corporate Finance - Levered and unlevered cost of capital
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-15   23:14:00 -0500
# image:
# path:
media_subpath: /assets/media
---
# Overview of the financing decision

## The Role of Capital Structure

- **The goal of corporate finance**: make decisions that maximize the value of the firm.
- **In theory**: financing decisions can have a substantial impact on the value of the firm.
- **In practice**: CFOs say financing decisions add the most value.

  - 因为合理的资本结构能**优化资金成本** ，降低财务风险，提高股东回报
- **Financing decisions involve capital structure choices**

  - How much debt is optimal?企业必须在**负债融资** 和**股权融资** 之间找到平衡，以最大化价值
  - What type of debt to issue (e.g., bank loans, public debt, or private debt)?
    - **银行贷款（Bank Loans）** ：通常利率较低，但需要抵押资产。
    - **公开债务（Public Debt）** ：例如公司债券，利率可能更低但需要信用评级。
    - **私募债务（Private Debt）** ：非公开发行，灵活但利率可能较高
- Equity issuance.

## **Leverage**

- **Leverage**: use of debt to finance investment. 杠杆是指使用债务来为投资融资
  - Leverage is a type of risk that is different from typical business risk.
- Illustrative example:
  - Tony uses $400,000 of his own cash to purchase a condo with a total cost of $400,000. Tony is *not using leverage*. **Tony** ：用40万美元现金购买了一套40万美元的公寓，没有使用杠杆
  - Jasmine uses $400,000 of her own cash and borrows $800,000 to purchase a townhouse with a total cost of $1,200,000. Jasmine is *using leverage*.**asmine** ：用40万美元现金+80万美元贷款购买了一套120万美元的联排别墅，使用了杠杆
- **If the properties increase in value by 25%**, then:
  - Tony will have a $100,000 gain on his $400,000 investment, earning a **25% return**.**Tony** ：资产增值10万美元，回报率 **25%**
  - Jasmine’s home will sell for $1,500,000, for a gain of $300,000.
    - This gain on the $400,000 investment is a **75% return**.**Jasmine** ：资产增值30万美元，回报率 **75%** （因杠杆放大）
  - **Takeaway**: *When assets increase in value, leverage works well*.**结论** ：当资产增值时，杠杆可以带来更高的收益
- **If the properties decrease in value by 25%**, then:
  - Tony will have a $100,000 loss on his $400,000 investment, a **25% loss**.**Tony** ：损失10万美元，损失率 **25%**
  - Jasmine’s home will sell for $900,000, for a loss of $300,000.
    - This loss on the $400,000 investment is a **75% loss**.**Jasmine** ：损失30万美元，损失率 **75%** （因杠杆放大）
  - **Takeaway**: *When assets decrease in value, leverage magnifies losses*.**结论** ：当资产贬值时，杠杆会放大损失

## Leverage & Firm Value

- Leverage affects firm value.
- Today, we’ll focus on **3 tools** that help us quantify this effect:
  1. Levering and unlevering beta.**杠杆化和去杠杆化 Beta** （衡量公司系统性风险的指标
  2. Levering and unlevering the cost of equity.**杠杆化和去杠杆化权益成本** （影响公司资本成本和股东回报）
  3. Adjusted Present Value (APV) approach.**调整后的现值法 (APV)** （评估杠杆的财务影响）

# Levered and unlevered beta

## **Beta & leverage**

- Recall: *Cost of Equity* = $r_E = r_F + \beta_E (r_M - r_F)$
  - Beta is a measure of the **risk of equity in comparison to the market**
- Beta and the cost of equity $r_E$ are determined by fundamental decisions managers make
  1. What businesses to be in
  2. How much leverage to use
- If leverage increases → equity beta (and $r_E$) of firm increases
  - Why? As leverage increases, equity investors bear increasing amounts of risk
  - 杠杆增加时，公司的股权 Beta（βE）会上升，因为杠杆加大了投资者所承受的风险
  - 杠杆高的公司，其盈利波动性更大，市场风险溢价更高
- **Intuition**:
  - Fixed payments on debt increase earnings in good times but decrease earnings in bad times**固定债务还款** 会使得公司在经济上行时收益更大，但经济下行时损失更严重
  - Higher leverage → higher *variance* of earnings
    - Which makes investments in the equity *riskier*
    - **更高的杠杆** 意味着**更大的盈利波动** ，使得股票投资变得更**风险更高**

## Levered & unlevered beta

$$
\beta_U = \frac{\beta_L}{1 + (1 - \tau_c) \left(\frac{D}{E}\right)}

$$

- Where:
  - $\beta_L$ = firm's beta with leverage
    - That is, the equity beta you get from stock price data or Bloomberg
    - 市场上观测到的 Beta，包含了公司的资本结构影响
  - $\tau_c$ = the corporate tax rate
  - $\frac{D}{E}$ = debt-to-equity ratio of the firm
  - $\beta_U$ is the **unlevered beta** or asset beta
    - That is, what would be the firm beta if the firm had zero leverage (when $D = 0$)
    - 剔除杠杆影响后的 Beta，衡量公司**仅受业务风险影响的 Beta**
    - 用于跨公司比较，因为它不受资本结构影响

## Example: Effect of leverage on beta

- Based on stock price data from 2008-2013, Disney’s beta is 1.25

  - The average debt-to-equity ratio over the period was 19.44%
  - Marginal corporate tax was 36.1%
- **What is the unlevered beta?**
- **What would the levered beta be if the debt-to-equity ratio changed to 10%?**
- First, compute unlevered beta:

$$
\beta_U = \frac{\beta_L}{1 + (1 - \tau_c) \left(\frac{D}{E}\right)}
= \frac{1.25}{1 + (1 - .361)(.1944)} = 1.1119

$$

- Second, re-lever beta assuming a debt-to-equity ratio of 10%?
  - Rewrite to solve for $\beta_L$:

$$
\beta_L = \beta_U \left[ 1 + (1 - \tau_c) \left(\frac{D}{E}\right) \right]

$$

- Knowing $\beta_U$ from the previous calculation, then:

$$
\beta_L = 1.1119 \times \left[ 1 + (1 - 0.361)(.10) \right] = 1.1829

$$

- 降低债务权益比（D/E）可以降低杠杆 Beta（𝛽𝐿），即降低股票的市场风险
- 增加杠杆会提高 Beta，增加股东风险
- 结论：
  - Beta 衡量股票的市场风险，杠杆会影响 Beta。
  - 杠杆 Beta（𝛽𝐿）受资本结构影响，无杠杆 Beta（𝛽𝑈）仅衡量公司的业务风险。
  - 高杠杆公司在市场上行时回报更大，但市场下行时风险更高。
  - 调整资本结构可以降低或增加 Beta，影响公司的股票风险和资本成本。

## **𝛽U vs. 𝛽L: intuition of example**

- As leverage increases, the risk of equity increases
- Consistent with this, 𝛽L increases
- ![beta](betalu.png)
  Step by step:
- Initial state:
  - Firm has 19.4% D/E
  - Estimated beta from stock returns reflects the 19.4% D/E
- Plans:
  - Decrease to 10% D/E
  - What will beta be?
  - (We need to estimate beta in to re-estimate 𝑟𝐸 and WACC to evaluate future projects)
- Challenge:
  - Can’t directly estimate beta from the stock returns, since the stock returns reflect the current 19.4% D/E
- Solution:
  1. Unlever beta: find beta (equity risk) if D = 0
  2. Re-lever beta to 10% D/E

* 核心思想：

  * **杠杆越高，股权风险越大** → **βL****（杠杆**** Beta** **）增加**
  * **当公司没有杠杆时** （D/E=0），**βL=βU ** （无杠杆 Beta）
  * **如果公司的资本结构变化（债务权益比变化），需要先去杠杆化（** **Unlever** **）再重新加杠杆（** **Re-lever** **）**，需要重新计算**** Beta** 以用于 WACC 估算
  * **无杠杆**** Beta** **（** **βU** **）是业务风险的真实衡量，不受资本结构影响**
  * **杠杆**** Beta** **（** **βL** **）用于计算股权成本，影响**** WACC**

## **More adjustments if debt beta ≠ 0**

- In practice, financial professionals assume that debt carries no market risk (i.e., it has a beta of 0). Hence:

$$
\beta_U = \frac{\beta_L}{1 + (1 - \tau_c) \left(\frac{D}{E}\right)}

$$

- But sometimes debt does carry market risk, in which case we can estimate the unlevered beta using:

$$
\beta_U = \frac{\beta_L + \beta_D (1 - \tau_c) \left(\frac{D}{E}\right)}{1 + (1 - \tau_c) \left(\frac{D}{E}\right)}

$$

- This may be more realistic, but it’s typically hard to estimate beta for debt and it is often small for firms for which we can estimate it (~between 0.0 and 0.2).
- 传统假设是债务无市场风险，这时**βD=0**，意味着**债务不会受到市场波动的影响**，在这种情况下，公司的风险全部归因于股权（βL），债务不会对市场 Beta 造成额外影响
- **如果债务市场 Beta 不为0，βL 就不能单独代表公司的市场风险** ，需要额外考虑债务风险对 Beta 的贡献

# Levered and unlevered cost of capital

## **WACC & leverage**

- Recall: we used the WACC as the discount rate (or hurdle rate) for investment decisions because it reflects the firm’s current financing mix (i.e., its debt and equity)
  - **WACC（加权平均资本成本）** 一般用作投资决策的折现率（即项目最低可接受收益率），因为它反映了企业当前的融资结构（即 **债务 + 股权** ）。
- However, if a new project (or potential M&A deal) involves large changes in capital structure, then 但当企业的资本结构发生重大变化（如并购、融资等），WACC 可能不再适用
  - WACC may not be the appropriate discount rate
  - (E.g., we used the post-merger WACC for Urbanspoon acquisition)
- Sometimes, you may need to use the **unlevered cost of equity** instead of the levered cost of equity **解决方案** ：可以使用 **非杠杆股权成本（Unlevered Cost of Equity）** 进行评估，然后单独加入债务的影响
  1. Evaluate the project as if it were zero debt (using $r_U$)先假设项目**没有债务**
  2. Then we separately add the effects of debt然后再**单独考虑债务的影响**

## Levered & unlevered cost of equity

- Before, we had:

  $$
  Cost\ of\ Equity = r_E = r_F + \beta_E (r_M - r_F)

  $$
- Alternatively, we can express the cost of equity as a function of the **unlevered cost of equity** and **cost of debt**:**如果考虑资本结构的影响** ，可以将 **杠杆股权成本** 表达为 **非杠杆股权成本（Unlevered Cost of Equity）** 和 **债务成本（Cost of Debt）** 的函数

  $$
  r_E = r_U + (r_U - r_D) \left(\frac{D}{E}\right) (1 - \tau_c)

  $$
- Where:

  - $r_U$ = unlevered cost of equity 非杠杆股权成本
  - $r_D$ = cost of debt
  - $\frac{D}{E}$ = debt-to-equity ratio 债务-股权比率
  - $\tau_c$ = corporate tax rate

## Example: Unlevered cost of equity

- **JAX** has 1 million shares of stock outstanding
  - Stock sells for **$50** a share
- The firm’s debt is publicly traded and was recently quoted at **90%** of the face value
  - Face value is **$30 million**
- JAX has an **equity beta** of **1.2**
- The **corporate tax rate** is **40%**
- The firm has a **levered cost of equity** of **15.5%**
- The firm has a **cost of debt** of **6.0%**

**What is the unlevered cost of equity?**

- **E**: $1 \text{ million shares} \times \$50/\text{share} = \$50 \text{ million}$
- **D**: $0.90 \times \$30 \text{ million} = \$27 \text{ million} \Rightarrow \frac{D}{E} = \frac{27}{50} = 54\%$

$$
r_E = r_U + (r_U - r_D) \left( \frac{D}{E} \right) (1 - \tau_c)

$$

$$
0.155 = r_U + (r_U - 0.06) \times 0.54 \times (1 - 0.4)

$$

$$
0.155 = r_U + 0.324 \times r_U - 0.01944

$$

$$
1.324 \times r_U = 0.1744

$$

$$
r_U = 0.1318 = 13.2\%

$$

- 重要结论：
  1.	非杠杆股权成本（rU = 13.2%）低于杠杆股权成本（r_E = 15.5%），因为债务的存在增加了股东的风险，导致股东要求更高的回报率。
  2.	企业的债务比率越高，杠杆股权成本（rE ）就越高，但债务成本通常较低，因为债务有税盾效应（1−τc）。
