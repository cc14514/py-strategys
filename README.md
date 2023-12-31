# py-strategys

High frequency trading strategy learning and research


* 移动平均线（Moving Average，MA）：使用不同周期的移动平均线，观察价格与移动平均线之间的关系，从而判断趋势的走势。

* 相对强弱指标（Relative Strength Index，RSI）：RSI是一种用来度量市场超买超卖情况的指标，可以帮助判断价格是否过度拉升或回调。

* 布林带（Bollinger Bands）：布林带可以用来衡量价格的波动性，当价格位于上下限之间时，可能预示着趋势的转折。

* 随机指标（Stochastic Oscillator）：随机指标可以帮助判断价格的超买超卖情况，进而预测价格反转的可能性。

## 移动平均线

1. 交叉策略：利用短期移动平均线（如 MA7）和长期移动平均线（如 MA99）的交叉信号来进行买卖决策。当短期移动平均线上穿长期移动平均线时，产生“黄金交叉”买入信号；当短期移动平均线下穿长期移动平均线时，产生“死亡交叉”卖出信号。注意，这种策略可能会导致频繁交易，需要谨慎使用。

2. 趋势跟随策略：观察 MA7、MA25 和 MA99 的走势，如果三条线均呈上升趋势，说明市场可能处于上涨趋势，可以考虑买入；如果三条线均呈下降趋势，说明市场可能处于下跌趋势，可以考虑卖出。这种策略更适合用于较长时间周期的投资。

3. 震荡策略：当市场处于震荡阶段时，移动平均线可能会呈水平或交叉状态，此时可以考虑采用震荡策略。例如，当价格位于短期移动平均线上方时卖出，位于短期移动平均线下方时买入。

4. 动态调整阈值：可以根据历史数据动态调整交易阈值，例如利用移动平均线的标准差来确定止盈止损的阈值，当标准差较大时放宽阈值，当标准差较小时缩小阈值。

5. 结合其他指标：移动平均线可以与其他技术指标如MACD、RSI等结合使用，形成综合判断。同时，也可以结合基本面分析来做出更明智的买卖决策。

6. 需要强调的是，没有一个策略能够完全预测市场的走势，市场行情是复杂且随机的，任何策略都存在一定的风险。因此，在实际交易中应该谨慎对待，不宜盲目跟风，建议根据个人风险承受能力和投资目标制定适合自己的交易策略，并且始终保持谨慎和冷静的心态。使用模拟账户进行测试和验证策略的有效性，也是一个降低风险的好方法。



## MACD (Moving Average Convergence Divergence)

MACD是一种趋势指标，用于衡量价格的短期和长期移动平均线之间的差异。它由两条线组成：

DIF（快速线）：计算短期（通常为12天）和长期（通常为26天）移动平均线之间的差值。
DEA（慢速线）：计算DIF线的9天移动平均值。
MACD的计算公式：
DIF = EMA(Close, 12) - EMA(Close, 26)
DEA = EMA(DIF, 9)
MACD = 2 * (DIF - DEA)

当MACD从负值转为正值时，被认为是买入信号；当MACD从正值转为负值时，被认为是卖出信号。

MACD（Moving Average Convergence Divergence）指标包括两条线：DIF（Difference）和DEA（Signal Line），同时还有一根表示两者差异的柱状线 MACD。这三条线通常用于分析价格的动能和趋势状况。

DIF（Difference）线：DIF 线是短期移动平均线（EMA12）减去长期移动平均线（EMA26）的结果。DIF 反映了短期和长期移动平均线之间的差异，用于判断价格的快速变化。

DEA（Signal Line）线：DEA 线是对 DIF 线进行一次移动平均（一般取9日移动平均），它平滑了 DIF 的波动，使得 DEA 变得更加稳定。

MACD 柱状线：MACD 柱状线是 DIF 线减去 DEA 线的结果。MACD 柱状线直观地展示了 DIF 和 DEA 之间的差异，其正负值表明了短期和长期移动平均线的相对位置和动能。

