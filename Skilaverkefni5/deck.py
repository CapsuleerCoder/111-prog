import random
from card import Card

class Deck():

    SUITS_LIST = ["H", "S", "D", "C"]
    RANKS = list(range(2,15))

    def __init__(self):
        self.deck = []
        for suit in Deck.SUITS_LIST:
            for rank in Deck.RANKS:
                self.deck.append(Card(rank, suit))
    
    def __str__(self):
        deck_str = ""
        for i, card in enumerate(self.deck, start = 1):
            deck_str += str(card) + " "
            if i % 13 == 0:
                deck_str += "\n"
        return deck_str.rstrip()
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)