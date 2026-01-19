# ============================================
# Ternary Operator (Conditional Expression)
# ============================================
# KEY POINTS:
# - Ternary: value_if_true if condition else value_if_false
# - Compact way to write simple if-else statements
# - Use for simple assignments, not complex logic
# ============================================

order_amount = int(input("Enter the order amount: "))

# Ternary operator for concise conditional assignment
delivery_fee = 0 if order_amount > 300 else 45

if delivery_fee == 0:
    print("Congrats! Free delivery.")
else:
    print(f"Delivery fee: ${delivery_fee}")