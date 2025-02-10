---
title: Investment and Portfolio - Diversification
description: Course review for Spring course in MAF program at Emory.
categories: [Finance,Course]
tags: [note]
math: true
date: 2025-02-08   16:25:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
## **Definition of Diversification**

- An approach for reducing total investment risk by **combining stocks** into a portfolio
- 多样化是一种投资策略，通过将投资分散到不同的金融工具、行业和其他类别中来管理风险。其目的是通过在不同领域进行投资来最大化回报，这些领域对同一事件的反应各不相同。
  - “Don’t put all your eggs in one basket”
  - Important because investors **dislike** risk
    - Humans are **“risk averse”** (psychological trait), preferring certainty over uncertainty

## **Diversification Part 1**

- Although the returns of different stocks are almost always **positively correlated** across time, the **correlation is imperfect** --> 这种不完美的相关性允许在这些股票组成的组合中降低风险。
  - Positive correlation arises because **stock returns are driven by common factors** 共同的驱动因素，如经济变化、政治事件或市场广泛的技术进步。
    - For instance, when the stock market moves up, individual stock prices tend to move up
- **Correlation(ρ)** ranges from **-1 to +1**
  - 股票之间的相关性可以从-1（完全负相关）到+1（完全正相关）变化
-

$$
R^2 = \rho^2

$$

## **Diversification Part 2**

- When **correlation between stocks < 1**, one stock’s movement is partially **offset** at times by the other stock’s movement --> 这允许组合的整体波动性低于单个股票。
  - A stock’s movement across time contributes to its **risk**
  - If a portfolio of stocks moves less than the individual stocks, the portfolio is deemed **less risky**
- Diversification is called the only **“free lunch”** in finance --> 表明它提供了一种降低风险而不成比例降低预期回报的方式。
  - General belief is that to **get higher expected returns, an investor needs to take on more risk**
    - This ignores the **risk reduction**  associated with diversification
    - 多样化挑战了这一观念(更高的回报与更高的风险相关联)，通过分散投资来潜在降低风险，而不降低预期回报。

> ## **Magnificent 7 Example**
>
> - The average standard deviation of the Magnificent 7 stocks during 2023:
>   - 10.2% per month
>   - 35.3% annualized
> - The standard deviation of an equal-weighted portfolio of Magnificent 7 stocks during 2023:
>   - 8.0% per month
>   - 27.7% annualized
>   - The reduction in risk in going from individual stocks to the equal-weighted portfolio is 21.5%
>     {: .green-text}

> ## **FAANG Example**
>
> - The average standard deviation of FAANG stocks during 2022:
>   - 13.4% per month
>   - 46.5% annualized
> - The standard deviation of an equal-weighted portfolio of FAANG stocks during 2022:
>   - 9.7% per month
>   - 33.6% annualized
>   - The reduction in risk in going from individual stocks to the equal-weighted portfolio is 27.7%
> - “七雄”和FAANG股票的例子：这些例子展示了多样化如何影响风险度量，如标准差，这是衡量波动性或风险的常用指标。**两个例子都显示了与单只股票相比，多样化组合的标准差显著降低，量化了多样化的好处。**

## **Diversification Part 3**

- Although diversification reduces some risk, it cannot eliminate **all risk**
  - For instance, the S&P 500 is comprised of a diversified portfolio of 500 large cap U.S. stocks
    - The S&P 500 has an annual standard deviation of around 20% across its history
- The risk that can be diversified away is called **idiosyncratic risk** (特异性风险)
  - 也称为非系统性风险或可分散风险，这种风险特定于单个资产或特定资产组，并可以通过多样化来减少。
- The risk that remains after eliminating idiosyncratic risk is called **systematic risk**(系统性风险)
  - 也称为非可分散风险或市场风险，这种风险影响整个市场或资产类别，仅仅通过多样化是无法减轻的。
- Other terms:
  - **Idiosyncratic risk is also called non-systematic risk and diversifiable risk**
  - **Systematic risk is also called non-diversifiable risk and market risk**

> #### **Risk**
>
> **- Total risk = systematic risk + idiosyncratic risk**
>
> - For **an individual stock**, both systematic risk and idiosyncratic risk are **nonzero**
> - For **a well-diversified portfolio**, **idiosyncratic risk = 0**, and **total risk = systematic risk**

