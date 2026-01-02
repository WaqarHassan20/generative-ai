# ============================================
# Built-in Function Attributes and Docstrings
# ============================================
# KEY POINTS:
# - Docstrings: First string in function (documentation)
# - Access via __doc__ attribute or help() function
# - __name__ attribute stores function name
# - Triple quotes allow multi-line docstrings
# - Good docstrings explain purpose, parameters, return value
# ============================================

print("EXAMPLE 1: Function Attributes")
print("="*50)

def chai_flavour(flavour="Lemon"):
    """Returns the flavour of chai."""
    category = "Ginger Chai"
    return flavour

# Access function docstring and name
print(f"Docstring: {chai_flavour.__doc__}")
print(f"Function name: {chai_flavour.__name__}")
print(f"Default parameter: {chai_flavour()}\n")

print("="*50)
print("EXAMPLE 2: Comprehensive Docstring")
print("="*50)

def generate_bill(chai=0, samosa=0):
    """
    Generates the total bill for chai and samosas.
    
    Parameters:
        chai (int): Number of chai cups at ₹10 each
        samosa (int): Number of samosas at ₹15 each
    
    Returns:
        int: Total bill amount in rupees
    """
    return (chai * 10) + (samosa * 15)

# Using the function
total = generate_bill(chai=3, samosa=8)
print(f"Total bill is: ₹{total}")
print(f"\nFunction documentation:\n{generate_bill.__doc__}")
print("\nThank you for visiting us!")

print("\n" + "="*50)

# TIP: Use help(function_name) for formatted documentation
# Example: help(generate_bill)

# BEST PRACTICE: Always write docstrings for public functions
# Format: Summary line, blank line, detailed description
