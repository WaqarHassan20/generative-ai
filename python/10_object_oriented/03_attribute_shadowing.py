# ============================================
# Attribute Shadowing and Deletion
# ============================================
# KEY POINTS:
# - Instance attributes SHADOW class attributes
# - Shadowing doesn't delete the class attribute
# - del removes attributes from instance namespace
# - After deletion, class attribute becomes visible again
# - hasattr() checks if an object has an attribute
# ============================================

# -------------------------------
# DEFINING A CLASS WITH ATTRIBUTES
# -------------------------------
class chai:
    # Class attributes - shared by all instances
    temperature = "hot"
    strength = "strong"

print("="*50)
print("INITIAL STATE: Accessing Class Attributes")
print("="*50 + "\n")

# -------------------------------
# CREATING AN INSTANCE
# -------------------------------
# 'cutting' is slang for half-cup chai in South Asia
cutting = chai()

# At first, instance has no attributes of its own
# It accesses class attributes
print(f"Instance temperature: {cutting.temperature}")  # Reads from class
print(f"Instance strength: {cutting.strength}")        # Reads from class
print()

print("="*50)
print("SHADOWING: Creating Instance Attributes")
print("="*50 + "\n")

# -------------------------------
# CREATING INSTANCE ATTRIBUTES (SHADOWING)
# -------------------------------
# When we assign to instance.attribute, we create an INSTANCE attribute
# This SHADOWS (hides) the class attribute for this instance only
cutting.temperature = "warm"  # Instance attribute shadows class attribute
cutting.done = False           # New instance attribute (doesn't exist in class)

# Now let's see what happened:
print(f"Class temperature (unchanged): {chai.temperature}")      # Output: hot
print(f"Instance temperature (shadowed): {cutting.temperature}")  # Output: warm
print()

print("Note: Class attribute still exists, just hidden for this instance!\n")

print("="*50)
print("DELETION: Removing Instance Attributes")
print("="*50 + "\n")

# -------------------------------
# DELETING INSTANCE ATTRIBUTES
# -------------------------------
# 'del' removes an attribute from the instance's namespace
del cutting.temperature  # Remove instance attribute
del cutting.done         # Remove the custom attribute

# After deletion, the class attribute becomes visible again!
print(f"After deletion, temperature is: {cutting.temperature}")  # Output: hot (from class)
print()

# Check if 'done' attribute still exists
print(f"Does 'done' attribute exist? {hasattr(cutting, 'done')}")  # Output: False
print()

# ============================================
# ATTRIBUTE LOOKUP ORDER:
# When you access obj.attribute, Python looks:
# 1. In the instance's __dict__ (instance namespace)
# 2. In the class's __dict__ (class namespace)
# 3. In parent classes (if inheritance is used)
# ============================================

print("="*50)
print("NAMESPACE INSPECTION")
print("="*50 + "\n")

# See what's in each namespace
print("Instance namespace:", cutting.__dict__)  # Instance attributes
print("Class namespace:", chai.__dict__)       # Class attributes

# ============================================
# SUMMARY:
# - Instance attributes shadow class attributes
# - Shadowing is NOT deletion - class attribute remains
# - del removes from instance, revealing class attribute
# - hasattr() checks if attribute exists (in instance or class)
# ============================================