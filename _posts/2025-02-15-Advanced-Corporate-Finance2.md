title: Advanced Corporate Finance - NPV & IRR applications, cash flows & WACC
description: Course review for Spring course in MAF program at Emory.
categories: [Course,Advanced Corporate Finance]
tags: [note]
math: true
date: 2025-02-15   19:21:00 -0500

# image:

# path:

media_subpath: /assets/media
----------------------------

# **NVP & IRR in practice**

## **The Pros and Cons of NPV and IRR**

- Pros and Cons of NPV:

  - Pros of NPV: **Direct Measurement**: NPV provides a direct measure of the expected increase in firm value attributable to the investment. NPV 是直接衡量投资项目对企业价值增长的贡献，是具体的金额，能反映投资的实际经济效益。
  - Cons of NPV: **Investment Size Ignored**: NPV does not consider the size of the investment, which can skew comparisons when evaluating projects of different scales.	NPV 没有反映项目的相对规模。例如，一个小规模但NPV高的项目，可能被误认为优于大规模但NPV较低的项目。
- Pros and cons of IRR

  - Pros of IRR: **Percentage Profitability**: IRR captures profitability as a percentage, making it easy to understand how far a project stands from achieving a negative NPV.IRR 是一个相对值（百分比），便于与资本成本（必要回报率）进行比较。
  - Cons of IRR: **Consistency Issues**: Project IRR ranking is not always consistent with NPV and can yield multiple values in cases of sporadic cash flows, complicating decision-making. IRR 的排序不一定与NPV一致。例如，一个项目可能有较高的IRR但较低的NPV。
- Bottom Line

  - **NPV as a Guide**: For accept/reject investment decisions, follow the NPV. The NPV criterion is economically sound and accurately reflects the goal of maximizing firm value. 在接受/拒绝投资决策中，优先使用 NPV。原因是：NPV 更加经济合理，能够准确反映企业价值最大化的目标。

## Positive NPV & Attractive IRR

Even if a project has a **positive NPV and an attractive IRR**, management may choose not to proceed due to several factors: 尽管一个项目具有正的净现值（Positive NPV）和有吸引力的内部收益率（Attractive IRR），管理层可能仍然决定不执行该项目。这通常与外部或内部的战略、运营、资源分配等因素相关。

- **Risk Factors**: Higher than accounted risks might deter progress despite attractive financial figures.
- **Resource Allocation**: Limited resources might be better allocated to projects with even higher returns or strategic value.
- **External Conditions**: Market volatility, economic downturns, or changes in consumer behavior could affect project viability post-evaluation.
- **Regulatory and Social Impact**: Potential regulatory changes and negative social impacts can also prevent project initiation.

## How NPV Analysis May Go Astray

- Failing to Incorporate All Economic Response

  - **Overlooking Externalities**: Not including all economic impacts can lead to inaccurate NPVs. 为考虑所有经济相应：NPV 分析可能遗漏了重要的经济因素，例如市场反应、竞争行为或外部环境变化。
- Abusing Templates

  - **Misunderstanding Templates**: Ensure understanding of the financial model's assumptions, especially around terminal value calculations and growth rates.滥用模版：	金融模型模板被广泛使用，但滥用模板可能导致错误。例如：
    - 将上期的现金流视为终值，而未明确其是否会持续增长。
    - 模板可能默认假设现金流按恒定增长率无限延续
- Ethics and Office Politics

  - **Subjective Influences**: Be wary of projects that are favored due to political reasons rather than solid financial justification.管可能有个人偏好的“宠物项目”，夸大销售预测以支持项目决策。
- Mixing Real and Nominal Terms

  - **Discount Rate Confusion**: Always match the type of cash flow (real vs nominal) with the appropriate discount rate to avoid miscalculations.在计算 NPV 时，折现率类型（实际利率或名义利率）未与现金流类型匹配
- Cash Flow Blunders

  - **Double Counting**: For complex projects, ensure that cash flows are not counted more than once or overlooked. 在处理复杂项目时，容易出现重复计入某些现金流或遗漏关键现金流的问题
