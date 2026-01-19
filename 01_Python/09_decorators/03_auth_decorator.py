# ============================================
# Authorization Decorator
# ============================================
# KEY POINTS:
# - Decorators can control access to functions
# - Check conditions before executing function
# - Return None or error if conditions not met
# - Common in web frameworks (Flask, Django)
# - Can check: user roles, permissions, authentication
# ============================================

from functools import wraps

print("EXAMPLE: Role-Based Access Control")
print("="*50 + "\n")

def require_admin(function):
    """Decorator that requires admin role to execute function."""
    
    @wraps(function)
    def wrapper(user_role):
        # Check authorization before executing
        if user_role != "admin":
            print("❌ Access denied. Admins only.")
            return None  # Don't execute function
        else:
            print("✅ Access granted.")
            return function(user_role)  # Execute function
    
    return wrapper

@require_admin
def access_tea_inventory(user_role):
    """Sensitive function - only admins can access."""
    print(f"Accessing the tea inventory as {user_role}...")
    print("Inventory: 100 tea bags, 50 sugar packets")
    return "Inventory accessed successfully"

print("-"*50)
print("Guest trying to access:")
result1 = access_tea_inventory("guest")
print(f"Result: {result1}")

print("\n" + "-"*50 + "\n")

print("Admin trying to access:")
result2 = access_tea_inventory("admin")
print(f"Result: {result2}")

print("-"*50)

# NOTE: Authorization decorators are crucial for security
# They centralize access control logic

# REAL-WORLD USAGE:
# - @login_required: User must be logged in
# - @require_role('admin'): User must have specific role
# - @rate_limit: Limit API calls per user
# - @cache: Cache expensive function results