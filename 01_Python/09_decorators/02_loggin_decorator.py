# ============================================
# Logging Decorator with Arguments
# ============================================
# KEY POINTS:
# - *args and **kwargs allow decorator to work with any function
# - Captures all positional and keyword arguments
# - Returns function result (important for chaining)
# - Useful for debugging and monitoring function calls
# - Can log function name, arguments, return value, timing
# ============================================

from functools import wraps

print("EXAMPLE: Logging Function Calls")
print("="*50 + "\n")

def log_activity(function):
    """Decorator that logs function entry and exit."""
    
    @wraps(function)
    def wrapper(*args, **kwargs):
        # Before function execution
        print(f"Calling function: {function.__name__}")
        
        # Execute original function
        result = function(*args, **kwargs)
        
        # After function execution
        print(f"Ending function: {function.__name__}")
        
        return result  # Return result to caller
    
    return wrapper

@log_activity
def make_tea(chai, milk=True, sugar=False):
    """Prepare tea with specified ingredients."""
    print(f"Making {chai} tea")
    print(f"Milk: {milk}, Sugar: {sugar}")
    return f"{chai} tea is ready!"

print("-"*50)
result1 = make_tea("Lemon")
print(f"Result: {result1}")

print("\n" + "-"*50 + "\n")

result2 = make_tea("Ginger", milk=True, sugar=True)
print(f"Result: {result2}")

print("-"*50)

# NOTE: *args captures positional arguments as tuple
# **kwargs captures keyword arguments as dictionary
# This makes decorator work with any function signature

# IMPORTANT: Always return result from wrapper
# Otherwise decorated function always returns None