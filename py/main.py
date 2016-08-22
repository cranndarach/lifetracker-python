#! python

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from glob import glob
from json import load, dumps
import pandas as pd

from form_general import Form

class App:
    def __init__(self, master):
        self.master = master
        self.rowmaster = 0
        self.row = 1    # allows menu to be at row 0
        self.colmaster = 0
        self.col = 0
        s = ttk.Style()
        s.configure('TButton', width=25)

        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.grid(row=0)
        self.file_button = tk.Menubutton(self.menu_frame, text="File", underline=0)
        self.file_button.pack(side='left')  #grid(row=0, column=0)
        self.file_button.menu = tk.Menu(self.file_button, tearoff=0)
        self.file_button['menu'] = self.file_button.menu
        self.file_button.menu.add_cascade(label="Export data to CSV", command=self.export)

        self.event = ttk.Button(self.master, text="Add Event", command=self.new_event)
        self.event.grid(row=self.row, column=self.col)
        self.count()
        self.spoons = ttk.Button(self.master, text="Update Spoon Level", command=self.update_spoons)
        self.spoons.grid(row=self.row, column=self.col)
        self.count()
        self.mood = ttk.Button(self.master, text="Update Mood", command=self.update_mood)
        self.mood.grid(row=self.row, column=self.col)
        self.count()
        self.task = ttk.Button(self.master, text="Add Task", command=self.new_task)
        self.task.grid(row=self.row, column=self.col)
        self.count()
        self.sleep = ttk.Button(self.master, text="Add Sleep Entry", command=self.new_sleep)
        self.sleep.grid(row=self.row, column=self.col)
        self.count()
        self.copech = ttk.Button(self.master, text="Add Coping Mechanism", command=self.new_copech)
        self.copech.grid(row=self.row, column=self.col)
        self.count()
        self.health = ttk.Button(self.master, text="Update Health/Symptoms", command=self.update_health)
        self.health.grid(row=self.row, column=self.col)
        self.count()
        self.meds = ttk.Button(self.master, text="Record Medicine Taken", command=self.meds_taken)
        self.meds.grid(row=self.row, column=self.col)
        self.count()
        self.mega = ttk.Button(self.master, text="Add Generic", command=self.new_everything)
        self.mega.grid(row=self.row, column=self.col)
        self.count()

    def count(self):
        self.rowmaster += 1
        self.row = int(self.rowmaster/3) + 1
        self.colmaster += 1
        self.col = self.colmaster%3

    def new_event(self):
        self.event_window = tk.Toplevel()
        event = Form(self.event_window)
        event.add_entry('Title:', 'title')
        event.add_entry('Category:', 'category')
        event.add_date_time('Start:', 'start')
        event.add_date_time('End:', 'end')
        event.add_entry('Location:', 'location')
        event.add_scale('Mood at start:', 'start_mood')
        event.add_scale('Spoons at start:', 'start_spoons')
        event.add_scale('Mood at end:', 'end_mood')
        event.add_scale('Spoons at end:', 'end_spoons')
        event.populate()
    def update_spoons(self):
        self.spoons_window = tk.Toplevel()
        spoons = Form(self.spoons_window)
        spoons.add_scale('Spoons:', 'spoons')
        spoons.add_date_time('When:', 'when')
        spoons.populate()
    def new_task(self):
        self.task_window = tk.Toplevel()
        task = Form(self.task_window)
        task.add_entry('Title:', 'title')
        task.add_entry('Category:', 'category')
        task.add_date_time('Start:', 'start')
        task.add_date_time('End:', 'end')
        task.add_entry('Location:', 'location')
        task.add_scale('Mood at start:', 'start_mood')
        task.add_scale('Spoons at start:', 'start_spoons')
        task.add_scale('Mood at end:', 'end_mood')
        task.add_scale('Spoons at end:', 'end_spoons')
        task.add_scale('Progress/completion:', 'progress')
        task.add_scale('Satisfaction/Quality:', 'quality')
        task.add_numeric('Exp gained:', 'exp_gained')
        task.populate()
    def new_sleep(self):
        self.sleep_window = tk.Toplevel()
        sleep = Form(self.sleep_window)
        sleep.add_date_time('Went to bed:', 'sleep_start')
        sleep.add_date_time('Woke up:', 'sleep_end')
        sleep.add_entry('Location:', 'location')
        sleep.add_scale('Mood when you went to bed:', 'start_mood')
        sleep.add_scale('Mood when you woke up:', 'end_mood')
        sleep.add_scale('Quality:', 'quality')
        sleep.populate()
    def update_mood(self):
        self.mood_window = tk.Toplevel()
        mood = Form(self.mood_window)
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
        copech = Form(self.copech_window)
        copech.add_entry('Coping mechanism used:', 'coping_mech')
        copech.add_entry('Category:', 'category')
        copech.add_entry('Reason (optional):', 'reason')
        copech.add_date_time('When/start:', 'start')
        copech.add_date_time('End (set to same as start if not applicable):', 'end')
        copech.add_scale('Benefit/Improvement:', 'quality')
        copech.add_scale('Mood afterward:', 'mood')
        copech.add_scale('Spoons:', 'spoons')
        copech.add_numeric('Exp gained:', 'exp_gained')
        copech.add_entry('Location:', 'location')
        copech.populate()
    def update_health(self):
        self.health_window = tk.Toplevel()
        health = Form(self.health_window)
        health.add_entry('Symptom:', 'symptom')
        health.add_entry('Category:', 'category')
        health.add_date_time('When/start:', 'start')
        health.add_date_time('End (set to same as start if not applicable):', 'end')
        health.add_entry('Trigger (if applicable/known):', 'trigger')
        health.add_entry('Location:', 'location')
        health.add_scale('Intensity of symptom:', 'symptom_intensity')
        health.add_scale('Spoons:', 'spoons')
        health.populate()
    def meds_taken(self):
        self.med_window = tk.Toplevel()
        med = Form(self.med_window)
        med.add_entry('Medicine name:', 'med_name')
        med.add_entry('Category:', 'category')
        med.add_entry('Dosage:', 'dosage')
        med.add_entry('Reason for taking (optional):', 'reason')
        med.add_date_time('Start of dose:', 'start')
        med.add_date_time('End of dose (set to same as start if not applicable):', 'end')
        med.add_scale('Benefit/Improvement (leave at 0 if NA/unknown):', 'quality')
        med.populate()
    def new_everything(self):
        self.mega_window = tk.Toplevel()
        mega = Form(self.mega_window)
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
        datafiles = glob('data/data-*')
        for d in datafiles:
            with open(d, 'r') as dfile:
                dfile_data = load(dfile)
                # dfile_data["tags"] = ', '.join(dfile_data["tags"])
                data[index] = dfile_data
                index += 1
        datajson = dumps(data)
        datapd = pd.read_json(datajson, orient='index')
        outfile = filedialog.asksaveasfilename(initialdir = '/', title = 'Save as...',
            filetypes = (('csv files', '*.csv'), ('all files', '*.*')))
        datapd.to_csv(outfile, index=False)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