- Sunk Costs vs. Incremental Costs

  - **Ignoring Sunk Costs**: Do not include costs that have already been incurred and cannot be recovered. 沉没成本是过去已发生且不可挽回的成本，不应纳入项目决策中。
- Misestimating Overhead Costs

  - **Overhead Costs**: Include only incremental overhead costs related to management time and IT support, which are often difficult to quantify accurately. 项目间接成本的估算通常较难，如管理时间或IT支持成本

## **What methods do CFOs use?**

![Graph](CFO.png)

- 主要结论：

1. 最常用的方法：**IRR（内部收益率）和NPV（净现值）**是CFO最常用的两种方法，使用比例均接近80%。

- IRR：提供一个直观的百分比指标，便于评估项目的盈利能力。
- NPV：直接量化项目对公司价值的贡献，被认为是最经济合理的方法。

2. 次常用的方法：**Hurdle rate（门槛率）和Payback（回收期）**紧随其后，使用比例约为50%-60%。

- Hurdle rate：设置最低回报要求，快速评估项目是否达到公司标准。
- Payback：关注投资的回本时间，直观但可能忽略长期效益。

3. 敏感性分析（Sensitivity Analysis）：约40%的CFO选择这一方法，用于评估项目在不同假设下的表现，帮助应对不确定性。
4. 较少使用的方法：P/E倍数（市盈率倍数）、Discounted Payback（折现回收期）、**Real Options（实物期权）**等方法使用率逐渐降低。
5. 最不常用的方法：**APV（调整现值）和Profitability Index（盈利指数）**的使用率最低，可能因为这些方法相对复杂或不够直观。

- CFO为什么选择这些方法？

1. IRR和NPV被广泛使用，因为：

- 它们能够准确衡量项目的经济效益。
- 考虑了时间价值和资本成本，是经济理论上较优的选择。

2. Payback和Hurdle Rate被使用，因为：

- 简单易用，便于快速评估项目是否满足最低要求。
- 尤其适用于需要快速决策的短期项目。

3. 较少使用的方法（如APV和Real Options）：

- 这些方法尽管在特定场景中有价值，但其复杂性和实际应用范围的局限性使其不如IRR和NPV普及。

# **Calculating after-tax cash flows**

## Steps to Calculate After-Tax CFs

1. **Initial Outlay** --> 初始支出是项目启动时的一次性投入成本，通常包括安装费用、购买设备或厂房的费用，以及初始库存投资。

   - Includes fixed capital investment (e.g., new plant, equipment) and working capital investment (changes in net working capital).
   - 初始支出通常是一个负现金流，它影响了NPV和IRR的基准
2. **Operating Cash Flow Over the Project’s Life** --> 项目生命周期中的运营现金流

   - Consider revenues, expenses, and tax effects.
   - 这是整个项目的核心，决定了项目的盈利能力和投资价值
   - **Operational Cash Flow (OCF) 公式**

     - **从净利润计算**：
       $$
       OCF = Net\ Income + Depreciation\ (Non-cash\ Expenses) + Changes\ in\ Working\  Capital

       $$
     - **从总收入计算**：
       $$
       OCF = Total\ Revenue - Operating\ Expenses - Taxes

       $$
     - **从 EBIT 计算**：
       $$
       OCF = EBIT \times (1 - Tax\ Rate) + Depreciation

       $$
     - **从 EBITDA 计算**：

     $$
     CF = EBITDA \times (1 - Tax\ Rate) + Depreciation \times Tax\ Rate

     $$
3. **Terminal-Year After-Tax Cash Flow** --> 项目结束时产生的额外现金流，包括出售设备的收入和营运资本回收

   - Consider salvage value and any working capital recoveries.
     - 设备残值：出售设备的收入，扣除可能的税务影响。
     - 营运资金减少：释放出来的营运资本，如库存或应收账款的减少。

## **1. Initial Outlay**

