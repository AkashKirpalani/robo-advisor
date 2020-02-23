#INFO INPUTS 
import json
import csv
from dotenv import load_dotenv
import os
import requests 


load_dotenv() #> loads contents of the .env file into the script's environment

symbol = "TSLA"
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
#ask user for the symbol 
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
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
    Source: https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/datatypes/numbers.md #formatting-as-currency
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
print("WRITING DATA INTO CSV...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
#write a csv file into the data directory 

csv_file_path = "data/prices.csv" # a relative filepath

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"] 

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames= csv_headers)
    writer.writeheader() # uses fieldnames set above
    daily_prices = tsd[date]
    for date in dates: 
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"], 
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
        })
 

