#! python

import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from glob import glob
import pandas as pd
# from json import load, dumps
import json

from py import get_settings
from form_general import Form
from page import Page
from page_status import Status
from page_influence import Influence
from page_main import MainPage

class App:
    """The main LifeTracker application."""
    def __init__(self, master):
        """Instantiates the application with the specified layout.

        Attributes:
            self.master: The root Tk instance
            self.saveloc: The path to the directory where data files will be saved
            self.nb: The ttk.Notebook widget for organizing pages of the app
            self.main: The 'main' page of entry options
            self.influence: The page of entries that generally influence one's state
            self.status: The page of entries for updating one's state
            self.menu_frame: The tk.Frame where the menu is held
            self.file_button, self.edit_button: Buttons on the menu
        """
        self.master = master
        self.saveloc = get_settings()  #saveloc
        self.s = ttk.Style()
        self.s.configure('TButton', width=25)
        self.s.configure('TEntry', width=40)
        self.s.configure('Prefs.TButton', width=10)
        # self.s.configure('Prefs.TEntry', width=80)

        self.add_menu()
        self.master.rowconfigure(0, pad=10)

        self.nb = ttk.Notebook(self.master)
        self.main = MainPage(self.nb)    # Page()
        self.influence = Influence(self.nb)   # Page()
        self.status = Status(self.nb) # Page()

        self.nb.add(self.main, text='Main')
        self.nb.add(self.influence, text='Influences')
        self.nb.add(self.status, text='Status')
        self.nb.grid(row=1, column=0)

    def add_menu(self):
        self.menubar = tk.Menu(self.master, tearoff=0)
        self.master.config(menu=self.menubar)

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Export data to CSV...", command=self.export,
            underline=1)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="About LifeTracker", command=self.about,
            underline=0)
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Preferences...", command=self.preferences,
            underline=0)

        self.menubar.add_cascade(label="File", underline=0, menu=self.filemenu)
        self.menubar.add_cascade(label="Edit", underline=0, menu=self.editmenu)

    def export(self):
        """Gather data files, combine into Pandas data frame, save to .csv file.

        Retrieves all files starting with 'data-' from the data directory.
        Reads each one and appends it to a dictionary.
        Stringifies into a JSON object.
        Reads JSON object into a pandas data frame.
        Writes this data frame to a file of the user's choice, using tkinter.filedialog.asksaveas().
        """
        data = {}
        index = 0
        datafiles = glob(self.saveloc+'/data-*')
        for d in datafiles:
            with open(d, 'r') as dfile:
                dfile_data = json.load(dfile)
                # dfile_data["tags"] = ', '.join(dfile_data["tags"])
                data[index] = dfile_data
                index += 1
        datajson = json.dumps(data)
        datapd = pd.read_json(datajson, orient='index')
        outfile = filedialog.asksaveasfilename(initialdir = '/', title = 'Save as...',
            defaultextension='.csv', filetypes = (('csv files', '*.csv'), ('all files', '*.*')))
        datapd.to_csv(outfile, index=False)

    def browse_directory(self):
        """Shorthand function for allowing user to select a directory.

        Returns the user's choice.
        """
        directory = filedialog.askdirectory(initialdir='/', title='Select folder...')
        return(directory)

    def preferences(self):
        """Window with program behavior options for the user to determine.

        Currently, this allows users to set an alternate location to save
        data files for the current session.
        This will be changed to perseverate across sessions, as well as having
        more options, as the program evolves.
        """
        self.preferences_window = tk.Toplevel()
        self.preferences_window.title('Edit Preferences')
        prefs = tk.Frame(self.preferences_window)
        ttk.Label(prefs, text='Save data files to:').pack(side='left', padx=7)
        self.data_dir = tk.StringVar()
        self.data_dir.set(self.saveloc)
        self.enter_data_dir = ttk.Entry(prefs, width=35, textvariable=self.data_dir)
        self.enter_data_dir.pack(side='left')
        browse = ttk.Button(prefs, text='Browse...', style='Prefs.TButton', command=self.set_data_dir)
        browse.pack(side='left', padx=2)
        buttons = tk.Frame(self.preferences_window)
        # I just want to center each button within its column
        cancelframe = tk.Frame(buttons)
        applyframe = tk.Frame(buttons)
        ttk.Button(cancelframe, text='Cancel', style='Prefs.TButton', command=self.close_window).pack(anchor='center')
        ttk.Button(applyframe, text='Apply', style='Prefs.TButton', command=self.save_prefs).pack(anchor='center')
        cancelframe.grid(row=0, column=0, padx=20)
        applyframe.grid(row=0, column=1, padx=20)
        topspacer = tk.Frame(self.preferences_window)
        topspacer.pack(pady=7)
        prefs.pack(padx=1)
        midspacer = tk.Frame(self.preferences_window)
        midspacer.pack(pady=11)
        buttons.pack(pady=6)

    def set_data_dir(self):
        """Ask for user's preference on the directory where data files will be saved."""
        usrdir = self.browse_directory()
        self.data_dir.set(usrdir)

    def save_prefs(self):
        """Save the preferences for the current session."""
        settings = {}
        self.saveloc = self.enter_data_dir.get()
        settings['saveloc'] = self.saveloc

        s = json.dumps(settings)
        while True:
            try:
                with open('usrsettings/settings.json', 'w') as f:
                    f.write(s)
                    break
            except FileNotFoundError:
                os.mkdir('usrsettings')
        messagebox.showinfo('Success', 'Your preferences have been saved.')

    def close_window(self):
        self.master.destroy()

    def about(self):
        with open('LICENSE', 'r') as lic:
            mit_text = lic.read()
        self.about_window = tk.Toplevel()
        self.about_window.title("About LifeTracker")
        about_box = tk.Text(self.about_window, height=50, width=60, wrap='word')
        about_box.insert('1.0', "LifeTracker is currently in active development.\n")
        about_box.insert('end', "Find the project's repository at https://github.com/cranndarach/lifetracker\n\n")
        about_box.insert('end', mit_text)
        about_box.config(state='disabled')
        about_box.grid(row=0, padx=15, pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("LifeTracker")
    app = App(root)
    root.mainloop()
