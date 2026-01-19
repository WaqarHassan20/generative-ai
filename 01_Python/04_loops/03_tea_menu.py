# ============================================
# Using enumerate() for Index and Value
# ============================================
# KEY POINTS:
# - enumerate() returns both index and value
# - start parameter sets the starting index number
# - Useful when you need position along with item
# ============================================

menu = ["lemon", "ginger", "green", "mint"]

# Get both index and item, starting count from 1
for index, item in enumerate(menu, start=1):
    print(f"{index}: Preparing {item} tea")

