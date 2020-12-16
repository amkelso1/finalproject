"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

from func import black_jack_func as bj
from func import card_game as cd

blackjack = bj.BlackJack()
cd.CardGame().start_game(game_name='BlackJack')
blackjack.deal()


