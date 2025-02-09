---
title: Investment and Portfolio - The Efficient Frontier
description: Course review for Spring course in MAF program at Emory.
categories: [Finance,Course]
tags: [note]
math: true
date: 2025-02-08   22:41:00 -0500
# image:
#   path:
media_subpath: /assets/media
---
## **Key Takeaways**


| **Concept**                          | **Definition**                                                                                               | **Characteristics & Implications**                                                                                                                                                                                        | **Graph Representation**                        |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Efficient Frontier**               | The set of portfolios that provide the highest return for a given risk or the lowest risk for a given return | - Represents**optimal risky portfolios**<br/>- Calculated using **historical returns, variance, and covariance**<br/>- Diversification reduces risk                                                                       | 曲线形状，**向上弯曲**                          |
| **Capital Market Line (CML)**        | Represents the best possible portfolio selection, combinin risk-free assets and the optimal risky portfolio  | -**CML slope = Sharpe Ratio**<br/>- **Risk-free asset** (y-axis intercept of CML)<br/>- **Optimal risky portfolio** (tangent point between CML & Efficient Frontier)                                                      | 一条**直线** ，从无风险资产穿过最优风险投资组合 |
| **Minimum Variance Portfolio (MVP)** | The portfolio with the lowest volatility on the efficient frontier                                           | - Suitable for**highly risk-averse investors**<br/>- Low risk but also **lower returns**                                                                                                                                  | 有效前沿上最左侧的点                            |
| **Indifference Curve**               | Represents an investor’s risk-return preference                                                             | -**Higher risk aversion → Steeper curve** (requires higher returns)<br/>- **Lower risk aversion → Flatter curve** (willing to take on more risk)                                                                        | 一系列**凸向上的曲线**                          |
| **Optimal Complete Portfolio**       | The combination of the optimal risky portfolio & risk-free asset, tailored to an investor’s risk preference | -**Investor’s individual risk preference determines the final allocation**<br/>- Determined by the intersection of the **indifference curve & CML**                                                                      | CML 与投资者**无差异曲线的交点**                |
| **Key Takeaways**                    | Core principles of portfolio optimization                                                                    | -**Risk-return tradeoff** (CML is linear, Efficient Frontier is nonlinear)<br/>-  **Diversification reduces unit risk**<br/>- **Different investors choose different allocations** between risk-free and risky portfolios | -                                               |
| **Shortcomings**                     | Challenges in real-world application                                                                         | -**Based on historical data** , may not reflect future returns<br/>- **Ignores transaction costs**<br/>- **Difficult to quantify investor preferences**<br/>- **Limited use in real-world portfolio management**          | -                                               |

###

## **The Efficient Frontier**

- Shows the **greatest return** for a given level of risk or the lowest risk for a given return 有效前沿代表在给定风险水平下能够获得的最大回报，或者在给定回报水平下的最低风险。
- Computed using **historical returns**, **variances**, and the **covariance matrix** of returns

## **Two Asset Example**

$$
\sigma_p^2 = (w_1 \sigma_1)^2 + (w_2 \sigma_2)^2 + 2w_1w_2\sigma_1\sigma_2\rho_{12}

$$

- This formula captures diversification benefits associated with including two assets in a portfolio

  - Diversification depends on the correlation between the assets being **< 1**
    - 资产之间的**相关性越低（ρ < 1）** ，分散化效果越好。
- The formula gets increasingly complicated as the number of assets increases
- ![Graph](Two Asset example.png)

  - 有效前沿（Efficient Frontier）是投资组合理论中的一个重要概念，它表示在给定风险水平下，能够实现的最高期望收益的投资组合集合
  - 该曲线由众多不同资产的投资组合构成，任何位于曲线上的点都是最优的，即在相同风险下，收益最高。
  - 红色散点：代表不同的投资组合，其中有些组合的风险过高，但收益不一定最优。
  - 蓝色曲线（Efficient Frontier）：代表所有最优的投资组合
  - 绿色箭头：标记了有效前沿上的一个典型最优投资组合
  - 有效前沿上的组合优于红色点上的组合，因为它们在相同风险水平下能提供更高回报
  - 低风险投资者可以选择曲线左侧的投资组合，这些组合的波动性较小，但回报率也较低
  - 高风险投资者可以选择曲线右侧的投资组合，这些组合的潜在回报较高，但风险也更大
  - 有效前沿上的投资组合比红色散点上的投资组合更优，因为在相同的风险水平下，能够提供更高的回报

