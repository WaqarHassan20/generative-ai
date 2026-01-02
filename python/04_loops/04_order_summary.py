# ============================================
# Using zip() for Parallel Iteration
# ============================================
# KEY POINTS:
# - zip() pairs elements from multiple lists
# - Stops when shortest list ends
# - Perfect for processing related data together
# ============================================

customers = ["hitesh", "pooja", "simran", "anjali", "rahul"]
bills = [250, 400, 150, 300, 500]

# Iterate through both lists simultaneously
for customer, bill in zip(customers, bills):
    print(f"Customer {customer.title()} paid bill of ${bill}")