* 公式：$ \text{Initial Outlay} = \text{Fixed Capital Investment} + \text{NWC Investment} $
  - Initial outlay 的组成：
    - **Fixed capital investment**: investment in new plant, equipment, etc.
      - 固定资本投资（Fixed Capital Investment）：如购买新设备、厂房建设等。
    - **Working capital investment**: investment in net working capital (NWC)
      - 营运资本投资 (NWC)：代表企业在 非现金流动资产 (如应收账款、存货) 和 非债务流动负债 (如应付账款) 之间的变化
      - Must be included when making investment decisions
  - NWC 投资的计算：
    - **NWC investment = Change in non-cash current assets – Change in non-debt current liabilities**
    - If NWC investment (i.e., change in NWC) > 0 , this means that additional financing is necessary!
      - 如果NWC变化为正，意味着需要额外融资，因为项目需要更多的流动资金。
      - 如果NWC变化为负，表明释放了资金，实际是一种现金流入。
    - Add positive NWC to positive up-front fixed cost
  - NWC的影响：
    - 如果 NWC 增加，则需要 额外的融资，增加了初始支出。
    - 计算 NPV (净现值) 时，初始支出应为负数，因为它代表了企业的现金流出 (投资支出)。
  - Then, put a negative sign in front of the sum in the NPV calculation as the initial outlay is cash flow **leaving** the firm
  - 将固定资本投资和NWC变化相加：**Total initial outlay = Fixed capital investment + Increase in NWC**

> ## **Example: After-tax CF calculation, NPV, & IRR Part1**
>
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
>
> ![Graph](Initial Outlay.png)
> Key insights:
>
> - Because **NWC increased** (likely because you had to purchase inventory), it is considered an **outlay**.
> - If you had **reduced inventory by $15,000 instead**, then the initial outlay would have been **negative $45,000**.
> - If you had done a feasibility study with consultants first, this would **not be included in the initial outlay (sunk cost)**. --> 之前的可行性研究或咨询费用被视为沉没成本，不包含在初始支出中，因为这些费用不是决策中的增量成本

## **2. Operating Cash Flow Over Project Life**

* After-tax operating cash flows are the incremental inflows over the capital asset's economic life.
  - **Formula**:
    - $$
      CF = (Sale - Exp - Depr)(1 - tc) + Depr - CapEx - ΔNWC

      $$
    - $$
      CF = (Sale - Exp)(1 - tc) + tcDepr - CapEx - ΔNWC

      $$
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
  - 它不涉及实际的现金流出，但在现金流分析中非常重要，因为它可以**减少应税收入** ，从而降低公司需要支付的税款
* **Key intuition for depreciation**:

  - Higher depreciation expense → Higher tax savings, higher after-tax cash flow.

  * 更高的折旧费用会带来**更高的税收节约** ，因为它降低了应税收入。
* **Accelerated depreciation methods** lead to higher depreciation expenses earlier in the life of the project. -->加速折旧法在资产生命周期的早期分配较高的折旧费用。

  - When compared to straight-line depreciation (i.e., an equal percent depreciation in each year).
* Which type leads to a higher NPV, all else equal?

  * **在其他条件相同的情况下** ，加速折旧法通常会**提高** **NPV** ，因为更早的现金流入更有价值，这种方法对需要早期现金流的项目或融资成本较高的项目尤为有利。

## **An aside: Interest & Cash Flows**

* We include depreciation in the operating cash flow over the life of the project because it has a **tax advantage**.

  - What about interest rates? Interest also has a tax advantage!
  - 折旧包含在项目生命周期的运营现金流中，主要是因为它提供了**税收优势** ：折旧作为非现金费用，减少了应税收入，从而降低公司需要支付的税款
* **Do not include interest in after-tax cash flows**

  - Interest is **already incorporated** into the cost of capital (or discount rate) used to analyze if the investments' return surpasses the required rate of return.
  - **不将利息纳入税后现金流** ：利息已经包含在用于项目分析的资本成本或折现率中。利息的税收优势已经通过折现率的调整间接考虑到了。
