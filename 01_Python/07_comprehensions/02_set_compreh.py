# ============================================
# Set Comprehensions
# ============================================
# KEY POINTS:
# - Syntax: {expression for element in iterable if condition}
# - Creates set (unordered, unique elements)
# - Automatically removes duplicates
# - Curly braces {} instead of square brackets []
# - Supports nested comprehensions for flattening
# ============================================

print("EXAMPLE 1: Basic Set Comprehension")
print("="*50)

menu = {"ginger tea", "iced lemon tea", "honey tea", "ginger tea", "iced peach tea"}
print(f"Original menu (duplicates removed): {menu}\n")

# Filter iced teas
iced_tea = {tea for tea in menu if "iced" in tea}
print(f"Iced teas: {iced_tea}\n")

print("="*50)
print("EXAMPLE 2: Filter by Length")
print("="*50)

length_8 = {tea for tea in menu if len(tea) < 8}
print(f"Teas with length < 8: {length_8}\n")

print("="*50)
print("EXAMPLE 3: Nested Comprehension (Flattening)")
print("="*50)

# Dictionary with recipes
recipes = {
    "ginger chai": ["clove", "cardamom", "ginger"],
    "lemon tea": ["cardamom", "milk"],
    "spicy tea": ["black pepper", "ginger", "clove"],
}

# Extract all unique spices from all recipes
# Nested loop: outer iterates recipes.values(), inner iterates each spice list
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(f"All unique spices: {unique_spices}")

# NOTE: Set comprehensions automatically remove duplicates
# Note 'ginger' and 'cardamom' appear only once despite being in multiple recipes
