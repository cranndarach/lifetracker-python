#! python

# import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from glob import glob
from json import load, dumps
import pandas as pd

from form_general import Form
from page import Page

class App:
    def __init__(self, master):
        self.master = master
        self.saveloc = '../data'
        # self.rowmaster = 0
        # self.row = 1    # allows menu to be at row 0
        # self.colmaster = 0
        # self.col = 0
        s = ttk.Style()
        s.configure('TButton', width=25)

        self.nb = ttk.Notebook(self.master)
        self.main = Page() #tk.Frame()
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

        # self.simple = ttk.Button(self.main, text="Add Simple Entry", command=self.new_simple)
        # self.simple.grid(row=self.row, column=self.col)
        # self.count()
        # self.influence = ttk.Button(self.main, text="Add External Influence", command=self.new_influence)
        # self.influence.grid(row=self.row, column=self.col)
        # self.count()
        # self.event = ttk.Button(self.main, text="Add Event", command=self.new_event)
        # self.event.grid(row=self.row, column=self.col)
        # self.count()
        # self.spoons = ttk.Button(self.main, text="Update Spoon Level", command=self.update_spoons)
        # self.spoons.grid(row=self.row, column=self.col)
        # self.count()
        # self.mood = ttk.Button(self.main, text="Update Mood", command=self.update_mood)
        # self.mood.grid(row=self.row, column=self.col)
        # self.count()
        # self.task = ttk.Button(self.main, text="Add Task", command=self.new_task)
        # self.task.grid(row=self.row, column=self.col)
        # self.count()
        # self.sleep = ttk.Button(self.main, text="Add Sleep Entry", command=self.new_sleep)
        # self.sleep.grid(row=self.row, column=self.col)
        # self.count()
        # self.copech = ttk.Button(self.main, text="Add Coping Mechanism", command=self.new_copech)
        # self.copech.grid(row=self.row, column=self.col)
        # self.count()
        # self.health = ttk.Button(self.main, text="Update Health/Symptoms", command=self.update_health)
        # self.health.grid(row=self.row, column=self.col)
        # self.count()
        # self.meds = ttk.Button(self.main, text="Record Medicine Taken", command=self.meds_taken)
        # self.meds.grid(row=self.row, column=self.col)
        # self.count()
        # self.pain = ttk.Button(self.main, text="Update Pain Levels", command=self.update_pain)
        # self.pain.grid(row=self.row, column=self.col)
        # self.count()
        # self.mega = ttk.Button(self.main, text="Add Generic", command=self.new_everything)
        # self.mega.grid(row=self.row, column=self.col)
        # self.count()

        self.main.new_button("Add Simple Entry", self.new_simple)
        self.influence.new_button("Add External Influence", self.new_influence)
        self.main.new_button("Add Event", self.new_event)
        self.status.new_button("Update Spoon Level", self.update_spoons)
        self.status.new_button("Update mood", self.update_mood)
        self.main.new_button("Add Task", self.new_task)
        self.influence.new_button("Add Sleep Entry", self.new_sleep)
        self.influence.new_button("Add Coping Mechanism", self.new_copech)
        self.status.new_button("Update Health/Symptoms", self.update_health)
        self.influence.new_button("Record Medicine Taken", self.meds_taken)
        self.status.new_button("Update Pain Leves", self.update_pain)
        self.main.new_button("Add Generic", self.new_everything)

        self.nb.add(self.main, text='Main')
        self.nb.add(self.status, text='Status')
        self.nb.add(self.influence, text='Influences')
        self.nb.grid(row=1, column=0)

    # def count(self):
    #     self.rowmaster += 1
    #     self.row = int(self.rowmaster/3) + 1
    #     self.colmaster += 1
    #     self.col = self.colmaster%3

    def new_simple(self):
        self.simple_window = tk.Frame() #tk.Toplevel()
        # self.simple_tab = self.nb.add(self.simple_window, text="Add Simple Entry")
        self.nb.add(self.simple_window, text="Add Simple Entry")
        simple = Form(self.simple_window, self.saveloc)
        simple.add_entry('Title:', 'title')
        simple.add_entry('Category:', 'category')
        simple.add_date_time('When:', 'when')
        simple.add_entry('Location:', 'location')
        simple.populate()
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
    def update_spoons(self):
        self.spoons_window = tk.Toplevel()
        self.spoons_window.title("Update Spoons")
        spoons = Form(self.spoons_window, self.saveloc)
        spoons.add_scale('Spoons:', 'spoons')
        spoons.add_date_time('When:', 'when')
        spoons.populate()
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
    def update_mood(self):
        self.mood_window = tk.Toplevel()
        self.mood_window.title("Update Mood")
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
    def update_health(self):
        self.health_window = tk.Toplevel()
        self.health_window.title("Update Health/Symptoms")
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
    def meds_taken(self):
        self.med_window = tk.Toplevel()
        self.med_window.title("Record Medicine Taken")
        med = Form(self.med_window, self.saveloc)
        med.add_entry('Medicine name:', 'med_name')
        med.add_entry('Category:', 'category')
        med.add_entry('Dosage:', 'dosage')
        med.add_entry('Reason for taking (optional):', 'reason')
        med.add_date_time('Start of dose:', 'start')
        med.add_date_time('End of dose (set to same as start if not applicable):', 'end')
        med.add_scale('Benefit/Improvement (leave at 0 if NA/unknown):', 'quality')
        med.populate()
    def update_pain(self):
        self.pain_window = tk.Toplevel()
        self.pain_window.title("Update Pain Levels")
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
        data = {}
        index = 0
        datafiles = glob('../data/data-*')
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
        directory = filedialog.askdirectory(initialdir='/', title='Select folder...')
        return(directory)

    def preferences(self):
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
        usrdir = self.browse_directory()
        self.data_dir.set(usrdir)

    def save_prefs(self):
        self.saveloc = self.enter_data_dir.get()
        messagebox.showinfo('Success', 'Your preferences have been saved.')

if __name__ == "__main__":
    root = tk.Tk()
    root.title("LifeTracker")
    app = App(root)
    root.mainloop()
