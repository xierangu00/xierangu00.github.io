---
title: Advanced Corporate Finance - Introduction & investment decision rules
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-12   14:10:00 -0500
# image:
# path:
media_subpath: /assets/media
---
# **Corporate finance decisions and the goal of the firm**

## **The finance function**

* The financial manager should be viewed as a custodian of value that serves as an intermediary between the firm’s operations and capital markets
* The financial manager has three main tasks:
  1. Investment decisions: which projects to invest in (e.g., building a new plant, investing in R&D)
  2. Financing decisions: capital structure (how to raise funds – get a bank loan, sell stock, …)
  3. Payout decisions: whether/when/how to return capital to investors
* ![Graph](Finance Function.png)
* These threee tasks tend to be closely related
* Profits from investment decisions --> financing decisions --> payout decisions
* These decisions entail many different types of assets
  - Real assets: land, building, cars, commodities,...
  - Financial assetsL cash, stocks, bonds, ...

## **Corporations**

* Corporation: a business owned by many stockholders and tun by professional managers
* ![Graph](Corporations.png)

## **Features of a corporation**

* Legally distinct from its owners
  - i.e., a legal entity
  - Can borrow/lend money, sue or be sued, and pay its taxes (but cannot vote)
* Limited liability of stockholders
  - Stockholders are not financially responsible for debt
  - For Example, if you buy shares of Nissan and the firm then goes bankrupt, nobody comes to your house and takes your car away
* Separation of ownership and control
  - Stockholders own the firm but do not manage it
  - Instead, stockholders elect a board of directors to represent them
  - Advantage: ownership can change without affecting the firm's operations
  - Disadvantges: issues of misalignment of incentives, conflicts of interest, moral hazard, etc. (need good corporate governance)

## **The financial manager**

* Who is the financial manager?
  - Key financial managers: Chief Financial Officer (CFO), Treasurer, Controller (for larger companies)
  - In the largest companies, financial managers may report to the CFO
* The financial manager’s job entails understanding:
  - Capital markets
  - The effects of time on value
  - The effects of risk on value
  - Valuation and investment decisions
  - Investors’ desires
  - Communicating effectively with investors
* What is the manager’s ultimate objective?

## **The classic objective function**

* Financial managers are meant to maximize the payoffs of the firm’s owners
  - Who are the firm’s owners?
  - Many claim-holders have a stake in the firm’s income
  - But shareholders are ultimately the owners → Financial managers need to act in their interest
* What are the payoffs?
  - Shareholders are made better off by any decision which increases the value of their stake in the firm
  - So, managers should maximize the value of the shares of the firm
    - Shareholders can use financial markets (e.g., save, invest) to move this value across time
    - What about a firm’s social responsibility, worker ethics, etc.? Theoretically, these appear in the share value
  - Maximizing value is more complex than maximizing profit
    - Time value of money and risk

## **Utopian world vs. reality**

* In a utopian world, managers maximize shareholder value
* In reality, there can be conflicts of interest
  - The goals of different the parties are incompatible
  - Between managers (e.g., those who want to maximize their own payoff) and stockholders, among others that have claims (banks, customers, etc.)
* How can we incentivize managers to maximize shareholder value?
  - Compensation: stock options, restricted stock, etc. (pay off if shares’ values increase)
  - Market pressure: reputation in managerial labor markets, customer/investor backlash
  - Governance: boards, hostile takeovers, laws

## **Maximizing Share Price ≠ Maximizing Firm Value**

- **Maximizing firm value** equals maximizing stock price **only if**:
  - Financial markets are efficient.
  - Investors are rational.
- However, these conditions might not always hold true, particularly in the short term:
  - A manager might focus on short-term stock price at the expense of long-term value, which can harm both society and long-term investors.
- **In this class, we will always consider maximizing firm value:**
  - It's beneficial for society.
  - It reflects how we want managers to behave.
  - We assume consequences for managers who do not follow this objective.

# **Investment decision rules (NPV and IRR)**

## **5 Principles of Investment Decisions**

1. **Decisions are based on cash flows, not on accounting income**

   - The relevant cash flows are incremental, i.e., the changes in cash if a project is undertaken.
   - Sunk costs (costs that cannot be avoided even if the project is not taken) should not be included in incremental cash flows.
   - Potential cannibalization effects that a new project may have on other firm cash flows should be considered.
2. **Cash Flows are based on opportunity costs**

   - Opportunity costs are the cash flows a firm loses by taking the new investment. These are included in incremental cash flows.
   - When doing an analysis, go through each of the assets a firm already owns and think about how they will each be affected.
3. **The timing of Cash Flows is important**

   - Investment decisions account for the time value of money using Net Present Value (NPV) calculations.
   - The fundamental idea of NPV: Cash Flows received earlier are worth more than Cash Flows received later because of the time value of money.
   - NPV = sum of the present values of expected incremental cash flows if a project is undertaken, where:
   - The NPV formula is:

$$
NPV = CF_0 + \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + \ldots + \frac{CF_T}{(1+r)^T}

$$

>  - (CF_0) is the initial outlay (a negative cash flow),
>  - (CF_t) is the after-tax cash flow at time \( t \),
>  - (r) is a required rate of return for the project,
>  - (T) is the duration of the project.

4. **Cash Flows are analyzed on an after-tax basis**

   - The impact of taxes must be considered because firm value is based on Cash Flows that investors get to keep, not those sent to the government.
   - Key tax considerations include tax credits, depreciation, amortization (cost of use of assets, debts), and interest expenses.

