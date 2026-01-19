# ============================================
# Constructors and __init__ Method
# ============================================
# KEY POINTS:
# - __init__ is the constructor method (initializer)
# - Automatically called when creating a new instance
# - Used to set up initial state of the object
# - 'self' refers to the newly created instance
# - Can accept parameters to customize each instance
# - Instance attributes created in __init__ are unique per object
# ============================================

# -------------------------------
# CLASS WITH CONSTRUCTOR
# -------------------------------
class chai_order:
    # Class attribute - shared by ALL instances
    flavor = "Ginger"  # Default flavor for all orders

    # -------------------------------
    # CONSTRUCTOR METHOD (__init__)
    # -------------------------------
    # This method is called AUTOMATICALLY when you create an instance
    # It initializes the object with starting values
    #
    # Parameters:
    #   self   - The instance being created (provided automatically)
    #   type_  - The type of chai being ordered (e.g., "Lemon", "Honey")
    #   size   - The size in milliliters
    def __init__(self, type_, size):
        print(f"🔧 Constructor called! Creating a {type_} chai order...")
        
        # Create INSTANCE ATTRIBUTES
        # These belong to this specific object only
        self.type = type_   # Each order has its own type
        self.size = size    # Each order has its own size
        
        print(f"✅ Order created successfully!\n")

    # -------------------------------
    # INSTANCE METHOD
    # -------------------------------
    # Returns a summary of this specific order
    def summary(self):
        return f"📋 Order: {self.size} ml {self.type} chai"

print("="*50)
print("CREATING INSTANCES WITH CONSTRUCTOR")
print("="*50 + "\n")

# -------------------------------
# CREATING INSTANCES
# -------------------------------
# When we call chai_order(), Python:
# 1. Creates a new empty object
# 2. Calls __init__ on that object
# 3. Returns the initialized object

print("Creating first order...")
print("-"*50)
order1 = chai_order("Lemon", 250)
print(order1.summary())
print()

print("Creating second order...")
print("-"*50)
order2 = chai_order("Honey", 300)
print(order2.summary())
print()

print("="*50)
print("COMPARING INSTANCES")
print("="*50 + "\n")

# Each instance has its own attributes
print(f"Order 1 type: {order1.type}, size: {order1.size}")
print(f"Order 2 type: {order2.type}, size: {order2.size}")
print()

# Both share the CLASS attribute
print(f"Order 1 flavor (class attr): {order1.flavor}")
print(f"Order 2 flavor (class attr): {order2.flavor}")
print()

# ============================================
# WHY USE __init__?
# ============================================
# Without __init__, you'd have to do this:
#   order = chai_order()
#   order.type = "Lemon"
#   order.size = 250
#
# With __init__, you do this:
#   order = chai_order("Lemon", 250)
#
# Benefits:
# - Cleaner, more concise code
# - Ensures all instances start with required attributes
# - Can perform validation or calculations during creation
# - Makes object creation more intuitive
# ============================================

print("="*50)
print("KEY DIFFERENCES")
print("="*50)
print("""
┌─────────────────────┬──────────────────────────────┐
│ Class Attributes    │ Instance Attributes          │
├─────────────────────┼──────────────────────────────┤
│ Shared by all       │ Unique to each instance      │
│ Defined in class    │ Defined in __init__ (self.x) │
│ chai_order.flavor   │ order1.type, order1.size     │
└─────────────────────┴──────────────────────────────┘
""")
