from tradingview_ta import TA_Handler, Interval, Exchange
from flask import Flask, request

app = Flask(__name__)
@app.route('/api/query', methods=['GET'])

def query_data():
    try:
       symbol = request.args.get("symbol")
       interval = request.args.get("interval")
       return {"data": get_data(symbol,interval=interval), "success": True}  
    except Exception as e:
        return {"data": {}, "success": False}
  
   
def get_data(symbol,interval='1d'):
  print(symbol,interval)
  tesla = TA_Handler(
    symbol=symbol,
    screener="crypto",
    exchange="BINANCE",
    # interval=Interval.INTERVAL_1_DAY
    interval=interval
  )
  print(tesla.get_analysis().summary)
  return  tesla.get_analysis().summary



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8686,debug=True)
    # get_data("BNBUSDT",'1h')