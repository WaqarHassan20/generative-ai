# ============================================
# Boolean Data Type
# ============================================
# KEY POINTS:
# - True = 1, False = 0 in numeric context
# - Any non-zero number converts to True
# - Zero converts to False
# - Logical operators: and, or, not
# ============================================

# Type coercion: Boolean to Integer (True = 1)
is_boiling = True
stir_count = 5
total_actions = is_boiling + stir_count  # True acts as 1
print(f"Total stir counts are: {total_actions}")

# Converting integer to boolean (0 = False)
is_milk = 0
print(f"Is there milk? {bool(is_milk)}")

# Logical AND operator (both must be True)
water_hot = True
tea_added = False
should_serve_tea = water_hot and tea_added
print(f"Should we serve tea? {should_serve_tea}")