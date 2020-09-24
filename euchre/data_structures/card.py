class Card:

    def __init__(self, rank, suit):  # initializes card with rank and suit attributes
        self.rank = rank
        self.suit = suit

    def Get_rank(self):  # gets the rank
        return self.rank

    def Get_suit(self):  # gets the suit
        return self.suit

    def show(self):
        print("{} or {}".format(self.rank, self.suit))

    def Get_color(self):  # gets the color
        if self.Get_suit() == 'Hearts' or self.Get_suit() == 'Diamonds':
            return 'Red'
        else:
            return 'Black'

    def Is_playable(self):
        return None  # should return True if card either has same suit as first card played or no card in hand matches
        # the suit of first card played.  Should be a function of Hand?

    def Compare_whos_best(self,
                          played_cards):  # played_cards: an ordered list(?) of the the 4 cards played in the trick
        ranks = ['9', '10', 'J', 'Q', 'K', 'A']
        return None  # Compares all four cards played in a hand and determines the winner.
        # Should this be a function of something else?


if __name__ == '__main__':
    C = Card(rank='', suit='')
