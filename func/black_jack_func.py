"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

import random
from func import card_game as cd


class BlackJack(cd.CardGame):

    # display game start messages
    def start_game(self):
        start_messege = "Welcome To BlackJack...\nDealing your cards...\n"
        print(start_messege)
        return start_messege

    # function to deal first two cards and keep a total of hand
    def deal_hand(self):
        hand = []
        deck = cd.CardGame.create_deck(self)
        total = 0
        for i in range(2):
            card_drawn = random.choice(list(deck))
            hand.append(card_drawn)
            if 'J' in card_drawn or 'Q' in card_drawn or 'K' in card_drawn:
                total = total ++ 10
            elif 'A' in card_drawn:
                if total <= 10:
                    total = total ++ 11
                else:
                    total = total ++ 1
            elif any(char.isdigit() for char in card_drawn):
                total = total ++ int(card_drawn[0])
        print('Your Current Hand: ', hand)
        print('Your Hand\'s Total: ', total)
        if total == 21:
            print('HECK YEAH! WINNER!!!')

    def hit(self):
        print('Would you like to hit? Yes or No?')




