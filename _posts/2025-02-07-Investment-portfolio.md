---
title: Investment and Portfolio - Types of Stock Positions
description: Course review for Spring course in MAF program at Emory.
categories: [Finance,Course]
tags: [note]
math: true
date: 2025-02-08 01:06:00 -0500
# image:
#   path:
---
# Types of Stock Positions

## **Types of Stock Positions**
### Long
- Buy shares (assume no initial short position)
  - 这里的initial Short position 指的是你需要先买回股票以覆盖空头，然后再持多头
- This means you own these shares
- If the stock price goes up, you will benefit.
  - The idea is pretty simple, you buy at one price and hope to sell at a higher price in the future for a profit

### Short
- Sell shares you do not hold
- Would eventually need to buy them back to cover your short
- **Process**:
  - Borrow the stock from a BROKER-->Sell it at the current market price-->Buy the stock back in the future at a lower price
    - The process is known as converting a short
  - **Then 2 situations**:
    - If the stock price goes down:
      - Return the borrowed stock to the broker and Make a profit on the price difference (arbitrage)
    - If the stock price goes up:
      - You will suffer a loss because you have to buy back the stock at a higher price
- Our default is that we buy in the secondary market from another investor, rather than via an initial public offering
  - 默认在二级市场（而不是一级市场，即发行公司筹集新资本）发生股票交易，这意味交易已经存在的股票。
- Transactions occur on an exchange, such as the NYSE, via a stock broker like Schwab or Robinhood

#### **NB: Difference between Primary Market and Secondary Market:**
- **Primary Market**: securities are created and sold for the first time. Companies issue new stocks or bonds directly to investors, often through IPOs or private placements.
  - 通常通过投资银行或其他金融机构的帮助。这些金融机构经常承担承销商的角色，即他们保证以特定价格购买剩余的新股票，并将其销售给公众。
- **Secondary Market**: After securities are issued in the primary market, they are traded among investors on the secondary market. This trading does not involve the issuing company directly, instead, it occurs between investors on exchanges or OTC (over the counter) markets.不会直接为发行公司增加新资金，但会通过市场表现反映公司的经济状况。


## **Short Selling**
- Broker lends the stock to the short seller
  - **Where do the shares come from?**
    - The shares come from the brokerage's own inventory, the margin accounts of other brokerage clients, or from another broker-dealer. These are typically shares held by long-term investors who are not planning to sell them soon.
    - Brokers source shares from clients’ margin accounts or institutional investors who participate in securities lending programs.
    - When you hold shares in a brokerage account, brokers may lend your shares to short sellers, often in exchange for a fee or interest.
- **Short seller could be**
  1. charged interest for borrowing shares, or
     - **Why?** Interest is charged if the demand to short is high (e.g., a heavily shorted meme stock), brokers charge interest (called the "short borrow fee").
  2. paid interest associated with the short sale proceeds
     - Some brokers give the owner of the shares (i.e., the person who lent the shares that the short seller borrowed) a portion of this interest
     - **How?** When the short seller sells borrowed shares, the cash proceeds are held as collateral in a margin account. If the broker invests this cash (e.g., in risk-free Treasury bills), they may pay the short seller a portion of the interest earned.
     - **Reality**: This is rare. Most brokers keep the interest or use it to offset costs.
  3. neither charged nor paid
     - **Occurs when**:
       - There’s low demand to borrow shares (no interest charged).
       - The broker holds proceeds in a non-interest-bearing account (no interest to share).
- Individual stocks are not always shortable:
  - Shares can be “hard to borrow”
  - Broker is unable to locate shares for the short seller to borrow
  - It is illegal in the U.S. for a broker to allow a client to short a stock when the broker is unable to locate shares to borrow
  - Broker can cover a short without prior notice
    - 经纪人在某些情况下可以在没有事先通知的情况下平仓空头股票的相关规定。这通常是在涉及到股票回购或者被迫买入的情况下发生的。

