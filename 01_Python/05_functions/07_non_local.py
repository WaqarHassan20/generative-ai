# ============================================
# Nonlocal Keyword
# ============================================
# KEY POINTS:
# - 'nonlocal' modifies variable from enclosing (outer) scope
# - Works only with nested functions
# - Cannot be used for global scope variables
# - Allows inner function to modify outer function's variables
# - Different from 'global' which accesses module-level variables
# ============================================

def update_order():
    chai_type = "Elaichi chai"  # Enclosing scope variable
    print(f"Chai Type before kitchen: {chai_type}")
    
    def kitchen():
        nonlocal chai_type  # Reference to outer function's variable
        chai_type = "Lemon chai"  # Modifies outer scope variable
    
    kitchen()  # Call inner function
    print(f"Chai Type after kitchen: {chai_type}")  # Modified!

update_order()

# IMPORTANT: Without 'nonlocal', assignment would create new local variable
# With 'nonlocal', we modify the enclosing scope's variable