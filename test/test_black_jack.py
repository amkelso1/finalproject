import unittest
from func import black_jack_func as bj
from func import card_game as cd


class TestDeck(unittest.TestCase):
    def test_deck_size(self):
        self.assertEqual(len(bj.BlackJack().bj_deck), 52)

    def test_card_in_deck(self):
        self.assertIn('3 of Hearts', bj.BlackJack().bj_deck)

    def test_card_not_in_deck(self):
        self.assertNotIn('12 of Spades', bj.BlackJack().bj_deck)

    def test_remove_card_from_deck(self):
        deck = bj.BlackJack().bj_deck
        deck.remove('3 of Spades')
        self.assertNotIn('3 of Spades', deck)  # check for string removal
        self.assertEqual(len(deck), 51)  # Check for size of deck change


"""
    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(True, False)
"""

if __name__ == '__main__':
    unittest.main()
