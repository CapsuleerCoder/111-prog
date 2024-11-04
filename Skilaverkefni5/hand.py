
class Hand:
    '''
    
    '''
    NUMBER_OF_CARDS = 13

    def __init__(self):
        self.cards = []

    def __str__(self):
        if len(self.cards) == 0:
            return "Empty"
        else:
            return " ".join(str(card) for card in self.cards).rstrip() + " "
    
    def add_card(self, card):
        if len(self.cards) < Hand.NUMBER_OF_CARDS:
            self.cards.append(card)