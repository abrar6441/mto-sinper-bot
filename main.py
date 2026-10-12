import time, os
import ccxt

SYMBOL = 'MTO/USDT'
AMOUNT_USD = 5

exchange = ccxt.mexc({
    'apiKey': os.getenv('MEXC_API_KEY'),
    'secret': os.getenv('MEXC_SECRET_KEY'),
    'enableRateLimit': False,
})

print("Bot started... waiting for listing")
bought = False
while not bought:
    try:
        ticker = exchange.fetch_ticker(SYMBOL)
        if ticker['last'] is not None:
            print(f"Market opened! Price: {ticker['last']}")
            order = exchange.create_market_buy_order(SYMBOL, AMOUNT_USD)
            print("Buy order success!")
            bought = True
            break
    except:
        pass
    time.sleep(0.1)
