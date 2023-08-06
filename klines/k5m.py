
# -*- coding: UTF-8 -*-

# https://binance-docs.github.io/apidocs/spot/cn/#c59e471e81

# pip3 install numpy
# pip3 install requests
# pip3 install mysql-connector-python
# pip3 install matplotlib

'''
CREATE TABLE `kline_ethusdt_5m` (
  `id` bigint NOT NULL,
  `o` decimal(20,8) DEFAULT NULL,
  `h` decimal(20,8) DEFAULT NULL,
  `l` decimal(20,8) DEFAULT NULL,
  `c` decimal(20,8) DEFAULT NULL,
  `v` bigint DEFAULT NULL,
  `t` bigint DEFAULT NULL,
  `q` varchar(45) DEFAULT NULL,
  `n` bigint DEFAULT NULL,
  `vv` varchar(45) DEFAULT NULL,
  `qq` varchar(45) DEFAULT NULL,
  `ct` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
'''


'''
request:

symbol	STRING	YES	
interval	ENUM	YES	详见枚举定义：K线间隔
startTime	LONG	NO	
endTime	LONG	NO	
limit	INT	NO	默认 500; 最大 1000.

response:

[
  [
    1499040000000,      // k线开盘时间
    "0.01634790",       // 开盘价
    "0.80000000",       // 最高价
    "0.01575800",       // 最低价
    "0.01577100",       // 收盘价(当前K线未结束的即为最新价)
    "148976.11427815",  // 成交量
    1499644799999,      // k线收盘时间 t
    "2434.19055334",    // 成交额
    308,                // 成交笔数
    "1756.87402397",    // 主动买入成交量
    "28.46694368",      // 主动买入成交额
    "17928899.62484339" // 请忽略该参数
  ]
]

{
  "E": 123456789,   // 事件时间
  "k": {
    "o": "0.0010",  // 这根K线期间第一笔成交价
    "h": "0.0025",  // 这根K线期间最高成交价
    "l": "0.0015",  // 这根K线期间最低成交价
    "c": "0.0020",  // 这根K线期间末一笔成交价
    "v": "1000",    // 这根K线期间成交量
    "t": 111        // 收盘时间
    "q": "1.0000",  // 这根K线期间成交额
    "n": 100,       // 这根K线期间成交笔数
    "V": "500",     // 主动买入的成交量
    "Q": "0.500",   // 主动买入的成交额
    "B": "123456"   // 忽略此参数
  }
}
'''



# -*- coding: UTF-8 -*-

# https://binance-docs.github.io/apidocs/spot/cn/#c59e471e81

# pip3 install numpy
# pip3 install requests
# pip3 install mysql-connector-python


'''
request:

symbol	STRING	YES	
interval	ENUM	YES	详见枚举定义：K线间隔
startTime	LONG	NO	
endTime	LONG	NO	
limit	INT	NO	默认 500; 最大 1000.

response:

[
  [
    1499040000000,      // k线开盘时间
    "0.01634790",       // 开盘价
    "0.80000000",       // 最高价
    "0.01575800",       // 最低价
    "0.01577100",       // 收盘价(当前K线未结束的即为最新价)
    "148976.11427815",  // 成交量
    1499644799999,      // k线收盘时间 t
    "2434.19055334",    // 成交额
    308,                // 成交笔数
    "1756.87402397",    // 主动买入成交量
    "28.46694368",      // 主动买入成交额
    "17928899.62484339" // 请忽略该参数
  ]
]

{
  "E": 123456789,   // 事件时间
  "k": {
    "o": "0.0010",  // 这根K线期间第一笔成交价
    "h": "0.0025",  // 这根K线期间最高成交价
    "l": "0.0015",  // 这根K线期间最低成交价
    "c": "0.0020",  // 这根K线期间末一笔成交价
    "v": "1000",    // 这根K线期间成交量
    "t": 111        // 收盘时间
    "q": "1.0000",  // 这根K线期间成交额
    "n": 100,       // 这根K线期间成交笔数
    "V": "500",     // 主动买入的成交量
    "Q": "0.500",   // 主动买入的成交额
    "B": "123456"   // 忽略此参数
  }
}
'''

import time
import requests
import datetime
import math
import mysql.connector 
import numpy as np 
import sys
import taf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pytz


proxies = {
    "http":"http://127.0.0.1:9981", 
    "https":"http://127.0.0.1:9981"
}

# 数据表的配置 >>>>
table_name = 'kline_ethusdt_5m'
data_interval = '5m'
data_limit = 100
# 数据表的配置 <<<< 


y1_ts = 31536000
api_url = 'https://api.binance.com/api/v3/klines?symbol=%s&interval=%s&limit=%d'

stop_loss_threshold = 0.01  # 止损百分比
take_profit_threshold = 0.01  # 止盈百分比
window_size = 300
threshold = 0.002


def connect_database():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',     # 数据库主机地址
            user='root',      # 数据库用户名
            password='12345678',  # 数据库密码
            database='exchange'     # 数据库名
        )
        print("数据库连接成功")
        return conn
    except mysql.connector.Error as err:
        print("数据库连接失败：", err)
        return None


