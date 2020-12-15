"""
Author: Alex Kelso
Date: 12/14/2020
program: gui_bj_app.py
purpose: create a graphical interface for blackjack program
"""
import tkinter as tk
from func import black_jack_func as bj
import os


class BlackJackGUI:
    """GUI for blackjack game"""
    def __init__(self, window):
        self.bj = bj()
        window.title('BlackJack')
        self.button_start = tk.Button(window, height=2, width=10, text='Start', command=lambda: self.start_game())
        self.button_start.pack()

    main = tk.Tk()

    box1 = tk.Canvas(main, width=800, height=600)
    box1.pack()

    bg = tk.Canvas(main, bg='#36373D')
    bg.place(relwidth=1, relheight=1)

    box2 = tk.Frame(main, bg='#D1DBE6')
    box2.place(relwidth=.8, relheight=.8, relx=0.1, rely=0.1)

    start = tk.Button(box2, text='Play Game', padx=10, pady=10, fg='white', bg='#36373D')
    start.pack()

    main.mainloop()

    hit = tk.Button()