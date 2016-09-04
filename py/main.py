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

from form_general import Form
from page import Page

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
        while True:
            try:
                with open('usrsettings/settings.json', 'r') as s:
                    settings = json.load(s)
                self.saveloc = settings['saveloc']
                break
            except FileNotFoundError:
                try:
                    with open('usrsettings/settings.json', 'w+') as s:
                        write_settings = {}
                        write_settings['saveloc'] = 'data'
                        ws = json.dumps(write_settings)
                        s.write(ws)
                        settings = json.load(s)
                    self.saveloc = settings['saveloc']
                    break
                except FileNotFoundError:
                    os.mkdir('usrsettings')
        try:
            with open('usrsettings/presets.json', 'r') as p:
                self.presets = json.load(p)
        except FileNotFoundError:
            pass

        self.master = master
        s = ttk.Style()
        s.configure('TButton', width=25)

        self.nb = ttk.Notebook(self.master)
        self.main = Page()
        self.influence = Page()
        self.status = Page()

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.grid(row=0)
        self.file_button = ttk.Menubutton(self.menu_frame, text="File", underline=0)
        self.file_button.pack(side='left')  #grid(row=0, column=0)
        self.file_button.menu = tk.Menu(self.file_button, tearoff=0)
        self.file_button['menu'] = self.file_button.menu
        self.file_button.menu.add_cascade(label="Export data to CSV...", command=self.export)
        self.edit_button = ttk.Menubutton(self.menu_frame, text="Edit", underline=0)
        self.edit_button.pack(side='left')
        self.edit_button.menu = tk.Menu(self.edit_button, tearoff=0)
        self.edit_button['menu'] = self.edit_button.menu
        self.edit_button.menu.add_cascade(label="Preferences...", command=self.preferences)

        self.main.new_button("Add Event", self.new_event)
        self.main.new_button("Add Task", self.new_task)
        self.main.new_button("Add Simple Entry", self.new_simple)
        self.main.new_button("Add Generic", self.new_everything)

        self.status.new_button("Log Spoon Level", self.update_spoons)
        self.status.new_button("Log Mood", self.update_mood)
        self.status.new_button("Log Health/Symptoms", self.update_health)
        self.status.new_button("Log Pain Level", self.update_pain)
        self.status.new_button("Log Mobility", self.update_mobility)
        self.status.new_button("Log Hunger", self.update_hunger)
        self.status.new_button("Log Headache", self.add_headache)

        self.influence.new_button("Add External Influence", self.new_influence)
        self.influence.new_button("Add Sleep Entry", self.new_sleep)
        self.influence.new_button("Add Coping Mechanism", self.new_copech)
        self.influence.new_button("Record Medicine Taken", self.meds_taken)

        self.nb.add(self.main, text='Main')
        self.nb.add(self.status, text='Status')
        self.nb.add(self.influence, text='Influences')
        self.nb.grid(row=1, column=0)

    def load_presets(self):
        self.presets_page = Page()
        # This will be updated in the future

    # Log a simple entry with few options.
    def new_simple(self):
        self.simple_window = tk.Toplevel()  #tk.Frame()
        # self.simple_tab = self.nb.add(self.simple_window, text="Add Simple Entry")
        # self.nb.add(self.simple_window, text="Add Simple Entry")
        simple = Form(self.simple_window, self.saveloc)
        simple.add_entry('Title:', 'title')
        simple.add_entry('Category:', 'category')
        simple.add_date_time('When:', 'when')
        simple.add_entry('Location:', 'location')
        simple.populate()

    # Log an external influence, something that may impact
    # your state or other variable of interest.
    def new_influence(self):
        self.infl_window = tk.Toplevel()
        self.infl_window.title("Add External Influence")
        infl = Form(self.infl_window, self.saveloc)
        infl.add_entry('Title:', 'title')
        infl.add_entry('Category:', 'category')
        infl.add_date_time('When:', 'when')
        infl.add_scale('Intensity:', 'intensity')
        # infl.add_date_time('End:', 'end')
        infl.add_entry('Location:', 'location')
        infl.populate()

    # Log an event, typically something where
    # you were not the "do-er."
    def new_event(self):
        self.event_window = tk.Toplevel()
        self.event_window.title("New Event")
        event = Form(self.event_window, self.saveloc)
        event.add_entry('Title:', 'title')
        event.add_entry('Category:', 'category')
        event.add_date_time('Start:', 'start')
        event.add_date_time('End:', 'end')
        event.add_entry('Location:', 'location')
        event.add_scale('Mood at start:', 'start_valence')
        event.add_scale('Spoons at start:', 'start_spoons')
        event.add_scale('Mood at end:', 'end_valence')
        event.add_scale('Spoons at end:', 'end_spoons')
        event.populate()

    # Log your "spoon" levels.
    def update_spoons(self):
        self.spoons_window = tk.Toplevel()
        self.spoons_window.title("Log Spoons")
        spoons = Form(self.spoons_window, self.saveloc)
        spoons.add_scale('Spoons:', 'spoons')
        spoons.add_date_time('When:', 'when')
        spoons.populate()

    # Log a task, typically where you are the "do-er."
    def new_task(self):
        self.task_window = tk.Toplevel()
        self.task_window.title("New Task")
        task = Form(self.task_window, self.saveloc)
        task.add_entry('Title:', 'title')
        task.add_entry('Category:', 'category')
        task.add_date_time('Start:', 'start')
        task.add_date_time('End:', 'end')
        task.add_entry('Location:', 'location')
        task.add_scale('Mood at start:', 'start_valence')
        task.add_scale('Spoons at start:', 'start_spoons')
        task.add_scale('Mood at end:', 'end_valence')
        task.add_scale('Spoons at end:', 'end_spoons')
        task.add_scale('Size of task:', 'size')
        task.add_scale('Difficulty of task:', 'difficulty')
        task.add_scale('Progress/completion:', 'progress')
        task.add_scale('Satisfaction/Quality:', 'quality')
        task.add_numeric('Exp gained:', 'exp_gained')
        task.populate()

    # Log times and quality of sleep.
    def new_sleep(self):
        self.sleep_window = tk.Toplevel()
        self.sleep_window.title("New Sleep Entry")
        sleep = Form(self.sleep_window, self.saveloc)
        sleep.add_date_time('Went to bed:', 'sleep_start')
        sleep.add_date_time('Woke up:', 'sleep_end')
        sleep.add_entry('Location:', 'location')
        sleep.add_scale('Mood when you went to bed:', 'start_valence')
        sleep.add_scale('Mood when you woke up:', 'end_valence')
        sleep.add_scale('Quality:', 'quality')
        sleep.populate()

    # Log your mood on various dimensions.
    def update_mood(self):
        self.mood_window = tk.Toplevel()
        self.mood_window.title("Log Mood")
        mood = Form(self.mood_window, self.saveloc)
        mood.add_scale('Valence (higher for better mood):', 'valence')
        mood.add_scale('Worry/anxiety:', 'anxiety')
        mood.add_scale('Tension (emotional or physical):', 'tension')
        mood.add_scale('Focus:', 'focus')
        mood.add_scale('Intensity of mood:', 'mood_intensity')
        mood.add_scale('Energy:', 'energy')
        mood.add_scale('Spoons:', 'spoons')
        mood.add_date_time('When:', 'when')
        mood.add_entry('Location:', 'location')
        mood.populate()

    # Log a coping mechanism used.
    def new_copech(self):
        self.copech_window = tk.Toplevel()
        self.copech_window.title("New Coping Mechanism")
        copech = Form(self.copech_window, self.saveloc)
        copech.add_entry('Coping mechanism used:', 'coping_mech')
        copech.add_entry('Category:', 'category')
        copech.add_entry('Reason (optional):', 'reason')
        copech.add_date_time('When/start:', 'start')
        copech.add_date_time('End (set to same as start if not applicable):', 'end')
        copech.add_scale('Benefit/Improvement:', 'quality')
        copech.add_scale('Mood afterward:', 'valence')
        copech.add_scale('Spoons:', 'spoons')
        copech.add_numeric('Exp gained:', 'exp_gained')
        copech.add_entry('Location:', 'location')
        copech.populate()

    # Log symptoms or other health-related factors.
    def update_health(self):
        self.health_window = tk.Toplevel()
        self.health_window.title("Log Health/Symptoms")
        health = Form(self.health_window, self.saveloc)
        health.add_entry('Trait/Symptom:', 'symptom')
        health.add_entry('Category:', 'category')
        health.add_date_time('When/start:', 'start')
        health.add_date_time('End (set to same as start if not applicable):', 'end')
        health.add_entry('Trigger (if applicable/known):', 'trigger')
        health.add_entry('Your location:', 'location')
        health.add_scale('Intensity of symptom:', 'symptom_intensity')
        health.add_scale('Spoons:', 'spoons')
        health.populate()

    # Log medicine taken.
    def meds_taken(self):
        self.med_window = tk.Toplevel()
        self.med_window.title("Log Medicine Taken")
        med = Form(self.med_window, self.saveloc)
        med.add_entry('Medicine name:', 'med_name')
        med.add_entry('Category:', 'category')
        med.add_entry('Dosage:', 'dosage')
        med.add_entry('Reason for taking (optional):', 'reason')
        med.add_date_time('Start of dose:', 'start')
        med.add_date_time('End of dose (set to same as start if not applicable):', 'end')
        med.add_scale('Benefit/Improvement (leave at 0 if NA/unknown):', 'quality')
        med.populate()

    # Log hunger level.
    def update_hunger(self):
        self.hunger_window = tk.Toplevel()
        self.hunger_window.title("Log Hunger")
        hunger = Form(self.hunger_window, self.saveloc)
        hunger.add_scale('Hunger:', 'hunger')
        hunger.add_date_time('When:','when')
        hunger.populate()

    # Log headache, including what kind and the intensity.
    def add_headache(self):
        self.headache_window = tk.Toplevel()
        self.headache_window.title("Log headache")
        headache = Form(self.headache_window, self.saveloc)
        headache.add_entry('Headache type:', 'headache_type')
        headache.add_entry('Trigger (if known):', 'trigger')
        headache.add_scale('Intensity:', 'headache_intensity')
        headache.add_date_time('When:','when')
        headache.populate()

    # Log status of various facets of mobility.
    def update_mobility(self):
        self.mobility_window = tk.Toplevel()
        self.mobility_window.title("Log Mobility")
        mobility = Form(self.mobility_window, self.saveloc)
        mobility.add_scale('Shakiness:', 'shakiness')
        mobility.add_scale('Dyspraxia (fine):', 'dyspraxia_fine')
        mobility.add_scale('Dyspraxia (gross):', 'dyspraxia_gross')
        mobility.add_scale('Weakness:', 'weakness')
        mobilith.add_date_time('When:', 'when')
        mobility.populate()

    # Log intensity of various types of pain.
    def update_pain(self):
        self.pain_window = tk.Toplevel()
        self.pain_window.title("Log Pain Levels")
        pain = Form(self.pain_window, self.saveloc)
        pain.add_scale('Left shoulder pain:', 'left_shoulder_pain')
        pain.add_scale('Left neck pain:', 'left_neck_pain')
        pain.add_scale('Left head/upper neck pain:', 'left_upper_neck_pain')
        pain.add_scale('Left jaw pain:', 'left_jaw_pain')
        pain.add_scale('Left upper back pain:', 'left_high_back_pain')
        pain.add_scale('Left mid back pain:', 'left_mid_back_pain')
        pain.add_scale('Left low back pain:', 'left_low_back_pain')
        pain.add_scale('Left wrist pain:', 'left_wrist_pain')
        pain.add_scale('Left knee pain:', 'left_knee_pain')
        pain.add_scale('Right shoulder pain:', 'right_shoulder_pain')
        pain.add_scale('Right neck pain:', 'right_neck_pain')
        pain.add_scale('Right head/upper neck pain:', 'right_upper_neck_pain')
        pain.add_scale('Right jaw pain:', 'right_jaw_pain')
        pain.add_scale('Right upper back pain:', 'right_high_back_pain')
        pain.add_scale('Right mid back pain:', 'right_mid_back_pain')
        pain.add_scale('Right low back pain:', 'right_low_back_pain')
        pain.add_scale('Right wrist pain:', 'right_wrist_pain')
        pain.add_scale('Right knee pain:', 'right_knee_pain')
        pain.add_scale('Tension (emotional or physical):', 'tension')
        pain.add_scale('Focus:', 'focus')
        pain.add_scale('Spoons:', 'spoons')
        pain.add_date_time('When:', 'when')
        pain.add_entry('Your location:', 'location')
        pain.populate()

    # Log basically anything.
    def new_everything(self):
        self.mega_window = tk.Toplevel()
        self.mega_window.title("New Custom Entry")
        mega = Form(self.mega_window, self.saveloc)
        mega.add_entry('Title:', 'title')
        mega.add_entry('Category:', 'category')
        mega.add_entry('Reason:', 'reason')
        mega.add_date_time('Start:', 'start')
        mega.add_date_time('End:', 'end')
        mega.add_entry('Location:', 'location')
        mega.add_entry('Trigger:', 'trigger')
        mega.add_scale('Valence at start (higher for better mood):', 'start_valence')
        mega.add_scale('Worry/anxiety at start:', 'start_anxiety')
        mega.add_scale('Tension at start (emotional or physical):', 'start_tension')
        mega.add_scale('Focus at start:', 'start_focus')
        mega.add_scale('Intensity of mood at start:', 'start_mood_intensity')
        mega.add_scale('Energy at start:', 'start_energy')
        mega.add_scale('Spoons at start:', 'start_spoons')
        mega.add_scale('Valence at end (higher for better mood):', 'end_valence')
        mega.add_scale('Worry/anxiety at end:', 'end_anxiety')
        mega.add_scale('Tension at end (emotional or physical):', 'end_tension')
        mega.add_scale('Focus at end:', 'end_focus')
        mega.add_scale('Intensity of mood at end:', 'end_mood_intensity')
        mega.add_scale('Energy at end:', 'end_energy')
        mega.add_scale('Spoons at end:', 'end_spoons')
        mega.add_scale('Progress/completion:', 'progress')
        mega.add_scale('Satisfaction/Quality/ Benefit:', 'quality')
        mega.add_numeric('Exp gained:', 'exp_gained')
        mega.populate()

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
                dfile_data = load(dfile)
                # dfile_data["tags"] = ', '.join(dfile_data["tags"])
                data[index] = dfile_data
                index += 1
        datajson = dumps(data)
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
        self.preferences_window.title('Preferences')
        prefs = tk.Frame(self.preferences_window)
        enter = tk.Frame(prefs)
        ttk.Label(prefs, text='Save data files to:').grid(row=0, column=0)
        self.data_dir = tk.StringVar()
        self.data_dir.set(self.saveloc)
        self.enter_data_dir = ttk.Entry(enter, textvariable=self.data_dir)
        self.enter_data_dir.pack(side='left')
        browse = ttk.Button(enter, text='Browse...', command=self.set_data_dir)
        browse.pack(side='left')
        enter.grid(row=0, column=1)
        ttk.Button(prefs, text='Apply', command=self.save_prefs).grid(row=1, column=1)
        prefs.pack()

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

if __name__ == "__main__":
    root = tk.Tk()
    root.title("LifeTracker")
    app = App(root)
    root.mainloop()
