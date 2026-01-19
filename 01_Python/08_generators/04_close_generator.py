# ============================================
# Generator Delegation and Cleanup
# ============================================
# KEY POINTS:
# - yield from delegates to another generator
# - Chains multiple generators together
# - close() stops generator and raises GeneratorExit
# - Use try-except to handle cleanup on close()
# - Useful for managing resources
# ============================================

print("EXAMPLE 1: yield from (Generator Delegation)")
print("="*50)

def local_chai():
    """Generator for local chai varieties."""
    yield "Lemon chai"
    yield "Ginger chai"

def imported_chai():
    """Generator for imported chai varieties."""
    yield "Masala chai"
    yield "Cardamom chai"

def full_menu():
    """Combine multiple generators using yield from."""
    yield from local_chai()     # Delegates to local_chai
    yield from imported_chai()  # Then delegates to imported_chai

print("Full menu:")
for chai in full_menu():
    print(f"- {chai}")

print("\n" + "="*50)
print("EXAMPLE 2: close() Method and Cleanup")
print("="*50 + "\n")

def chai_stall():
    """Generator with cleanup logic."""
    try:
        while True:
            order = yield "Waiting for chai order..."
            print(f"Received order: {order}")
    except GeneratorExit:
        # This runs when close() is called
        print("Chai stall is closing. No more orders will be taken.")

stall = chai_stall()
print(next(stall))  # Start generator

# Uncomment to send orders:
# print(stall.send("Lemon chai"))
# print(stall.send("Ginger chai"))

print("\nClosing the stall...")
stall.close()  # Triggers GeneratorExit exception

print("\nTrying to use closed generator:")
try:
    next(stall)
except StopIteration:
    print("Generator is closed - cannot use anymore")

# NOTE: yield from is shorthand for delegating to another generator
# Instead of: for item in other_gen(): yield item
# Use:        yield from other_gen()

# NOTE: close() is useful for cleanup (closing files, connections, etc.)