def insert_data_to_db(conn, data):
    try:
        # 连接数据库
        cursor = conn.cursor()
        # 插入数据的 SQL 语句
        insert_sql = f'''
        INSERT INTO {table_name} (id, o, h, l, c, v, t, q, n, vv, qq, ct)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        del_sql = f'''
        delete from {table_name} where id=%s;
        '''
        # 遍历 data 列表并插入数据
        for row in data:
            ts = int(row[0])
            ct = datetime.datetime.fromtimestamp(ts/1000) 
            ctt = ct.strftime('%Y-%m-%d %H:%M:%S')
            print(ts, ct, ctt)
            row[-1] = ctt
            cursor.execute(del_sql, (row[0],))
            cursor.execute(insert_sql, row)

        # 提交事务
        conn.commit()
        print("数据插入成功")

        # 关闭连接
        cursor.close()
    except mysql.connector.Error as err:
        print("数据插入失败：", err)

def query_max_id(conn):
    sql_query = f'select max(id) from {table_name}'
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchone()
    _id = result[0]
    cursor.close()
    return _id

def query_min_id(conn):
    sql_query = f'select min(id) from {table_name}'
    cursor = conn.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchone()
    _id = result[0]
    cursor.close()
    print(">>>>>>>>>>>>>>>>>>>", _id)
    return _id

def query_data(conn, limit, startTime=None, endTime=None):
    '''
    # 结果集倒叙，需要 reverse
    返回的结果集：(id, o, c, c-o)
    '''
    # sql_query = "SELECT (o+h+l+c)/4 , id FROM exchange.{table_name} ORDER BY id DESC LIMIT 0, %d" % n
    if startTime is not None and endTime is not None : 
        sql_query = f"SELECT id, o, c, (c-o) FROM exchange.{table_name} where id >= %d and id <= %d order by id desc limit 0, %d" % (startTime, endTime, limit)
    else:
        sql_query = f"SELECT id, o, c, (c-o) FROM exchange.{table_name} order by id desc limit 0, %d" % limit 
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    cursor.close()   
    return results

def get_kline_data(symbol='ETHUSDT', interval='5m', startTime=0, endTime=0, limit=100) :
    url = api_url
    if startTime > 0 :
        url = url + ("&startTime=%d" % startTime) 
    if endTime > 0 :
        url = url + ("&endTime=%d" % endTime) 
    url = url % (symbol, interval, limit)
    # print(url)
    try :
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            data = response.json()
            data = sorted(data, key=lambda x: x[0], reverse=True)
            return data
        else:
            print(f"HTTP GET 请求失败，状态码：{response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP GET 请求异常：{e}\n\n{url}")

    return None


position = 0
contract_quantity = 0
buy_price = 0.0

def mean_reversion_strategy(price_data):
    global position, contract_quantity, buy_price 
    __window_size = len(price_data)

    if __window_size < window_size + 1:
        # 数据不足，暂不进行交易
        print("want %d , current %d" % (window_size, __window_size))
        return 0

    # 计算移动窗口的平均值和标准差
    window = price_data
    window_mean = sum(window) / __window_size
    window_std = np.std(window)

    current_price = price_data[-1]
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if position == 0:
        # 若当前没有持仓
        if current_price > window_mean + threshold * window_std:
            print("%s <---- 开空: current_price=%f, window_mean=%f, window_std=%f" % (current_time, current_price, window_mean, window_std)) 
            buy_price = current_price
            position = -1
            return -1  # 返回负数表示卖出
        elif current_price < window_mean - threshold * window_std:
            # 当前价格偏低，执行买入操作，开多仓
            print("%s <---- 开多: current_price=%f, window_mean=%f, window_std=%f" % (current_time, current_price, window_mean, window_std)) 
            buy_price = current_price
            position = 1
            return 1  # 返回正数表示买入
    elif position == 1:
        # 若当前持有多头仓位（持有多仓）
        if current_price < buy_price * (1 - stop_loss_threshold):
            print("****> 多单止损") 
            position = 0  # 平仓
            return -1  # 返回负数表示卖出
        elif current_price > buy_price * (1 + take_profit_threshold):
            print("----> 多单止盈") 
            position = 0  # 平仓
            return -1  # 返回负数表示卖出
    elif position == -1:
        # 若当前持有空头仓位（持有空仓）
        if current_price > buy_price * (1 + stop_loss_threshold):
            # 止损平空仓
            print("****> 空单止损") 
            position = 0  # 平仓
            return 1  # 返回正数表示买入
        elif current_price < buy_price * (1 - take_profit_threshold):
            # 止盈平空仓
            print("----> 空单止盈") 
            position = 0  # 平仓
            return 1  # 返回正数表示买入        
    print("-- 无交易 current_price=%f, buy_price=%f" % (current_price, buy_price))
    return 0  # 无交易信号



def init_history_data():
    f = True
    conn = connect_database() 

    t = query_min_id(conn)
    if t is None :
        t = time.time()*1000 

    while f :
        data = get_kline_data(interval=data_interval, limit=data_limit, startTime=(t-data_limit*60*5*1000), endTime=t) # 初始化历史数据时，使用 endtime 来向前检索
        if data is not None and len(data) > 0 :
            insert_data_to_db(conn, data)
            t = data[-1][0] - 1 # 检索历史数据时用第一条
            time.sleep(0.07)
        else:
            f = False
            print("done.")
    conn.close()


pil = []
pvl = []
def live_data() :
    # last_ts = (time.time() - y1_ts) * 1000 
    # t = time.time()*1000 历史数据时用最新时间
    global pil, pvl

    f = True
    conn = connect_database() 
    while f :
        t = query_max_id(conn)
        if t is None :
            return None
        # print("time->", t)
        data = get_kline_data(limit=data_limit, startTime=t, endTime=(t+data_limit*60*5*1000)) # 追踪最新数据时使用 starttime 向后检索
        # data = get_kline_data(limit=100, endTime=t) # 初始化历史数据时，使用 endtime 来向前检索
        if data is not None and len(data) > 0 :
            insert_data_to_db(conn, data)
            # if data[0][0] < last_ts : 
            #     f = False
            #     print("done.")
            # t = data[0][0] - 1 # 检索历史数据时用第一条
            time.sleep(0.2)
        else :
            results = query_data(conn, 301)
            il = []
            vl = []
            for result in results:
                i = result[0]
                o = float(result[1])
                c = float(result[2])
                s = float(result[3])
                il.append(i)
                vl.append(c)
                # if s < 0 : # 下跌用收盘价，上涨用开盘价，始终用支撑位
                #     vl.append(c)
                # else :
                #     vl.append(o)
                # print("xxxxxx", i, o, c, s)
            
            il.reverse()
            vl.reverse()

            if pil != il :
                pil.clear()
                pvl.clear()
                pil = il.copy()
                pvl = vl.copy()
                print(">>------- TODO : try trading ------->>", pil[-1])
                mean_reversion_strategy(pvl) 
                print("<<------- TODO : try trading -------<<", pil[-1])

            else:
                print(">>------- pass ------->>")

            time.sleep(60)

    conn.close()

def test_taf():
    conn = connect_database() 
    results = query_data(conn, 300) 
    #results = query_data(conn, 30, startTime=1690992000000, endTime=1691078100000)
    lc = []
    lt = []
    for r in results :
        lc.append(float(r[2]))
        lt.append(float(r[0]))
    lc.reverse()
    lt.reverse()
    # print(lc)
    k5m_m5 = taf.ma(lc, 5) # MA5
    k5m_m10 = taf.ma(lc, 10) # MA10
    # k5m_boll_u, k5m_boll_m, k5m_boll_l 分别为 上轨 中轨 下轨 
    k5m_boll_u, k5m_boll_m, k5m_boll_l = taf.boll(lc, ma = k5m_m5, window = 5) #BOLL5
    # 价格数据
    lc = lc[-len(k5m_boll_m):]
    # 对应的时间戳列表
    lt = lt[-len(k5m_boll_m):]


    # 将时间戳转换为时分秒（H:M:S）的形式
    # Convert timestamps to datetime objects and specify timezone
    tz = pytz.timezone('Asia/Shanghai')  # Replace 'Asia/Shanghai' with your desired timezone
    lt_time = [datetime.datetime.utcfromtimestamp(ts/1000).replace(tzinfo=pytz.utc).astimezone(tz) for ts in lt]
    
    print(lt_time)

    # Creating the figure and axis objects
    fig, ax = plt.subplots()

    # Plotting the lines
    ax.plot(lt_time, k5m_boll_u, label='Upper Bollinger Band', color='blue')
    ax.plot(lt_time, k5m_boll_m, label='Middle Bollinger Band', color='green')
    ax.plot(lt_time, k5m_boll_l, label='Lower Bollinger Band', color='red')
    ax.plot(lt_time, lc, label='Price', color='black', linewidth=2)
    ax.plot(lt_time, k5m_m5, label='MA 5', color='Yellow', linewidth=1)

    # Adding legend
    ax.legend()

    # Adding title and axis labels
    ax.set_title('Bollinger Bands')
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')

    date_format = mdates.DateFormatter('%Y-%m-%d %H:%M:%S', tz=tz)  # Specify the timezone
    ax.xaxis.set_major_formatter(date_format)

    # Automatically adjust the angle of x-axis labels to avoid overlapping
    plt.gcf().autofmt_xdate()

    # Show the plot
    plt.show()


    # TODO 
    conn.close()
    pass

if __name__ == '__main__' :
    print(len(sys.argv), sys.argv)
    if len(sys.argv) > 1 and sys.argv[-1] == "init" :
        init_history_data()
    if len(sys.argv) > 1 and sys.argv[-1] == "test" :
        test_taf()
    else:
        live_data()
