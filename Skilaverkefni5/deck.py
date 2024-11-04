import random
from card import Card

class Deck():
    '''
    Deck class, makes a deck of 52 cards,13 each sort or suit
    uses the card class to insert the cards
    has 2 constants, the SUITS_LIST and RANKS
    '''

    SUITS_LIST = ["H", "S", "D", "C"]
    RANKS = list(range(2,15))

    def __init__(self):
        self.deck = []
        for suit in Deck.SUITS_LIST:
            for rank in Deck.RANKS:
                self.deck.append(Card(rank, suit))
    
    def __str__(self):
        '''
        prints the deck using a enumerate list, Prints a new line 
        after every 13 cards. has some spaces and stuff for format reasons
        '''
        deck_str = ""
        for i, card in enumerate(self.deck, start = 1):
            deck_str += str(card) + " "
            if i % 13 == 0:
                deck_str += "\n"
        return deck_str.rstrip() + " "
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        '''pops the first card and returns it '''
        return self.deck.pop(0)