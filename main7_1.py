# pip install currencyconverter    => Currency Calculation Library

from currency_converter import CurrencyConverter

# Create a CurrencyConverter object using the European Central Bank's exchange rate data.
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
# cc = CurrencyConverter()

# Convert 1 US Dollar (USD) to South Korean Won (KRW) using the CurrencyConverter object.
conversion_result = cc.convert(1, 'USD', 'KRW')

# Print the result of the currency conversion.
print(conversion_result)