5. **Financing costs are reflected in the project’s required rate of return**

   - Do not consider financing costs specific to the project when estimating incremental cash flows.
   - Instead, financing costs are reflected by the project's required rate of return:
     - The discount rate in the NPV equation, which we use to evaluate the project, takes into consideration the firm's cost of capital.
     - This rate is higher than the firm’s cost of capital if the project is riskier than the average firm project, and analogously, less than the firm's cost of capital if less risky.
   - Only projects that return more than the cost of capital (or required rate of return) will increase firm value.

## **NPV catch up**
### **NPV using Formula**
Using the project cash flows, determine whether each project should be rejected or accepted, assume the cost of capital is 10%
- Time 0 = current period (beginning of first period)
  - Often when cash outflow occurs
- Time 1 = One period from now (end of first period)
  - Often when cash inflow begin

![Graph](NPV.png)
The NPV calculations for two projects are as follows:
- **Project A**:
  $$NPV = -2,000 + \frac{1,000}{(1+0.10)^1} + \frac{800}{(1+0.10)^2} + \frac{600}{(1+0.10)^3} + \frac{200}{(1+0.10)^4} = \$157.6$$
- **Project B**:
  $$NPV = -2,000 + \frac{200}{(1+0.10)^1} + \frac{600}{(1+0.10)^2} + \frac{800}{(1+0.10)^3} + \frac{1,200}{(1+0.10)^4} = \$98.35$$

Would you accept the projects? If you had to choose only one project, which would you choose and why?
  - Both projects have positive NPVs, indicating that they are expected to add value to the firm after considering the cost of capital at 10%. This suggests that if possible, both projects should be accepted as they offer returns greater than the required rate
  - However, if you must choose only one project, **Project A** would be the preferable choice because it has a higher NPV of $157.6 compared to $98.35 for Project B. This means that Project A is expected to generate more value over its life relative to the initial investment and the firm’s cost of capital. Project A provides a higher return on investment, making it the more attractive option between the two.

### **NPV using Excel**
![Graph](NPVexcel.png)
- Excel NPV formula assumes
  - The First CF is one period after the beginning of the investment
  - The last CF is the cash flow at the end of the list
- If the first CF occurs at time 0 (which is very common)
  - Add first CF to Excel NPV result (as in the previous example)
  - Do not include the first CF in the values arguments


## **IRR catch up**
This is the most important alternative to NPV:
- Often used in practice, and it is intuitively appealing.
- It is based entirely on the estimated cash flows, and it is independent of interest rates found elsewhere.

### **IRR's definition:**
The discount rate at which the project’s NPV equals zero:

$$ NPV = 0 = CF_0 + \frac{CF_1}{(1+IRR)^1} + \frac{CF_2}{(1+IRR)^2} + \ldots + \frac{CF_T}{(1+IRR)^T} $$

### Investment rule:
Accept projects with a greater IRR than the opportunity cost of capital.

### Example Calculations:
![Graph](NPV.png)
- **Project A**: 
  $$ NPV_A = 0 = -2,000 + \frac{1,000}{(1+IRR_A)^1} + \frac{800}{(1+IRR_A)^2} + \frac{600}{(1+IRR_A)^3} + \frac{200}{(1+IRR_A)^4} \rightarrow IRR_A = 14.49\% $$
- **Project B**:
  $$ NPV_B = 0 = -2,000 + \frac{200}{(1+IRR_B)^1} + \frac{600}{(1+IRR_B)^2} + \frac{800}{(1+IRR_B)^3} + \frac{1,200}{(1+IRR_B)^4} \rightarrow IRR_B = 11.79\% $$

These calculations find the discount rate at which the present value of the cash flows, resulting in a net present value of zero. The IRR for each project represents the break-even rate of return, above which an investment would yield a positive return.

Would you accept these projects based on their IRR compared to an opportunity cost of capital of, say, 10%? 
- Project A with an IRR of 14.49% and Project B with an IRR of 11.79% both exceed this rate, suggesting both projects should be accepted.

### **IRR's definition:**
IRR can also be computed using Excel
### Option 1 : Using IRR forumula
![Graph](IRR.png)
### Option 2: Using Goal Seek
![Graph](GoalSeek.png)
- Data->What-if analysis --> Goal Seek
  1. Set cell : NPV
  2. To Value: 0
  3. By changing cell: Disc.rate

## **Sensitivity analysis and NPV profiles**
![Graph](Sensitivity Analysis.png)

## **NPV vs. IRR**
If used properly, the NPV and IRR rules will generally give the same decision outcome. However, there are exceptions:
- **Non-conventional cash flows**: Cash flow signs change more than once over time. For example, there are interim maintenance costs exceeding revenues from the project at the periods (net cash outflows).
- **Mutually exclusive projects**: Initial investments are substantially different, or the timing of cash flows is substantially different.
- **Be careful when borrowing**: Changes decision rule.


## **NPV & IRR Rules vs. Maximizing Share Value**

- Choosing investments where \( NPV > 0 \) (meaning \( IRR > \) required rate of return) is equivalent to maximizing shareholder wealth and payoffs:
  - This holds especially when markets are efficient and investors are rational.
- Why is this approach effective?
    - **Positive-NPV Projects:** These yield (expected) payoffs that are higher than the outside option (given by the required rate of return). This means that these projects offer a higher payoff than other investments with the same risk, such as investing in other stock/projects.
    - **Capital Market Utilization:** Shareholders can use capital markets to allocate their wealth over time. This allows them to distribute positive-NPV project outcomes across time to meet their preferences, whether they prefer cash today or more in the future.
- Implications:
  - By following NPV and IRR rules, companies essentially aim to increase the value of their shares, assuming rational behaviors and efficient markets. Positive-NPV projects directly contribute to raising a company's stock price, thereby benefiting shareholders by providing them the flexibility to manage their investments according to their financial goals.
