# ============================================
# Integer Data Type
# ============================================
# KEY POINTS:
# - Integers are immutable (cannot be changed in place)
# - Each integer value has a unique ID in memory
# - Reassigning a variable creates a new reference
# ============================================

# Initial assignment
sugar_amount = 2
print("Initial Sugar Value:", {sugar_amount})
print(f"Initial Sugar Value: {sugar_amount}")

# Reassigning the variable (creates new reference)
sugar_amount = 12
print(f"Updated sugar value: {sugar_amount}")

# Demonstrating that different integer values have different memory IDs
print(f"Id of value 2 is: {id(2)}")
print(f"Id of value 12 is: {id(12)}")

# Checking if IDs are the same (they won't be)
if id(2) == id(12):
    print("Same IDs")
else:
    print("Different IDs")