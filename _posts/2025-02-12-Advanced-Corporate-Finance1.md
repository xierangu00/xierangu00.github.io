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

* The **financial manager** should be viewed as a custodian of value that serves as an **intermediary between the firm’s operations and capital markets** 财务经理应被视为价值的保管人，充当公司运营与资本市场之间的中间人
* The financial manager has three main tasks:
  1. **Investment decisions**: which projects to invest in (e.g., building a new plant, investing in R&D)
     * **投资决策**: 金融经理需要决定企业应该投资哪些项目，例如建立新工厂、投资研发等。这称为资本预算（Capital Budgeting）。正确的投资决策可以帮助公司扩大其业务并提高其长期盈利能力。
  2. **Financing decisions**: capital structure (how to raise funds – get a bank loan, sell stock, …)
     * **融资决策**: 这涉及如何筹集资金来支持企业的运营和扩展，包括选择银行贷款、发行股票或其他债务工具等方式。这些决策将决定公司的资本结构，即公司的债务与股本的比例，直接影响公司的风险和回报率。
  3. **Payout decisions**: whether/when/how to return capital to investors
     * **支付决策**: 这涉及决定是否、何时以及如何将资本回报给投资者，例如通过股息或股票回购。支付政策应与公司的长期战略和资本需要相协调
* ![Graph](Finance Function.png)
* These threee tasks tend to be **closely related**
* **Profits from investment decisions --> financing decisions --> payout decisions**
* These decisions entail many different types of assets
  - Real assets: land, building, cars, commodities,...
  - Financial assetsL cash, stocks, bonds, ...

## **Corporations**

* Corporation: a business owned by many stockholders and tun by professional managers
* ![Graph](Corporations.png)
* 尽管公司数量不如独资企业多，但它们在总收入中占有压倒性的比例，反映了公司相比于其他企业形式在资本积累和经营规模上的优势。这种情况通常是因为公司能够通过发行股票和债券来获得更多资金，支持更大规模的运营和投资。此外，公司通常由专业经理人管理，这可能有助于实现更高效的运营和更大的市场扩张。

## **Features of a corporation**

* Legally distinct from its owners

  - i.e., a legal entity
  - Can borrow/lend money, sue or be sued, and pay its taxes (but cannot vote)

  * 公司是一个独立的法律实体，这意味着它可以像个人一样进行借贷、提起诉讼或被起诉，并且需要独立缴纳税款。然而，作为一个实体，公司本身没有投票权。
* Limited liability of stockholders

  - Stockholders are not financially responsible for debt
  - For Example, if you buy shares of Nissan and the firm then goes bankrupt, nobody comes to your house and takes your car away

  * 公司股东的财务责任限于他们对公司股份的投资。这意味着如果公司破产，股东不需要用个人资产来偿还公司债务，他们的最大损失仅限于他们投资的金额。
* Separation of ownership and control

  - Stockholders own the firm but do not manage it
  - Instead, stockholders elect a board of directors to represent them
  - Advantage: ownership can change without affecting the firm's operations-->所有权与控制权的分离允许公司的所有权在股东之间转换，而不影响公司的运营
  - Disadvantges: issues of misalignment of incentives, conflicts of interest, moral hazard, etc. (need good corporate governance)-->这种分离可能导致激励不对称、利益冲突和道德风险等问题

  * 股东拥有公司，但不直接参与公司的日常管理。公司的管理由董事会负责，董事会由股东选举产生，代表股东利益行使管理职权。

## **The financial manager**

* Who is the financial manager?
  - Key financial managers: Chief Financial Officer (CFO), Treasurer, Controller (for larger companies)
  - In the largest companies, financial managers may report to the CFO
* The financial manager’s job entails understanding:
  - Capital markets-->了解和利用资本市场来筹集资金，以及如何有效地投资
  - The effects of time on value-->理解时间价值的概念，如现金流的现值和未来值
  - The effects of risk on value-->评估投资风险和其对资产价值的影响
  - Valuation and investment decisions-->进行资产和投资项目的估值，作出投资决策
  - Investors’ desires-->了解和满足投资者的财务需求和预期
  - Communicating effectively with investors--> 保持透明和开放的沟通，确保投资者理解公司的财务状况和前景
