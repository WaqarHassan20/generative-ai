# ============================================
# Function Basics - Defining and Calling Functions
# ============================================
# KEY POINTS:
# - Functions reduce code duplication
# - def keyword defines a function
# - Parameters allow passing data to functions
# - Functions improve code organization and reusability
# ============================================

def print_chai(name, chai_type):
    """Print a personalized chai order message."""
    print(f"{name.title()} ordered the {chai_type.title()} chai!")


# Calling the function multiple times with different arguments
print_chai("Raj", "lemon")
print_chai("Rahul", "honey")
print_chai("Priya", "ginger")