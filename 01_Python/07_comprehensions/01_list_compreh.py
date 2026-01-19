# ============================================
# List Comprehensions
# ============================================
# KEY POINTS:
# - Syntax: [expression for element in iterable if condition]
# - Creates new list in single line
# - More readable and faster than for loops
# - Optional 'if' condition filters elements
# - Can replace map() and filter() functions
# ============================================

# List comprehension structure:
# [expression for element in iterable if condition]
# └─────┬────┘ └────┬────┘ └───┬───┘ └─────┬────┘
#   what to     loop var  source   optional
#   include                        filter

menu = ["ginger tea", "iced lemon tea", "honey tea", "black tea", "iced peach tea"]

print("EXAMPLE 1: Filter items containing 'iced'")
print("="*50)

# Get all iced teas
iced_tea = [tea for tea in menu if "iced" in tea]
print(f"Iced teas: {iced_tea}\n")

print("="*50)
print("EXAMPLE 2: Filter by length > 5")
print("="*50)

length_5 = [tea for tea in menu if len(tea) > 5]
print(f"Teas with length > 5: {length_5}\n")

print("="*50)
print("EXAMPLE 3: Filter by length > 12")
print("="*50)

length_12 = [tea for tea in menu if len(tea) > 12]
print(f"Teas with length > 12: {length_12}")

# NOTE: List comprehensions are more Pythonic than traditional loops
# Traditional loop equivalent:
# iced_tea = []
# for tea in menu:
#     if "iced" in tea:
#         iced_tea.append(tea)