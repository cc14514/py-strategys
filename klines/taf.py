# -*- coding: UTF-8 -*-
import numpy as np
import csv


def boll(price_list, ma=None, window=20, long_window=100, base_multiplier=2.0, threshold=0.2):
    '''
    动态调整倍数
    返回:
        上轨
        中轨：移动均线 MA(window)
        下轨
    '''
    # 计算移动平均值和标准差
    if ma is None:
        ma = np.convolve(price_list, np.ones(window) / window, mode='valid')

    # 使用更长期的标准差计算
    long_std = np.std(price_list[-long_window:])

    # 根据标准差的大小来调整倍数
    if long_std > threshold:
        multiplier = base_multiplier * (1 + (long_std - threshold))
    else:
        multiplier = base_multiplier / (1 + (threshold - long_std))

    # 计算BOLL指标中上轨和下轨
    upper_band = ma + multiplier * np.std(price_list[-window:])
    lower_band = ma - multiplier * np.std(price_list[-window:])

    return upper_band, ma, lower_band

def boll2(price_list, ma=None, window=20, base_multiplier=2.0, threshold=0.5) :
    '''
    动态调整倍数
    返回:
        上轨
        中轨：移动均线 MA(windo)
        下跪
    '''
    # 计算移动平均值和标准差
    # ma = np.mean(price_list[-window:])
    if ma is None :
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
    return upper_band, ma, lower_band


# MA5 MA10 MA20 
def ma(data, window):
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
    m3 = ma(data, 3)
    m5 = ma(data, 5)
    print("DATA",data)
    print("MA3",m3)
    print("MA5",m5)

def test_boll():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    u, ma, l = boll(data, window=5)
    a = zip(data, ma, u , l)
    l = list(a)
    print("日期,当前价,中轨,上轨,下轨,")
    for i in l :
        print(",%d,%d,%d,%d," % i)

def write_to_csv(file_path, data_lists):
    # 获取列表长度，假设所有列的长度都一样，取第一个列表的长度即可
    data_len = len(data_lists[0])
    
    # 转换数据结构，将多个列表合并成一个列表的列表，并在每个列表前面添加一个空元素
    data_to_write = [list(row) for row in zip(*data_lists)]
    
    # 在整个二维列表的第一行和第一列都添加空元素
    data_to_write.insert(0, [''] * (len(data_lists) + 1))
    for row in data_to_write:
        row.insert(0, '')

    # 写入 CSV 文件
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)

def test_ma_boll():
    pass

if __name__ == '__main__' : 
    # test_moving_average()
    test_boll()