## **Diversification Part 4**

- Diversification is an integral component of portfolio optimization, where an overarching goal is to provide a favorable **return / risk ratio**
  - The **Sharpe ratio** is commonly used to measure investment performance 通常用来衡量投资性能
    - The S&P 500 has an annual standard deviation of around **20%** across its history
    - $$
      S_p = \frac{r_p - r_f}{\sigma(r_p - r_f)}

      $$
    - **Standard deviation** is generally used to measure **risk**, including in the Sharpe ratio 通常用来衡量风险

## **Approaches to Diversification**

- Random selection of stocks  随机选择股票
- Stock selection based on **correlation of stock returns**
  - 选择相关性低的股票组成投资组合，以期通过降低资产间的相关性来降低整体风险。

## **Diversification Via Random Portfolio Selection**

- Substantial diversification benefits can be achieved even by randomly selecting a portfolio of stocks
  - **No consensus** :但是关于消除特异性风险所需的持股数量并无共识，因为这取决于考察的时间周期、牛市与熊市、股票类型等因素:
    - Time period examined
    - Bull vs. bear market
    - Stock style
      - For example, 与大盘股投资组合相比，**小盘股投资组合通常需要更多的股票才能实现充分的多样化**
      - ![Example](Peak Diversification.png)
        - The prior plot suggests that diversification benefits drop substantially at less than 100 stocks 当股票数量少于 100 只时，分散投资的效益会大幅下降
        - 从持有10只股票到40只股票，可以看到大盘股组合的标准差从20%降到17%，而小盘股组合从32%降到25%。

## **Diversification Part 5**

- Some say over-diversification is **lazy portfolio management** 过度多样化被认为是一种“懒惰”的投资组合管理方式
  - Many portfolio managers would have fewer than 100 favorite stocks
  - By holding 100 stocks, the portfolio manager holds many **less-favorite stocks**
  - Presumably, the portfolio would benefit from holding **fewer, higher-return stocks**

## **Diversification Beyond Random Selection**

- Can use **historical stock returns** to estimate correlation and then combine stocks with low correlation
- 过去的相关性不完全反映未来的相关性
- 相似风格、行业或资产类别的股票显示出更高的回报相关性
- 因此，通过在一个投资组合中结合小盘股、大盘股、价值股等可以实现更大的多样化。
  - For example,
    - A 100% value portfolio is **riskier** than a portfolio with ½ value and ½ growth stocks
    - A 100% technology portfolio is **riskier** than a portfolio consisting of stocks across a mix of sectors
    - A 100% stock portfolio is **riskier** than a portfolio consisting of a third stocks, a third bonds, and a third real estate

## **Risk and Return**

- 由于**idiosyncratic risk**可以通过diversification来消除，市场只补偿投资者承担的**systematic risk** 。
- Systematic risk is estimated via the **slope coefficient** from a **regression of portfolio returns** on the **market returns**
- The slope coefficient is referred to as **beta** -->斜率系数

  - 通过回归分析投资组合收益对市场收益的斜率系数（β系数）来估算系统性风险
- Theory postulates a **linear relation** between **beta and expected returns**

  - The **“security market line”** reflects this relationship -->CAPM理论：提出了β系数和预期回报之间的线性关系，这种关系通过“证券市场线”（SML）来体现。

    - 证券市场线（Security Market Line, SML）是资本资产定价模型（CAPM）中的一条线，它展示了**资产的系统性风险（Beta）与预期收益之间的关系**

    * **如果资产的预期收益高于 SML，则说明该资产被低估，具有投资价值。**
    * **如果资产的预期收益低于 SML，则说明该资产被高估，投资回报不足。**
    * **如果资产在 SML 上，则资产的定价是合理的。**
  - Not necessarily borne out with realized returns, i.e., **higher beta does not guarantee higher realized returns** --> 高β并不保证实现更高的实际回报，实际回报可能高于或低于根据β系数计算的预期回报。
- **Alpha**: **the difference between realized returns and expected returns** (based on beta and realized market returns)

  - alpha is the **intercept** in the regression of excess portfolio returns on excess market returns
- **Formula:**

$$
E(R_p) = r_f + \beta_p (R_m - r_f)

$$

$$
\alpha_p = R_p - E(R_p) = R_p - r_f - \beta_p (R_m - r_f)

