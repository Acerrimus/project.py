import requests
import json
import sys
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import plotly.graph_objects as go



country_currency =  {
     
    'usa': 'USD',  # United States Dollar
    'italy': 'EUR',  # Euro
    'egypt': 'EGP',  # Egyptian Pound
    'united_kingdom': 'GBP',  # British Pound Sterling

}
country_codes = {
   "Egypt": "eg", "Italy": "it", "United Kingdom": "gb", "United States Of America": "us",
}

parser = ArgumentParser()
parser.add_argument('-c')
parser.add_argument('-i', default='econ')
args = parser.parse_args() 

# USE YOUR OWN KEYS
key = 'DEMO'
news_key = 'DEMO'

def main():

    # If no arguments are given when running, prompt for them.

    if len(sys.argv) == 1:
        
        country = input("Country to research: ").lower().strip()
        infoType = input ("What kind of info?   -econ   -news   -politic \n")


    # Otherwise, use Arg Parse cl interface
    else:

        country = str(args.c).lower().strip()
        infoType = str(args.i).lower().strip()

    # Output depending on infoType:

    if infoType == 'econ':
        econ(country)


    elif infoType == 'news':
         news(country.title())

    elif infoType == 'politics':
         ...

    else:
        print("Expected infoType argument, none given.")

def econ(country, graph='y'):
        try:
            coin = country_currency[country] 
        except KeyError:
             print("Country does not exist")
             pass

        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={coin}&to_currency=GBP&apikey={key}'

        r = requests.get(url)
        data = r.json()

        try:
            conversion = (float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]))
            gbp_conversion = 1/ float(conversion)
            print(f"The current rate of {country_currency[country]} to GBP is £{conversion} \n £1 = {gbp_conversion}")      
            
        except KeyError:
            print("Coin does not exist")
            pass

        # SECOND SOURCE (OECD) For more detailed info
        
        # url = f'http://stats.oecd.org/SDMX-JSON/data/<dataset identifier>/<filter expression>/<agency name>[ ?<additional parameters>]'
        
        if not(graph):
            graph = (input("Display graph? [Y/N]").lower() == 'y')

        while graph:
            dateRange = int(input("1. Week 2. Month 3. Year :"))

            if dateRange == 2:

                url = f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol={coin}&to_symbol=GBP&apikey={key}'
                r = requests.get(url)
                data = r.json()

                dates = [dates for dates in data['Time Series FX (Monthly)']]
                print('DATES SUCCESS')
                exchange_rates = [(data['Time Series FX (Monthly)'][dates]['4. close']) for dates in data['Time Series FX (Monthly)']]


            fig = go.Figure(data=go.Scatter(x=dates, y=exchange_rates, mode='lines+markers'))

            fig.update_layout(title='EGP to GBP Exchange Rates',
                            xaxis_title='Date',
                            yaxis_title='Exchange Rate')

            fig.show()
        

            graph = False

def news(country):
        
        try:
             country = country_codes[country]

        except KeyError:
             print("Your country does not exist, please refer to an official country names list")
             pass
        # url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics={country}&tickers=AAPL&apikey={key}'
        url = f'https://api.worldnewsapi.com/search-news?source-countries={country}&language=en&api-key={news_key}'
        r = requests.get(url)
        data = r.json()

        try:
            output = [article['title'] for article in data['news']]
            for _ in range(10):
                print(f"{_}. {output[_]}\n")
            
        except KeyError:
            print("Country does not exist")
            pass

def crypto():
        coin = input("What coin do you want? :").strip()
        cryptourl = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={coin}&to_currency=GBP&apikey={key}'

        r = requests.get(cryptourl)
        data = r.json()

        try:
            return(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

        except KeyError:
            print("Coin does not exist")
            pass



if __name__ == "__main__":
     main()
