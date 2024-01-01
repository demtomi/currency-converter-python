# Currency Converter

This is a simple Python program that converts currency from one denomination to another. You can use fixed conversion rates or fetch real-time exchange rates from an API.

## Features

- **Fixed Conversion Rates:** The program uses predefined conversion rates stored in a dictionary. You can easily replace them with real-time rates from an API.

- **User Input:** Users can input the amount to convert, the source currency, and the target currency.

- **Conversion Function:** The core functionality is encapsulated in the `currency_converter` function.

## How to Use

1. Clone or download this repository to your local machine.

2. Make sure you have Python installed on your machine.

3. Run the program by executing the following command in your terminal:

   ```bash
   python currency_converter.py
   ```

4. Follow the on-screen instructions to enter the amount, source currency (e.g., USD), and target currency (e.g., EUR).

5. The program will display the converted amount.

## Example

```bash
Enter the amount to convert: 100
Enter the currency to convert from (e.g., USD): USD
Enter the currency to convert to (e.g., EUR): EUR
```

Output:

```bash
100 USD is equal to 85.0 EUR
```

## Dependencies

This program does not have external dependencies. If you plan to fetch real-time exchange rates, you may need to install the `requests` library using the following command:

```bash
pip install requests
```

## Note

- The conversion rates in the program are for demonstration purposes. Replace them with real rates if you plan to use an API.

- Handle API keys and HTTP requests appropriately if integrating with a real-time currency exchange API.