# ============================================
# Basic For Loop with range()
# ============================================
# KEY POINTS:
# - range(start, stop) generates numbers from start to stop-1
# - range(1, 11) produces 1 through 10
# - Useful for repeating tasks a specific number of times
# ============================================

# Loop through token numbers 1 to 10
for token in range(1, 11):
    print(f"Serving chai to token number {token}")

print("\n" + "="*40 + "\n")

# Loop through batch numbers 1 to 4
for batch in range(1, 5):
    print(f"Preparing chai for batch number {batch}")