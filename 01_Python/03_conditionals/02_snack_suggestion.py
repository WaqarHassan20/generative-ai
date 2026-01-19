# ============================================
# Using OR Operator in Conditionals
# ============================================
# KEY POINTS:
# - 'or' operator returns True if any condition is True
# - .lower() makes input case-insensitive
# - Can also use: if snack in ["samosa", "cookies"]
# ============================================

snack = input("Enter your preferred snack: ").lower()

if snack == "samosa" or snack == "cookies":
    print(f"Great Choice! You ordered {snack}")
else:
    print("Sorry, we only serve samosa or cookies with tea.")