# ============================================
# Dictionary Operations and Best Practices
# ============================================
# KEY POINTS:
# - .get(key, default) returns default if key doesn't exist
# - Tuple unpacking: percent, flat = (value1, value2)
# - This prevents KeyError exceptions
# - Clean, readable code with proper formatting
# ============================================

# User data with coupon codes
users = [
    {"id": 1, "total": 100, "coupon": "F10"},
    {"id": 2, "total": 200, "coupon": "P20"},
    {"id": 3, "total": 300, "coupon": "N30"},
    {"id": 4, "total": 400, "coupon": None},
]

# Discount structure: {coupon_code: (percentage, flat_amount)}
discounts = {
    "F10": (0.2, 0),
    "P20": (0.5, 3),
    "N30": (0.7, 7),
    "None": (0, 0)
}

# Process each user's discount
for user in users:
    # Safely get discount values, default to (0, 0) if coupon not found
    percent, flat = discounts.get(user["coupon"], (0, 0))
    
    # Calculate total discount
    discount = user["total"] * percent + flat
    
    print(
        f"User ID {user['id']} paid ${user['total']} "
        f"and gets ${discount:.2f} discount for next visit."
    )
