class chai_order:

    def __init__(
        self,
        tea_type,
        sweetness,
        size,
    ):
        # INITIALIZING INSTANCE ATTRIBUTES
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(order_data["type"], order_data["sweetness"], order_data["size"])

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split(",")
        return cls(tea_type, sweetness, size)


class chai_utils:

    @staticmethod
    def is_valid_size(size):
        return size in ["small", "medium", "large", "grande"]


print(chai_utils.is_valid_size("medium"))


order1 = chai_order("Lemon", "Medium", "Large")
print(order1.__dict__)


order2_dict = chai_order.from_dict(
    {"type": "ginger", "sweetness": "low", "size": "grande"}
)
print(order2_dict.__dict__)


order3_string = chai_order.from_string("Cardamom, high, small")
print(order3_string.__dict__)