* **Summary**:

  - **Depreciation affects cash flows** --> 折旧影响**现金流** ：折旧通过减少应税收入间接提高现金流，需在现金流预测中计入
  - **Interest affects discount rates** --> 利息影响折现率：利息的成本已经包含在资本成本或折现率中，无需额外计入现金流

> ## **Example: After-tax CF calculation, NPV, & IRR Part 2**
>
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
>
> ![Graph](CashFlow.png)
> Key insights:
>
> - Operating expenses include variable and fixed cost
> - Subtract depreciation first to get to operating income, then add it back to get cash flows
> - Sales are just projections; make sure the forecasts are reasonable (e.g., if the economy is slumping, are sales growth of 25% reasonable?)

## 3. Terminal Value Calculations

* Main idea: even if at the end of the project the new plant is no longer of use to your firm, it may be of use to some other firm → they will buy it from you!

  - **Formula**:
    - $ TV = Price_T - \tau_c (Price_T - BookValue_T) + \Delta NWC $
* **Where**:

  - **TV** = terminal value
  - **Price_T** = sale price (e.g., of plant) in terminal period T
  - **BookValue_T** = book value (e.g., of plant) in terminal period T
    - Non-zero only if you don’t fully depreciate the asset; if you fully depreciate it, then BookValue_T=0 by definition
  - **ΔNWC** = unwinding net working capital (NWC balance at end of project must equal 0)
  - **𝜏_c** = marginal tax rate

> ## **Example: After-tax CF calculation, NPV, & IRR Part 3**
>
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
> 计算细节：
>
> - Initial Outlay = Up-front Costs+Net Working Capital Investment = −60,000 + (−15,000) = −75,000
> - Sales = Projected unit sales × Sale price per unit = 1500 × 50 = 75,000
> - Variable Costs = Projected unit sales×Variable cost per unit = 1500 × 20 = 30,000
> - Fixed Costs=5,000
> - Total Operating Costs=Variable Costs+Fixed Costs = 30,000 + 5,000 = 35,000
> - Gross Profit = Sales − Total Operating Costs = 75,000 − 35,000 = 40,000
> - Annual Depreciation = Initial Fixed Capital Investment / Project Duration = 6,000/3 = 2,000
> - Operating Income Before Taxes = Gross Profit−Depreciation = 40,000−20,000=20,000
> - Taxes = Operating Income Before Taxes × Tax Rate = 20,000 × 40% = 8,000
> - Operating Income After Taxes = Operating Income Before Taxes − Taxes = 20,000 − 8,000=12,000
> - Depreciation Tax Shield= Depreciation × Tax Rate = 20,000×40%=8,000
> - After-Tax Operating CF = Operating Income After Taxes + Depreciation Tax Shield = 12,000+8,000 = 32,000
> - Terminal Value calculation:
>
>   - After-tax salvage value=Salvage Value×(1−Tax Rate) = 10,000×(1−40%)=6,000
>   - Return of Net Working Capital Investment = 15,000
>   - Total Terminal Cash Flow=After-tax salvage value+Return of NWC = 6,000+15,000=21,000
> - Discounted Cash Flows：
>
>   - $ \text{Discounted CF} = \frac{\text{After-Tax CF}_t}{(1 + \text{Cost of Capital})^t} $
>   - Year 1 = 27862
>   - Year 2 = 24197
>   - Year 3 = 34848
> - NPV:
>
>   - $ \text{NPV} = \sum_{t=1}^{T} \frac{\text{After-Tax CF}_t}{(1 + r)^t} - \text{Initial Outlay} $
>   - $ \text{NPV} = 27,826 + 24,197 + 34,848 - 75,000 = 11,871$
>   -
> - IRR:
>
>   - $ \sum_{t=1}^{T} \frac{\text{After-Tax CF}_t}{(1 + \text{IRR})^t} - \text{Initial Outlay} = 0 $
>   - **IRR**=**23.5%**

## Sensitivity Analysis

* Sensitivity analysis involves changing an input (e.g., projected sales) to see what effect this change has on a project’s NPV or IRR.
  - If the NPV or IRR changes a lot (i.e., is sensitive) when the input changes, we should think carefully about how confident we are about the input before making an investment decision.
