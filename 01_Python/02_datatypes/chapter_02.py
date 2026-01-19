# ============================================
# Set Data Type
# ============================================
# KEY POINTS:
# - Sets are mutable (can be modified in place)
# - Sets maintain the same ID even after adding elements
# - Sets are unordered and don't allow duplicates
# - Unlike integers, sets don't create new objects when modified
# ============================================

# Create an empty set
spice_mix = set()
id1 = id(spice_mix)

print(f"Initial spice mix ID: {id(spice_mix)}")
print(f"Initial value is: {spice_mix}")

# Adding elements to the set (modifies in place)
spice_mix.add("ginger")
spice_mix.add("cardamon")
spice_mix.add("lemon")

id2 = id(spice_mix)

print(f"Updated spice mix ID: {id(spice_mix)}")
print(f"Updated value is: {spice_mix}")

# Sets maintain the same ID after modification (mutable)
if id1 == id2:
    print("Same IDs - Sets are mutable!")
else:
    print("Different IDs")