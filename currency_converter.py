def currency_converter(amount, from_currency, to_currency):
    conversion_rates = {
        "USD": {"EUR": 0.85, "GBP": 0.74, "JPY": 110.32},
        "EUR": {"USD": 1.18, "GBP": 0.87, "JPY": 129.91},
        "GBP": {"USD": 1.35, "EUR": 1.15, "JPY": 149.75},
        "JPY": {"USD": 0.0091, "EUR": 0.0077, "GBP": 0.0067},
    }

    if (
        from_currency not in conversion_rates
        or to_currency not in conversion_rates[from_currency]
    ):
        print("Invalid currency pair")
        return None

    converted_amount = amount * conversion_rates[from_currency][to_currency]

    return converted_amount


amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency to convert from (USD,EUR,GBP,JPY): ").upper()
to_currency = input("Enter the currency to convert to (USD,EUR,GBP,JPY): ").upper()

result = currency_converter(amount, from_currency, to_currency)

if result is not None:
    print(f"{amount} {from_currency} is equal to {result} {to_currency}")
