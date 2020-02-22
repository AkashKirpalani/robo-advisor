#INFO INPUTS 
import requests 
import json

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)
#print(type(response)) 
#print(response.status_code)
#print(response.text)


parsed_response = json.loads(response.text)

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())
lastest_day = dates[0] 
#sort this to ensure that the latest day is first 


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = parsed_response["Time Series (Daily)"][lastest_day]["4. close"]
#max of all high prices 
high_prices = []
low_prices = []

for date in dates: 
	high_price = tsd[date]["2. high"]
	high_prices.append(float(high_price))
	low_price = tsd[date]["3. low"]
	low_prices.append(float(low_price))


recent_high = max(high_prices) 
recent_low = min(low_prices)

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md#formatting-as-currency
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" 


#INFO OUTPUTS 
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
#use date time module for this 
print("REQUEST AT: 2018-02-20 02:00pm") 
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
#format as USD
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")