* What is the manager’s ultimate objective?
  * 金融经理的最终目标是增加公司的股东价值。

## **The classic objective function**

* Financial managers are meant to maximize the payoffs of the firm’s owners
  - Who are the firm’s owners?
    - Many claim-holders have a stake in the firm’s income
    - But **shareholders** are ultimately the owners → Financial managers need to act in their interest
    - 公司的所有者主要是股东，他们通过持有公司的股份来拥有公司的一部分。虽然公司可能有多种利益相关者（如债权人、员工等），但股东是公司的最终所有者
* What are the payoffs?
  - Shareholders are made better off by any decision which **increases the value of their stake in the firm** --> 股东的回报通常来自公司价值的增加，这可能表现为股价上涨、分红支付等。
  - So, managers should maximize the value of the shares of the firm-->金融经理的任务是通过合理的决策和资源分配来增加股东的这种收益
    - Shareholders can use financial markets (e.g., save, invest) to move this value across time
    - What about a firm’s **social responsibility, worker ethics**, etc.?
      - Theoretically, these appear in the **share value**
  - Maximizing value is more complex than maximizing profit
    - Time value of money and risk ---> 最大化价值比简单的利润最大化更为复杂，因为它需要考虑资金的时间价值和相关风险

## **Utopian world vs. reality**

* In a utopian world, managers maximize shareholder value
* In reality, there can be conflicts of interest
  - The goals of different the parties are incompatible
  - Between managers (e.g., those who want to maximize their own payoff) and stockholders, among others that have claims (banks, customers, etc.)
* How can we incentivize managers to maximize shareholder value?
  - Compensation: stock options, restricted stock, etc. (pay off if shares’ values increase)-->通过股票期权、限制性股票等形式的薪酬，将管理者的报酬与公司股价表现挂钩，以激励他们作出增加股东价值的决策
  - Market pressure: reputation in managerial labor markets, customer/investor backlash -->管理者需要维护其在经理人劳动市场中的声誉，这意味着他们必须有效地管理公司以避免投资者或客户的反弹
  - Governance: boards, hostile takeovers, laws --> 董事会、敌意收购和法律规定可以作为监督管理者行为的机制，确保他们的决策符合股东的最佳利益

## **Maximizing Share Price ≠ Maximizing Firm Value**

- **Maximizing firm value** equals **maximizing stock price** ***only if***:
  - **Financial markets are efficient**.
  - Investors are rational.
  - 理论上，最大化公司价值等同于最大化股价的情况只有在金融市场完全有效和投资者完全理性的前提下才成立。这意味着市场能够准确反映所有可用信息在股价中，投资者总是做出最优的决策
- However, these conditions might not always hold true, particularly in the short term:短期内最大化股价可能并不等同于最大化公司的长期价值。
  - A manager might focus on short-term stock price at the expense of long-term value, which can harm both society and long-term investors.
  - 管理者可能通过牺牲公司的长期利益（如减少研发支出）来短期提高股价，这对社会和长期投资者是不利的
- **In this class, we will always consider maximizing firm value:**
  - It's beneficial for society.
  - It reflects how we want managers to behave.
  - We assume consequences for managers who do not follow this objective.

# **Investment decision rules (NPV and IRR)**

## **5 Principles of Investment Decisions**

1. **Decisions are based on cash flows, not on accounting income** --> **基于现金流而非会计收入的决策**

   * **Only consider incremental cash flows, and neglect sunk costs**
   * **Consider potential cannibalization effects**
     * The relevant cash flows are **incremental**, i.e., the changes in cash if a project is undertaken.
     * **Sunk costs** (costs that cannot be avoided even if the project is not taken) should not be included in incremental cash flows.
     * Potential cannibalization effects that a new project may have on other firm cash flows should be considered.
       * 例如，如果一个公司推出一个新产品，但它会部分**抢占已有产品的市场份额** ，那么这种负面影响应该计入增量现金流
