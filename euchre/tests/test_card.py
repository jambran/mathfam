import unittest
from euchre.data_structures.card import Card


class TestCard(unittest.TestCase):

    def setUp(self) -> None:
        self.default_card = Card(suit='clubs',
                                 rank='A',
                                 )

    def test_card_knows_its_color(self):
        observed_color = self.default_card.get_color()
        expected_color = 'Black'
        self.assertEqual(observed_color, expected_color)



if __name__ == '__main__':
    unittest.main()
