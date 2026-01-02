def chai_serve(chai_type):
    print(f"Preparing your {chai_type} chai...")
    try:
        if chai_type == "unknown":
            raise ValueError("Unknown chai type requested!")
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"Your {chai_type} chai is served.")
    finally:
        print("Thank you for visiting our chai shop!")


print("---------------------------------------")

# Test the function with a valid chai type
chai_serve("Ginger")

print("---------------------------------------")

# Test the function with an unknown chai type
chai_serve("unknown")

print("---------------------------------------")