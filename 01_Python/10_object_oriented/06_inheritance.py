    # ============================================
# INHERITANCE IN PYTHON - Complete Guide
# ============================================
# KEY POINTS:
# - Inheritance allows a class to inherit attributes/methods from another class
# - Parent class (base class) provides common functionality
# - Child class (derived class) inherits and can extend/override
# - Promotes code reuse and establishes relationships
# - Class variables can be overridden in child classes
# - Factory pattern: using class variables to control object creation
# ============================================

# -------------------------------
# BASE CLASS: base_chai
# -------------------------------
# This class represents a GENERIC chai (tea)
# It defines common behavior that ALL types of chai will have
# Think of this as the "parent" or "blueprint" class

class base_chai:
    """
    Base class for all chai types.
    Provides the fundamental behavior shared by all chai varieties.
    """

    # -------------------------------
    # CONSTRUCTOR METHOD
    # -------------------------------
    # This runs automatically when an object of base_chai (or its child) is created
    # 
    # Parameters:
    #   self  - The instance being created
    #   type_ - What kind of chai it is (e.g., "Honey Tea", "Black Tea")
    def __init__(self, type_):
        # Store the chai type as an instance attribute
        self.type_ = type_
        print(f"🔧 Creating {type_} using base_chai constructor")

    # -------------------------------
    # COMMON METHOD FOR ALL CHAI TYPES
    # -------------------------------
    # Every chai needs to be prepared, regardless of type
    # This method will be inherited by all child classes
    def prepare(self):
        print(f"☕ Preparing {self.type_}...")
        print("   - Boiling water")
        print("   - Adding tea leaves")


# -------------------------------
# CHILD CLASS: ginger_chai
# -------------------------------
# This class INHERITS from base_chai
# Syntax: class ChildClass(ParentClass):
# 
# What it gets automatically:
#   - __init__() method from base_chai
#   - prepare() method from base_chai
#   - Any other attributes/methods from base_chai

class ginger_chai(base_chai):
    """
    Specialized chai class for ginger chai.
    Inherits all base_chai functionality and adds ginger-specific features.
    """

    # -------------------------------
    # ADDITIONAL METHOD (NOT IN PARENT)
    # -------------------------------
    # This method is UNIQUE to ginger_chai
    # base_chai does NOT have this method
    # This is how we EXTEND functionality through inheritance
    def add_spices(self):
        print(f"🌶️  Adding fresh ginger spice to the {self.type_}")
        print("   - Grating ginger root")
        print("   - Adding to boiling water")


# -------------------------------
# CHAI SHOP CLASS (FACTORY PATTERN)
# -------------------------------
# This class represents a shop that SERVES chai
# It uses a "factory" design pattern to create different types of chai

class chai_shop:
    """
    A chai shop that can serve different types of chai.
    Uses a class variable to determine which chai class to instantiate.
    """

    # -------------------------------
    # CLASS VARIABLE (IMPORTANT!)
    # -------------------------------
    # This decides WHICH chai class the shop will use to create chai objects
    # By default, it uses base_chai
    # Child classes can OVERRIDE this to use different chai classes
    chai_cls = base_chai

    # -------------------------------
    # CONSTRUCTOR
    # -------------------------------
    def __init__(self, type_):
        print(f"\n🏪 Opening shop to serve {type_}...")
        
        # Create a chai object using the class stored in chai_cls
        # self.chai_cls could be:
        #   - base_chai (default)
        #   - ginger_chai (if overridden in child class)
        #   - any other chai class
        # 
        # This is the FACTORY PATTERN:
        # The shop doesn't know exactly which type of chai it's creating
        # It just calls self.chai_cls() and lets the class variable decide
        self.chai = self.chai_cls(type_)
        print(f"✅ Shop ready with {type_}!\n")

    # -------------------------------
    # METHOD TO SERVE CHAI
    # -------------------------------
    def serve_chai(self):
        print(f"\n{'='*50}")
        print(f"👨‍🍳 Serving {self.chai.type_}...")
        print(f"{'='*50}")
        
        # Call the prepare() method on the chai object
        # This method exists because:
        #   - base_chai has it
        #   - ginger_chai inherits it
        self.chai.prepare()
        
        print(f"✅ {self.chai.type_} is ready to serve!\n")


