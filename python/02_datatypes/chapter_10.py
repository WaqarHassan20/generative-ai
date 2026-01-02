# ============================================
# Dictionary Data Type
# ============================================
# KEY POINTS:
# - Dictionaries store key-value pairs
# - Keys must be unique and immutable
# - Use get() to avoid KeyError when key doesn't exist
# - Methods: keys(), values(), items(), update(), popitem()
# - Dictionaries are mutable and ordered (Python 3.7+)
# ============================================

# Creating dictionary using dict() constructor
chai_order = dict(type="chai", size="grande", sugar=2)
print(f"Chai Order: {chai_order}")

# Creating empty dictionary and adding key-value pairs
chai_recipe = {}
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "Milk"

print(f"\nChai Recipe: {chai_recipe}")
print(f"Base: {chai_recipe['base']}")
print(f"Liquid: {chai_recipe['liquid']}")

# Deleting a key-value pair
del chai_recipe["liquid"]
print(f"After deletion: {chai_recipe}")

# Checking if key exists
print(f"\nIs 'sugar' in chai_order? {'sugar' in chai_order}")

# Dictionary methods
chai_order = dict(type="ginger chai", size="medium", sugar=1)
print(f"\nKeys: {chai_order.keys()}")
print(f"Values: {chai_order.values()}")
print(f"Items: {chai_order.items()}")

# popitem() removes and returns last inserted key-value pair
last_item = chai_order.popitem()
print(f"\nLast Item Popped: {last_item}")

# update() merges another dictionary
extra_spices = {"cinnamon": "1 tsp", "cardamom": "2 pods"}
chai_order.update(extra_spices)
print(f"Updated Chai Order: {chai_order}")

# Direct access (raises KeyError if key doesn't exist)
chai_size = chai_order["size"]
print(f"\nChai Size: {chai_size}")

# get() method with default value (safer)
default_value_handler = chai_order.get("size", "Not Given")
print(f"Chai Size (using get): {default_value_handler}")
default_value_handler = chai_order.get("precautions", "Not Given")
print(f"Precautions: {default_value_handler}")