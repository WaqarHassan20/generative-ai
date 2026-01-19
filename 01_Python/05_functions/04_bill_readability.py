# ============================================
# Function Return Values
# ============================================
# KEY POINTS:
# - return statement sends value back to caller
# - Functions can be used in expressions and assignments
# - Makes functions reusable in different contexts
# - Return values enable function composition
# ============================================

def calculate_bill(cups, price_per_cup):
    """Calculate total bill amount.
    
    Args:
        cups: Number of chai cups ordered
        price_per_cup: Price per cup in rupees
        
    Returns:
        Total bill amount
    """
    return cups * price_per_cup


# Using return value in assignment
my_bill = calculate_bill(3, 50)
print(f"My total bill is {my_bill} rupees.")

# Using return value directly in print
print(f"Table 2 has the bill of {calculate_bill(3, 80)} rupees.")