2. **Cash Flows are based on opportunity costs**

   - Opportunity costs ≠ sunk costs
   - **Should include Opportunity costs in incremental cash flows**
     - Opportunity costs are the cash flows a firm loses by taking the new investment.
     - When doing an analysis, go through each of the assets a firm already owns and think about how they will each be affected.
3. **The timing of Cash Flows is important**

   - Investment decisions account for the time value of money using **Net Present Value (NPV)** calculations.
   - The fundamental idea of NPV: Cash Flows received earlier are worth more than Cash Flows received later because of **the time value of money**.
     - 早期收到的现金流（CFs）比晚期的现金流更有价值-->这是因为资金可以再投资以获得回报，因此**时间越长，未来现金流的折现值越低**
   - NPV = sum of the present values of expected incremental cash flows if a project is undertaken, where:
   - The NPV formula is:

$$
NPV = CF_0 + \frac{CF_1}{(1+r)^1} + \frac{CF_2}{(1+r)^2} + \ldots + \frac{CF_T}{(1+r)^T}

$$

> - (CF_0) is the initial outlay (a negative cash flow),
> - (CF_t) is the after-tax cash flow at time \( t \),
> - (r) is a required rate of return for the project,贴现率（项目的必要回报率）
> - (T) is the duration of the project.

4. **Cash Flows are analyzed on an after-tax basis** 税收影响必须考虑!!!

   - The impact of taxes must be considered because **firm value is based on Cash Flows that investors get to keep, not those sent to the government.** --> 现金流的真正价值取决于企业能留住多少，而不是支付给政府的部分
   - Key tax considerations include tax credits, depreciation, amortization (cost of use of assets, debts), and interest expenses.
     - 估值、NPV（净现值）、APV（调整现值法）等计算都基于**税后现金流**
5. **Financing costs are reflected in the project’s required rate of return**

   - Do not consider financing costs specific to the project when estimating incremental cash flows. 项目估算增量现金流时，不要直接考虑特定融资成本
   - Instead, financing costs are reflected by the project's **required rate of return**:

     - The discount rate in the NPV equation, which we use to evaluate the project, takes into consideration the firm's cost of capital.
     - **Rate of return > the firm’s cost of capital**, if the project is **riskier** than the average firm project
     - **Rate of return > the firm’s cost of capital**, if the project is **less risky** than the average firm project
       - **风险较高 = 折现率较高** → 需要更高的回报率，否则项目不会被接受。
   - Only projects that **return > the cost of capital** (or required rate of return) will increase firm value.

     - 只有当**项目的预期回报率 > 资本成本** 时，该项目才能创造价值。
     - 如果 **项目回报 < 资本成本** ，公司实际上是在破坏股东价值。

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
  $$
  NPV = -2,000 + \frac{1,000}{(1+0.10)^1} + \frac{800}{(1+0.10)^2} + \frac{600}{(1+0.10)^3} + \frac{200}{(1+0.10)^4} = \$157.6
  $$
- **Project B**:
  $$
  NPV = -2,000 + \frac{200}{(1+0.10)^1} + \frac{600}{(1+0.10)^2} + \frac{800}{(1+0.10)^3} + \frac{1,200}{(1+0.10)^4} = \$98.35
  $$

Would you accept the projects? If you had to choose only one project, which would you choose and why?

- Both projects have positive NPVs, indicating that they are expected to add value to the firm after considering the cost of capital at 10%. This suggests that if possible, both projects should be accepted as they offer returns greater than the required rate
- However, if you must choose only one project, **Project A** would be the preferable choice because it has a higher NPV of $157.6 compared to $98.35 for Project B. This means that Project A is expected to generate more value over its life relative to the initial investment and the firm’s cost of capital. Project A provides a higher return on investment, making it the more attractive option between the two.

* **NPV 代表项目为企业带来的绝对价值** ，NPV 越高，公司股东的财富增长越多。
* **项目 A 的 NPV（$157.6）高于项目 B（$98.35）** ，因此**项目 A 更有价值** 。

### **NPV using Excel**

![Graph](NPVexcel.png)

