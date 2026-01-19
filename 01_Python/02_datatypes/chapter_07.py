# ============================================
# Tuple Data Type
# ============================================
# KEY POINTS:
# - Tuples are immutable (cannot be changed after creation)
# - Use parentheses () to create tuples
# - Tuple unpacking assigns values to multiple variables
# - 'in' operator checks membership (case-sensitive)
# ============================================

# Tuple unpacking
masala_spices = ("cardamom", "cinnamon", "cloves")
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices are: {spice1}, {spice2}, {spice3}")

# Swapping values using tuple unpacking
ginger_ratio, cardamom_ratio = 2, 1
print(f"Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

# Elegant swap without temporary variable
cardamom_ratio, ginger_ratio = ginger_ratio, cardamom_ratio
print(f"After swap - Ginger ratio: {ginger_ratio}, Cardamom ratio: {cardamom_ratio}")

# Membership testing (case-sensitive)
print(f"Is ginger in masala spices? {'ginger' in masala_spices}")
print(f"Is cinnamon in masala spices? {'cinnamon' in masala_spices}")

# Demonstrating case sensitivity
print(f"Is Cinnamon (capitalized) in masala spices? {'Cinnamon' in masala_spices}")
