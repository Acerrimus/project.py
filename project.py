import requests
import json
import sys
from argparse import ArgumentParser
import matplotlib.pyplot as plt



country_currency =  {
     
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
country_codes = {
    "Afghanistan": "af",
    "Albania": "al",
    "Algeria": "dz",
    "American Samoa": "as",
    "Anguilla": "ai",
    "Australia": "au",
    "Austria": "at",
    "Bahamas": "bs",
    "Bahrain": "bh",
    "Bangladesh": "bd",
    "Barbados": "bb",
    "Belarus": "by",
    "Belgium": "be",
    "Belize": "bz",
    "Benin": "bj",
    "Bermuda": "bm",
    "Bhutan": "bt",
    "Bosnia And Herzegovina": "ba",
    "Bouvet Island": "bv",
    "Brazil": "br",
    "British Indian Ocean Territory": "io",
    "Brunei Darussalam": "bn",
    "Bulgaria": "bg",
    "Burkina Faso": "bf",
    "Burundi": "bi",
    "Cambodia": "kh",
    "Cameroon": "cm",
    "Canada": "ca",
    "Cape Verde": "cv",
    "Central African Republic": "cf",
    "Chile": "cl",
    "China": "cn",
    "Colombia": "co",
    "Comoros": "km",
    "Congo, Democratic Republic Of The": "cd",
    "Congo, Republic Of The": "cg",
    "Costa Rica": "cr",
    "Cote D'ivoire": "ci",
    "Croatia": "hr",
    "Cuba": "cu",
    "Cyprus": "cy",
    "Czech Republic": "cz",
    "Denmark": "dk",
    "Djibouti": "dj",
    "Dominican Republic": "do",
    "Ecuador": "ec",
    "Egypt": "eg",
    "El Salvador": "sv",
    "Eritrea": "er",
    "Ethiopia": "et",
    "Europe": "eu",
    "Fiji": "fj",
    "Finland": "fi",
    "France": "fr",
    "French Guiana": "gf",
    "French Polynesia": "pf",
    "Gambia": "gm",
    "Germany": "de",
    "Ghana": "gh",
    "Greece": "gr",
    "Guatemala": "gt",
    "Guinea": "gn",
    "Guyana": "gy",
    "Honduras": "hn",
    "Hong Kong": "hk",
    "Hungary": "hu",
    "Iceland": "is",
    "India": "in",
    "Indonesia": "id",
    "Iran": "ir",
    "Iraq": "iq",
    "Ireland": "ie",
    "Israel": "il",
    "Italy": "it",
    "Japan": "jp",
    "Jordan": "jo",
    "Kazakhstan": "kz",
    "Kenya": "ke",
    "Kuwait": "kw",
    "Laos": "la",
    "Latvia": "lv",
    "Lebanon": "lb",
    "Lesotho": "ls",
    "Liberia": "lr",
    "Liechtenstein": "li",
    "Lithuania": "lt",
    "Luxembourg": "lu",
    "Macedonia": "mk",
    "Madagascar": "mg",
    "Malawi": "mw",
    "Malaysia": "my",
    "Maldives": "mv",
    "Mali": "ml",
    "Malta": "mt",
    "Mauritania": "mr",
    "Mauritius": "mu",
    "Mexico": "mx",
    "Micronesia, Federated States Of": "fm",
    "Moldova": "md",
    "Monaco": "mc",
    "Montenegro": "me",
    "Montserrat": "ms",
    "Morocco": "ma",
    "Myanmar": "mm",
    "Namibia": "na",
    "Nepal": "np",
    "Netherlands": "nl",
    "New Zealand": "nz",
    "Niger": "ne",
    "Nigeria": "ng",
    "North Korea": "kp",
    "Norway": "no",
    "Oman": "om",
    "Pakistan": "pk",
    "Palestinian Territory": "ps",
    "Paraguay": "py",
    "Peru": "pe",
    "Philippines": "ph",
    "Poland": "pl",
    "Portugal": "pt",
    "Qatar": "qa",
    "Romania": "ro",
    "Russia": "ru",
    "Rwanda": "rw",
    "Saint Kitts And Nevis": "kn",
    "Saint Vincent And The Grenadines": "vc",
    "San Marino": "sm",
    "Saudi Arabia": "sa",
    "Senegal": "sn",
    "Serbia": "rs",
    "Seychelles": "sc",
    "Sierra Leone": "sl",
    "Singapore": "sg",
    "Slovakia": "sk",
    "Slovenia": "si",
    "Solomon Islands": "sb",
    "Somalia": "so",
    "South Africa": "za",
    "South Korea": "kr",
    "Spain": "es",
    "Sri Lanka": "lk",
    "Suriname": "sr",
    "Swaziland": "sz",
    "Sweden": "se",
    "Switzerland": "ch",
    "Syria": "sy",
    "Taiwan": "tw",
    "Tajikistan": "tj",
    "Thailand": "th",
    "Timor-leste": "tl",
    "Togo": "tg",
    "Tonga": "to",
    "Trinidad And Tobago": "tt",
    "Turkey": "tr",
    "Tuvalu": "tv",
    "Ukraine": "ua",
    "Uganda": "ug",
    "United Arab Emirates": "ae",
    "United Kingdom": "gb",
    "United States Of America": "us",
    "Uruguay": "uy",
    "Uzbekistan": "uz",
    "Vanuatu": "vu",
    "Zambia": "zm",
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

                url = f'https://www.alphavantage.co/query?function=FX_MONTHLY&from_symbol=EUR&to_symbol=USD&apikey=demo'
                r = requests.get(url)
                data = r.json()

                dates = [dates for dates in data['Time Series FX (Monthly)']]
                print('DATES SUCCESS')
                exchange_rates = [(data['Time Series FX (Monthly)'][dates]['4. close']) for dates in data['Time Series FX (Monthly)']]


            plt.plot(dates, exchange_rates, marker='o')
            plt.title(f'{country_currency[country]} to GBP Exchange Rates')
            plt.xlabel('Date')
            plt.ylabel('Exchange Rate')
            plt.grid(True)
            plt.show()
        

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
