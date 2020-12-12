"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

from random import randint


def create_deck():
    # function for creating a proper 52 card deck
    cards_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'A', 'J', 'Q', 'K']
    card_symbol = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    deck = []
    for i in card_symbol:
        for j in cards_value:
            deck.append(j + ' of ' + i)
    return deck


def start_game():
    print("Welcome To BlackJack...")
    print("Dealing your cards...\n")


def deal_first_hand():
    pass


def black_back_game():
    start_game()
    deal_first_hand()


if __name__ == "__main__":
    black_back_game()
    create_deck()