## **Capital Market Line**

- ![Graph](Capital Maket LIne.png)
  - 资本市场线（CML）表示的是投资者可以通过结合无风险资产（如国债）与市场组合（由所有可投资资产构成的最优组合）来构建最优投资组合
  - 这条直线的斜率代表夏普比率（Sharpe Ratio），即每单位风险（标准差）所能获得的超额收益
  - 棕色线（Capital Market Line）：连接无风险资产（左下角的小圆点）与市场投资组合（位于曲线上最优风险资产组合）
  - 蓝色曲线（Efficient Frontier）：代表仅由风险资产构成的投资组合，其上的点是有效投资组合
  - 散点图：代表不同股票或资产的风险-收益组合，每个点对应某只股票或资产
  - 任何位于**资本市场线**上的投资组合都是最优的，意味着投资者可以通过杠杆或借贷调整自己的风险偏好，选择合适的点进行投资
  - 若投资者是**风险厌恶者**，可以选择靠近无风险资产的一侧（低波动率）
  - 若投资者是**风险偏好者**，可以选择市场组合以上的投资（即借钱投资）
- The **capital market line (CML)** depicts the **trade-off** between **portfolio risk** and **return for portfolios containing both the risk-free and risky securities**
- CML 代表了同时包含无风险资产和风险资产的最优投资组合
  - The point on the CML that intersects the y-axis represents the **risk-free asset**
    - 与y轴的交点：代表无风险资产，通常是短期政府债券，如美国国债。该点的收益率是无风险利率
  - The point located at the **tangency point** of the efficient frontier represents the **optimal risky portfolio**, which theory suggests is the **market portfolio**
    - 与有效前沿（Efficient Frontier）的切点：代表最优风险投资组合（Optimal Risky Portfolio），理论上，这个投资组合就是市场组合（Market Portfolio），因为它在所有可能的风险资产组合中提供了最高的夏普比率（Sharpe Ratio）
  - The CML shows the portfolios (combining both risk free and risky securities) with the highest return for a given level of risk
    - **All portfolios along the CML, including the optimal risky portfolio, have the highest Sharpe ratio**
- ![Graph](optimal risky portfolio.png)
  - 无风险资产（Risk-Free Asset）
    - 图中左下角的红点表示无风险资产，通常指政府债券，如美国国债。
    - 其波动率（Volatility）= 0，意味着没有风险。
    - 预期收益率为无风险利率（通常在0.5%~2%之间）。
  - 最优风险投资组合（Optimal Risky Portfolio）
    - CML 和有效前沿（蓝色曲线）相切的点。
    - 这一点代表了所有风险资产的最优组合，理论上相当于市场组合（Market Portfolio）。
    - 这个投资组合提供了最高的夏普比率，意味着它在所有可能的风险组合中提供了最优的风险调整回报。

## **Minimum Variance**

- The minimum variance portfolio (MVP) is the portfolio on the efficient frontier with the **lowest volatility**
- 最小方差投资组合（MVP，Minimum Variance Portfolio） 是**有效前沿（Efficient Frontier）**上波动率（风险）最低的投资组合
- ![Graph](Minimum Variance.png)
  - MVP 位于有效前沿上，并且是风险最小的投资组合
    - 有效前沿上的所有投资组合都是最优的，因为在相同风险水平下，它们的收益最大。而在这些最优组合中，MVP 是波动性最低的组合。
  - 投资者如果追求最低风险，MVP 是最优选择 --> MVP 适合极度厌恶风险的投资者，因为它保证最小的波动性。但是，由于风险低，其预期收益也可能相对较低。

