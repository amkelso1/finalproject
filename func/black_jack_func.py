"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

import random
from func import card_game as cd


class BlackJack(cd.CardGame):
    """Subclass BlackJack from CardGame"""
    def __init__(self):
        self.hand = []
        self.d_hand = []
        self.master_deck = cd.CardGame()
        self.total = 0
        self.d_total = 0

    # display game start messages
    def start_game(self):
        start_message = "Welcome To BlackJack...\nDealing your cards...\n"
        print(start_message)
        return start_message

    # gets the value of the player's card
    def card_value(self, card_drawn, d_card_drawn):
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
        # for loop for the first two cards dealt to player
        for i in range(2):
            card_drawn = random.choice(list(self.master_deck.deck))
            self.master_deck.remove_card_from_deck(card_drawn)
            self.hand.append(card_drawn)
            d_card_drawn = random.choice(list(self.master_deck.deck))
            self.master_deck.remove_card_from_deck(d_card_drawn)
            self.d_hand.append(d_card_drawn)
            self.card_value(card_drawn, d_card_drawn)
            # print(self.d_hand)  # for testing purposes
            # print(len(self.master_deck.deck))  # verifying card removal from deck
        print('Dealer\'s Hand: {} | {}'.format('Face Down', self.d_hand[1]))
        print('Dealer Hand\'s Total: ', self.d_total, '\n')  # for testing purposes only
        print('Your Current Hand: {} | {}'.format(self.hand[0], self.hand[1]))
        print('Your Hand\'s Total: ', self.total)

        # hit or not hit prompt and functionality
        y = ['Yes', 'yes', 'y']
        n = ['No', 'no', 'n']
        # Choice to hit or keep hand

        try:
            if self.total == 21 or self.d_total == 21:
                self.instant_win()
            else:
                print('\nWould you like to hit? yes or no?')
                answer = str(input())
                # follow up loop for hit or no hit choice
                while answer not in n:
                    if answer in y:
                        card_drawn = random.choice(list(self.master_deck.deck))
                        self.master_deck.remove_card_from_deck(card_drawn)
                        self.hand.append(card_drawn)
                        self.card_value(card_drawn, '0 of Null')  # work around for dealer not drawing a card too early
                        print('\nYour Hand: ', end="")
                        for i in self.hand:
                            print(i, ' | ', end='')
                        print('\nYour Hand\'s Total: ', self.total)
                        print('\nDealer\'s Hand\'s total: ', self.d_total)
                        self.yes_hit_score()
                        answer = str(input())
                while self.d_total < 16:
                    d_card_drawn = random.choice(list(self.master_deck.deck))
                    self.master_deck.remove_card_from_deck(d_card_drawn)
                    self.d_hand.append(d_card_drawn)
                    self.card_value('0 of Null', d_card_drawn)  # '0 of Null' so that player doesnt draw extra cards
                self.no_hit_score_score()
                print('\nDealer\'s Hand: ', end="")
                for i in self.d_hand:
                    print(i, ' | ', end='')
                print('\nDealer Hand\'s Total: ', self.d_total) # dealer score for testing purposes
                print('\nYour Hand: ', end="")
                for i in self.hand:
                    print(i, ' | ', end='')
                print('\nYour Hand\'s Total: ', self.total)
                print('\nDealer\'s Hand\'s total: ', self.d_total)

                # calculate a winner
        except ValueError:
            print('Please Retry')

    # function for dealer and/or player win on initial cards dealt
    def instant_win(self):
        if self.total == 21:
            if self.d_total != 21:
                print('HECK YEAH! WINNER!!!')
            else:
                print('It\'s a Push!')
        elif self.d_total == 21:
            print('Too Bad, Dealer Wins')

    # function for win/loss possibilities
    def no_hit_score_score(self):
        if self.total <= 21 and self.d_total <= 21:
            if self.total == 21 and self.d_total == 21:
                print('It\'s a Push!')
            elif self.d_total == self.total:
                print('It\'s a Push')
            elif self.total == 21:
                print('HECK YEAH! WINNER!!!')
            elif self.total <= 21 and self.d_total <= 21:
                if self.total > self.d_total:
                    print('HECK YEAH! WINNER!!!')
                if self.d_total > self.total:
                    print('Too Bad, Dealer Wins')
        elif self.total > 21:
            print('It\'s a Bust!')
        elif self.d_total > 21:
            print('You Won! Dealer Bust!')

    def yes_hit_score(self):
        if self.total > 21:
            print('It\'s a Bust!')