## **Short Squeeze (空头挤压)**
- A short squeeze occurs when short sellers of a stock rush to cover their positions en masse, usually due to a sudden price increase. This covering often happens over a short period and can drive the stock price even higher. 空头挤压是指当市场上大量持有空头仓位的投资者被迫在短时间内平仓（买回股票）时发生的现象。这通常导致股价迅速上升，因为大量的买入订单推高了价格。
- Concentrated short covering usually over a brief period of time
- Possible causes:
  - Positive stock news
    - 如果一家公司发布了积极的新闻，比如盈利超预期，它可能会导致股价上涨，迫使空头卖出者买入股票以避免更大的损失。
  - Shares are hard to borrow, and broker needs to return borrowed shares (e.g., owner of shares wants to sell them)
    - 如果持有股票的投资者想要卖出他们的股票，经纪人可能需要从空头卖出者那里回收股票以归还给股东，迫使空头卖出者平仓。
  - Hard to borrow interest rate increases substantially
  - Short seller does not want to pay the high interest to borrow
    - 如果借入股票的成本（利率）大幅上升，持有空头仓位的成本将增加，迫使空头卖出者平仓以减少损失。
- Examples
  - Gamestop, AMC, other WallStreetBets stocks, 2021
    - 由于散户投资者，尤其是来自 Reddit 社区 WallStreetBets 的散户投资者集体大举买入，迫使卖空者回补，这些股票的价格大幅上涨。
  - Obliterated Melvin Capital (hedge fund)
    - 该对冲基金因持有这些股票的空头头寸而遭受巨额损失。
  - Volkswagen, 2008
    - 在2008年，大众汽车的股票因为保时捷秘密购买了大量股份而导致股票供应短缺，进而引发了空头挤压，股价短时间内飙升。
  - KaloBios Pharmaceuticals, 2015
    - 当马丁·斯克雷利（Martin Shkreli）和其他投资者购买了大量股票后，这家公司的股票也发生了空头挤压。

## **Stock prices are not always sensible**
- “The market can stay irrational longer than you can stay solvent”
- “It's about making money, not about being right.”
  - George Soros

## **Short Interest on Bloomberg**
- Enter ticker [EQUITY] SI [GO]
  - E.g., TSLA [EQUITY] SI [GO]
  - Shows:
    - Short interest and change in short interest
    - Short interest ratio and change in short interest ratio
    - % float and change in % float
    - Markit SI score
    - S3 squeeze

## **Types of Portfolios**
- Long only
  - expect price to go high预期市场或特定股票将上涨
  - 风险承受能力: 较低到中等
- Long-short
  - The investor buys stocks that are expected to increase in value (long positions) and sells stocks that are expected to decrease in value (short positions).
  - aims to profit from both rising and falling market conditions and can provide better risk management.
  - 常见于对冲基金和希望通过市场波动来获利的高级投资者
  - 实现市场中立，降低市场系统性风险，追求绝对回报
  - 风险承受能力: 中等到高
- Short only
  - capitalize on declining market trends.
  - 适合于市场崩盘或经济衰退时期，或者对某些行业或公司持悲观态度的投资者
  - 风险承受能力: 高


## **Regression Statistics**
1. **regression of portfolio excess returns vs. the market’s excess returns**:
$$
r_p - r_f = \alpha_p + \beta_p (r_m - r_f) + \epsilon
$$
- `r_p`: Excess return of the portfolio over the risk-free rate.投资组合回报率
- `r_m - r_f`: Excess return of the market over the risk-free rate.
- `α_p`: measures the portfolio's risk-adjusted (abnormal) return above the market.
  - 表示投资组合的超额回报或风险调整后的回报
  - alpha > 0 indicates the portfolio is performing better than expected based on its risk (beta).
- `β_p`: measures the portfolio's sensitivity to market movements.衡量投资组合回报对市场回报变动的敏感度。
  - beta = 1 means the portfolio moves in line with the market；投资组合的回报将平均而言完全跟随市场波动
  - beta > 1 means more volatile than the market;表示投资组合比市场更为波动
  - beta < 1 means less volatile. 小于1则表示投资组合相对稳定
- `ε`: Error term, the amount of return not explained by the market movements.
2. **R-squared**: This statistic measures how much of the portfolio's excess return variability is explained by the movements in the market's excess returns. R-squared值表示市场回报变动中有多少百分比能通过投资组合的回报变动来解释。
   - R-squared = 1 (or 100%) means all movements in the portfolio returns are perfectly explained by market movements, 意味着投资组合的表现与市场紧密相关
   - R-squared = 0 indicates no correlation.低R-squared值则表示较小的相关性。
3. **Portfolio Types**: Different types of portfolios, such as long-only or long-short, can be characterized by different values of beta and R-squared, reflecting their varying market sensitivities and the effectiveness with which market movements explain their returns.


## **Beta vs. R-squared Examples**
- Beta = 2 implies if the stock market’s return is 1%, the portfolio’s return is 2%, on average
- High r-squared implies the portfolio return correlates (either positively or negatively) with the market return
- For instance, could have a high r-squared and a negative beta, implying that the fund’s return is opposite the market’s return


