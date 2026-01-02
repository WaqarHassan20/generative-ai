# ============================================
# Nested Conditionals
# ============================================
# KEY POINTS:
# - Conditionals can be nested inside other conditionals
# - Inner conditions only execute if outer condition is True
# - Can simplify: 20 < temperature < 25 (chained comparison)
# ============================================

device_status = input("Enter device current status (active/inactive): ").lower()

if device_status == "active":
    temperature = float(input("Enter temperature in Celsius: "))
    
    if temperature < 20:
        print("Temperature is below 20°C. Turning on the heater.")
    elif 20 <= temperature < 25:
        print("Normal temperature.")
    elif temperature >= 25:
        print("Temperature is above 25°C. Turning on the cooler.")
else:
    print("Device is inactive.")
