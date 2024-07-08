import requests
import json
import sys
from argparse import ArgumentParser


country_list =  {

    'usa': 'USD',  # United States Dollar
    'italy': 'EUR',  # Euro
    'france': 'EUR',  # Euro
    'germany': 'EUR',  # Euro
    'united_kingdom': 'GBP',  # British Pound Sterling
    'japan': 'JPY',  # Japanese Yen
    'australia': 'AUD',  # Australian Dollar
    'canada': 'CAD',  # Canadian Dollar
    'india': 'INR',  # Indian Rupee
    'brazil': 'BRL',  # Brazilian Real
    'china': 'CNY',  # Chinese Yuan
    'russia': 'RUB',  # Russian Ruble
    'south_korea': 'KRW',  # South Korean Won
    'switzerland': 'CHF',  # Swiss Franc
    'mexico': 'MXN',  # Mexican Peso
    'netherlands': 'EUR',  # Euro
    'spain': 'EUR',  # Euro
    'turkey': 'TRY',  # Turkish Lira
    'uae': 'AED',  # United Arab Emirates Dirham
    'argentina': 'ARS',  # Argentine Peso
    'sweden': 'SEK',  # Swedish Krona
    'norway': 'NOK',  # Norwegian Krone
    'denmark': 'DKK',  # Danish Krone
    'singapore': 'SGD',  # Singapore Dollar
    'poland': 'PLN',  # Polish Złoty
    'thailand': 'THB',  # Thai Baht
    'south_africa': 'ZAR',  # South African Rand
    'new_zealand': 'NZD',  # New Zealand Dollar
    'israel': 'ILS',  # Israeli New Shekel
    'egypt': 'EGP',  # Egyptian Pound
    'saudi_arabia': 'SAR',  # Saudi Riyal
    'malaysia': 'MYR',  # Malaysian Ringgit
    'indonesia': 'IDR',  # Indonesian Rupiah
    'belgium': 'EUR',  # Euro
    'austria': 'EUR',  # Euro
    'greece': 'EUR',  # Euro
    'portugal': 'EUR',  # Euro
    'ireland': 'EUR',  # Euro
    'finland': 'EUR',  # Euro
    'hungary': 'HUF',  # Hungarian Forint
    'czech_republic': 'CZK',  # Czech Koruna
    'bahrain': 'BHD',  # Bahraini Dinar
    'qatar': 'QAR',  # Qatari Riyal
    'kuwait': 'KWD',  # Kuwaiti Dinar
    'oman': 'OMR',  # Omani Rial
    'lebanon': 'LBP',  # Lebanese Pound
    'cyprus': 'EUR',  # Euro
    'luxembourg': 'EUR',  # Euro
    'iceland': 'ISK',  # Icelandic Króna
    'estonia': 'EUR',  # Euro
    'latvia': 'EUR',  # Euro
    'lithuania': 'EUR',  # Euro
}
parser = ArgumentParser()
parser.add_argument('-c')
parser.add_argument('-i', default='econ')
args = parser.parse_args()


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
        conversion = econ(country)
        gbp_conversion = 1/ float(conversion)
        print(f"The current rate of {country_list[country]} to GBP is £{conversion} \n £1 = {gbp_conversion}")

    elif infoType == 'news':
         news(country)

    elif infoType == 'politics':
         ...

    else:
        print("Expected infoType argument, none given.")

def econ(country):
        try:
            coin = country_list[country]

        except KeyError:
             print("Country does not exist")
             pass

        url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={coin}&to_currency=GBP&apikey=A4JSMHQUEASHWS4Q'

        r = requests.get(url)
        data = r.json()

        try:
            return(float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]))

        except KeyError:
            print("Coin does not exist")
            pass

def news(country):

        url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics={country}&tickers=AAPL&apikey=A4JSMHQUEASHWS4Q'
        r = requests.get(url)
        data = r.json()

        try:
            output = [article['title'] for article in data['feed']]
            for _ in range(10):
                print(f"{_}. {output[_]}\n")

        except KeyError:
            print("Country does not exist")
            pass

def crypto():
        coin = input("What coin do you want? :").strip()
        cryptourl = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={coin}&to_currency=GBP&apikey=A4JSMHQUEASHWS4Q'

        r = requests.get(cryptourl)
        data = r.json()

        try:
            return(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])

        except KeyError:
            print("Coin does not exist")
            pass



if __name__ == "__main__":
     main()
