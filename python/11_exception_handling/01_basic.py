# Index Error Example
def get_item_from_list(items, index):
    try:
        return items[index]
    except IndexError:
        return f"❌ Error: Index {index} is out of range for the list."


# Zero Division Error Example
def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "❌ Error: Cannot divide by zero."


# Value Error Example
def convert_to_integer(value):
    try:
        return int(value)
    except ValueError:
        return f"❌ Error: Cannot convert '{value}' to an integer."


# TypeError Example
def add_numbers(a, b):
    try:
        return a + b
    except TypeError:
        return (
            f"❌ Error: Cannot add values of different types: {type(a)} and {type(b)}."
        )


# NameError Example
def use_undefined_variable():
    try:
        # This intentionally references an undefined variable to demonstrate NameError
        return undefined_variable + 10  # type: ignore
    except NameError:
        return "❌ Error: The variable 'undefined_variable' is not defined."


# KeyError Example
def get_value_from_dict(data_dict, key):
    try:
        return data_dict[key]
    except KeyError:
        return f"❌ Error: Key '{key}' does not exist in the dictionary."


# Examples of using the above functions
if __name__ == "__main__":
    # Index Error Example
    fruits = ["apple", "banana", "cherry"]
    print(get_item_from_list(fruits, 5))  # Out of range index

    # Zero Division Error Example
    print(divide_numbers(10, 0))  # Division by zero

    # Value Error Example
    print(convert_to_integer("abc"))  # Invalid integer conversion
    print(
        "Valid Integer conversion : ", convert_to_integer("123")
    )  # Valid integer conversion

    # TypeError Example
    print(add_numbers(10, "20"))  # Adding different types
    print("Valid types adding : ", add_numbers(10, 20))  # Adding same types

    # NameError Example
    print(use_undefined_variable())  # Using undefined variable

    # KeyError
    sample_dict = {"name": "Alice", "age": 30}
    print(get_value_from_dict(sample_dict, "address"))  # Non-existent key
