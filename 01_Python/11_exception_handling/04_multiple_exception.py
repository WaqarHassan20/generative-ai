def process_order(item, quantity):
    try:
        price = {"ginger": 3.0}[item]
        cost = price * quantity
        print("Total cost : ", cost)
    except KeyError:
        print("Item not found in price list.")
    except TypeError:
        print("Invalid type for quantity. Please provide a number.")


ginger = process_order("ginger", 2)  # Valid case

print("Total ginger cost : ", ginger)

cardamom = process_order("cardamom", 2)  # KeyError case

print("Total cardamom cost : ", cardamom)