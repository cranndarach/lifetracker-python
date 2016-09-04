import tkinter as tk
from form_general import Form
from page import Page

class Status(Page):
    def __init__(self, master):
        super(Status, self).__init__()
        self.master = master
        self.new_button("Log Spoon Level", self.update_spoons)
        self.new_button("Log Mood", self.update_mood)
        self.new_button("Log Health/Symptoms", self.update_health)
        self.new_button("Log Pain Level", self.update_pain)
        self.new_button("Log Mobility", self.update_mobility)
        self.new_button("Log Hunger", self.update_hunger)
        self.new_button("Log Headache", self.add_headache)

    # Log your "spoon" levels.
    def update_spoons(self):
        self.spoons_window = tk.Toplevel()
        self.spoons_window.title("Log Spoons")
        spoons = Form(self.spoons_window)
        spoons.add_scale('Spoons:', 'spoons')
        spoons.add_date_time('When:', 'when')
        spoons.populate()

    # Log your mood on various dimensions.
    def update_mood(self):
        self.mood_window = tk.Toplevel()
        self.mood_window.title("Log Mood")
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

    # Log symptoms or other health-related factors.
    def update_health(self):
        self.health_window = tk.Toplevel()
        self.health_window.title("Log Health/Symptoms")
        health = Form(self.health_window)
        health.add_entry('Trait/Symptom:', 'symptom')
        health.add_entry('Category:', 'category')
        health.add_date_time('When/start:', 'start')
        health.add_date_time('End (set to same as start if not applicable):', 'end')
        health.add_entry('Trigger (if applicable/known):', 'trigger')
        health.add_entry('Your location:', 'location')
        health.add_scale('Intensity of symptom:', 'symptom_intensity')
        health.add_scale('Spoons:', 'spoons')
        health.populate()

    # Log hunger level.
    def update_hunger(self):
        self.hunger_window = tk.Toplevel()
        self.hunger_window.title("Log Hunger")
        hunger = Form(self.hunger_window)
        hunger.add_scale('Hunger:', 'hunger')
        hunger.add_date_time('When:','when')
        hunger.populate()

    # Log headache, including what kind and the intensity.
    def add_headache(self):
        self.headache_window = tk.Toplevel()
        self.headache_window.title("Log headache")
        headache = Form(self.headache_window)
        headache.add_entry('Headache type:', 'headache_type')
        headache.add_entry('Trigger (if known):', 'trigger')
        headache.add_scale('Intensity:', 'headache_intensity')
        headache.add_date_time('When:','when')
        headache.populate()

    # Log status of various facets of mobility.
    def update_mobility(self):
        self.mobility_window = tk.Toplevel()
        self.mobility_window.title("Log Mobility")
        mobility = Form(self.mobility_window)
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
        pain = Form(self.pain_window)
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
