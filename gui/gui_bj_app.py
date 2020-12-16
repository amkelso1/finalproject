"""
Author: Alex Kelso
Date: 12/14/2020
program: gui_bj_app.py
purpose: create a graphical interface for blackjack program
"""
import tkinter as tk
from func import black_jack_func as bj
import os


window = tk.Tk()

box1 = tk.Canvas(window, width=800, height=600)
box1.pack()

bg = tk.Canvas(window, bg='#36373D')
bg.place(relwidth=1, relheight=1)

box2 = tk.Frame(window, bg='#D1DBE6')
box2.place(relwidth=.9, relheight=.9, relx=0.05, rely=0.05)

start = tk.Button(box1, text='Play Game', width=50, padx=100, pady=25, fg='white', bg='#36373D')
start.pack()
deal = tk.Button(box2, text='Deal', padx=10, pady=10, fg='white', bg='#36373D', command=lambda: bj.BlackJack.deal)
deal.pack()
hit = tk.Button(box2, text='Hit', padx=10, pady=10, fg='white', bg='#36373D')
hit.pack()
stand = tk.Button(box2, text='Stand', padx=10, pady=10, fg='white', bg='#36373D')
stand.pack()


window.mainloop()

