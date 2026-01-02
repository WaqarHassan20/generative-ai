# ============================================
# Set Operations
# ============================================
# KEY POINTS:
# - Sets support mathematical set operations
# - Union (|): combines all unique elements
# - Intersection (&): finds common elements
# - Difference (-): elements in first but not in second
# - Sets are case-sensitive and unordered
# ============================================

essential_ingredients = {"cardamom", "ginger", "cloves"}
optional_ingredients = {"Cinnamon", "black pepper", "cloves"}

# Union: all unique elements from both sets
all_spices = essential_ingredients | optional_ingredients
print(f"All spices (using |): {all_spices}")
all_spices = essential_ingredients.union(optional_ingredients)
print(f"All spices (using union): {all_spices}")

# Intersection: elements present in both sets
common_spices = essential_ingredients & optional_ingredients
print(f"\nCommon spices (using &): {common_spices}")
common_spices = essential_ingredients.intersection(optional_ingredients)
print(f"Common spices (using intersection): {common_spices}")

# Difference: elements in first set but not in second
only_in_essential = essential_ingredients - optional_ingredients
print(f"\nOnly in essential (using -): {only_in_essential}")
only_in_essential = essential_ingredients.difference(optional_ingredients)
print(f"Only in essential (using difference): {only_in_essential}")

# Membership testing
print(f"\nIs 'ginger' in essential ingredients? {'ginger' in essential_ingredients}")
print(f"Is 'ginger' in optional ingredients? {'ginger' in optional_ingredients}")
