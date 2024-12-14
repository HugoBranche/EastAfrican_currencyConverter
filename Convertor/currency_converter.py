# exchange rates (example rates, not real-time)
EXCHANGE_RATES = {
    "KES": {"TZS": 22.0, "UGX": 30.0, "RWF": 8.0, "BIF": 5.0, "SSP": 15.0, "ETB": 1.5},
    "TZS": {"KES": 0.045, "UGX": 1.36, "RWF": 0.36, "BIF": 0.23, "SSP": 0.68, "ETB": 0.068},
    "UGX": {"KES": 0.033, "TZS": 0.74, "RWF": 0.27, "BIF": 0.19, "SSP": 0.50, "ETB": 0.065},
    "RWF": {"KES": 0.12, "TZS": 2.8, "UGX": 3.7, "BIF": 0.70, "SSP": 1.5, "ETB": 0.12},
    "BIF": {"KES": 0.20, "TZS": 4.3, "UGX": 5.3, "RWF": 1.4, "SSP": 2.0, "ETB": 0.15},
    "SSP": {"KES": 0.067, "TZS": 1.47, "UGX": 2.0, "RWF": 0.67, "BIF": 0.50, "ETB": 0.10},
    "ETB": {"KES": 0.67, "TZS": 14.7, "UGX": 15.4, "RWF": 8.3, "BIF": 6.7, "SSP": 10.0},
}

# List of East African currencies
EAST_AFRICAN_CURRENCIES = {
    "KES": "Kenyan Shilling",
    "TZS": "Tanzanian Shilling",
    "UGX": "Ugandan Shilling",
    "RWF": "Rwandan Franc",
    "BIF": "Burundian Franc",
    "SSP": "South Sudanese Pound",
    "ETB": "Ethiopian Birr"
}

def print_currencies():
    for _id, name in EAST_AFRICAN_CURRENCIES.items():
        print(f"{_id} - {name}")

def convert(currency1, currency2, amount):
    if currency1 not in EXCHANGE_RATES or currency2 not in EXCHANGE_RATES[currency1]:
        print("Invalid currency conversion.")
        return

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount.")
        return

    rate = EXCHANGE_RATES[currency1][currency2]
    converted_amount = rate * amount
    print(f"{amount} {currency1} is equal to {converted_amount} {currency2}")

def main():
    print("Welcome to the East African currency converter!")
    print("List - lists the different East African currencies")
    print("Convert - convert from one currency to another")
    print()

    while True:
        command = input("Enter a command (q to quit): ").lower()

        if command == "q":
            break
        elif command == "list":
            print_currencies()
        elif command == "convert":
            currency1 = input("Enter a base currency (e.g., KES): ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to (e.g., TZS): ").upper()
            convert(currency1, currency2, amount)
        else:
            print("Unrecognized command!")

main()