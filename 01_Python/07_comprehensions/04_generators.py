# ============================================
# Generator Expressions
# ============================================
# KEY POINTS:
# - Syntax: (expression for element in iterable)
# - Like list comprehension but with parentheses ()
# - Memory efficient - generates values on demand
# - Can only iterate once (not reusable)
# - Perfect for large datasets or when you don't need list
# ============================================

print("EXAMPLE: Memory-Efficient Calculation")
print("="*50)

daily_sales = [100, 200, 300, 400, 500]

# Generator expression - doesn't create list in memory
# Values are generated on-the-fly as needed by sum()
total_sales = sum(sale for sale in daily_sales if sale > 200)

print(f"Daily sales: {daily_sales}")
print(f"Total sales over 200: {total_sales}")

# NOTE: Generator expressions are more memory efficient than list comprehensions
# List:      [sale for sale in daily_sales if sale > 200]  # Creates list
# Generator: (sale for sale in daily_sales if sale > 200)  # Generates on demand