- Excel NPV formula assumes
  - The First CF is one period after the beginning of the investment
  - The last CF is the cash flow at the end of the list
- If the first CF occurs at time 0 (which is very common)
  - Add first CF to Excel NPV result (as in the previous example)
  - Do not include the first CF in the values arguments

## **IRR catch up**

**内部收益率 (IRR, Internal Rate of Return)** 是资本预算和投资决策中最常用的指标之一。它是**使得项目净现值（NPV）等于零的折现率**

This is the most important alternative to NPV:

- It is based **entirely on the estimated cash flows**, and it is independent of interest rates found elsewhere.**IRR 是项目的内部回报率** ，它表示项目本身能带来的收益率，不依赖于外部的折现率（如市场利率或融资成本）。
- **一般的 "Rate of Return"（投资回报率）可以指不同的收益率** ，包括：* **IRR（内部收益率）**：表示项目在不考虑外部市场环境的情况下能产生的年化收益率。
  - **ROR（Return on Investment, ROI）** ：通常指总投资回报率，但不考虑时间价值。
  - **Cost of Capital（资本成本）** ：投资者要求的回报率（比如加权平均资本成本 WACC）
  - **Discount Rate（贴现率）** ：用于计算 NPV 时的折现率。

### **IRR's definition:**

The discount rate at which the project’s NPV equals zero:

$$
NPV = 0 = CF_0 + \frac{CF_1}{(1+IRR)^1} + \frac{CF_2}{(1+IRR)^2} + \ldots + \frac{CF_T}{(1+IRR)^T}

$$

### Investment rule:

Accept projects with a greater IRR than the opportunity cost of capital.

* **当 IRR > Cost of Capital时**，项目是值得投资的，因为它能产生超额回报。
* **当 IRR < Cost of Capital时**，项目不值得投资，因为它无法覆盖投资的机会成本。

### Example Calculations:

![Graph](NPV.png)

- **Project A**:
  $$
  NPV_A = 0 = -2,000 + \frac{1,000}{(1+IRR_A)^1} + \frac{800}{(1+IRR_A)^2} + \frac{600}{(1+IRR_A)^3} + \frac{200}{(1+IRR_A)^4} \rightarrow IRR_A = 14.49\%

  $$
- **Project B**:
  $$
  NPV_B = 0 = -2,000 + \frac{200}{(1+IRR_B)^1} + \frac{600}{(1+IRR_B)^2} + \frac{800}{(1+IRR_B)^3} + \frac{1,200}{(1+IRR_B)^4} \rightarrow IRR_B = 11.79\%

  $$
- These calculations find the discount rate at which the present value of the cash flows, resulting in a net present value of zero.通过这些计算可以找到现金流现值的贴现率，从而得出净现值为零
- The IRR for each project represents the **break-even rate of return**, above which an investment would yield a positive return.每个项目的内部收益率代表收支平衡的收益率，超过这个收益率，投资就会产生正收益。

Would you accept these projects based on their IRR compared to an opportunity cost of capital of, say, 10%?

- Project A with an IRR of 14.49% and Project B with an IRR of 11.79% both exceed this rate, suggesting both projects should be accepted.如果仅根据 IRR 进行决策，**Project A 更具吸引力** ，因为它的 IRR 更高，投资回报率更快。

## **IRR can also be computed using Excel**

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

* 这个图展示了**项目 A（Project A）在不同贴现率（Discount Rate）下的净现值（NPV）** ，用于**敏感性分析（Sensitivity Analysis）** 。X 轴是**贴现率（Discount Rate）** ，Y 轴是**NPV** 。
* **向下倾斜的趋势** ：随着贴现率的增加，项目的 NPV 逐渐降低。这符合**贴现率越高，未来现金流的现值越低** 的基本金融逻辑。
* **特殊点（蓝色箭头所指的点）** ：这个点出现在**贴现率 15% 附近** ，并且 NPV 恰好为**0** 。
* 如果**资本成本（WACC）低于 15%** ，NPV 为正，意味着**项目创造价值，应该接受**
* 如果**资本成本高于 15%** ，NPV 为负，意味着**项目销毁价值，不应接受**
* 当 WACC = 15% 时，投资者对项目的回报与资本成本相等，项目带来的回报刚好覆盖资金成本，NPV 为 0


