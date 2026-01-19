# ============================================
# Discount Calculation Utilities
# ============================================
# KEY POINTS:
# - Functions to calculate various types of discounts
# - Percentage-based discounts
# - Flat amount discounts
# - Seasonal and loyalty discounts
# ============================================

def calculate_percentage_discount(price, percentage):
    """
    Calculate discount based on percentage.
    
    Args:
        price (float): Original price
        percentage (float): Discount percentage (e.g., 10 for 10%)
    
    Returns:
        float: Discounted price
    
    Example:
        >>> calculate_percentage_discount(100, 10)
        90.0
    """
    if percentage < 0 or percentage > 100:
        raise ValueError("Percentage must be between 0 and 100")
    
    discount_amount = price * (percentage / 100)
    return price - discount_amount


def calculate_flat_discount(price, flat_amount):
    """
    Calculate discount with flat amount.
    
    Args:
        price (float): Original price
        flat_amount (float): Flat discount amount
    
    Returns:
        float: Discounted price (minimum 0)
    
    Example:
        >>> calculate_flat_discount(100, 15)
        85.0
    """
    discounted_price = price - flat_amount
    return max(0, discounted_price)  # Ensure non-negative


def apply_loyalty_discount(price, is_member, member_discount=15):
    """
    Apply loyalty member discount.
    
    Args:
        price (float): Original price
        is_member (bool): Whether customer is a loyalty member
        member_discount (float): Discount percentage for members
    
    Returns:
        float: Final price
    """
    if is_member:
        return calculate_percentage_discount(price, member_discount)
    return price


def bulk_order_discount(quantity, price_per_item):
    """
    Calculate discount based on bulk purchase.
    
    Discount tiers:
    - 10+ items: 5% off
    - 20+ items: 10% off
    - 50+ items: 15% off
    
    Args:
        quantity (int): Number of items
        price_per_item (float): Price per item
    
    Returns:
        float: Total price after bulk discount
    """
    total = quantity * price_per_item
    
    if quantity >= 50:
        return calculate_percentage_discount(total, 15)
    elif quantity >= 20:
        return calculate_percentage_discount(total, 10)
    elif quantity >= 10:
        return calculate_percentage_discount(total, 5)
    
    return total


# Example usage (commented out - uncomment to test)
if __name__ == "__main__":
    # Test percentage discount
    print("Percentage Discount:")
    print(f"₹100 with 10% off = ₹{calculate_percentage_discount(100, 10)}")
    
    # Test flat discount
    print("\nFlat Discount:")
    print(f"₹100 with ₹15 off = ₹{calculate_flat_discount(100, 15)}")
    
    # Test loyalty discount
    print("\nLoyalty Discount:")
    print(f"Member price: ₹{apply_loyalty_discount(100, True)}")
    print(f"Non-member price: ₹{apply_loyalty_discount(100, False)}")
    
    # Test bulk discount
    print("\nBulk Order Discount:")
    print(f"25 items @ ₹10 each = ₹{bulk_order_discount(25, 10)}")
