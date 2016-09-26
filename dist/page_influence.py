import tkinter as tk
from form_general import Form
from page import Page

class Influence(Page):
    def __init__(self, master):
        super(Influence, self).__init__()
        self.master = master
        self.new_button("Add Sleep Entry", self.new_sleep)
        self.new_button("Add Coping Mechanism", self.new_copech)
        self.new_button("Record Medicine Taken", self.meds_taken)
        self.new_button("Add Misc. Influence", self.new_influence)

    # Log an external influence, something that may impact
    # your state or other variable of interest.
    def new_influence(self):
        self.infl_window = tk.Toplevel()
        self.infl_window.title("Add Misc. Influence")
        infl = Form(self.infl_window  )  #, self.saveloc)
        infl.add_entry('Title:', 'title')
        infl.add_entry('Category:', 'category')
        infl.add_date_time('When:', 'when')
        infl.add_scale('Intensity:', 'intensity')
        # infl.add_date_time('End:', 'end')
        infl.add_entry('Location:', 'location')
        infl.populate()

    # Log times and quality of sleep.
    def new_sleep(self):
        self.sleep_window = tk.Toplevel()
        self.sleep_window.title("New Sleep Entry")
        sleep = Form(self.sleep_window)  #, self.saveloc)
        sleep.add_date_time('Went to bed:', 'sleep_start')
        sleep.add_date_time('Woke up:', 'sleep_end')
        sleep.add_entry('Location:', 'location')
        # sleep.add_scale('Mood when you went to bed:', 'start_valence')
        sleep.add_scale('Mood when you woke up:', 'valence')
        sleep.add_scale('Quality:', 'quality')
        sleep.populate()

    # Log a coping mechanism used.
    def new_copech(self):
        self.copech_window = tk.Toplevel()
        self.copech_window.title("New Coping Mechanism")
        copech = Form(self.copech_window  )  #, self.saveloc)
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

    # Log medicine taken.
    def meds_taken(self):
        self.med_window = tk.Toplevel()
        self.med_window.title("Log Medicine Taken")
        med = Form(self.med_window)  #, self.saveloc)
        med.add_entry('Medicine name:', 'med_name')
        med.add_entry('Category:', 'category')
        med.add_entry('Dosage:', 'dosage')
        med.add_entry('Reason for taking (optional):', 'reason')
        med.add_date_time('Start of dose:', 'start')
        med.add_date_time('End of dose (set to same as start if not applicable):', 'end')
        med.add_scale('Benefit/Improvement (leave at 0 if NA/unknown):', 'quality')
        med.populate()
