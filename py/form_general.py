#! python

from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from uuid import uuid4
from json import dump

class Form:
    def __init__(self, master):
        self.master = master
        self.send = ttk.Button(self.master, text='Submit', command=self.submit)
        self.close = ttk.Button(self.master, text='Close', command=self.close_window)
        self.notes = tk.Text(self.master, width=30, height=5)
        self.tags = ttk.Entry(self.master, width=40)
        self.entries = []
        self.rowmaster = 0
        self.colmaster = 0
        self.row = 0
        self.col = 0
        s = ttk.Style()
        s.configure('TLabel', wraplength=125)

    def count(self):
        self.rowmaster += 1
        self.row = self.rowmaster%13
        self.colmaster += 1
        self.col = int(self.colmaster/13) * 2  # this will work for the time being

    def add_entry(self, label, name):
        ttk.Label(self.master, text=label).grid(row=self.row, column=self.col)
        e = ttk.Entry(self.master, width=40)
        e.grid(row=self.row, column=self.col+1)
        self.__setattr__(name, e)
        self.entries.append(name)
        self.count()

    def add_date_time(self, label, name):
        # text variables:
        month = tk.IntVar()
        month.set(datetime.now().month)
        day = tk.IntVar()
        day.set(datetime.now().day)
        year = tk.IntVar()
        year.set(datetime.now().year)
        hour = tk.IntVar()
        c_hour = datetime.now().hour
        ap = tk.StringVar()
        if int(c_hour) > 12:
            c_hour -= 12
            ap.set("PM")
        elif int(c_hour) == 0:
            c_hour = 12
            ap.set("AM")
        else:
            ap.set("AM")
        hour.set(c_hour)
        minute = tk.IntVar()
        minute.set(datetime.now().minute)
        # everything else:
        dateframe = tk.Frame(self.master)
        ttk.Label(self.master, text=label).grid(row=self.row, column=self.col)
        mm = tk.Spinbox(dateframe, from_=1, to=12, wrap=True, width=3, textvariable=month)
        mm.pack(side="left")
        self.__setattr__(name+'_month', mm)
        self.entries.append(name+'_month')
        ttk.Label(dateframe, text='/').pack(side="left")
        d = tk.Spinbox(dateframe, from_=1, to=31, wrap=True, width=3, textvariable=day)
        d.pack(side="left")
        self.__setattr__(name+'_day', d)
        self.entries.append(name+'_day')
        ttk.Label(dateframe, text='/').pack(side="left")
        y = tk.Spinbox(dateframe, width=4, textvariable=year)
        y.pack(side="left")
        self.__setattr__(name+'_year', y)
        self.entries.append(name+'_year')
        h = tk.Spinbox(dateframe, from_=1, to=12, wrap=True, width=3, textvariable=hour)
        h.pack(side="left")
        self.__setattr__(name+'_hour', h)
        self.entries.append(name+'_hour')
        ttk.Label(dateframe, text=':').pack(side="left")
        m = tk.Spinbox(dateframe, from_=00, to=59, wrap=True, width=3, textvariable=minute)
        m.pack(side="left")
        self.__setattr__(name+'_minute', m)
        self.entries.append(name+'_minute')
        ap = tk.Spinbox(dateframe, values=("AM", "PM"), width=3, wrap=True, textvariable=ap)
        ap.pack(side="left")
        self.__setattr__(name+'_ampm', ap)
        self.entries.append(name+'_ampm')
        dateframe.grid(row=self.row, column=self.col+1)
        self.count()

    def add_scale(self, label, name, min_=0, max_=100):
        ttk.Label(self.master, text=label).grid(row=self.row, column=self.col)
        s = ttk.Scale(self.master, from_=min_, to=max_, variable=tk.IntVar())
        s.grid(row=self.row, column=self.col+1)
        self.__setattr__(name, s)
        self.entries.append(name)
        self.count()

    def add_numeric(self, label, name):
        ttk.Label(self.master, text=label).grid(row=self.row, column=self.col)
        n = tk.Spinbox(self.master, width=4)
        n.grid(row=self.row, column=self.col+1)
        self.__setattr__(name, n)
        self.entries.append(name)
        self.count()

    def populate(self):
        ttk.Label(self.master, text='Notes:').grid(row=self.row, column=self.col)
        self.notes.grid(row=self.row, column=self.col+1)
        self.count()
        ttk.Label(self.master, text='Tags (separated by commas):').grid(row=self.row, column=self.col)
        self.tags.grid(row=self.row, column=self.col+1)
        self.count()
        self.send.grid(row=self.row, column=self.col+1)
        self.close.grid(row=self.row, column=self.col)
        self.count()
        self.entries.extend(['notes', 'tags'])
        i = 0
        while i <= self.row:
            self.master.rowconfigure(i, pad=3)
            i += 1
        j = 0
        while j <= self.col+1:
            self.master.columnconfigure(j, pad=7)
            j += 1

    def submit(self):
        uuid = str(uuid4())
        data = {'uuid': uuid}
        for e in self.entries:
            if e == 'notes':
                data[e] = self.__getattribute__(e).get('1.0', 'end')
            elif e == 'tags':
                tags = self.__getattribute__(e).get()
                tags = tags.split(',')
                tags = [t.strip() for t in tags]
                data[e] = tags
            else:
                data[e] = self.__getattribute__(e).get()
        while True:
            try:
                with open('../data/data-'+uuid+'.json', 'w') as df:
                    dump(data, df)
                messagebox.showinfo('Success', 'Your entry has been saved.')
                break
            except FileNotFoundError:
                os.mkdir('../data')

    def close_window(self):
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    ln = [['Name:', 'name'], ['Say:', 'say']]
    form = Form(root, ln)
    root.mainloop()
