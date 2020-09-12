import unittest
from ..data_structures.card import Card


class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.default_card = Card(suit='clubs',
                                 value='A',
                                 )

    def test_card_knows_its_color(self):
        observed_color = self.default_card.get_color()
        expected_color = 'black'
        self.assertEqual(observed_color, expected_color)

    def test_card_can_be_played_appropriately(self):
        lead_card = Card(suit='clubs',
                         value='9',
                         )
        is_playable = self.default_card.can_be_played_on(lead_card)
        self.assertTrue(is_playable)

        lead_card = Card(suit='spades',
                         value='9',
                         )
        is_playable = self.default_card.can_be_played_on(lead_card)
        self.assertFalse(is_playable)

    def test_card_knows_who_beats_it(self):
        worst_card = Card(suit='clubs',
                          value='9')
        better_card = Card(suit='clubs',
                           value='10')
        self.assertTrue(better_card.beats(worst_card))


if __name__ == '__main__':
    unittest.main()
