from bot import BasicBot

def main():
    api_key = input("Enter your API Key: ")
    api_secret = input("Enter your API Secret: ")

    bot = BasicBot(api_key, api_secret)

    while True:
        print("\n--- Trading Bot Menu ---")
        print("1. Place Market Order")
        print("2. Place Limit Order")
        print("3. Place Stop-Limit Order (Bonus)")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (buy/sell): ").lower()
            qty = float(input("Quantity: "))
            result = bot.place_market_order(symbol, side, qty)
            print(result)
        elif choice == "2":
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (buy/sell): ").lower()
            qty = float(input("Quantity: "))
            price = float(input("Limit Price: "))
            result = bot.place_limit_order(symbol, side, qty, price)
            print(result)
        elif choice == "3":
            symbol = input("Symbol (e.g., BTCUSDT): ").upper()
            side = input("Side (buy/sell): ").lower()
            qty = float(input("Quantity: "))
            stop_price = float(input("Stop Price: "))
            limit_price = float(input("Limit Price: "))
            result = bot.place_stop_limit_order(symbol, side, qty, stop_price, limit_price)
            print(result)
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
