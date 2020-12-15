"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Card game class for basic card game functions
"""


class CardGame:
    """CardGame basics"""

    def __init__(self):
        # function for creating a proper 52 card deck
        card_key = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_symbol = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.deck = []

        for i in card_symbol:
            for j in card_key:
                self.deck.append(j + ' of ' + i)

    def reset_game(self, reset_game):
        pass

    def remove_card_from_deck(self, remove_card):
        self.deck.remove(remove_card)



