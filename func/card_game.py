"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""


class CardGame:
    """CardGame basics"""

    def create_deck(self):
        # function for creating a proper 52 card deck
        card_key = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        card_symbol = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        deck = []
        for i in card_symbol:
            for j in card_key:
                deck.append(j + ' of ' + i)
        return deck

    def reset_game(self):
        pass

    def remove_card_from_deck(self):
        pass

