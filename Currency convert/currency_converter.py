from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://free.currconv.com/'
API_KEY = '34c3527fda4512e4ad6c'
#to print out json file neater
printer = PrettyPrinter()

#get list of currencies from public API
def get_currencies():
    endpoint = f"api/v7/currencies?apiKey={API_KEY}"
    url = BASE_URL + endpoint
    data = get(url).json()['results']
    
    data = list(data.items())
    data.sort()

    return data

#print list of currencies from list of json
def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        #.get will try and get value for currencySymbol, if not, will put symbol as default value of empty string
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")

#get exchange rate between 2 currencies selected by user input
def exchange_rate(currency1, currency2):
    #more can be added to query but for now endpoint will make 1 request at a time
    endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
    url = BASE_URL +endpoint
    response = get(url)
    data = response.json()

    if len(data)==0:
        print('Invalid currencies')
        return
    rate =  list(data.values())[0]
    print(f"1 {currency1} = {rate} {currency2}")

    return rate

#from exchange rate, convert amount of one currency to another
def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print("Invalid amount")
        return
    
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")
    return converted_amount

#main program
def main():
    currencies = get_currencies()
    def menu():
        print()
        print("Currency converter")
        print("-------------------------------------------------------------")
        print("Commands: ")
        print("-------------")
        print("List - lists the different currencies")
        print("Convert - convert from one currency to another")
        print("Rate - get the exchange rate of two currencies")
        print()

    menu()
    while True:
        command = input("Enter a command (q to exit): ").lower()

        if command == "q":
            print()
            print("Goodbye!")
            break
        elif command == "list":
            print_currencies(currencies)
            menu()
        elif command == "convert":
            currency1 = input("Enter a base currency: ").upper()
            amount = input(f"Enter an amount of {currency1} to convert: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
            menu()
        elif command =="rate":
            currency1 = input("Enter a base currency: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
            menu()
        else:
            print("Unrecognized command!")
            menu()

main()