$$

$$
R_p - r_f = \alpha_p + \beta_p (R_m - r_f)

$$

- **Active stock selection --> generate positive alpha**

> - **Security Market Line** Graph:
> - ![Expected Return](expected return.png)
> - Beta = 0 --> expect to get the risk free return (3% in plot)
> - Beta = 1 -->  expect to get the market return (10% in plot)
> - **Undervalued stocks** produce **positive alpha**, return that is greater than what we expect given beta
>   > - 产生正阿尔法，即实际回报高于基于β的预期回报
>   >
> - **Overvalued stocks** produce **negative alpha**, return that is lower than what we expect given beta
>   > - 产生负阿尔法，即实际回报低于基于β的预期回报
>   >

- **CAPM:Capital Asset Pricing Model**
  - The theoretical model that **relates returns to market exposure**
  - CAPM（资本资产定价模型）用于评估某种资产的预期收益率并解释股票等证券的价格，特别是它们为何会偏离市场平均值。
- However, empirical tests find evidence that returns relate to **additional exposures**, such as exposure to small cap stocks, value stocks, and momentum stocks
  - Real world implication is that an investment manager should be judged on their returns relative to a benchmark that factors in these other exposures
  - For instance, performance could be computed based on a multi-factor regression, i.e., multi-factor alpha

## **Real world Diversification**

- Investment managers *primarily emphasize stock selection*
  - Picking individual stocks that they expect to outperform投资经理主要强调选择他们认为会超额表现的个股
- *Portfolio diversification typically represents a secondary consideration*
- As such, many investment managers achieve a degree of diversification somewhat randomly by simply holding a portfolio that includes many stocks 通常是第二位的考虑因素，许多投资经理通过简单持有多种股票来实现一定程度的多样化。

## **Real World**

- Mutual funds
  - Most hold diversified portfolios (**long only**)
    - For instance, the median U.S. equity mutual fund holds around 100 stocks
  - Many funds do not diversify across styles 许多基金并不跨风格多样化，例如只集中在价值股或增长股。
    - Concentrate on **value stocks only**, **growth stocks only**, **small cap stocks only**, etc.
    - As such, an investor needs to consider diversifying across his/her portfolio of mutual fund holdings
      - I.e., offsetting the risk of a value mutual fund with a growth mutual fund, that of a large cap fund with a small cap fund, etc.

## **Diversification Part 6**

- Suppose you equal-weight your stocks to achieve maximum diversification假设你将投资组合中的股票等权重配置，以实现最大程度的多样化 --> 这意味着每只股票在投资组合中占据相同的权重或价值。
  - > Over time, **winning stocks would be over-weighted** compared to losing stocks 随着时间的推移，表现好的股票（赢家）的价值会上升，从而在投资组合中的权重变大，而表现不佳的股票（输家）的价值则会下降 --> 这种现象会导致原本等权重的投资组合逐渐失去平衡。
    >

    - > To rebalance, **you sell winners to buy losers**, i.e., **diworsification** 为了维持等权重的多样化策略，你需要定期进行再平衡，即卖出表现好的股票（赢家），买入表现差的股票（输家）。这种做法被称为“你卖赢家买输家”，实质上是一种减少多样化的做法（**diworsification**），因为它可能会使你持有一些长期表现不佳的股票。
      >
  - An **equal-weighted portfolio** holds the **same $ amount** in the portfolio manager’s favorite stocks and less-favorite stocks
  - 虽然再平衡可以帮助保持多样化，但它也引出了一个问题——如何识别和选择最佳股票。例如，如果你决定从30只股票的多样化投资组合中，集中到你最喜欢的10只，而卖出其他20只，这是否真的是一个明智的决定？你有足够的信心和数据支持这10只股票将长期跑赢其他的吗？这种策略是否值得牺牲一部分多样化的保护？
- Anecdotally, some extremely wealthy individuals (e.g., Warren Buffet) became wealthy by holding a concentrated portfolio of a small number of stocks that became blockbusters 从历史上看，像沃伦·巴菲特这样的极度富有的个人通过持有一小部分可能成为市场领头羊的股票而积累了巨大财富 --> 这表明，高度集中的投资策略在某些情况下可以非常成功，但这需要极高的市场洞察力和选择能力。
