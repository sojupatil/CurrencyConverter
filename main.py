currencies = {
    "USD" : 85,
    "Euro" : 100,
}

currency = input("Enter currency to convert (USD/Euro): ")

if currency in currencies:
    to_convert = float(input("Enter amount to convert: "))
    result = to_convert * currencies[currency]
    print(f"{to_convert} {currency} = {result} INR")
else:
    print("Currency is not available")
