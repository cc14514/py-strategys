# -*- coding: UTF-8 -*-

# pip install websocket-client
# pip3 install numpy

"""
币安：

https://binance-docs.github.io/apidocs/futures/cn/#api

合约类型 (contractType):

PERPETUAL 永续合约
CURRENT_MONTH 当月交割合约
NEXT_MONTH 次月交割合约
CURRENT_QUARTER 当季交割合约
NEXT_QUARTER 次季交割合约
PERPETUAL_DELIVERING 交割结算中合约


订单种类 (orderTypes, type):

LIMIT 限价单
MARKET 市价单
STOP 止损限价单
STOP_MARKET 止损市价单
TAKE_PROFIT 止盈限价单
TAKE_PROFIT_MARKET 止盈市价单
TRAILING_STOP_MARKET 跟踪止损单


订单方向 (side):

BUY 买入
SELL 卖出

有效方式 (timeInForce):

GTC - Good Till Cancel 成交为止
IOC - Immediate or Cancel 无法立即成交(吃单)的部分就撤销
FOK - Fill or Kill 无法全部立即成交就撤销
GTX - Good Till Crossing 无法成为挂单方就撤销

条件价格触发类型 (workingType)

MARK_PRICE
CONTRACT_PRICE

testnet的 REST baseurl 为 "https://testnet.binancefuture.com"
testnet的 Websocket baseurl 为 "wss://stream.binancefuture.com"

生产 Base Url：
wss://fstream.binance.com

"""
