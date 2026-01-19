# ============================================
# Continue and Break Statements
# ============================================
# KEY POINTS:
# - continue: skip rest of current iteration, move to next
# - break: exit loop immediately
# - Useful for controlling loop flow based on conditions
# ============================================

chai_flavours = ["lemon", "out of stock", "ginger", "discontinued", "saffron"]

for flavour in chai_flavours:
    # Skip items that are out of stock
    if flavour == "out of stock":
        continue
    
    # Stop completely if discontinued item is found
    if flavour == "discontinued":
        break
    
    print(f"Item {flavour} found.")

print("End of search.")