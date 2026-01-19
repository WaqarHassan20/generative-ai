# ============================================
# Class Attributes and Namespaces
# ============================================
# KEY POINTS:
# - Class attributes are shared by all instances
# - Instance attributes belong to individual objects
# - You can add attributes to a class after definition
# - Instances inherit class attributes
# - Each instance has its own namespace
# ============================================

print("-"*50)
print("EXAMPLE 1: Class Attributes Shared by All Instances")
print("-"*50 + "\n")

# -------------------------------
# DEFINING A CLASS WITH ATTRIBUTES
# -------------------------------
class chai:
    # This is a CLASS ATTRIBUTE
    # It belongs to the class itself, not to any specific instance
    # ALL instances will share this attribute
    origin = "Pakistan"

# -------------------------------
# ACCESSING CLASS ATTRIBUTES VIA INSTANCE
# -------------------------------
# Create an instance of chai
lemon_tea = chai()

# Access class attribute through the instance
# lemon_tea doesn't have 'origin' itself, so it looks in the class
print(f"Lemon tea origin: {lemon_tea.origin}")
print()  # Output: Pakistan

# -------------------------------
# ADDING NEW CLASS ATTRIBUTES DYNAMICALLY
# -------------------------------
# We can add new attributes to the class even after it's defined!
chai.sugar = False  # Adding 'sugar' attribute to the CLASS

print(f"Class attribute 'sugar': {chai.sugar}")
print()  # Output: False

print("-"*50)
print("EXAMPLE 2: New Instances Inherit Class Attributes")
print("-"*50 + "\n")

# -------------------------------
# NEW INSTANCE SEES NEW CLASS ATTRIBUTES
# -------------------------------
# Create a new instance AFTER adding 'sugar' attribute
ginger_tea = chai()

# This instance can see BOTH class attributes
print(f"Ginger tea origin: {ginger_tea.origin}")  # Output: Pakistan
print(f"Ginger tea sugar: {ginger_tea.sugar}")    # Output: False
print()

print("-"*50)
print("EXAMPLE 3: Instance Attributes vs Class Attributes")
print("-"*50 + "\n")

# -------------------------------
# CREATING INSTANCE-SPECIFIC ATTRIBUTE
# -------------------------------
# Now we set 'sugar' on the INSTANCE, not the class
# This creates an instance attribute that SHADOWS the class attribute
ginger_tea.sugar = True

# Check the values:
print(f"Class sugar attribute: {chai.sugar}")         # Output: False (unchanged!)
print(f"Instance sugar attribute: {ginger_tea.sugar}")  # Output: True (instance-specific)
print()

# ============================================
# SUMMARY:
# - Class attributes (chai.origin) are shared by all instances
# - Instance attributes (ginger_tea.sugar) are specific to one instance
# - Instance attributes SHADOW class attributes with the same name
# - When accessing attribute, Python looks:
#   1. First in instance namespace
#   2. Then in class namespace
#   3. Then in parent class namespaces
# ============================================