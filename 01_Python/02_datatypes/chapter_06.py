# ============================================
# String Data Type
# ============================================
# KEY POINTS:
# - Strings are immutable sequences of characters
# - Slicing syntax: string[start:end:step]
# - Negative indices count from the end
# - encode() converts string to bytes, decode() reverses it
# ============================================

# String interpolation with f-strings
chai_type = "ginger chai"
customer_name = "Piya"
print(f"Hello {customer_name}, your {chai_type} is ready!")

chai_description = "Aromatic and Bold taste"

# String slicing examples
print(f"First 8 characters: {chai_description[0:8]}")
print(f"First 8 characters (shorthand): {chai_description[:8]}")
print(f"From index 12 onwards: {chai_description[12:]}")

# Slicing with step (every 2nd character)
print(f"Every 2nd character: {chai_description[0:8:2]}")

# Reverse string using negative step
print(f"Reversed string: {chai_description[::-1]}")

# String encoding and decoding
label_text = "Chai Special"
encoded_label = label_text.encode("utf-8")  # Convert to bytes

print(f"\nOriginal label: {label_text}")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")  # Convert back to string
print(f"Decoded label: {decoded_label}")

