class invalidChaiError(Exception):
    pass


def bill(flavor, cups):
    menu = {"Ginger": 30, "Lemon": 25, "Honey": 35}

    try:
        if flavor not in menu:
            raise invalidChaiError(f"Invalid chai flavor: {flavor}")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"{cups} cups {flavor} chai : ${total}")

    except invalidChaiError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")

    finally:
        print("Thank you for visiting!")


print("-------------------------")

bill("Lemon", 2)

print("-------------------------")

bill("Ginger", "two")

print("-------------------------")

bill("Mint", 3)

print("-------------------------")