"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

import random
from func import card_game as cd


class BlackJack(cd.CardGame):
    """Subclass BlackJack Child of CardGame"""

    def __init__(self):
        super().__init__()
        self.bj_deck = cd.CardGame().deck
        self.hand = []
        self.d_hand = []
        self.total = 0
        self.d_total = 0
        self.again = True
        self.play = True

    # gets the value of the player's and dealer's card / adding them to a separate total
    def card_value(self, card_drawn, d_card_drawn):
        # gets value of player card
        if 'J' in card_drawn or 'Q' in card_drawn or 'K' in card_drawn or '10' in card_drawn:
            self.total += 10
        elif 'A' in card_drawn:
            if self.total <= 10:
                self.total += 11
            else:
                self.total = self.total + 1
        elif any(char.isdigit() for char in card_drawn):
            self.total = self.total + int(card_drawn[0])
        # gets the value of the dealer's card
        if 'J' in d_card_drawn or 'Q' in d_card_drawn or 'K' in d_card_drawn or '10' in d_card_drawn:
            self.d_total = self.d_total + 10
        elif 'A' in d_card_drawn:
            if self.d_total <= 10:
                self.d_total = self.d_total + 11
            else:
                self.d_total = self.d_total + 1
        elif any(char.isdigit() for char in d_card_drawn):
            self.d_total = self.d_total + int(d_card_drawn[0])

    # runs the main gameplay / decision making code
    def deal(self):
        # for loop to draw card and remove from deck as well as print results
        while self.play:
            self.total = 0
            self.d_total = 0
            self.hand = []
            self.d_hand = []
            for i in range(2):
                card_drawn = random.choice(list(self.bj_deck))
                self.bj_deck.remove(card_drawn)
                self.hand.append(card_drawn)
                d_card_drawn = random.choice(list(self.bj_deck))
                self.bj_deck.remove(d_card_drawn)
                self.d_hand.append(d_card_drawn)
                self.card_value(card_drawn, d_card_drawn)
                # print(self.d_hand)  # for testing purposes
            print('____________________________________________')
            print('Dealer\'s Hand: {} | {}'.format('Face Down', self.d_hand[1]))  # prints dealer's hand. one card face down
            # print('Dealer Hand\'s Total: ', self.d_total, '\n')  # for testing purposes only
            print('\nYour Current Hand: {} | {}'.format(self.hand[0], self.hand[1]))
            print('Your Hand\'s Total: ', self.total)

            # answer possibilities
            y = ['Yes', 'yes', 'y']
            n = ['No', 'no', 'n']

            # loop for hit or stand
            while self.again:
                # check for win from first two cards
                if self.total == 21:
                    print('\nDealer\'s Hand: ', end="")
                    for i in self.d_hand:
                        print(i, ' | ', end='')
                    self.instant_win()
                    self.again = False

                # input validation for hit again question
                repeat = True
                while repeat:
                    answer = (input('\nWould you like to hit? yes or no?'))
                    if answer in y or answer in n:
                        repeat = False
                    else:
                        print('invalid, please try again')
                        repeat = True

                    # adds card to hand and prints hand(yes, hit option)
                    if answer in y:
                            print('____________________________________________')
                            print('Dealer\'s Hand: {} | {}'.format('Face Down', self.d_hand[1]))
                            card_drawn = random.choice(list(self.bj_deck))
                            self.bj_deck.remove(card_drawn)
                            self.hand.append(card_drawn)
                            self.card_value(card_drawn, '0 of Null')  # 0 of null - so dealer doesnt draw again
                            print('\nYour Hand: ', end="")
                            for i in self.hand:
                                print(i, ' | ', end='')
                            print('\nYour Hand\'s Total: ', self.total)
                            # print('\nDealer\'s Hand\'s total: ', self.d_total) for testing dealers total
                            self.yes_hit_score()
                    # ends turn and draws final cards for dealer --> prints results
                    elif answer in n:
                        while self.d_total < 17:
                            d_card_drawn = random.choice(list(self.bj_deck))
                            self.bj_deck.remove(d_card_drawn)
                            self.d_hand.append(d_card_drawn)
                            self.card_value('0 of Null', d_card_drawn)  # '0 of Null' so that player doesnt draw
                        print('\nDealer\'s Hand: ', end="")
                        for i in self.d_hand:
                            print(i, ' | ', end='')
                        print('\nDealer Hand\'s Total: ', self.d_total)  # dealer score for testing purposes
                        print('\nYour Hand: ', end="")
                        for i in self.hand:
                            print(i, ' | ', end='')
                        print('\nYour Hand\'s Total: ', self.total)
                        self.no_hit_score()
                        self.again = False

            # input validation for play again question
            repeat = True
            while repeat:
                again_answer = input('\nWould you like to play again? \'y\' or \'n\'\n')
                if again_answer in y:
                    self.play = True
                    self.again = True
                    repeat = False
                    self.bj_deck = cd.CardGame().deck
                elif again_answer in n:
                    print('Goodbye!')
                    self.again = False
                    self.play = False
                    repeat = False
                else:
                    repeat = True
                    print('Invalid Answer, Please try again.')

    # function for dealer and/or player win on initial cards dealt
    def instant_win(self):
        if self.total == 21:
            if self.d_total != 21:
                print('\n\nHECK YEAH! WINNER!!!')
                self.again = False
            else:
                print('\nIt\'s a Push!')
                self.again = False

    # function for win/loss possibilities
    def no_hit_score(self):
        if self.total <= 21 and self.d_total <= 21:
            if self.total == 21 and self.d_total == 21:
                print('\nIt\'s a Push!')
                self.again = False
            elif self.d_total == self.total:
                print('\nIt\'s a Push')
                self.again = False
            elif self.total == 21:
                print('\nHECK YEAH! WINNER!!!')
                self.again = False
            elif self.total <= 21 and self.d_total <= 21:
                if self.total > self.d_total:
                    print('\nHECK YEAH! WINNER!!!')
                    self.again = False
                if self.d_total > self.total:
                    print('\nToo Bad, Dealer Wins')
                    self.again = False
        elif self.total > 21:
            print('\nIt\'s a Bust!')
            self.again = False
        elif self.d_total > 21:
            print('\nYou Won! Dealer Bust!')
            self.again = False

    # checks score after yes, hit option
    def yes_hit_score(self):
        if self.total > 21:
            print('\nIt\'s a Bust!')
            self.again = False
        elif self.total == 21:
            if self.d_total != 21:
                print('\nHECK YEAH! WINNER!!!')
                self.again = False
            else:
                print('\nIt\'s a Push!')
                self.again = False