* **Key**: only change **one factor** at a time (hold all other factors constant).
* Rule of thumb: change the factor by a fixed percentage (e.g., what if sales were 5% lower), and compare it to the base case NPV and IRR calculations.

> ## **Example: Sensitivity analysis**
>
> ![Graph](Sensitivity analysis2.png)
>
> **Which inputs are the NPV and IRR most and least sensitive to?**
>
> * NPV 和 IRR 对哪个变量最敏感？
>
>   * Price（价格） 变化对 NPV 和 IRR 的影响最大，因为价格直接决定了收入的多少。
>   * 当价格下降 20% 时，NPV 变为 -$8,678，IRR 仅为 8.6%（接近不可接受）。说明如果价格下降，项目很可能变得不可行。
> * NPV 和 IRR 对哪个变量最不敏感？
>
>   * Salvage Value（残值） 变化的影响最小。
>   * 即使残值下降 20%，NPV 也只减少 $789，IRR 仅下降 0.5%，说明残值对整体财务影响不大。
> * 总结
>
>   * 价格（Price）是影响 NPV 和 IRR 的最关键变量，企业应 优先管理价格策略，确保不会出现大幅降价导致项目亏损。
>   * 残值（Salvage Value）影响最小，即使发生变化，也不会显著改变项目的可行性。
>   * 销量（Unit Sales）和可变成本（Variable Costs）次之，它们的变动仍然对项目的财务状况有较大影响。

# Discount rates (WACC)

## **What Discount Rate Should Firms Use?**

* The **discount rate** should be the rate a firm expects to pay all its security holders (equityholders and debtholders) to finance its assets.
* A discount rate that accounts for both debt and equity is:
  - **The weighted average cost of capital (WACC)**
  - Often referred to simply as the cost of capital.
* The WACC formula is a weighted average of the cost of equity and the after-tax cost of debt.
  - By looking at the after-tax cost of debt when calculating the WACC, we incorporate the tax savings of interest into the discount rate.

- 关键点
- ✅ **折现率 = 资金提供者（股东+债权人）要求的回报率**
  ✅ **WACC 是最常用的折现率，能综合反映企业融资成本**
  ✅ **债务的税收优惠降低了实际债务成本，因此 WACC 考虑了税后债务成本**-->Tax Shield
  ✅ **如果投资项目的IRR > WACC，企业就应该投资，否则应该拒绝**

## **WACC, Discount, and Hurdle Rates**

* Most firms use the WACC as their discount rate and hurdle rate.

  - **Hurdle rate**: the minimum rate of return required on a project or investment. **障碍率（Hurdle Rate）** 是投资项目的 **最低可接受回报率** ，即项目的收益至少要达到 WACC 才值得投资。
* **Why?**

  - Because firms can **buy back their shares** as an alternative to making new investments.如果一个项目的回报率低于 WACC，公司更倾向于 **回购股票** ，而不是投资这个项目。
  - Investing in their shares (earning their WACC) is the **opportunity cost** of alternative investments. **WACC 反映了企业股东和债权人对资本的期望回报率** ，也是企业进行资本配置的 **机会成本（Opportunity Cost）**--> 如果一个项目的回报率低于 WACC，那说明它的回报甚至不如回购公司股票，因此不值得投资。
* Therefore, the WACC is the required rate of return investors demand.

  - It is the discount rate.
  - Any project the company invests in should have a return **greater or equal** than the WACC. 任何 **低于 WACC 的项目都不应该被接受** ，因为它会降低股东价值

- **📌 关键 Takeaways**
- ✅ **WACC 既是折现率（Discount Rate），也是投资的障碍率（Hurdle Rate）。**
  ✅ **如果投资回报率 < WACC，公司应该选择回购股票，而不是投资该项目。**
  ✅ **WACC 代表的是企业的资本成本，也就是投资者要求的最低回报。**
  ✅ **任何新项目的回报率必须 ≥ WACC，否则不值得投资。

