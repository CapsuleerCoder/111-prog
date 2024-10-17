#Water Bottle

# Kemst 75% í gegn, eitthvað eitt edge case sem er að angra Kattiss ennþá

class WaterBottle:
    def __init__(self, max_capacity=5):
        self.max_capacity = float(max_capacity)
        self.current_contents = 0.0

    def fill(self):
        self.current_contents = self.max_capacity

    def drink(self, amount):
        if amount <= 0 or self.current_contents == 0:
            return 0
        elif amount >= self.current_contents:
            amount = self.current_contents
            self.current_contents = 0
            return amount
        else:
            self.current_contents -= amount
            return amount

    def __str__(self):
        return f"The bottle currently holds {self.current_contents:.1f}L of water."