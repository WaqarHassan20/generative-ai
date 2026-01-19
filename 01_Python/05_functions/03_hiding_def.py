# ============================================
# Abstraction and Encapsulation with Functions
# ============================================
# KEY POINTS:
# - Hide implementation details behind simple interfaces
# - User only needs to know what function does, not how
# - Makes code easier to maintain and modify
# - Changes to internal logic don't affect external code
# ============================================

def get_input():
    """Get user input from form or API."""
    print("Getting the input...")


def validating_input():
    """Validate user input against business rules."""
    print("Validating the user input...")


def saving_to_db():
    """Persist validated data to database."""
    print("Saving data into database...")


def register_user():
    """Complete user registration process (public interface)."""
    # Internal implementation hidden from caller
    get_input()
    validating_input()
    saving_to_db()
    print("User registration completed!")


# Simple, clean interface - complexity is hidden
register_user()