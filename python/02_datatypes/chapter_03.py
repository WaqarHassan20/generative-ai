# ============================================
# Integer Arithmetic Operations
# ============================================
# KEY POINTS:
# - Addition (+), Subtraction (-), Multiplication (*)
# - Division (/) returns float, Floor Division (//) returns integer
# - Modulus (%) returns remainder
# - Underscores can improve readability of large numbers
# ============================================

# Addition
black_tea_grains = 14
ginger_grains = 4
total_grains = black_tea_grains + ginger_grains
print(f"Total grains are: {total_grains}")

# Subtraction
remaining_grains = black_tea_grains - ginger_grains
print(f"Total base tea grains are: {remaining_grains}")

# Division (returns float)
milk_in_liters = 7
servings = 4
milk_per_serving = milk_in_liters / servings
print(f"Milk per serving is: {milk_per_serving}")

# Floor Division (returns integer, rounds down)
total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"Bags per pot is: {bags_per_pot}")

# Modulus (returns remainder)
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Left over pods are: {leftover_pods}")

# Multiplication
strength_factor = 2
power_factor = 4
powerful_factor = strength_factor * power_factor
print(f"Scaled Strength is: {powerful_factor}")

# Using underscores for readability in large numbers
number_of_leaves = 1_000_000_000
print(f"Total number of leaves are: {number_of_leaves}")