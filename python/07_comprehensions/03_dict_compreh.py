# ============================================
# Dictionary Comprehensions
# ============================================
# KEY POINTS:
# - Syntax: {key: value for key, value in iterable}
# - Creates new dictionary in single line
# - Can transform both keys and values
# - Use .items() to iterate over key-value pairs
# - More concise than traditional loops
# ============================================

print("EXAMPLE: Currency Conversion")
print("="*50)

tea_prices_pkr = {"lemon tea": 40, "ginger tea": 50, "honey tea": 60}
print(f"Prices in PKR: {tea_prices_pkr}")

# Convert prices from PKR to USD (1 USD = 268 PKR)
tea_prices_usd = {tea: price / 268 for tea, price in tea_prices_pkr.items()}
print(f"Prices in USD: {tea_prices_usd}")

# Traditional loop equivalent:
# tea_prices_usd = {}
# for tea, price in tea_prices_pkr.items():
#     tea_prices_usd[tea] = price / 268

# NOTE: Dictionary comprehensions are perfect for transforming dictionaries