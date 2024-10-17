#Water Bottle

class WaterBottle:
    def __init__(self, max_capacity=5, current_contents = 0):
        self.max_capacity = float(max_capacity)
        self.current_contents = float(current_contents)

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
    

bottle = WaterBottle(5)
print(f"Bottle max capacity: {bottle.max_capacity}L.")

bottle.fill()
print(f"Currently holding {bottle.current_contents}L of water.")

sip = bottle.drink(3.7)
print(f"Received {sip} liters.")

print(bottle)