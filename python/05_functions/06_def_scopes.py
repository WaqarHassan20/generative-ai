# ============================================
# Variable Scopes in Python (LEGB Rule)
# ============================================
# KEY POINTS:
# - Local: Variables defined inside a function
# - Enclosing: Variables in outer function (for nested functions)
# - Global: Variables defined at module level
# - Built-in: Python's built-in names (print, len, etc.)
# - Inner scope can access outer scope (read-only by default)
# - Each function creates its own local scope
# ============================================

# Example 1: Nested functions with same variable names
def print_counter():
    chai_order = "Masala chai"  # Enclosing scope
    
    def print_order():
        chai_order = "Ginger chai"  # Local scope (shadows outer)
        print(f"Inner function: {chai_order}")
    
    print_order()
    print(f"Outer function: {chai_order}")  # Unchanged

# Global scope variable
chai_order = "Tulsi chai"
print_counter()
print(f"Global scope: {chai_order}")  # Still original value

print("\n" + "="*50 + "\n")

# Example 2: Function accessing global variable
def serve_chai():
    chai_type = "Masala chai"  # Local variable (shadows global)
    print(f"Inside function: {chai_type}")

chai_type = "Lemon chai"  # Global variable
serve_chai()
print(f"Outside function: {chai_type}")  # Global unchanged

# NOTE: Without 'global' keyword, assignment creates new local variable