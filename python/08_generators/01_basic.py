# ============================================
# Generator Functions and yield Keyword
# ============================================
# KEY POINTS:
# - yield pauses function and returns value
# - Function state is preserved between yields
# - next() resumes execution until next yield
# - Generators are memory efficient (lazy evaluation)
# - Can iterate with for loop or next()
# - Use generators for large sequences
# ============================================

print("EXAMPLE 1: Basic Generator with yield")
print("="*50)

def serve_chai():
    """Generator function using yield."""
    yield "Boil water"
    yield "Steep tea leaves"
    yield "Add milk and sugar"
    yield "Pour into cup"

# Iterate through generator
result = serve_chai()
for step in result:
    print(f"- {step}")

print("\n" + "="*50)
print("EXAMPLE 2: Regular Function vs Generator")
print("="*50 + "\n")

# Regular function - returns entire list at once
def get_chai():
    """Regular function - creates entire list in memory."""
    return ["Boil water", "Steep tea leaves", "Add milk and sugar", "Pour into cup"]

print("Regular function (list):")
print(get_chai())

print("\n" + "-"*50 + "\n")

# Generator function - yields one item at a time
def get_chai_gen():
    """Generator function - yields items one by one."""
    yield "Boil water"
    yield "Steep tea leaves"
    yield "Add milk and sugar"
    yield "Pour into cup"

print("Generator function (using next):")
chai = get_chai_gen()
print(f"Step 1: {next(chai)}")
print(f"Step 2: {next(chai)}")
print(f"Step 3: {next(chai)}")
print(f"Step 4: {next(chai)}")
# print(next(chai))  # Would raise StopIteration

print("\n" + "-"*50 + "\n")

print("Generator function (using for loop):")
for step in get_chai_gen():
    print(f"- {step}")

# NOTE: Generators are memory efficient - values generated on demand
# Regular function creates entire list in memory
# Generator creates one value at a time
