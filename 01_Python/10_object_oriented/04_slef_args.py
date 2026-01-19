# ============================================
# The 'self' Parameter in Methods
# ============================================
# KEY POINTS:
# - 'self' refers to the instance calling the method
# - First parameter of instance methods is always 'self'
# - Python automatically passes instance as first argument
# - Can call methods via class (must pass instance manually)
# - 'self' allows access to instance attributes
# ============================================

# -------------------------------
# DEFINING A CLASS WITH METHODS
# -------------------------------
class chai_cup:
    # Class attribute - shared by all instances
    size = 150  # Default size in milliliters

    # -------------------------------
    # INSTANCE METHOD
    # -------------------------------
    # 'self' is a reference to the instance that calls this method
    # It's NOT a keyword - you could name it anything, but 'self' is convention
    def describe(self):
        # Access the instance's 'size' attribute via self
        return f"A {self.size} ml chai cup."

print("="*50)
print("EXAMPLE 1: Normal Method Call (Python Handles 'self')")
print("="*50 + "\n")

# -------------------------------
# CREATING INSTANCE AND CALLING METHOD
# -------------------------------
cup = chai_cup()

# When we call cup.describe(), Python automatically does:
# 1. Looks up 'describe' in the class
# 2. Calls it with 'cup' as the first argument (self)
# This is called "method binding"
print(cup.describe())
print()  # Output: A 150 ml chai cup.

print("-"*50)
print("What happens behind the scenes:")
print("cup.describe() is equivalent to chai_cup.describe(cup)")
print("-"*50 + "\n")

# -------------------------------
# CALLING METHOD VIA CLASS (MANUAL 'self')
# -------------------------------
# If we call method on the CLASS (not instance), we must pass instance manually

# This will give an error - no instance provided:
# print(chai_cup.describe())  # TypeError: describe() missing 1 required positional argument: 'self'

# Correct way - pass instance as first argument:
print("Calling via class:", chai_cup.describe(cup))
print()  # Output: A 150 ml chai cup.

print("="*50)
print("EXAMPLE 2: Instance-Specific Attributes")
print("="*50 + "\n")

# -------------------------------
# MODIFYING INSTANCE ATTRIBUTE
# -------------------------------
new_cup = chai_cup()
new_cup.size = 500  # Create instance attribute (shadows class attribute)

# Now this instance has its own 'size'
# The describe method will use the instance's size via self.size
print("Original cup:", cup.describe())      # Output: A 150 ml chai cup.
print("Larger cup:", new_cup.describe())   # Output: A 500 ml chai cup.
print()

# -------------------------------
# CALLING VIA CLASS WITH MODIFIED INSTANCE
# -------------------------------
# Again, calling via class - must pass instance manually
print("Via class:", chai_cup.describe(new_cup))
print()  # Output: A 500 ml chai cup.

# ============================================
# HOW 'self' WORKS:
# ============================================
# When you write:     cup.describe()
# Python translates:  chai_cup.describe(cup)
#                                        ↑
#                     This becomes 'self' inside the method
#
# The 'self' parameter allows the method to:
# 1. Access the instance's attributes
# 2. Call other methods on the same instance
# 3. Modify the instance's state
# ============================================

print("="*50)
print("SUMMARY")
print("="*50)
print("""
1. 'self' is the first parameter of instance methods
2. Python automatically passes the instance as 'self'
3. Use 'self' to access instance attributes and methods
4. Can call method via class: ClassName.method(instance)
5. 'self' is convention - could be named anything
""")