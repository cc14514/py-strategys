# -*- coding: UTF-8 -*-

# pip install websocket-client
# pip3 install numpy

#Real Trading: wss://fx-ws.gateio.ws/v4/ws/btc
#TestNet Trading: wss://fx-ws-testnet.gateio.ws/v4/ws/btc
ws_api_path = 'wss://fx-ws-testnet.gateio.ws/v4/ws/btc'

proxy_host = '127.0.0.1'  
proxy_port = 9981 

ws = None

def connect_to_websocket() :
    global ws  
    ws = create_connection(ws_api_path, http_proxy_host=proxy_host, http_proxy_port=proxy_port)

def close_websocket():
    global ws  
    if ws is not None:
        ws.close()
        ws = None  


# ws.send('{"time" : 123456, "channel" : "futures.ping"}')

# ws.send('{"time" : 123456, "channel" : "futures.tickers", "event": "subscribe", "payload" : ["BTC_USD"]}')

# ws.recv()
