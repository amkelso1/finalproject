"""
Author: Alex Kelso
Date: 11/28/2020
Program: BlackJack.py
Purpose: Provide a full working game of black jack with a dealer and player capabilities
"""

from func import black_jack_func as bjfunc


game = bjfunc.BlackJack()
game.start_game()
game.deal()


