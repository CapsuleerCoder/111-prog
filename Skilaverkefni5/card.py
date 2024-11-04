


class Card():
    
    RANK_DICT = {"J" : 11, "Q" : 12, "K" : 13, "A" : 14}

    def __init__(self, rank, suit):
        RANK_DICT = {"J" : 11, "Q" : 12, "K" : 13, "A" : 14}
        if type(rank) == str:
            if rank in RANK_DICT:
                self.rank = RANK_DICT.get(rank)
            else:
                self.rank = int(rank)
        else:
            self.rank = rank
            
        self.suit = suit

    def __str__ (self):
        if self.rank <= 10:
            rank_val = str(self.rank)
        else:
            rank_val = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}[self.rank]
        return f"{rank_val:>2}{self.suit}"
