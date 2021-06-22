import requests
# from .dotdoe import load_dotdoe

# d = load_dotdoe()

def get_crypto_price(coin):
    url = "https://api.wazirx.com/api/v2/tickers"
    response = requests.get(url)
    data = response.json()

    price = data[coin]['last']
    return price


def get_price(to):
    url = f'https://free.currconv.com/api/v7/convert?q={to}_INR&compact=ultra&apiKey=edd3482386b85f62cb8f'
    response = requests.get(url).json()[f'{to}_INR']
    return response


def get_crypto(crypto, realcurrency):
    price_inr = float(get_crypto_price(crypto.lower()+'inr')) 
    price_in_default = float(float(price_inr) / float(get_price(realcurrency)))
    return price_in_default


