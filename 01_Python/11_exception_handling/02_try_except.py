chai_menu = {"Lemon": 2.5, "Honey": 3.0, "Ginger": 3.5}

try:
    chai_menu["Oolong"]
except KeyError:
    print("Oolong chai is not available in menu.")


print("Continuing with rest of program...")