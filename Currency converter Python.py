# Simple Currency Converter for Beginners

def convert_currency():
    """
    Handles input, calculation, and output for currency conversion.
    Rates are hardcoded for simplicity.
    """

    # Hardcoded exchange rates based on 1 unit of the base currency (e.g., USD)
    # Note: These are simulated rates for educational purposes.
    RATES = {
        "USD": 1.00,  # US Dollar (Base)
        "EUR": 0.92,  # Euro
        "GBP": 0.80,  # British Pound
        "JPY": 149.00, # Japanese Yen
        "CAD": 1.35   # Canadian Dollar
    }

    print("\n--- Welcome to the Currency Converter ---")
    print(f"Available Currencies: {list(RATES.keys())}")
    
    # 1. Get and validate the amount
    try:
        amount = float(input("Enter the amount to convert: "))
        if amount <= 0:
            print("\n**Error:** Amount must be a positive number.")
            return

    except ValueError:
        print("\n**Error:** Invalid input. Please enter a valid number for the amount.")
        return

    # 2. Get and validate the currency codes
    try:
        source_code = input("Enter the source currency code (e.g., USD): ").upper()
        target_code = input("Enter the target currency code (e.g., EUR): ").upper()

        source_rate = RATES[source_code]
        target_rate = RATES[target_code]

    except KeyError:
        print("\n**Error:** One or both currency codes are invalid or not supported.")
        print(f"Supported codes are: {list(RATES.keys())}")
        return

    # 3. Perform the conversion calculation
    
    # Convert source amount to the base unit (USD in this case)
    amount_in_base = amount / source_rate

    # Convert the base unit amount to the target currency
    converted_amount = amount_in_base * target_rate

    # 4. Display the result
    print("\n--- Conversion Result ---")
    # Use f-string formatting to round the result to two decimal places
    print(f"{amount:.2f} {source_code} is equal to **{converted_amount:.2f} {target_code}**")
    print("-------------------------")

# Run the converter function
convert_currency()
