# ============================================
# Functions with Parameters in Loops
# ============================================
# KEY POINTS:
# - Functions can be called repeatedly with different arguments
# - Combine loops and functions for processing collections
# - Keep calculations DRY (Don't Repeat Yourself)
# - VAT calculation: price * (100 + rate) / 100
# ============================================

def calculate_vat(price, vat_rate):
    """Calculate price including VAT.
    
    Args:
        price: Original price before tax
        vat_rate: VAT rate as percentage (e.g., 10 for 10%)
        
    Returns:
        Final price including VAT
    """
    return price * (100 + vat_rate) / 100


orders = [10, 30, 70]

# Process each order and apply VAT
for order in orders:
    final_amount = calculate_vat(order, 10)
    print(f"Original: ${order} | Final with VAT: ${final_amount:.2f}")
