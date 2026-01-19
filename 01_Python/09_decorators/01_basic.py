# ============================================
# Decorators - Function Wrappers
# ============================================
# KEY POINTS:
# - Decorator modifies function behavior without changing its code
# - Syntax: @decorator_name above function definition
# - functools.wraps preserves original function metadata
# - Decorators are functions that take and return functions
# - Pattern: wrapper function inside decorator
# ============================================

from functools import wraps

print("EXAMPLE 1: Basic Decorator with @wraps")
print("="*50 + "\n")

def my_decorator(function):
    """Decorator that adds before/after messages."""
    
    @wraps(function)  # Preserves original function's name and docstring
    def wrapper():
        print("Before the function is called.")
        function()  # Call original function
        print("After the function is called.")
    
    return wrapper

# Using decorator with @ syntax
@my_decorator
def greeting():
    """Print a greeting message."""
    print("Hello! Decorated function.")

# Equivalent to: greeting = my_decorator(greeting)

greeting()
print(f"Function name: {greeting.__name__}")  # 'greeting' (thanks to @wraps)
print()

print("-"*50 + "\n")

@my_decorator
def farewell():
    """Print a farewell message."""
    print("Goodbye! Decorated function.")

farewell()
print(f"Function name: {farewell.__name__}")  # 'farewell' (preserved)

# NOTE: Without @wraps, __name__ would be 'wrapper'
# @wraps copies metadata from original function to wrapper

# IMPORTANT: Decorators allow adding functionality without modifying code
# Common uses: logging, authentication, timing, caching
