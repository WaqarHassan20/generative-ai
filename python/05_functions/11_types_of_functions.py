# ============================================
# Types of Functions in Python
# ============================================
# KEY POINTS:
# - Pure Function: No side effects, same input = same output
# - Impure Function: Has side effects (modifies external state)
# - Recursive Function: Calls itself, needs base case
# - Lambda Function: Anonymous function (single expression)
# - Higher-order Function: Takes/returns functions (map, filter)
# ============================================

print("EXAMPLE 1: Pure Function")
print("="*50)

def pure_chai(cups):
    """Pure function - no side effects, predictable output."""
    return cups * 10  # Only depends on input, no external state

chai_amount = pure_chai(3)
print(f"Pure chai amount: {chai_amount} ml")
print(f"Called again: {pure_chai(3)} ml (same result)\n")

print("="*50)
print("EXAMPLE 2: Impure Function")
print("="*50)

total_chai = 0  # External state

def impure_chai(cups):
    """Impure function - modifies external state (side effect)."""
    global total_chai
    total_chai = cups * 10  # Modifies global variable
    # Return value depends on/affects external state

print(f"Before: total_chai = {total_chai}")
impure_chai(3)
print(f"After: total_chai = {total_chai} ml (side effect!)\n")

print("="*50)
print("EXAMPLE 3: Recursive Function")
print("="*50)

def recursive_chai(cups):
    """Recursive function - calls itself until base case."""
    print(f"Pouring cup {cups}...")
    
    # Base case - stops recursion
    if cups == 0:
        return "All chai poured!"
    
    # Recursive case - calls itself with smaller problem
    return recursive_chai(cups - 1)

result = recursive_chai(3)
print(f"Result: {result}\n")

print("="*50)
print("EXAMPLE 4: Lambda Functions with filter()")
print("="*50)

chai_types = ["masala", "ginger", "cardamom", "ginger"]

# Lambda: anonymous function for simple operations
# filter() takes function and iterable, returns matching items
strong_chai = list(filter(lambda chai: chai == "ginger", chai_types))
print(f"Strong chai (ginger only): {strong_chai}")

weak_chai = list(filter(lambda chai: chai != "ginger", chai_types))
print(f"Weak chai (no ginger): {weak_chai}")

# Lambda syntax: lambda arguments: expression
# Equivalent to: def func(chai): return chai == "ginger"

# NOTE: Use lambdas for simple operations
# For complex logic, use regular def functions

