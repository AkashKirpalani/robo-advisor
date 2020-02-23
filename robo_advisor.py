#INFO INPUTS 
import datetime
import json
import csv
from dotenv import load_dotenv
import os
import requests 



load_dotenv() #> loads contents of the .env file into the script's environment

symbol = "99"
correct = 0

print("WELCOME TO THE ROBO ADVISOR PROGRAM! WE ADVISE ON STOCK SYMBOLS")


while(correct == 0):
    symbol = input("PLEASE INPUT A STOCK YOU ARE LOOKING TO BUY: ")
    if(symbol.isalpha() == 1):
        correct = 1
        if(len(symbol) > 5):
            print("OOPS! Sorry you inputed the wrong information. You inputed more than 5 letters! Please try again! A ticker is only between 1-5 letters")
            correct = 0
    else:
        print("OOPS! Sorry you inputed the wrong information. You inputed numbers instead of letters! Please try again! A ticker is only letters and is between 1-5 letters")



api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)
while(response.status_code != 200):
     print("OOPS sorry we encountered an error on calling the API. Please try again.")
     while(correct == 0):
        symbol = input("PLEASE INPUT A STOCK YOU ARE LOOKING TO BUY: ")
        if(symbol.isalpha() == 1):
            correct = 1
            if(len(symbol) > 5):
                print("OOPS! Sorry you inputed the wrong information. You inputed more than 5 letters! Please try again! A ticker is only between 1-5 letters")
                correct = 0
        else:
            print("OOPS! Sorry you inputed the wrong information. You inputed numbers instead of letters! Please try again! A ticker is only letters and is between 1-5 letters")



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

d = datetime.datetime.today()

#INFO OUTPUTS 
print("-------------------------")
print("SELECTED SYMBOL:",symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...") 
print("REQUEST AT:", d.strftime("%Y-%m-%d %I:%M %p")) 
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")

mean = (float(recent_high) + float(recent_low))/2

if(float(latest_close) < float(mean)):
    print("RECOMMENDATION: BUY!")
    print("RECOMMENDATION REASON: The company is currently trading below its mean price and therefore has a higher probability of going up due to mean reversion theory.")

high_percential = float(recent_high)*0.9

if(float(latest_close) > float(mean)): 
    if(float(latest_close) > float(high_percential)):
         print("RECCOMENDATION: SHORT THE STOCK OR SELL IF YOU OWN THE STOCK")
         print("RECOMMENDATION REASON: The company is currently trading above its mean price and about 90% of its recent high, you should short the stock or sell the stock if you own it!")
    else:
        print("RECCOMENDATION: DO NOT BUY! BUT IF YOU OWN THE STOCK YOU SHOULD HOLD IT!")
        print("RECOMMENDATION REASON: Do not buy stock as the stock is trading about its mean and will probably revert back to its mean.")

print("-------------------------")
print("WRITING DATA INTO CSV...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
print("THANK YOU! DONE--PROGRAM HAS ENDED.")
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
 

