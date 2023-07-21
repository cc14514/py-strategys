# -*- coding: UTF-8 -*-

from reversion import *
import numpy as np # pip3 install numpy
import random

_price_data = []


# 初始化
stop_loss_threshold = 0.005  # 止损百分比
take_profit_threshold = 0.005  # 止盈百分比
fee = 0.0005 # 手续费，吃单手续费，我们不挂单 

window_size = 30
threshold = 0.002

position = 0
cooldown_period = 0  # 冷却时间设为 10 个时间单位（例如10分钟）
cooldown_timer = 0

usdt_balance = 1000.00
contract_quantity = 0
leverage = 1 # 合约杠杆为 10 倍
buy_price = 0
total_fee = 0

min_price = 50.00

total_stop = 1.0 # 止损次数


def mean_reversion_strategy(price_data):
    global position, usdt_balance, contract_quantity, cooldown_timer, buy_price,  fee, total_fee, total_stop

    if len(price_data) < window_size + 1:
        # 数据不足，暂不进行交易
        return 0

    # 计算移动窗口的平均值和标准差
    window = price_data[-window_size:]
    window_mean = sum(window) / window_size
    window_std = np.std(window)

    current_price = price_data[-1]

    if cooldown_timer > 0:
        # 冷却时间内不进行交易
        cooldown_timer -= 1
        return 0
    print("\n usdt_balance=%f, current_price=%f, buy_price=%f, position=%d, window_mean=%f, window_std=%f, price_data=%s" 
          % (usdt_balance, current_price, buy_price, position, window_mean, window_std, price_data))
    if usdt_balance > min_price and position == 0:
        # 若当前没有持仓
        if current_price > window_mean + threshold * window_std:
            # 当前价格偏高，开空仓
            f = 1 - fee
            position = -1  # 做空 ETH
            contract_quantity = min_price / current_price  # 合约数量
            pay = contract_quantity * current_price 
            pay_fee = pay * fee
            total_fee += pay_fee
            usdt_balance -= pay * f 
            buy_price = current_price
            print("<---- 开空 : contract_quantity=%f, buy_price=%f, fee=%f,  balance(-%f)=%f" % 
                  (contract_quantity, buy_price, pay_fee, contract_quantity * current_price , usdt_balance) )
            return -1  # 返回负数表示卖出
        elif current_price < window_mean - threshold * window_std:
            # 当前价格偏低，执行买入操作，开多仓
            f = 1 + fee
            position = 1  # 做多 ETH
            contract_quantity = min_price / current_price  # 合约数量
            pay = contract_quantity * current_price 
            pay_fee = pay * fee
            total_fee += pay_fee
            usdt_balance -= pay * f 
            buy_price = current_price
            print("<---- 开多 : contract_quantity=%f, buy_price=%f, fee=%f, balance(-%f)=%f" % 
                  (contract_quantity, buy_price, pay_fee, contract_quantity * current_price , usdt_balance) )
            return 1  # 返回正数表示买入
    elif position == 1:
        # 若当前持有多头仓位（持有多仓）
        f = 1 - fee
        if current_price < buy_price * (1 - stop_loss_threshold):
            # 止损平多仓
            total_stop += 1
            sell = contract_quantity * current_price  
            sell_fee = sell * fee
            total_fee += sell_fee
            usdt_balance += sell * f 
            income = (current_price - buy_price) * contract_quantity - sell_fee 
            cooldown_timer = cooldown_period  # 进入冷却时间
            print("****> 多单止损 : contract_quantity=%f, buy_price=%f, fee=%f, balance(+%f)=%f, income=%f" % 
                  (contract_quantity, buy_price, sell_fee, contract_quantity * current_price , usdt_balance, income) )

            contract_quantity = 0 
            position = 0  # 平仓
            return -1  # 返回负数表示卖出
        elif current_price > buy_price * (1 + take_profit_threshold):
            # 止盈平多仓
            sell = contract_quantity * current_price  
            sell_fee = sell * fee
            total_fee += sell_fee
            usdt_balance += sell * f 
            income = (current_price - buy_price) * contract_quantity - sell_fee 
            cooldown_timer = cooldown_period  # 进入冷却时间
            print("----> 多单止盈 : contract_quantity=%f, buy_price=%f, fee=%f, balance(+%f)=%f, income=%f" % 
                  (contract_quantity, buy_price, sell_fee, contract_quantity * current_price , usdt_balance, income) )
            contract_quantity = 0 
            position = 0  # 平仓
            return -1  # 返回负数表示卖出
    elif position == -1:
        # 若当前持有空头仓位（持有空仓）
        f = 1 - fee
        if current_price > buy_price * (1 + stop_loss_threshold):
            # 止损平空仓
            total_stop += 1
            sell = contract_quantity * (2 * buy_price - current_price)  
            sell_fee = sell * fee
            total_fee += sell_fee
            usdt_balance += sell * f  
            income = (buy_price - current_price) * contract_quantity - sell_fee 
            cooldown_timer = cooldown_period  # 进入冷却时间
            print("****> 空单止损 : contract_quantity=%f, buy_price=%f, fee=%f, balance(+%f)=%f, income=%f" % 
                  (contract_quantity, buy_price, sell_fee, contract_quantity * current_price , usdt_balance, income) )
            contract_quantity = 0 
            position = 0  # 平仓
            return 1  # 返回正数表示买入
        elif current_price < buy_price * (1 - take_profit_threshold):
            # 止盈平空仓
            sell = contract_quantity * (2 * buy_price - current_price)  
            sell_fee = sell * fee
            total_fee += sell_fee
            usdt_balance += sell * f  
            income = (buy_price - current_price) * contract_quantity - sell_fee 
            cooldown_timer = cooldown_period  # 进入冷却时间
            print("----> 空单止盈 : contract_quantity=%f, buy_price=%f, fee=%f, balance(+%f)=%f, income=%f" % 
                  (contract_quantity, buy_price, sell_fee, contract_quantity * current_price , usdt_balance, income) )
            contract_quantity = 0 
            position = 0  # 平仓
            return 1  # 返回正数表示买入        
    print("-- 无交易")
    return 0  # 无交易信号


def make_random_list(i, j, k):
    global _price_data
    t = 0
    while( t < i) :
        _price_data.append(random.randint(j,k))
        t+=1


def do_loop() :
    # 假设_price_data为实时行情价格列表，不断更新
    # 调用均值回归策略获取交易信号
    global usdt_balance, _price_data, window_size
    cost = usdt_balance
    make_random_list(86400, 1875, 1917)
    print("all_price_data = %s" % (_price_data))
    t = 0
    for i in range(0, len(_price_data)-(window_size+2)) :
        signal = mean_reversion_strategy(_price_data[i:i+(window_size+2)])
        t+=np.abs(signal)

    income = usdt_balance - cost 
    print("\n total_order=%d, total_stop(%d)=%f, cost=%f, result=%f, income=%f, fee=%f" % (t, total_stop, total_stop/t, cost, usdt_balance, income, total_fee))
    return "done."
