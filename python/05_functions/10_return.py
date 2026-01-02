# ============================================
# Return Statement in Functions
# ============================================
# KEY POINTS:
# - 'return' sends value back to caller
# - Functions without 'return' implicitly return None
# - Can return multiple values as tuple
# - Tuple unpacking: a, b = func() if returns 2 values
# - 'return' immediately exits the function
# ============================================

print("EXAMPLE 1: Function with Return Value")
print("="*50)

def make_chai():
    """Returns a string message."""
    return "Chai is ready!"

chai_message = make_chai()
print(f"Message: {chai_message}\n")

print("="*50)
print("EXAMPLE 2: Function Without Return (Returns None)")
print("="*50)

def prepare_chai():
    """No return statement - implicitly returns None."""
    print("Preparing Chai...")
    # No return statement

chai_message = prepare_chai()
print(f"Return value: {chai_message}")  # None
print(f"Type: {type(chai_message)}\n")

print("="*50)
print("EXAMPLE 3: Returning Multiple Values (Tuple)")
print("="*50)

def multiple_values():
    """Returns multiple values as tuple."""
    return 10, 20  # Actually returns (10, 20)

# Tuple unpacking
one, two = multiple_values()
print(f"One: {one}, Two: {two}")
print(f"Type returned: {type(multiple_values())}")

# NOTE: Python functions can only return ONE object
# But that object can be a tuple containing multiple values