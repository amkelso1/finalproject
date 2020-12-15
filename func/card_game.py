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
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suit = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        self.deck = []
        for i in suit:
            for j in rank:
                self.deck.append(j + ' of ' + i)

    def reset_game(self, reset_game):
        pass

    def remove_card_from_deck(self, remove_card):
        self.deck.remove(remove_card)

    def start_game(self, game_name):
        name = game_name
        start_message = 'Welcome To ' + name + '...\nDealing your cards...\n'
        print(start_message)