对于给定的 MACD 值，例如 DIF: -99.11 DEA: 61.30 MACD: -37.81，可以按照以下理解：

DIF 的值为 -99.11，表示短期移动平均线（EMA12）相对于长期移动平均线（EMA26）偏向下跌，价格可能在短期内处于下降趋势。

DEA 的值为 61.30，表示对 DIF 进行了平滑处理，DEA 值在 61.30 左右，可能处于较为稳定的水平。

MACD 柱状线的值为 -37.81，为 DIF 和 DEA 之间的差异值。其为负值，表示 DIF 处于下降状态，并且 DIF 的下降速度相对于 DEA 稳定线较快。

综合来看，当前的 MACD 指标值表明价格可能处于下跌趋势，并且下降速度较快。需要结合其他指标和趋势来做进一步的判断和决策。请注意，MACD 是一种趋势追踪指标，它对于判断短期趋势的变化较为敏感，可以作为辅助指标来辅助交易决策。


## RSI (Relative Strength Index)

RSI是一种动能指标，用于衡量市场的超买和超卖情况，范围通常在0到100之间。RSI的计算公式如下：

RSI = 100 - (100 / (1 + RS))
其中，RS表示相对强度（RS = 平均涨幅 / 平均跌幅）。

RSI的典型取值范围：

RSI > 70：被认为是超买区，可能发生回调或调整；
RSI < 30：被认为是超卖区，可能发生反弹或反转。
这两个指标是技术分析中常用的指标，可以帮助判断价格的趋势和市场的超买超卖情况。在使用这些指标时，需要结合其他指标和价格走势进行综合分析，以做出更合理的交易决策。

结合不同周期的 RSI 可以更好地理解市场的超买和超卖情况，通常可以采用以下策略：

1. RSI 穿越策略：当较短期的 RSI 线（如 RSI6）穿越较长期的 RSI 线（如 RSI12 或 RSI24）时，产生买入或卖出信号。例如，RSI6 上穿 RSI12 或 RSI24 时，产生买入信号，RSI6 下穿 RSI12 或 RSI24 时，产生卖出信号。

2. RSI 超买超卖策略：当任一周期的 RSI 值超过设定的阈值（如 70 或 30）时，产生买入或卖出信号。例如，当 RSI6、RSI12、RSI24 中有任意一个的值大于 70 时，产生卖出信号，当它们中有任意一个的值小于 30 时，产生买入信号。

3. RSI 反转策略：当 RSI 值从超买区跌至超卖区，或从超卖区升至超买区时，产生买入或卖出信号。



## VOL 指标是交易量指标 

用于衡量市场中的交易量大小和趋势。它显示了在特定时间段内的成交量情况，可以帮助分析市场的活跃程度和趋势变化。

通常，VOL 指标显示为柱状图，每根柱子的高度代表了相应时间段内的交易量。VOL 指标可以结合价格走势一起观察，从而判断价格变动的成交量支持情况。

在理解 VOL 指标时，可以注意以下几点：

成交量与价格走势：成交量与价格走势之间通常存在正相关关系。在价格上涨时，成交量可能会增加，表明市场参与者对价格上涨趋势的支持。而在价格下跌时，成交量可能减少，表明市场参与者对价格下跌趋势的怀疑或观望态度。

成交量突破：高成交量的突破通常会引起市场关注，可能预示着价格趋势的变化。例如，成交量的突然增加可能是价格即将发生较大波动的信号。

成交量的背离：当价格走势形成新高或新低时，成交量没有相应增加，或者出现相反的走势，即形成背离。这可能意味着价格趋势可能即将反转。

综合来看，VOL 指标是一个重要的交易量指标，可以提供有关市场参与者的活动水平和市场趋势的信息。它可以用于辅助价格走势的分析和交易决策，但需要综合考虑其他指标和因素，避免单一指标导致的错误判断。


