# ============================================
# Iterating Over Lists
# ============================================
# KEY POINTS:
# - for loop can iterate directly over list elements
# - Each iteration, variable takes next value from list
# - More readable than using index-based access
# ============================================

orders = ["hitesh", "payal", "becky", "rahul"]

# Iterate through each customer name
for name in orders:
    print(f"Preparing tea for {name.title()}")
