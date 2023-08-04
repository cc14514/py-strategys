# -*- coding: UTF-8 -*-
import numpy as np


def boll(price_list, window=20, base_multiplier=2.0, threshold=0.5) :
    '''
    动态调整倍数
    返回:
        中轨：移动均线 MA(windo)
        上轨
        下跪
    '''
    # 计算移动平均值和标准差
    # ma = np.mean(price_list[-window:])
    ma = np.convolve(price_list, np.ones(window) / window, mode='valid')
    std = np.std(price_list[-window:])

    # 根据标准差的大小来调整倍数
    if std > threshold:
        multiplier = base_multiplier * (1 + (std - threshold))
    else:
        multiplier = base_multiplier / (1 + (threshold - std))

    # 计算BOLL指标中上轨和下轨
    upper_band = ma + multiplier * std
    lower_band = ma - multiplier * std
    #return ma, upper_band, lower_band, 1 + multiplier, 1 - multiplier
    return ma, upper_band, lower_band 


# MA5 MA10 MA20 
def moving_average(data, window):
    # 创建一个窗口大小的均值滤波器
    filt = np.ones(window) / window
    # 使用np.convolve计算移动平均
    ma = np.convolve(data, filt, mode='valid')
    return ma

# step 5m 
def window_5m(w) :
    return 5 * w

def test_moving_average():
    # 示例数据
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    data = [0, 1, 2, 3, 4, 5, 6, 7]
    # 计算移动平均
    m3 = moving_average(data, 3)
    m5 = moving_average(data, 5)
    print("DATA",data)
    print("MA3",m3)
    print("MA5",m5)

def test_boll():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    ma, u, l = boll(data, window=5)
    a = zip(data, ma, u , l)
    l = list(a)
    print("日期,当前价,中轨,上轨,下轨,")
    for i in l :
        print(",%d,%d,%d,%d," % i)


def test_ma_boll():
    pass

if __name__ == '__main__' : 
    # test_moving_average()
    test_boll()