import tkinter as tk
from form_general import Form
from page import Page

class MainPage(Page):
    def __init__(self, master):
        super(MainPage, self).__init__()
        self.master = master
        self.new_button("Add Event", self.new_event)
        self.new_button("Add Task", self.new_task)
        self.new_button("Add EXP Gained", self.add_exp)
        self.new_button("Add Simple Entry", self.new_simple)
        self.new_button("Add Generic", self.new_everything)

    # Log an event, typically something where
    # you were not the "do-er."
    def new_event(self):
        self.event_window = tk.Toplevel()
        self.event_window.title("New Event")
        event = Form(self.event_window) #, self.saveloc)
        event.add_entry('Title:', 'title')
        event.add_entry('Category:', 'category')
        event.add_date_time('Start:', 'start')
        event.add_date_time('End:', 'end')
        event.add_entry('Location:', 'location')
        # event.add_scale('Mood at start:', 'start_valence')
        # event.add_scale('Spoons at start:', 'start_spoons')
        event.add_scale('Mood:', 'valence')
        event.add_scale('Spoons:', 'spoons')
        event.populate()

    # Log a task, typically where you are the "do-er."
    def new_task(self):
        self.task_window = tk.Toplevel()
        self.task_window.title("New Task")
        task = Form(self.task_window)   #, self.saveloc)
        task.add_entry('Title:', 'title')
        task.add_entry('Category:', 'category')
        task.add_date_time('Start:', 'start')
        task.add_date_time('End:', 'end')
        task.add_entry('Location:', 'location')
        # task.add_scale('Mood at start:', 'start_valence')
        # task.add_scale('Spoons at start:', 'start_spoons')
        task.add_scale('Mood:', 'valence')
        task.add_scale('Spoons:', 'spoons')
        task.add_scale('Size of task:', 'size')
        task.add_scale('Difficulty of task:', 'difficulty')
        task.add_scale('Progress/completion:', 'progress')
        task.add_scale('Satisfaction/Quality:', 'quality')
        task.add_numeric('Exp gained:', 'exp_gained')
        task.populate()

    # log gained EXP
    def add_exp(self):
        self.exp_window = tk.Toplevel()
        self.exp_window.title("Add EXP")
        exp = Form(self.exp_window)
        exp.add_numeric('Exp gained:', 'exp_gained')
        exp.add_date_time('When:', 'when')
        exp.populate()

    # Log a simple entry with few options.
    def new_simple(self):
        self.simple_window = tk.Toplevel()
        simple = Form(self.simple_window)   #, self.saveloc)
        simple.add_entry('Title:', 'title')
        simple.add_entry('Category:', 'category')
        simple.add_date_time('When:', 'when')
        simple.add_entry('Location:', 'location')
        simple.populate()

    # Log basically anything.
    def new_everything(self):
        self.mega_window = tk.Toplevel()
        self.mega_window.title("New Custom Entry")
        mega = Form(self.mega_window)   #, self.saveloc)
        mega.add_entry('Title:', 'title')
        mega.add_entry('Category:', 'category')
        mega.add_entry('Reason:', 'reason')
        mega.add_date_time('Start:', 'start')
        mega.add_date_time('End:', 'end')
        mega.add_entry('Location:', 'location')
        mega.add_entry('Trigger:', 'trigger')
        # mega.add_scale('Valence at start (higher for better mood):', 'start_valence')
        # mega.add_scale('Worry/anxiety at start:', 'start_anxiety')
        # mega.add_scale('Tension at start (emotional or physical):', 'start_tension')
        # mega.add_scale('Focus at start:', 'start_focus')
        # mega.add_scale('Intensity of mood at start:', 'start_mood_intensity')
        # mega.add_scale('Energy at start:', 'start_energy')
        # mega.add_scale('Spoons at start:', 'start_spoons')
        mega.add_scale('Mood (higher for better mood):', 'valence')
        mega.add_scale('Worry/anxiety:', 'anxiety')
        mega.add_scale('Tension (emotional or physical):', 'tension')
        mega.add_scale('Focus:', 'focus')
        mega.add_scale('Intensity of mood:', 'mood_intensity')
        mega.add_scale('Energy:', 'energy')
        mega.add_scale('Spoons:', 'spoons')
        mega.add_scale('Progress/completion:', 'progress')
        mega.add_scale('Satisfaction/Quality/ Benefit:', 'quality')
        mega.add_numeric('Exp gained:', 'exp_gained')
        mega.populate()
