# ============================================
# Global vs Nonlocal Keywords
# ============================================
# KEY POINTS:
# - 'global' accesses/modifies module-level (global) variables
# - 'nonlocal' accesses/modifies enclosing function variables
# - Use 'global' sparingly - can make code harder to debug
# - Prefer passing parameters and returning values
# ============================================

# Global variable at module level
chai_type = "green chai"

print("EXAMPLE 1: Using 'nonlocal' keyword")
print("="*50)

def front_desk():
    chai_type = "ginger chai"  # Enclosing scope variable
    
    def kitchen():
        nonlocal chai_type  # Modifies enclosing scope
        print(f"Before updating: {chai_type}")
        chai_type = "lemon chai"
    
    kitchen()
    print(f"After updating: {chai_type}")  # Changed to "lemon chai"

front_desk()
print(f"Global variable unchanged: {chai_type}")  # Still "green chai"

print("\n" + "="*50)
print("EXAMPLE 2: Using 'global' keyword")
print("="*50 + "\n")

def front_desk_global():
    def kitchen():
        global chai_type  # Modifies global variable
        print(f"Before updating: {chai_type}")
        chai_type = "Irani chai"  # Changes global variable
    
    kitchen()
    print(f"After updating: {chai_type}")  # Reflects global change

front_desk_global()
print(f"Global variable changed: {chai_type}")  # Now "Irani chai"

# NOTE: 'global' affects module-level variable
# NOTE: 'nonlocal' affects enclosing function's variable