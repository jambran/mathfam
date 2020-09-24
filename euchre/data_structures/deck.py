from .card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['Spades', 'Clubs', 'Diamonds', 'Hearts']:
            for v in range(9, 15):
                self.cards.append(Card(s, v))

    def show(self):  # needs to be included in Card for this function to work
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1): # reverses the list
            r = random.randomint(0,i) # picks random number left of the current position
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i] #swaps position of cards in position i and r
    def draw(self):
        return self.cards.pop()
    """
    - Features
		○ Cards - dictionary (mapping (index of shuffle to Card))?
	- Functions
		○ Add_card(card)
		○ Remove_card()
		○ Shuffle()
			§ Generate list of random numbers (same size as num cards) - use these indices for the order
		○ Refresh()?
    """