## KDJ 指标是一种技术分析指标

用于衡量资产的超买超卖情况和价格趋势的强弱。KDJ 指标由三条曲线组成，分别是K线（%K）、D线（%D）和J线（%J）。

KDJ 指标的计算过程如下：

计算N日内的最高价（H）和最低价（L）。
计算当日的RSV值（Raw Stochastic Value）：RSV = (收盘价 - L) / (H - L) * 100。
计算K值：K = (2/3) * 前一日K值 + (1/3) * 当日RSV。
计算D值：D = (2/3) * 前一日D值 + (1/3) * 当日K值。
计算J值：J = 3 * 当日K值 - 2 * 当日D值。

在 KDJ 指标中，当 %K 线（K值）与 %J 线（J值）的交叉点出现时，并不能简单地说是超买或超卖区，而是表示价格的拐点。也就是说，当 %K 线上穿 %J 线，意味着价格可能从下跌转为上涨；当 %K 线下穿 %J 线，意味着价格可能从上涨转为下跌。

因此，在 KDJ 指标中，我们主要关注 %K 线和 %J 线的交叉点，以及它们与价格走势的关系，来判断价格的拐点和趋势的转变。不过需要注意的是，单独使用 KDJ 指标来做决策可能会有一定的风险，最好结合其他指标和形态分析来确认交易信号的有效性。


## EMA

EMA（Exponential Moving Average）指数移动平均线是一种常用的技术指标，用于平滑价格数据并显示其趋势。与简单移动平均线（SMA）相比，EMA对最近的价格数据给予更高的权重，因此更加敏感于价格的短期波动。

EMA的计算公式如下：
EMA（t）= α * 当前价格 + (1 - α) * EMA（t-1）

其中，EMA（t）是在时间t的EMA值，α是平滑因子，通常取较小的值，比如0.1或0.2。

EMA可以帮助我们识别价格的短期趋势和长期趋势，当价格在EMA线上方时，表明价格处于上升趋势；当价格在EMA线下方时，表明价格处于下降趋势。EMA也经常用来与其他指标结合使用，例如与MACD一起使用，从而更准确地判断价格的买入和卖出信号。因为EMA更加关注近期价格的变化，所以它可以更早地发现价格的拐点和趋势的转变，对于短期交易非常有用。


## WMA

WMA（Weighted Moving Average）加权移动平均线是一种技术指标，类似于SMA和EMA，用于平滑价格数据并显示其趋势。与EMA不同的是，WMA对不同时间段内的价格数据赋予不同的权重，最近的价格数据获得更高的权重，较早的价格数据获得较低的权重。

WMA的计算公式如下：
WMA（t）= (P1 * w1 + P2 * w2 + ... + Pn * wn) / (w1 + w2 + ... + wn)

其中，WMA（t）是在时间t的WMA值，P1、P2、...、Pn是n个价格数据，w1、w2、...、wn是对应的权重。一般情况下，权重是根据时间的先后顺序递减的，即最近的数据权重最高，最早的数据权重最低。

WMA在一些情况下可以比SMA和EMA更加敏感，特别是对于周期性的价格变动。它可以提供更早地发现价格趋势的能力，因为最近的价格变动得到了更高的权重。然而，由于WMA的计算较为复杂，有时会产生较大的波动，可能需要根据具体情况进行参数的优化和调整。


## BOLL

BOLL（Bollinger Bands）指标是一种常用的技术分析工具，由约翰·布林格（John Bollinger）在1980年代初提出。它通过计算股票或其他资产的移动平均线和标准差，来描述价格的波动性和趋势。

BOLL指标由三条线组成：

中轨（Middle Band）：即移动平均线，通常采用简单移动平均线（SMA）计算。中轨显示了一段时间内的平均价格，是股价的趋势线。

