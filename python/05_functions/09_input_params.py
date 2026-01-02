# ============================================
# Function Parameters and Arguments
# ============================================
# KEY POINTS:
# - Immutable types (str, int, tuple): pass by value (copy)
# - Mutable types (list, dict, set): pass by reference
# - *args: collects positional arguments into tuple
# - **kwargs: collects keyword arguments into dictionary
# - Default mutable arguments (list, dict) are dangerous!
# - Always use None as default for mutable types
# ============================================

print("EXAMPLE 1: Immutable Arguments (Strings)")
print("="*50)

chai = "ginger"

def prepare_chai(chai_name):
    """Strings are immutable - changes don't affect original."""
    chai_name = chai_name.capitalize()
    print(f"Preparing {chai_name} Chai")

prepare_chai(chai)
print(f"Original value unchanged: {chai}\n")

print("="*50)
print("EXAMPLE 2: Mutable Arguments (Lists)")
print("="*50)

chai = [1, 2, 3, 4]

def edit_chai(cup):
    """Lists are mutable - modifications affect original!"""
    cup[1] = 42  # Modifies the original list

edit_chai(chai)
print(f"Original list modified: {chai}\n")  # [1, 42, 3, 4]

print("="*50)
print("EXAMPLE 3: Positional vs Keyword Arguments")
print("="*50)

def make_chai(tea, milk, sugar):
    print(f"Chai: {tea}, Milk: {milk}, Sugar: {sugar}")

# Positional arguments (order matters)
make_chai("Gloria Jeans", "yes", "low")

# Keyword arguments (order doesn't matter)
make_chai(milk="yes", sugar="low", tea="Gloria Jeans")
print()

print("="*50)
print("EXAMPLE 4: *args and **kwargs")
print("="*50)

def special_chai(*ingredients, **extras):
    """*args catches positional, **kwargs catches keyword arguments."""
    print(f"Ingredients (tuple): {ingredients}")
    print(f"Extras (dict): {extras}")

special_chai("tea", "milk", sugar="low", spice="high")
print()

print("="*50)
print("EXAMPLE 5: DANGEROUS - Mutable Default Arguments")
print("="*50)

def chai_order(order=[]):
    """WARNING: Default list is created once and shared!"""
    order.append("Lemon chai")
    print(f"Order (accumulates!): {order}")

chai_order()  # ['Lemon chai']
chai_order()  # ['Lemon chai', 'Lemon chai'] - UNEXPECTED!
print()

print("="*50)
print("EXAMPLE 6: SAFE - Using None as Default")
print("="*50)

def chai_order_fixed(order=None):
    """CORRECT: Create new list each time."""
    if order is None:
        order = []  # New list created each call
    order.append("Lemon chai")
    print(f"Order (fresh each time): {order}")

chai_order_fixed()  # ['Lemon chai']
chai_order_fixed()  # ['Lemon chai'] - EXPECTED!

# IMPORTANT: Never use mutable defaults (list, dict, set)
# Always use None and create inside function