"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

import random
from func import card_game as cd


class BlackJack(cd.CardGame):
    def __init__(self):
        self.hand = []
        self.master_deck = cd.CardGame()
        self.total = 0

    # display game start messages
    def start_game(self):
        start_messege = "Welcome To BlackJack...\nDealing your cards...\n"
        print(start_messege)
        return start_messege

    def card_value(self, card_drawn):
        if 'J' in card_drawn or 'Q' in card_drawn or 'K' in card_drawn or '10' in card_drawn:
            self.total = self.total + + 10
        elif 'A' in card_drawn:
            if self.total <= 10:
                self.total = self.total + 11
            else:
                self.total = self.total + 1
        elif any(char.isdigit() for char in card_drawn):
            self.total = self.total + int(card_drawn[0])

    # function to deal first two cards and keep a total of hand
    def deal(self):
        # for loop for the first two cards dealt to player
        for i in range(2):
            card_drawn = random.choice(list(self.master_deck.deck))
            self.hand.append(card_drawn)
            self.card_value(card_drawn)
        print('Your Current Hand: {} | {}'.format(self.hand[0], self.hand[1]))
        print('Your Hand\'s Total: ', self.total)
        if self.total == 21:
            print('HECK YEAH! WINNER!!!')
        # hit or not hit prompt and functionality
        y = ['Yes', 'yes', 'y']
        n = ['No', 'no', 'n']
        # Choice to hit or keep hand
        print('\nWould you like to hit? yes or no?')
        try:
            answer = str(input())
            # follow up loop for hit or no hit choice
            while answer not in n:
                if answer not in y:
                    print('Please give valid answer')
                else:
                    card_drawn = random.choice(list(self.master_deck.deck))
                    self.hand.append(card_drawn)
                    self.card_value(card_drawn)
                    print('Your Current Hand: ', end="")
                    # for loop for printing added cards and values
                    for i in self.hand:
                        print(i, ' | ',  end='')
                    print('\nYour Hand\'s Total: ', self.total)
                    if self.total > 21:
                        print('Too Bad, It\'s a Bust!')
                    elif self.total == 21:
                        print('HECK YEAH! WINNER!!!')
                    else:
                        print('\nAgain?...\n')
                answer = str(input())

        except ValueError:
            print('Please Retry')








