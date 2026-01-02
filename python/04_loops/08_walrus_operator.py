# ============================================
# Walrus Operator (:=) - Assignment Expression
# ============================================
# KEY POINTS:
# - Walrus operator (:=) assigns AND returns value in one line
# - Syntax: variable := expression
# - Available in Python 3.8+
# - Reduces code duplication and improves readability
# ============================================

# Example 1: Basic usage
value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible by 5, remainder is {remainder}")

# Same logic using walrus operator (combines assignment and condition)
if remainder := value % 5:
    print(f"Using walrus - Not divisible by 5, remainder is {remainder}")

print("\n" + "="*40 + "\n")

# Example 2: Using walrus in condition with membership test
chai_sizes = ["small", "medium", "large", "grande"]

if (input_size := input("Enter chai size: ").lower()) in chai_sizes:
    print(f"Preparing a {input_size.upper()} chai")
else:
    print("Size not available")

print("\n" + "="*40 + "\n")

# Example 3: Using walrus operator in a while loop
chai_flavours = ["masala", "ginger", "tulsi", "cardamom"]

# Keep asking until valid flavour is entered
while (flavour := input("Enter chai flavour: ").lower()) not in chai_flavours:
    print("Not available, try something different.")

print(f"Preparing your {flavour.upper()} chai")