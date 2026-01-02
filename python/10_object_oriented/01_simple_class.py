# ============================================
# Introduction to Classes in Python
# ============================================
# KEY POINTS:
# - Classes are blueprints for creating objects
# - Everything in Python is an object (even classes!)
# - 'pass' is a placeholder when class has no body
# - type() shows the type/class of an object
# - Instance objects are created from class blueprints
# ============================================

# -------------------------------
# DEFINING A SIMPLE CLASS
# -------------------------------
# This creates a new class called 'chai'
# Think of it as a blueprint for creating chai objects
class chai:
    pass  # 'pass' means "do nothing" - empty class for now

# -------------------------------
# CHECKING THE TYPE OF A CLASS
# -------------------------------
# Even classes themselves are objects in Python!
# Classes are instances of the 'type' metaclass
print("Type of chai class:", type(chai))
print()  # Output: <class 'type'>

# IMPORTANT: Everything in Python is an object, including classes!
# The class 'chai' is an object of type 'type'

# -------------------------------
# CREATING AN INSTANCE (OBJECT)
# -------------------------------
# ginger_chai is an INSTANCE of the chai class
# We "instantiate" the class by calling it like a function: chai()
ginger_chai = chai()

# Check what type ginger_chai is
print("Type of ginger_chai instance:", type(ginger_chai))
print()  # Output: <class '__main__.chai'>

# -------------------------------
# COMPARING TYPES
# -------------------------------
# Is ginger_chai's type exactly the chai class? YES!
print("Is ginger_chai an instance of chai?", type(ginger_chai) is chai)
print()  # Output: True

# The opposite check - is it NOT an instance?
print("Is ginger_chai NOT an instance of chai?", type(ginger_chai) is not chai)
print()  # Output: False

# ============================================
# SUMMARY:
# - chai is a CLASS (blueprint)
# - ginger_chai is an INSTANCE (actual object created from blueprint)
# - type(chai) returns 'type' (classes are objects of type 'type')
# - type(ginger_chai) returns 'chai' (instances are objects of their class)
# ============================================