## **Indifference Curve**

- The indifference curve represents an individual’s particular preference for risk and return
- 无差异曲线代表投资者对**风险和收益的特定偏好**，即投资者在相同的效用水平下如何权衡风险与回报。
- As **risk aversion increases**, investors demand **higher returns** for bearing the same amount of additional risk

  - 当投资者的风险厌恶程度增加时，他们希望在承担同样额外风险的情况下获得更高的回报。
  - The indifference curve will be **steeper** as **risk aversion increases**
    - 风险厌恶程度高 → 无差异曲线更**陡峭**。
    - 风险偏好程度高 → 无差异曲线更**平缓**。
- ![Graph](Indifference curve.png)

  - 无差异曲线 (Indifference Curve) 在图中用 绿色曲线 表示
  - X 轴代表**波动率（风险）**，Y轴代表**回报率**
  - 无差异曲线的形状反映了投资者的风险偏好

  > - reminder：
  > - 投资者会选择位于自身无差异曲线上的最优投资组合，该组合提供了其所能接受的最佳风险-回报比率
  > - 资本市场线 (CML, Capital Market Line)：红色线，代表包含无风险资产的最优投资组合
  > - 有效前沿 (Efficient Frontier)：蓝色曲线，代表最优风险资产组合，不包含无风险资产
  > - 无差异曲线 (Indifference Curve)：绿色曲线，代表投资者的个人偏好，最优投资组合是其无差异曲线与资本市场线的切点
  >

## **Optimal Complete Portfolio**最优完整投资组合

- Combination of the **optimal risky portfolio** and the **risk-free asset**
- **最优完整投资组合 = 最优风险投资组合 + 无风险资产**
  - An investor’s **indifference curve** determines the mix between the optimal risky portfolio and the risk-free asset
    - 高风险厌恶投资者：会选择更高比例的无风险资产，减少风险暴露。
    - 低风险厌恶投资者：会选择更高比例的最优风险投资组合，甚至可能进行杠杆投资（借入资金投资）。
- Graphically, it is represented as the **intersection** between **the capital market line** and **the indifference curve**
- When investors have different risk preferences (e.g., one investor is more risk averse than another), their indifference curves will **differ**, leading to different optimal complete portfolios
- ![Graph](Optimal Complete Portfolio.png)
  - 不同投资者的影响：
    - 风险偏好低的投资者，其无差异曲线与资本市场线的交点靠近无风险资产，说明他们持有更大比例的无风险资产。
    - 风险偏好高的投资者，其无差异曲线与资本市场线的交点靠近最优风险投资组合，甚至可能超过它（使用杠杆投资）。

## **Main Takeaways**

- There is a **risk-return tradeoff**, i.e., greater return requires greater risk
  - Relationship is **linear** along the capital market line --> 意味着投资者可以通过持有无风险资产和市场投资组合的组合来调整风险
  - Relationship is **nonlinear** along the efficient frontier --> 因为不同资产的相关性影响了风险分散效果
- Diversification benefits --> **more return** per unit of risk after combining assets into a portfolio
- Among **risky portfolios** (i.e., no risk-free allocation), portfolios on the efficient frontier provide **the greatest return** for a given level of risk or **the lowest risk** for a given level of return
  - 仅由风险资产构成的投资组合中，有效前沿上的投资组合在**相同风险下提供最高收益** ，或者在**相同收益下提供最低风险** 。
- **Different** investors will choose **different** allocations between risky and risk-free portfolios if they have different risk preferences
- Shortcomings
  - The efficient frontier is calculated based on **historical stock returns**
    - Past stock returns differ from future stock returns, and correlations between stocks change over time
      - As such, efficient frontiers are **backward looking**
    - Results **differ depending on the historical time frame** of returns used (e.g., past 1 year vs. 2 years, etc.)
  - **Transaction costs are ignored**
- **It is difficult to quantify investor indifference curves**
- The concepts are useful, but given these shortcomings, the computations are not particularly useful
  - **Not used in real world money management**