上轨（Upper Band）：上轨是中轨上方一个标准差的距离，用来表示价格的上限。上轨可以看作是一种价格的“压力线”，当价格接近或超过上轨时，说明市场处于相对高位，可能出现回调或反转的可能性增加。

下轨（Lower Band）：下轨是中轨下方一个标准差的距离，用来表示价格的下限。下轨可以看作是一种价格的“支撑线”，当价格接近或跌破下轨时，说明市场处于相对低位，可能出现反弹或反转的可能性增加。

BOLL指标的主要用途是判断价格的波动区间和趋势。当价格在上下轨之间波动时，说明市场处于相对稳定的状态；而当价格突破上下轨时，可能会发生价格的大幅波动，可以作为买入或卖出的信号。


## VWAP

VWAP（Volume Weighted Average Price）指标是一种量价加权平均价格指标，用于衡量一段时间内的平均交易价格，同时考虑了交易量的影响。VWAP通常用于衡量大宗交易的价格水平，特别是在股票、期货等金融市场中广泛应用。

VWAP的计算方法是将每个交易价格乘以对应的交易量，然后将所有交易的加权价格求和，并将总和除以总交易量，得到加权平均价格。公式如下：

VWAP = Σ(交易价格 * 交易量) / 总交易量

VWAP指标的特点是它更加关注大宗交易的影响，因为交易量越大，其对VWAP的影响越大。相比于普通的简单移动平均线（SMA），VWAP能够更好地反映市场的实际交易情况。

VWAP指标主要用于以下几个方面：

衡量交易价格与平均交易价格的偏离程度：交易价格高于VWAP意味着买入者愿意以较高价格购买资产，而交易价格低于VWAP则意味着卖出者愿意以较低价格出售资产。这可以帮助交易者判断当前价格是高估还是低估。

交易策略：交易者可以将VWAP作为交易策略的参考，例如，当价格高于VWAP时，可能选择卖出或持有，而当价格低于VWAP时，可能选择买入或持有。

市场趋势判断：VWAP还可以用于判断市场的整体趋势。如果价格持续高于VWAP，则可能表明市场处于上涨趋势；如果价格持续低于VWAP，则可能表明市场处于下跌趋势。


## SAR

SAR指标，全称为"停损点和反转指标"（Stop and Reverse），是一种技术分析指标，用于判断趋势的转折点和可能的反转。SAR指标通常以点位的形式标识在价格图表上，其主要用途是提供潜在的止损和反转信号。

SAR指标在上升趋势中的点位是在价格下方的，随着价格上涨，点位逐渐上移，当价格达到或突破SAR点位时，可能会发生趋势反转，SAR点位会从价格下方跳转到价格上方，这时可考虑进行止损或反转仓位。

在下降趋势中，SAR指标的点位是在价格上方的，随着价格下跌，点位逐渐下移，当价格跌至或跌破SAR点位时，可能发生趋势反转，SAR点位会从价格上方跳转到价格下方。

SAR指标的计算方法比较复杂，需要使用一系列的计算公式，具体涉及到前期的最高价、最低价、加速因子等参数。它是一种相对较为简单和直观的技术指标，常用于股市和外汇市场等金融市场的交易分析。


## 入门级/初级重点学习

1. 移动平均线 (MA)：用于平滑价格数据，帮助分析趋势方向和支撑/阻力水平。
2. 相对强弱指标 (RSI)：用于衡量价格超买和超卖程度，判断市场是否过热或过冷。
3. 指数平滑移动平均线 (EMA)：类似于简单移动平均线，但对最近的数据赋予更高的权重，反映最新市场动态。
4. Bollinger Bands (布林带)：包含一条中轨和两条通道线，用于衡量价格的波动性，判断趋势的强弱。
5. MACD (移动平均收敛/发散指标)：结合短期和长期的指数平滑移动平均线，帮助判断价格的趋势和拐点。


## MA交叉如何结合 BOLL