## **Accounting for Risk**

* In practice, firms often add a **risk premium** to the WACC.在实际应用中，公司通常会在 WACC 基础上添加风险溢价（Risk Premium）
  - We call the resulting rate the **hurdle rate**.**加上风险溢价后，得到的比率称为** ：**障碍率（Hurdle Rate）**
    - **Hurdle rate = WACC + Risk premium**
  - Example: If the company is US-based but the investment is in a less-developed (riskier) country, firms may add a few percentage points to the WACC and use that as their hurdle rate for investments.

- **📌 关键 Takeaways**
- ✅ **WACC 代表企业的融资成本，但不能完全反映投资项目的风险水平。**
  ✅ **为了考虑风险，公司会在 WACC 上添加风险溢价，形成障碍率（Hurdle Rate）。**
  ✅ **在高风险国家或行业投资时，公司通常会使用更高的障碍率，以反映额外的风险。**
  ✅ **障碍率的设定可以帮助企业避免低回报、高风险的投资项目，确保合理的资本分配。**

## **WACC Formula and Example**

* **WACC Formula**:
  - $$
    WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D

    $$
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
    - 通常更推荐使用 **市场价值** market values ，因为资本市场定价反映了当前投资者的期望回报
    - 账面价值反映的是历史成本，而市场价值反映的是当前投资者对公司资产的估值，能更准确地衡量公司的资本成本。
  - How have market fluctuations affected value?
    - 如果股价大跌，股权市场价值减少，杠杆比率会上升，可能影响 WACC
    - 市场波动会影响股权市场价值，进而改变资本结构（Debt/Equity Ratio）
      - 当股市上涨，公司股权价值上升，杠杆比率下降，WACC 可能会降低
      - 当股市下跌，公司股权价值下降，杠杆比率上升，债务占比提高，WACC 可能会上升（因为债务成本可能更高，且违约风险增加）
* **Cost of Debt**
  - Expected, current, or historical rate of debt issuances?

    - **一般使用当前current的市场利率** ，因为它反映了企业新增债务的融资成本
    - 预期利率（Expected Rate）可能带有不确定性，历史利率（Historical Rate）可能已经过时，不能反映公司当前的融资成本。
  - Marginal or effective tax rate?

    - **通常使用边际Marginal税率** ，因为新增债务利息可减少税收
    - **边际税率** 指公司对新增利润支付的税率，能更准确地衡量债务利息的税收抵扣效果。
    - **有效税率（Effective Tax Rate）** 只是历史平均税率，不适用于新投资决策
* **Cost of Equity**
  - Investment horizon?

    - 如果评估长期项目，应使用长期利率（如 10-30 年国债利率）作为无风险利率。投资回报应该匹配企业的长期资本成本，而不是短期波
  - Risk-free rate (match investment horizon? Expected, current, or historical rate?)

    - 应匹配投资期限，并使用当前市场利率
    - **不要使用历史利率** ，因为它可能不能反映当前市场环境
    - 无风险利率通常基于**政府债券** （如美国 10 年期国债）
  - Equity market premium (how much data to include? What frequency?)

    - 需要决定使用**多少年的数据** 、使用**历史溢价还是预期溢价**
  - Firm’s beta (how much data to include?)

    - Beta 反映公司的市场风险，通常基于过去 2-5 年的数据计算
* **Risk Adjustment**
  - Comparable firms vs. gut feeling?
    - 应该使用可比公司（Comparable Firms），而非主观判断（Gut Feeling）
* **WACC Formula**:
  - $$
    WACC = \frac{E}{D+E} r_E + \frac{D}{D+E} (1 - \tau_c) r_D

    $$

## **Appropriate WACC Debt Assumptions**

