class tea_leaves:

    def __init__(self, age):
        self._age = age  # Private attribute

    @property
    def age(self):
        return self._age + 3

    @age.setter
    def age(self, age_value):
        if 1 <= age_value <= 5:
            self._age = age_value
        else:
            raise ValueError("❌ Age must be between 1 and 5 years.")
        
        
tea = tea_leaves(2)
print("Tea leaves age :", tea.age)  # Accessing via property

tea.age = 8
print("Updated tea leaves age :", tea.age)  # Accessing via property