## **Long-only Portfolios**
- Risk characteristics
  - Positively correlated with the stock market
  - Beta：纯多头投资组合的Beta值通常接近1，因为这类组合倾向于跟随市场趋势。
  - R-squared: Between 70% and 100%
    - A long-only portfolio has a high correlation with the market. This is because most of the portfolio's returns would move in line with market trends.
- Long-only represents the most popular form of equity portfolio
  - Mutual funds: 这些基金汇集了许多投资者的资金来购买股票、债券或其他证券。
    - For actively-managed, domestic equity funds
      - Average beta is ~1.0
      - Beta >= 0.80 for most funds
  - Pension funds:  养老基金通常管理大量资金，用于为退休员工提供长期资金保障。
  - Endowment funds: 大学或慈善机构等机构的捐赠基金用于支持其长期财务健康和任务执行。
  - Retirement portfolios: 个人为退休储蓄的投资组合往往采用长仓策略，通过股市实现长期资本增值。
  - Individual stock portfolios: 许多个人投资者选择长仓策略，购买并持有他们认为会随时间增值的股票。
  - Some hedge funds: 虽然对冲基金以使用复杂的投资和风险管理策略著称，但有些对冲基金也采用长仓策略，尤其是那些专注于股票长期增值的基金。


## **Long-short**
- Long some securities and short others, but typically (for real world “long-short” portfolios) more long exposure than short exposure
- Risk characteristics:
  - Typically positively correlated with the market, but not highly correlated
  - Beta around 0.5
- Products that use long-short strategies
  - Many hedge funds
  - A small fraction of mutual funds: 4-5%
- Bloomberg:
  - FSRC: fund screen
  - Universe Criteria: Fund Type: Open-End Funds (for example)
  - Fields: Classifications: Fund Strategy: Long Short
  - View historical beta of ticker = KLSMKFU ID


## **Long-short Example**
- Covered call 覆盖式认购期权
  - Long stock
  - Short a call option on the same stock: 同时，投资者卖出（或“写”）一个认购期权，授予买方在未来某一特定日期前以特定价格（执行价）购买该股票的权利。卖方获得卖出期权的权利金（premium）作为收入
  - E.g: 
    - Hold AMZN long at $150 & Sell a call option on AMZN with a $160 strike price
    - Earn the premium from selling the call
    - 思路：
      - 如果AMZN的股价在期权到期时低于$160，期权将不会被行使，投资者保留股票并获得期权权利金。
      - 如果AMZN股价超过$160，买方将行使期权，以$160的价格购买股票。这意味着投资者将以$160的价格卖出股票，加上收到的期权权利金，但将错失任何超过$160的额外上涨。
    - Downside:
      - 收益限制：如果股价大幅上涨，超过了$160的执行价格，投资者将不会从股价上涨中获得超过$160的收益，因为股票将被以$160的价格卖出。
      - 下行风险：尽管卖出认购期权可以提供一些收入以抵消股价下跌的影响，但如果股价大跌，这种策略并不能提供充分的保护。如果AMZN的股价跌破了购入价格（$150），则依然会面临亏损。


## **Market Neutral市场中性策略**
- 长短策略（Long-short）的一种特定形式，核心在于尝试从选定的股票或资产中获得绝对回报，同时尽量减少或消除市场波动的影响。这意味着投资组合的表现独立于市场表现，仅依赖于投资经理在选择和平衡仓位上的技巧，而非依靠市场动向。
- A subset of long-short
- Risk characteristics
- Characteristics:
  - R square very close to zero: 由于策略旨在消除市场波动的影响，因此市场中性组合通常展现出非常低的市场相关性。
  - Beta very close to zero: 理想情况下，市场中性策略的Beta值（即与市场波动的相关性）接近于零，表明该策略几乎不受市场上涨或下跌的影响。
  - Reduce volatility: 通过对冲不同股票或资产之间的风险，市场中性策略旨在减少投资组合的整体波动性，从而在市场不稳定时保护投资。