* **The cost of debt** should be estimated with the **expected rate on debt issuances** and the **marginal tax rate**.
  - What proxies for the expected debt rate?

    - The market rate of a firm’s debt.
    - The **yield to maturity (YTM) **on current debt captures this market rate. **YTM 代表当前市场投资者对公司债务的要求回报率** ，比名义利率（coupon rate）更能反映真实融资成本
    - This is the relevant rate because it represents the **cost of debt that will be available for the firm to finance the project**. **YTM 代表了如果公司在当前市场环境下重新融资，它需要支付的真实利率** ，因此更适合作为 WACC 计算的债务成本。（票面利率（Coupon Rate）是债券发行时确定的，不能反映市场环境的变化。）
* **Cost of Equity Inputs**:
  1. **Investment horizon**
  2. **Risk-free rate, \( r_F \)**

     - How does it match the investment horizon? 长期投资应该用长期国债的收益率
     - Is it based on expected, current, or historical rates? 通常使用当前市场利率
  3. **Equity market premium, \( r_M - r_F \)**

     - How much data to include?
     - What equity index is appropriate? 如 S&P 500、MSCI World
  4. **Firm’s beta, \( \beta_E \)**

     - Beta is a measure of **systematic risk**.
     - How much data to include for calculating beta?
     - 若 βE>1，则该股票比市场波动更大，风险更高。

     * 若 βE<1，则该股票波动性小于市场，风险较低。
* **Cost of equity based on CAPM model**:
  - $$
    r_E = r_F + \beta_E (r_M - r_F)

    $$

## **The Risk-Free Interest Rate \( r_F \)**

* Use the risk-free rate on the day of the valuation.**应使用估值日当天的无风险利率** （最新市场数据）

  - Example: if your final analysis for a 5-year project is on Jan 20, 2018, use the 5-year US Treasury rate for Jan 20, 2018.如果你在 **2018年1月20日** 进行一个 **5年期项目** 的最终分析，你应该 **使用2018年1月20日的5年期美国国债收益率**
