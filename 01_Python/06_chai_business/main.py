# ============================================
# Module Imports and Package Organization
# ============================================
# KEY POINTS:
# - Modules are .py files containing Python code
# - Packages are directories with __init__.py file
# - import module: imports entire module, use module.function()
# - from module import func: imports specific function, use func()
# - Organize code into packages for better structure
# ============================================

print("EXAMPLE 1: Importing Entire Module")
print("="*50)

# Import the entire flavours module
import recipes.flavours

# Must use full path to access functions
print(recipes.flavours.lemon_chai())
print(recipes.flavours.ginger_chai())

print("\n" + "="*50)
print("EXAMPLE 2: Importing Specific Functions")
print("="*50 + "\n")

# Import only specific functions
from recipes.flavours import lemon_chai, ginger_chai

# Can use functions directly without module prefix
print(lemon_chai())
print(ginger_chai())

# NOTE: Use 'import module' for clarity, 'from module import' for convenience
