import requests
import time

api_key = "3f5b8a1d-5eb4-429b-8117-3986a7a52132"
bot_key = "1878765694:AAE3OQdmGQMufcOPIVK3dG0nkllLMOAYKh4"
chat_id = "1289688077"
time_limit = 5
limit = 59000


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '10'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    response = requests.get(url, headers=headers, params=parameters).json()
    btc_price = response['data'][0]['quote']['USD']['price']
    return btc_price


def send_updates(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={chat_id}&text={msg}"
    requests.get(url)


def main():
    while True:
        price = get_price()
        print(price)
        if price < limit:
            send_updates(chat_id, f"بقولك ايه يا زميلي سعر البتكوين اتغير ودا السعر الجديد:{price}")
        time.sleep(time_limit)


main()