* The Federal Reserve has current and historical risk-free rates:

  - [Federal Reserve Historical Data](https://www.federalreserve.gov/releases/h15/)
  - Note: if a 6-year project, take the average of the 5- and 7-year rates, etc. 如果没有完全匹配的期限，可以取相邻期限的平均值
* ![Graph](IR.png)

## **The Equity Market Premium \( r_M - r_F \)**

* The **equity market premium** is the excess return that the overall stock market provides over the risk-free rate. **整个股票市场提供的超额回报** ，相比 **无风险利率（rFr_F**r****F******）** 多出的收益
  - Also called the **equity risk premium** (higher risk, higher reward).
  - Compensates investors for taking on the relatively high risk of the equity market.
* For example: if the average return on the stock market over some period is 11% and the risk-free rate over the same period is 5% → equity market premium = 6%.

## **Everyone Uses Historical Premiums \( r_M - r_F \)**

* The historical premium is the premium that stocks have historically earned over risk-free securities.
* But practitioners rarely agree on the premium! Sensitive to:

  - How far back you go in history.
  - Whether you use T-bills or T-bonds (i.e., short or long-term risk-free).
    - **T-bills（短期国库券）** ：短期无风险利率，一般波动较大
    - **T-bonds（长期国债）** ：长期无风险利率，通常比短期 T-bills 更低
    - **通常 T-bills 计算出的溢价比 T-bonds 高** ，因为短期债券的波动性更大
  - Whether you use arithmetic or geometric mean.
    - Arithmetic mean:
      $$
      {am} = \frac{a_1 + a_2 + ... + a_n}{n}

      $$
    - Geometric mean:
      $$
      {gm} = \sqrt[n]{a_1 \times a_2 \times ... \times a_n}

      $$

  * **几何平均值通常小于算术平均值** ，因为几何平均考虑了收益的波动性，避免了过高估计
* For example, for the US:

  * ![Graph](StockTbill.png)

## **Arguments for Using Lots of Historical Data \( r_M - r_F \)**

* When using historical premiums, go back as far as possible. Why?
  - A risk premium comes with a standard error (it's an estimate).
  - If the annual standard deviation of stock prices is 25%
  - So, the standard error of a historical premium estimated over 25 years is:
    - $$
      SE = \frac{25\%}{\sqrt{25 \text{ years}}} = 5\%

      $$
* In other words, adding more years makes our estimate more precise.
* **📌 结论** ：
  ✅ **历史数据越多，市场风险溢价的估计越精准（标准误差更小）** 。
  ✅ **如果只使用短期数据，市场的波动性可能导致溢价的估计值不准确** 。
* Some practitioners prefer the geometric mean over the arithmetic mean:
  - Because geometric is how investors think about risk over long periods.
  - However, the arithmetic (or simple mean) is more commonly used.
  - **📌 结论** ：
    ✅ **算术平均更常用于 WACC 计算** ，但可能会高估长期投资回报。
    ✅ **几何平均更适合长期投资分析** ，因为它考虑了市场波动和复利影响。
    ✅ **在实践中，投资者通常更倾向于几何平均，因为它更符合长期风险的概念** 。

## **The Firm’s Beta**

* We use the **CAPM** (Capital Asset Pricing Model) to determine a firm’s beta.
  - CAPM: an idealized portrayal of how financial markets price securities and thus determine expected returns on capital investments.
* **Review of CAPM**:
  - Risk is separated into systematic and unsystematic:
    - **Unsystematic (i.e., firm-specific) risk** can be diversified away.
    - **Systematic (i.e., market) risk** cannot.
  - A diversified investor is:
    - Compensated for taking on systematic risk.  投资者因承担系统性风险而可能获得更高的回报得到补偿。这是因为系统性风险影响整个市场，除了通过对冲策略，没有其他方法可以避免这些风险，而对冲策略可能不是每个人都偏好的。
    - Not compensated for taking on unsystematic risk. 投资者不会因非系统性风险获得补偿，因为可以通过多样化降低或消除这种类型的风险
* For our purposes of using beta to help evaluate an investment decision, beta is an appropriate measure of investment risk.

## **The Basic CAPM Formula**

* The CAPM formula is used to determine the expected return of an asset:
  - $$
    E(R_i) = R_F + \beta_i [E(R_M) - R_F]

    $$

    - \( E(R_i) \) = expected return of the asset (e.g., firm stock)
    - \( R_F \) = risk-free rate
    - \( 𝛽_i \) = sensitivity to market
    - \( E(R_M) \) = expected return of the market
    - \( [E(R_M) - R_F] \) = the price of risk
* In a statistical analysis, the firm’s beta (\( \beta_i \)) is calculated as:
  - $$
    \beta_i = \frac{\text{cov}(R_i, R_M)}{\text{var}(R_M)} = \frac{\sigma_{iM}}{\sigma^2_M}

    $$

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
  - **为什么使用调整后的收盘价？** 使用调整后的收盘价是因为它们考虑了股息和股票拆分，更能清楚地反映由市场力量单独引起的股票价值变化。
- What frequency?
  - Daily is noisy, so weekly may be better. Monthly is less noisy but requires many years.
  - 通常选择每周或每月的频率来减少日常股价波动的干扰。日常价格太过波动，而月度数据可能需要更长的数据跨度才能提供可靠的估算。

### Step 2: Calculate returns

- ![Graph](Returns.png)
- **如何计算收益率：** 收益率是通过计算连续两个调整后的收盘价之间的百分比变化来得到的。例如，如果一只股票的调整后收盘价从100美元变为102美元，那么收益率是(102−100)/100=0.02或2%。

### Step 3: Calculate beta

- ![Graph](beta.png)
  - 使用统计分析：通过统计软件（如Excel）中的斜率函数计算贝塔值。股票收益率与市场收益率之间的回归线斜率就是贝塔值
  - 公式：贝塔（β）计算公式为 cov(Ri,RM)/var(RM)，其中Ri是股票的收益率，RM是市场的收益率。这可以通过电子表格中的斜率公式轻松完成。
- What does a beta lower than 1 mean?
  - 贝塔值低于1表明股票的波动性小于市场。这意味着与整体市场相比，它的价格波动较小。贝塔值小于1的股票通常被认为风险较低，但在市场表现强劲时，它们也可能提供较低的回报。
