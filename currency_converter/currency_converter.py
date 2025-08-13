def get_amount():

    while True:
        amount = float(input("Enter your amount: "))
        try:
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print("Invalid choice")


def get_currency(label):
    currencies = ("USD", "EUR", "CAD")
    while True:
        currency = input(f"{label} currency (USD/EUR/CAD): ").upper()
        if currency in currencies:
            return currency
        else:
            print("Invalid choice")


def convert(amount, source_currency, target_currency):
    exchange_rates = {
        "USD": {"EUR": 0.86, "CAD": 1.38},
        "EUR": {"USD": 1.17, "CAD": 1.60},
        "CAD": {"USD": 0.73, "EUR": 0.62}
    }
    if source_currency == target_currency:
        return amount

    return amount * exchange_rates[source_currency][target_currency]


def main():
    amount = get_amount()
    source_currency = get_currency("Source")
    target_currency = get_currency("Target")
    converted_amount = convert(amount, source_currency, target_currency)
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f}")


if __name__ == "__main__":
    main()
