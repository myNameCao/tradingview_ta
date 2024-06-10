from tradingview_ta import TA_Handler, Interval, Exchange
from flask import Flask, request

import time

app = Flask(__name__)
@app.route('/api/query', methods=['GET'])

def query_data():
    
    start= time.time()
    try:
       symbol = request.args.get("symbol")
       interval = request.args.get("interval")
       print(time.time()-start,111)
            
       data=  {"data": get_data(symbol,interval=interval), "success": True}  
       print(time.time()-start,111)
       return data
    except Exception as e:
        return {"data": {}, "success": False}
  
   
def get_data(symbol,interval='5m'):
  print(symbol,interval)
  tesla = TA_Handler(
    symbol=symbol,
    screener="crypto",
    exchange="BINANCE",
    # interval=Interval.INTERVAL_1_DAY
    interval=interval
  )
  analysis= tesla.get_analysis()
  return  {'summary':analysis.summary,'oscillators':analysis.oscillators,'moving_averages':analysis.moving_averages}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686,debug=True)
    # get_data("BNBUSDT",'1h')