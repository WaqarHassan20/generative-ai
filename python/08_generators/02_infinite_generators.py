# ============================================
# Infinite Generators
# ============================================
# KEY POINTS:
# - Generators can run infinitely with while True
# - Memory efficient - only current value stored
# - Each generator instance maintains own state
# - Use break or range() to limit iterations
# - Perfect for streams, counters, sequences
# ============================================

print("EXAMPLE: Infinite Counter Generator")
print("="*50)

def infinite_chai_generator():
    """Generator that counts infinitely."""
    count = 1
    while True:  # Infinite loop - never ends!
        yield f"Refill {count}"
        count += 1

refill = infinite_chai_generator()
print(f"Generator object: {refill}")
print("\nFirst 5 refills:")

# Safe - limits iterations even though generator is infinite
for _ in range(5):
    print(f"- {next(refill)}")

print("\n" + "="*50)
print("New Generator Instance (Independent State)")
print("="*50 + "\n")

# Create new generator - starts from 1 again
new_user = infinite_chai_generator()

print("First 8 refills for new customer:")
for _ in range(8):
    print(f"- {next(new_user)}")

# NOTE: Each generator instance maintains its own state
# Original 'refill' generator is still at count=6
# New 'new_user' generator starts fresh at count=1

# WARNING: Don't use 'for item in infinite_generator()' without break!
