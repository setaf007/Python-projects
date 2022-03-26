from requests import get
from matplotlib import pyplot as plt
from datetime import datetime

#refer to etherscan API documentation for more API call functions
API_KEY = "C93I5TIA2A2M454PAE4RWXZDB3W1JQS5PG"
BASE_URL = 'https://api.etherscan.io/api'
#ether value is used as results of API call gives values of ethereum in Wei (1eth = 10**18 Wei)
ETHER_VALUE = 10 ** 18

#function to make url for api call(**kwargs allow extra input values)
def make_api_url(module, action, address, **kwargs):
    url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={API_KEY}"

    for key, value in kwargs.items():
        url += f"&{key}={value}"

    return url

#function to get wallet account balance
def get_account_balance(address):
    balance_url = make_api_url("account", "balance", address, tag = "latest", x = "2")
    response = get(balance_url)
    data = response.json()
    value = (int(data['result']) / ETHER_VALUE)

    return value

#function to get transactions (transactions are seperated into internal(e.g. contracts) and normal)
def get_transactions(address):
    #normal transactions url
    transactions_url = make_api_url("account", "txlist", address, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc")
    response = get(transactions_url)
    data = response.json()["result"]
    
    #internal transactions url
    internal_tx_url = make_api_url("account", "txlistinternal", address, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc")
    response2 = get(internal_tx_url)
    data2 = response2.json()["result"]

    #extends data iterable with data 2 iterable
    data.extend(data2)
    data.sort(key=lambda x: int(x['timeStamp']))

    current_balance = 0
    balances = []
    times = []
    
    for tx in data:
        to = tx["to"]
        from_addr = tx["from"]
        value = int(tx["value"]) / ETHER_VALUE
        if "gasPrice" in tx:
            gas = int(tx["gasUsed"]) * int(tx["gasPrice"]) / ETHER_VALUE
        else:
            gas = int(tx["gasUsed"]) / ETHER_VALUE
        time = datetime.fromtimestamp(int(tx['timeStamp']))
        money_in = to.lower() == address.lower()

        if money_in:
            current_balance += value
        else:
            current_balance -= value + gas
        
        balances.append(current_balance)
        times.append(time)
    
    #plotting wallet balance over time
    plt.title("Eth in wallet over time")
    plt.xlabel("Date")
    plt.ylabel("Ethereum in wallet")
    plt.plot(times, balances)
    plt.show()

#replace this address value with wallet to be checked (input can be asked from user)
address = "0x73bceb1cd57c711feac4224d062b0f6ff338501e"
get_transactions(address)