# -------------------------------
# FANCY CHAI SHOP (INHERITANCE)
# -------------------------------
# This class INHERITS from chai_shop
# It's a specialized shop that only serves ginger chai

class fancy_chai_shop(chai_shop):
    """
    A fancy shop that specializes in ginger chai.
    Inherits all chai_shop functionality but uses ginger_chai class.
    """

    # -------------------------------
    # OVERRIDE THE chai_cls CLASS VARIABLE
    # -------------------------------
    # This is the KEY difference from regular chai_shop
    # Now when __init__ calls self.chai_cls(), it will create ginger_chai
    # instead of base_chai
    chai_cls = ginger_chai
    # 
    # Note: We don't need to rewrite __init__ or serve_chai
    # We inherit them from chai_shop!
    # They will automatically use ginger_chai because of this override


print("\n" + "="*60)
print("         CHAI SHOP DEMONSTRATION")
print("="*60)

# -------------------------------
# CREATING SHOP INSTANCES
# -------------------------------

print("\n🏪 Creating Regular Chai Shop...")
print("-"*60)
# Regular chai shop uses base_chai (default)
shop = chai_shop("Honey Tea")

print("\n🌟 Creating Fancy Chai Shop...")
print("-"*60)
# Fancy chai shop uses ginger_chai (overridden)
fancy = fancy_chai_shop("Black Tea")

# -------------------------------
# SERVING CHAI FROM BOTH SHOPS
# -------------------------------

print("\n" + "="*60)
print("         SERVING FROM REGULAR SHOP")
print("="*60)
shop.serve_chai()

print("\n" + "="*60)
print("         SERVING FROM FANCY SHOP")
print("="*60)
fancy.serve_chai()

# -------------------------------
# USING GINGER-SPECIFIC METHOD
# -------------------------------
print("\n" + "="*60)
print("         ADDING GINGER SPICES (FANCY SHOP ONLY)")
print("="*60 + "\n")

# Access the chai object inside fancy shop
# Since fancy shop uses ginger_chai, this object has add_spices() method
fancy.chai.add_spices()

# Note: shop.chai.add_spices() would give an error
# because shop uses base_chai which doesn't have add_spices()

print("\n" + "="*60)
print("         INHERITANCE HIERARCHY")
print("="*60)
print("""
┌──────────────────────────────────────────────────────┐
│  BASE CLASSES                                        │
├──────────────────────────────────────────────────────┤
│  base_chai                    chai_shop              │
│  ├─ __init__(type_)           ├─ chai_cls = base_chai│
│  └─ prepare()                 ├─ __init__(type_)     │
│                                └─ serve_chai()        │
└──────────────────────────────────────────────────────┘
           ↓ inherits                    ↓ inherits
┌──────────────────────────────────────────────────────┐
│  CHILD CLASSES                                       │
├──────────────────────────────────────────────────────┤
│  ginger_chai                  fancy_chai_shop        │
│  └─ add_spices()              └─ chai_cls=ginger_chai│
└──────────────────────────────────────────────────────┘

When fancy_chai_shop creates chai:
  1. Inherits __init__ from chai_shop
  2. __init__ uses self.chai_cls (which is ginger_chai)
  3. Creates ginger_chai instance
  4. That instance has prepare() + add_spices()
""")

# ============================================
# KEY TAKEAWAYS:
# ============================================
# 1. INHERITANCE: Child class gets parent's methods/attributes
# 2. EXTENDING: Child can add new methods (add_spices)
# 3. OVERRIDING: Child can change class variables (chai_cls)
# 4. FACTORY PATTERN: Use class variables to control object creation
# 5. CODE REUSE: Don't repeat code, inherit it!
# ============================================
