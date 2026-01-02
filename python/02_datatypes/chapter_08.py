# ============================================
# List Data Type
# ============================================
# KEY POINTS:
# - Lists are mutable and ordered collections
# - Common methods: append(), remove(), extend(), insert(), pop()
# - reverse() modifies in place and returns None
# - Lists support concatenation (+) and repetition (*)
# - bytearray is a mutable sequence of bytes
# ============================================

# Creating and modifying lists
chai_ingredients = ["water", "tea leaves", "milk"]
print(f"Ingredients are: {chai_ingredients}")

# append() adds element at the end
chai_ingredients.append("sugar")
print(f"After append: {chai_ingredients}")

# remove() removes first occurrence of value
chai_ingredients.remove("water")
print(f"After remove: {chai_ingredients}")

# extend() adds all elements from another list
spice_options = ["cardamom", "cinnamon", "cloves", "ginger"]
chai_ingredients.extend(spice_options)
print(f"After extend: {chai_ingredients}")

# insert() adds element at specific index
chai_ingredients.insert(2, "black tea")
print(f"After insert: {chai_ingredients}")

# pop() removes and returns last element
last_ingredient = chai_ingredients.pop()
print(f"Removed ingredient: {last_ingredient}")
print(f"Remaining Ingredients: {chai_ingredients}")

# reverse() modifies list in place (returns None)
chai_ingredients.reverse()
print(f"Reversed Ingredients: {chai_ingredients}")

# Built-in functions with lists
sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")

# List concatenation and repetition
base_liquids = ["water", "milk"]
extra_liquid = ["ginger juice"]
print(f"\nBase liquids: {base_liquids}")
print(f"Extra liquid: {extra_liquid}")

all_liquids = base_liquids + extra_liquid  # Concatenation
print(f"All liquids: {all_liquids}")

strong_brew = ["black tea"] * 3  # Repetition
print(f"Strong brew: {strong_brew}")

strong_brew = ["black tea, water"] * 3
print(f"Strong brew with water: {strong_brew}")

# Working with bytearray (mutable bytes)
raw_spice_data = bytearray(b"CINNAMON")
print(f"\nBytes before replacement: {raw_spice_data}")
raw_spice_data = raw_spice_data.replace(b"CINN", b"CARD")
print(f"Bytes after replacement: {raw_spice_data}")