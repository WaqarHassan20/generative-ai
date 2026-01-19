# ============================================
# For-Else Loop
# ============================================
# KEY POINTS:
# - else block executes only if loop completes without break
# - If break is triggered, else is skipped
# - Useful for search operations with fallback logic
# ============================================

staff = [("alice", 16), ("bob", 17), ("carol", 18)]

# Search for staff member who is 18 or older
for name, age in staff:
    if age >= 18:
        print(f"{name.title()} can manage staff.")
        break
else:
    # This executes only if no one was found (no break occurred)
    print("No one can manage staff.")

# NOTE: for-else is useful for fallback logic when search fails