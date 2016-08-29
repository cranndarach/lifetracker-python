#! python

import tkinter as tk
from tkinter import ttk

class Page(tk.Frame):
    def __init__(self):
        super(Page, self).__init__()
        # self.master = master
        # self.nb = notebook
        # self.title = tab_text
        self.rowmaster = 0
        self.row = 0
        self.colmaster = 0
        self.col = 0
        # self.nb.add(self, title=self.title)


    def count(self):
        self.rowmaster += 1
        self.row = int(self.rowmaster/3) + 1
        self.colmaster += 1
        self.col = self.colmaster%3

    def new_button(self, txt, cmd):
        btn = ttk.Button(self, text=txt, command=cmd)
        btn.grid(row=self.row, column=self.col)
        self.count()
