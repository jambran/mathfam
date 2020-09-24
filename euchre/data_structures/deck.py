from .card import Card


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
