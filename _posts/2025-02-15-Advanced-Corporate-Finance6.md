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
  - *Why?*  
- **Financing decisions involve capital structure choices**  
  - How much debt is optimal?  
  - What type of debt to issue (e.g., bank loans, public debt, or private debt)?  
- Equity issuance.  

## **Leverage**
- **Leverage**: use of debt to finance investment.
  - Leverage is a type of risk that is different from typical business risk.
- Illustrative example:
  - Tony uses $400,000 of his own cash to purchase a condo with a total cost of $400,000. Tony is *not using leverage*.
  - Jasmine uses $400,000 of her own cash and borrows $800,000 to purchase a townhouse with a total cost of $1,200,000. Jasmine is *using leverage*.
- **If the properties increase in value by 25%**, then:
  - Tony will have a $100,000 gain on his $400,000 investment, earning a **25% return**.
  - Jasmine’s home will sell for $1,500,000, for a gain of $300,000.
    - This gain on the $400,000 investment is a **75% return**.
  - **Takeaway**: *When assets increase in value, leverage works well*.
- **If the properties decrease in value by 25%**, then:
  - Tony will have a $100,000 loss on his $400,000 investment, a **25% loss**.
  - Jasmine’s home will sell for $900,000, for a loss of $300,000.
    - This loss on the $400,000 investment is a **75% loss**.
  - **Takeaway**: *When assets decrease in value, leverage magnifies losses*.

## Leverage & Firm Value
- Leverage affects firm value.
- Today, we’ll focus on **3 tools** that help us quantify this effect:
  1. Levering and unlevering beta.
  2. Levering and unlevering the cost of equity.
  3. Adjusted Present Value (APV) approach.

# Levered and unlevered beta
## **Beta & leverage**
- Recall: *Cost of Equity* = $r_E = r_F + \beta_E (r_M - r_F)$
  - Beta is a measure of the **risk of equity in comparison to the market**
- Beta and the cost of equity $r_E$ are determined by fundamental decisions managers make
  1. What businesses to be in
  2. How much leverage to use
- If leverage increases → equity beta (and $r_E$) of firm increases
  - Why? As leverage increases, equity investors bear increasing amounts of risk
- **Intuition**:
  - Fixed payments on debt increase earnings in good times but decrease earnings in bad times
  - Higher leverage → higher *variance* of earnings
    - Which makes investments in the equity *riskier*

## Levered & unlevered beta
$$
\beta_U = \frac{\beta_L}{1 + (1 - \tau_c) \left(\frac{D}{E}\right)}
$$
- Where:
  - $\beta_L$ = firm's beta with leverage
    - That is, the equity beta you get from stock price data or Bloomberg
  - $\tau_c$ = the corporate tax rate
  - $\frac{D}{E}$ = debt-to-equity ratio of the firm
  - $\beta_U$ is the **unlevered beta** or asset beta
    - That is, what would be the firm beta if the firm had zero leverage (when $D = 0$)

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


# Levered and unlevered cost of capital
## **WACC & leverage**
- Recall: we used the WACC as the discount rate (or hurdle rate) for investment decisions because it reflects the firm’s current financing mix (i.e., its debt and equity)
- However, if a new project (or potential M&A deal) involves large changes in capital structure, then
  - WACC may not be the appropriate discount rate
  - (E.g., we used the post-merger WACC for Urbanspoon acquisition)
- Sometimes, you may need to use the **unlevered cost of equity** instead of the levered cost of equity
  1. Evaluate the project as if it were zero debt (using $r_U$)
  2. Then we separately add the effects of debt

## Levered & unlevered cost of equity

- Before, we had:

  $$Cost\ of\ Equity = r_E = r_F + \beta_E (r_M - r_F)$$

- Alternatively, we can express the cost of equity as a function of the **unlevered cost of equity** and **cost of debt**:

  $$r_E = r_U + (r_U - r_D) \left(\frac{D}{E}\right) (1 - \tau_c)$$

- Where:
  - $r_U$ = unlevered cost of equity  
  - $r_D$ = cost of debt  
  - $\frac{D}{E}$ = debt-to-equity ratio  
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
