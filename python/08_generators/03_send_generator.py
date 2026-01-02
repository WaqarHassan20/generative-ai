# ============================================
# Generator .send() Method
# ============================================
# KEY POINTS:
# - send() passes value back into generator
# - yield becomes assignment expression
# - Enables two-way communication with generator
# - Must call next() first to "prime" generator
# - Useful for interactive generators
# ============================================

print("EXAMPLE: Interactive Order System")
print("="*50 + "\n")

def chai_customer():
    """Generator that receives orders via send()."""
    print("Welcome to the chai shop!")
    
    # First yield - starts generator
    order = yield "What would you like to order?"
    
    while True:
        # Process received order
        print(f"Preparing {order}...")
        
        # Yield result and wait for next order
        order = yield f"Here is your {order}. What would you like next?"

stall = chai_customer()

# STEP 1: Prime the generator (start it)
welcome_msg = next(stall)
print(welcome_msg)

print()

# STEP 2: Send first order
response1 = stall.send("Lemon Chai")
print(response1)

print()

# STEP 3: Send second order
response2 = stall.send("Ginger Chai")
print(response2)

# NOTE: send() allows generator to receive values
# The value sent becomes result of yield expression
# Pattern: order = yield response
#          └── receives value from send()

# IMPORTANT: Always call next() before first send()
# Or use: stall.send(None) to prime generator
