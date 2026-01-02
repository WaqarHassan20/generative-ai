# ============================================
# Float Data Type
# ============================================
# KEY POINTS:
# - Floats represent decimal numbers
# - Precision issues can occur with floating-point arithmetic
# - Use sys.float_info to see float limitations
# - Be careful when comparing floats for equality
# ============================================

import sys

# Demonstrating floating-point precision
ideal_temperature = 75.5
current_temperature = 75.499999
temperature_difference = ideal_temperature - current_temperature
print(f"Temperature difference is: {temperature_difference}°C")

# Different precision example
ideal_temperature2 = 75.5
current_temperature2 = 75.49
temperature_difference2 = ideal_temperature2 - current_temperature2
print(f"Temperature difference is: {temperature_difference2}°C")

# Display comprehensive float information (limits, precision, etc.)
print("\nFloat data type information:")
print(sys.float_info)