## **Market Neutral Examples**
- Strategies
  - Merger arbitrage并购套利
    - Buying the target and shorting the acquirer
    - 这种策略涉及在并购公告后购买目标公司的股票（假设它们被低估）并卖空收购方的股票（假设它们被高估）。目标是利用并购交易完成时股价的调整来获利。
    - 例如，如果公司A宣布将收购公司B，投资者可能会购买公司B的股票并卖空公司A的股票，期望在交易完成后从价格差异中获利。
  - Pairs trading配对交易
    - 这种策略涉及找到两个具有历史价格相关性的股票，当这两股的价格关系偏离历史平均值时买进被低估的一方并卖空被高估的一方。
    - E.g., Buying Home Depot and shorting Lowes
    - 例如，购买家得宝（Home Depot）的股票并同时卖空劳氏（Lowes）的股票，这两家公司都是大型家居改善零售商，通常它们的股价会显示出相似的市场行为。
  - Mutual funds
    - E.g., AQR Equity Market Neutral R6
    - ticker QMNRX： 这是一个市场中性共同基金，目标是提供与市场波动无关的稳定回报。通过采用多种市场中性策略，该基金试图降低系统性风险，同时寻求在各种市场环境下实现正回报。


## **L-S and MN vs. Long-only Performance**
- 比较市场中性（MN）和多空（L-S, Long-Short）策略相对于只做多（Long-only）策略在不同市场状况下的表现趋势
- Performance tendencies based on beta risk:
- On average, MN and LS underperforms long-only:
  - In the long-run
  - During bull markets
  - Mid-2009 through 2021：例如，从2009年中到2021年期间，当市场整体表现强劲时，这些策略因为其对冲和中性特性而未能充分利用市场上涨的机会。
- On average, MN and LS outperforms long-only:
  - During bear markets
  - 2008 financial crisis
  - Mid-Feb through mid-March 2020
  - 2022
- Exceptions exist, where MN and L-S funds outperform based on alpha：尽管通常情况下市场中性和多空策略在牛市不如只做多策略，但也存在例外。某些基金通过挖掘特定的市场机会（alpha）来超越市场平均表现。
- LS and MN strategies have favorable diversification benefits relative to a long-only portfolio
- Low correlation vs. stock market


## **Short-only**
- Typically used to bet against the market or to hedge a portfolio
- Risk characteristics
  - R-square < 0 :  即市场表现好时，只做空策略表现差；市场表现差时，只做空策略表现好。
  - Beta < 0 ： 


## **Short-only**
- Products with short-only portfolios
- Numerous bearish exchange traded funds (ETFs) 有多种熊市ETFs，这些基金设计用来在市场下跌时盈利。
  - E.g., ProShares Short S&P 500, ticker SH
- Some passively-managed mutual funds被动管理型共同基金
  - E.g., Rydex Inverse S&P 500, ticker RYURX
- A small fraction of actively-managed open-end mutual funds主动管理型开放式共同基金中的少数
  - Roughly one out of every 200 has beta < 0
- A small fraction of hedge funds少数对冲基金


## **Leveraged Portfolios**
- Leveraged portfolios use loans from the broker (called margin) to take stock positions greater than the value of the account
- 杠杆化投资组合是指使用从经纪商处借入的资金（通常称为保证金贷款）来购买股票，使得投资的总规模超过账户的实际价值。这种做法允许投资者以较小的初始资金控制更大金额的资产。
- 杠杆化投资组合的工作原理：
  - 借贷：投资者从经纪商处借入资金，用这些资金购买股票或其他资产。
  - 保证金：这是经纪商要求投资者作为借款担保而保持在账户中的最低现金或资产金额。
  - 放大收益与风险：通过杠杆，即使股票价格的小幅变动也会放大收益或亏损。这增加了潜在的高收益机会，同时也增加了风险。
- 风险：
  - 如果投资的资产价值下跌到一定程度，经纪商可能要求投资者追加保证金（称为保证金追加），或强制平仓，以确保贷款安全。
  - 杠杆化投资可能导致亏损迅速累积，尤其是在市场波动性大时。
  - 杠杆化投资组合的使用需要谨慎，通常适合经验丰富的投资者，因为需要妥善管理债务和复杂的风险管理策略。


## **ETF Examples**
- Many ETFs offer leverage directly
  - Direxion Funds
    - Triple leverage
    - Long： E.g., FAS, DRN, TNA
    - Short： E.g., FAZ, DRV, TZA
  — ProShares：通常涉及复制基础指数两倍表现的策略
    - Double leverage
- 功能和风险：
  - 杠杆ETF 通过使用金融衍生品如期货和期权来放大日常回报的正负变化。
  - 这些产品主要面向短期投资者，因为杠杆复合效果可能会在长期导致与预期不同的回报。
  - 高杠杆带来高风险
