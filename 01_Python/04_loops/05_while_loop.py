# ============================================
# While Loop
# ============================================
# KEY POINTS:
# - while loops continue until condition becomes False
# - Make sure condition eventually becomes False (avoid infinite loops)
# - Useful when number of iterations is unknown
# ============================================

temperature = 40

# Keep heating until temperature reaches 100°C
while temperature < 100:
    temperature += 15
    print(f"Current temperature is {temperature}°C")

print("\nTea is now ready to boil!")
