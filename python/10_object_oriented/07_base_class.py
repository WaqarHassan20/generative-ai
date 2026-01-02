class chai:

    def __init__(self, type_, strength):
        self.type = type_  # Each chai instance has its own type
        self.strength = strength  # Each chai instance has its own strength

        # but this approach is doing the code reptition of parent class


# class ginger_chai(chai):

#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level  # New attribute specific to ginger_chai


class ginger_chai(chai):
    
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level  # New attribute specific to ginger_chai