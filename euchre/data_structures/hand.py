class Hand:

    def __init__(self, cards):  # cards a list
        self.cards = cards

    def Remove_card(self, card):  # Removes a card from your hand if it is playable
        if Card.Is_playable(card):
            return cards.remove(card)

    def Add_card(self, card):  # Adds a card to your hand
        return cards.append(card)


if __name__ == '__main__':
    H = Hand([])
