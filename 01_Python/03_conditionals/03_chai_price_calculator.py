# ============================================
# If-Elif-Else Chain
# ============================================
# KEY POINTS:
# - elif allows checking multiple conditions
# - Only first True condition executes
# - else catches all other cases
# - Use snake_case for variable names (Python convention)
# ============================================

cup_size = input("Choose your cup size (Small/Medium/Large): ").lower()

if cup_size == "small":
    print("Small cup price is $2.50")
elif cup_size == "medium":
    print("Medium cup price is $4.00")
elif cup_size == "large":
    print("Large cup price is $5.00")
else:
    print("Invalid cup size selected.")
