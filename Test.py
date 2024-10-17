

class Wizard:
    def __init__(self, name, party, spells=None):
        self.name = name
        self.party = party
        self.spells = spells
        if self.spells is None:
            self.spells = []

    def __str_(self):
        return f"Name: {self.name}, currently a member of {self.party}, known spells are: {self.spells}."

# protagonistn=Wizard
# name="Vaarsuvius",
# party="the Order of the Stick",
# spells=["Magic Missile", "Fireball", "Expeditious Retreat"],
# }
protagonist = Wizard
print(type(protagonist))