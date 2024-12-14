# East African Currency Converter

## Overview
The **East African Currency Converter** is a Python-based tool designed to simplify currency conversion among East African currencies. This project supports conversion for currencies such as:
- Kenyan Shilling (KES)
- Tanzanian Shilling (TZS)
- Ugandan Shilling (UGX)
- Rwandan Franc (RWF)
- Burundian Franc (BIF)
- South Sudanese Pound (SSP)
- Ethiopian Birr (ETB)

## Features
- Lists available East African currencies.
- Converts an amount from one currency to another using predefined exchange rates.
- User-friendly command-line interface.

## Requirements
- Python 3.6+

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/HugoBranche/EastAfrican_currencyConverter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd EastAfrican_currencyConverter
   ```

## Usage
Run the script to start the currency converter:
```bash
python currency_converter.py
```
### Available Commands
- **list**: Displays all supported currencies.
- **convert**: Prompts for the base currency, target currency, and amount to convert.
- **q**: Quits the application.

### Example Conversion
1. Enter the command `convert`.
2. Input the base currency, e.g., `KES`.
3. Input the amount to convert, e.g., `1000`.
4. Input the target currency, e.g., `TZS`.
5. Output:
   ```plaintext
   1000 KES is equal to 22000.0 TZS
   ```

## Exchange Rates
The program uses predefined exchange rates as shown in the code. These are sample rates and may not reflect real-time values.

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## Acknowledgments
Thanks to PLP lecturers