结合MA交叉和BOLL指标可以帮助你更好地判断价格的波动情况和趋势。BOLL指标主要包括中轨线（MA20）和上下轨线，用于衡量价格的波动范围和趋势的稳定性。

当MA5向上穿越MA20，并且价格位于BOLL的下轨线附近时，意味着短期均线上升，可能预示着价格的反弹和回升。这时候，你可以考虑买入。

当MA5向下穿越MA20，并且价格位于BOLL的上轨线附近时，意味着短期均线下降，可能预示着价格的下跌。这时候，你可以考虑卖出或者持币观望。

另外，你还可以结合BOLL指标的宽度来判断价格的波动范围。当BOLL指标的宽度较窄时，意味着价格波动较小，市场可能处于盘整状态；而当BOLL指标的宽度较宽时，意味着价格波动较大，市场可能处于趋势行情。

综合运用MA交叉和BOLL指标，可以帮助你更准确地判断价格的走势和趋势，辅助你做出交易决策。然而，还是需要结合其他技术指标和市场情况，进行全面的分析和判断，以确保交易决策的准确性和稳健性。


结合MA、BOLL和RSI指标的策略可以帮助你更全面地分析价格的走势和市场情况，从而做出更明智的交易决策。以下是一个简单的MA + BOLL + RSI策略的示例：

确定交易方向：首先，你可以使用MA交叉来确定交易的方向。当短期均线（例如MA5）向上穿越长期均线（例如MA20），说明市场可能处于上涨趋势，可以考虑买入。反之，当短期均线向下穿越长期均线，说明市场可能处于下跌趋势，可以考虑卖出或持币观望。

判断价格波动范围：使用BOLL指标来判断价格的波动范围。当BOLL指标的宽度较窄时，说明价格波动较小，市场可能处于盘整状态；当BOLL指标的宽度较宽时，说明价格波动较大，市场可能处于趋势行情。在较宽的BOLL带下，价格可能有更大的波动，可以考虑采取更谨慎的交易策略。

识别超买和超卖区域：使用RSI指标来判断市场的超买和超卖区域。当RSI指标超过70，说明市场处于超买状态，可能出现价格回调或反转；当RSI指标低于30，说明市场处于超卖状态，可能出现价格反弹。在超买区域可以考虑卖出或持币观望，在超卖区域可以考虑买入。

综合运用这三个指标，你可以制定一套完整的交易策略，根据市场情况和指标信号做出相应的买入和卖出决策。然而，交易策略的制定并不是一成不变的，还需要根据实际情况灵活调整和优化，以保持策略的稳健性和适应性。同时，注意合理控制风险，设置止损和止盈等交易规则，保护资金安全。


## Average True Range（ATR）

平均真实波幅指标可以测量价格的波动幅度，它考虑了价格的波动性和价格间的差异。
较大的ATR值表示较大的价格波动，可以用来预测价格的可能区间。

## Keltner Channels

类似于Bollinger Bands，Keltner Channels也是一个包含上轨、中轨和下轨的指标。
它基于价格的波动幅度，可以用来预测价格的可能区间。

## Average Directional Index（ADX

平均趋向指数可以衡量价格的趋势强度，包括上升趋势和下降趋势。较高的ADX值表示较强的趋势，可能预示着价格的价格区间。

## Moving Average Convergence Divergence（MACD）

MACD是一个结合了短期和长期移动均线的指标，可以用来判断价格的趋势和反转。交叉点和柱状图的变化可以用来预测价格的可能区间。

## Volatility Index（VIX）

VIX指数是一个反映市场波动性的指标，通常与股市相关。较高的VIX值表示较大的市场波动性，可以用来预测价格的可能区间


# TODO

MA 函数
MACD 函数
RSI 函数

EMA
WMA
BOLL
VWAP
TRIX
SAR

VOL 
KDJ 没太整明白

深度学习、机器学习