## **NPV vs. IRR**

If used properly, the NPV and IRR rules will generally give the same decision outcome. However, there are exceptions:在大多数情况下，**净现值（NPV）** 和 **内部收益率（IRR）** 这两个方法会给出相同的投资决策。但在某些特殊情况下，它们可能会得出不同的结论，需要特别注意。

- **Non-conventional cash flows**: Cash flow signs change more than once over time. For example, there are interim maintenance costs exceeding revenues from the project at the periods (net cash outflows).通常情况下，项目的现金流是**先投资（负现金流），后回报（正现金流）** 。但某些项目的现金流可能在生命周期内多次由正变负，或由负变正，这会导致多个 IRR 值，无法正确评估项目。
  - 某项目前期需要投入资金（负现金流）
  - 中间阶段可能产生额外的维护成本（负现金流），这会导致 IRR 方法不适用
- **Mutually exclusive projects**: Initial investments are substantially different, or the timing of cash flows is substantially different.互斥项目:
  - (初始投资金额差异较大) 如果两个互斥项目的投资规模差别很大，IRR 可能会偏向小规模投资的项目，但 NPV 可能会显示大规模投资的项目更有价值
  - 现金流时序差异: 如果一个项目的现金流前期较大，而另一个项目的现金流集中在后期，IRR 可能会更偏向**早期现金流较大的项目** ，但 NPV 可能认为**长期价值更大的项目更优**
- **Be careful when borrowing**: Changes decision rule.
  - 负的 NPV 可能仍然有较高的 IRR: 如果项目的现金流模式涉及大量借款，IRR 可能会由于负现金流的影响而变得难以解释,这可能导致 IRR 方法给出误导性结果，因此**在考虑借款时，NPV 规则通常更加稳健**

## **NPV & IRR Rules vs. Maximizing Share Value**

- **投资决策应该基于 NPV > 0 的项目（即 IRR > 资本成本）**Choosing investments where \( NPV > 0 \) (meaning \( IRR > \) required rate of return) is equivalent to maximizing shareholder wealth and payoffs:

  - This holds especially when markets are efficient and investors are rational.
- Why is this approach effective?

  - **Positive-NPV Projects:** These yield (expected) payoffs that are higher than the outside option (given by the required rate of return). This means that these projects offer a higher payoff than other investments with the same risk, such as investing in other stock/projects.
    - 选择 NPV > 0 的项目意味着**投资的回报率高于资本成本** （required rate of return）。这种项目带来的预期回报 **高于市场上的其他同等风险的投资** （例如其他股票或项目）。换句话说，投资者如果将资金投向 NPV > 0 的项目，比投资其他机会（如债券、股票）更有利。
  - **Capital Market Utilization:** Shareholders can use capital markets to allocate their wealth over time. This allows them to distribute positive-NPV project outcomes across time to meet their preferences, whether they prefer cash today or more in the future.
    - 股东可以利用资本市场调整财富分配, 通过市场，股东可以自由选择**何时变现这些投资的回报**,如果公司进行一个 **正 NPV 项目** ，股东可以选择**在未来持有该投资** 并获得更高的收益
- Implications:

  - By following NPV and IRR rules, companies essentially aim to **increase the value of their shares**, assuming rational behaviors and efficient markets.
  - Positive-NPV projects directly contribute to raising a company's stock price, thereby benefiting shareholders by providing them the flexibility to manage their investments according to their financial goals.

  * **NPV 规则** 是**股东价值最大化的最佳决策工具** ，因为它确保了公司仅投资于能创造额外价值的项目。
  * **IRR 方法** 在大多数情况下也适用，但在某些特定情况下（如互斥项目、非标准现金流）可能导致误导性的决策。
  * **企业管理者应该优先考虑 NPV，而不是单纯看 IRR** ，以确保他们的投资决策符合长期股东利益。
