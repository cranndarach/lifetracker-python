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

from __init__ import get_settings
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
        # with open('LICENSE', 'r', encoding="utf-8") as lic:
        #     mit_text = lic.read()
        # with open('python_license_stack.txt', 'r', encoding="utf-8") as pylic:
        #     py_text = pylic.read()
        # with open('anaconda_eula.txt', 'r', encoding="utf-8") as condalic:
        #     conda_text = condalic.read()
        mit_text = """The MIT License (MIT)

Copyright (c) 2016 Rachael Steiner

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

        conda_text = """Anaconda End User License Agreement
Copyright 2016, Continuum Analytics, Inc.

All rights reserved under the 3-clause BSD License:

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
Neither the name of Continuum Analytics, Inc. nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL CONTINUUM ANALYTICS, INC. BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

        py_text = """Terms and conditions for accessing or otherwise using Python
PSF LICENSE AGREEMENT FOR PYTHON 3.5.2

1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
   the Individual or Organization ("Licensee") accessing and otherwise using Python
   3.5.2 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby
   grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
   analyze, test, perform and/or display publicly, prepare derivative works,
   distribute, and otherwise use Python 3.5.2 alone or in any derivative
   version, provided, however, that PSF's License Agreement and PSF's notice of
   copyright, i.e., "Copyright © 2001-2016 Python Software Foundation; All Rights
   Reserved" are retained in Python 3.5.2 alone or in any derivative version
   prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or
   incorporates Python 3.5.2 or any part thereof, and wants to make the
   derivative work available to others as provided herein, then Licensee hereby
   agrees to include in any such work a brief summary of the changes made to Python
   3.5.2.

4. PSF is making Python 3.5.2 available to Licensee on an "AS IS" basis.
   PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
   EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
   WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
   USE OF PYTHON 3.5.2 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.5.2
   FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
   MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.5.2, OR ANY DERIVATIVE
   THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of
   its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any relationship
   of agency, partnership, or joint venture between PSF and Licensee.  This License
   Agreement does not grant permission to use PSF trademarks or trade name in a
   trademark sense to endorse or promote products or services of Licensee, or any
   third party.

8. By copying, installing or otherwise using Python 3.5.2, Licensee agrees
   to be bound by the terms and conditions of this License Agreement.


BEOPEN.COM LICENSE AGREEMENT FOR PYTHON 2.0
BEOPEN PYTHON OPEN SOURCE LICENSE AGREEMENT VERSION 1

1. This LICENSE AGREEMENT is between BeOpen.com ("BeOpen"), having an office at
  160 Saratoga Avenue, Santa Clara, CA 95051, and the Individual or Organization
  ("Licensee") accessing and otherwise using this software in source or binary
  form and its associated documentation ("the Software").

2. Subject to the terms and conditions of this BeOpen Python License Agreement,
  BeOpen hereby grants Licensee a non-exclusive, royalty-free, world-wide license
  to reproduce, analyze, test, perform and/or display publicly, prepare derivative
  works, distribute, and otherwise use the Software alone or in any derivative
  version, provided, however, that the BeOpen Python License is retained in the
  Software, alone or in any derivative version prepared by Licensee.

3. BeOpen is making the Software available to Licensee on an "AS IS" basis.
  BEOPEN MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
  EXAMPLE, BUT NOT LIMITATION, BEOPEN MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
  WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
  USE OF THE SOFTWARE WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

4. BEOPEN SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF THE SOFTWARE FOR
  ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF USING,
  MODIFYING OR DISTRIBUTING THE SOFTWARE, OR ANY DERIVATIVE THEREOF, EVEN IF
  ADVISED OF THE POSSIBILITY THEREOF.

5. This License Agreement will automatically terminate upon a material breach of
  its terms and conditions.

6. This License Agreement shall be governed by and interpreted in all respects
  by the law of the State of California, excluding conflict of law provisions.
  Nothing in this License Agreement shall be deemed to create any relationship of
  agency, partnership, or joint venture between BeOpen and Licensee.  This License
  Agreement does not grant permission to use BeOpen trademarks or trade names in a
  trademark sense to endorse or promote products or services of Licensee, or any
  third party.  As an exception, the "BeOpen Python" logos available at
  http://www.pythonlabs.com/logos.html may be used according to the permissions
  granted on that web page.

7. By copying, installing or otherwise using the software, Licensee agrees to be
  bound by the terms and conditions of this License Agreement.


CNRI LICENSE AGREEMENT FOR PYTHON 1.6.1

1. This LICENSE AGREEMENT is between the Corporation for National Research
  Initiatives, having an office at 1895 Preston White Drive, Reston, VA 20191
  ("CNRI"), and the Individual or Organization ("Licensee") accessing and
  otherwise using Python 1.6.1 software in source or binary form and its
  associated documentation.

2. Subject to the terms and conditions of this License Agreement, CNRI hereby
  grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
  analyze, test, perform and/or display publicly, prepare derivative works,
  distribute, and otherwise use Python 1.6.1 alone or in any derivative version,
  provided, however, that CNRI's License Agreement and CNRI's notice of copyright,
  i.e., "Copyright © 1995-2001 Corporation for National Research Initiatives; All
  Rights Reserved" are retained in Python 1.6.1 alone or in any derivative version
  prepared by Licensee.  Alternately, in lieu of CNRI's License Agreement,
  Licensee may substitute the following text (omitting the quotes): "Python 1.6.1
  is made available subject to the terms and conditions in CNRI's License
  Agreement.  This Agreement together with Python 1.6.1 may be located on the
  Internet using the following unique, persistent identifier (known as a handle):
  1895.22/1013.  This Agreement may also be obtained from a proxy server on the
  Internet using the following URL: http://hdl.handle.net/1895.22/1013."

3. In the event Licensee prepares a derivative work that is based on or
  incorporates Python 1.6.1 or any part thereof, and wants to make the derivative
  work available to others as provided herein, then Licensee hereby agrees to
  include in any such work a brief summary of the changes made to Python 1.6.1.

4. CNRI is making Python 1.6.1 available to Licensee on an "AS IS" basis.  CNRI
  MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF EXAMPLE,
  BUT NOT LIMITATION, CNRI MAKES NO AND DISCLAIMS ANY REPRESENTATION OR WARRANTY
  OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE USE OF
  PYTHON 1.6.1 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. CNRI SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 1.6.1 FOR
  ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
  MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 1.6.1, OR ANY DERIVATIVE
  THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of
  its terms and conditions.

7. This License Agreement shall be governed by the federal intellectual property
  law of the United States, including without limitation the federal copyright
  law, and, to the extent such U.S. federal law does not apply, by the law of the
  Commonwealth of Virginia, excluding Virginia's conflict of law provisions.
  Notwithstanding the foregoing, with regard to derivative works based on Python
  1.6.1 that incorporate non-separable material that was previously distributed
  under the GNU General Public License (GPL), the law of the Commonwealth of
  Virginia shall govern this License Agreement only as to issues arising under or
  with respect to Paragraphs 4, 5, and 7 of this License Agreement.  Nothing in
  this License Agreement shall be deemed to create any relationship of agency,
  partnership, or joint venture between CNRI and Licensee.  This License Agreement
  does not grant permission to use CNRI trademarks or trade name in a trademark
  sense to endorse or promote products or services of Licensee, or any third
  party.

8. By clicking on the "ACCEPT" button where indicated, or by copying, installing
  or otherwise using Python 1.6.1, Licensee agrees to be bound by the terms and
  conditions of this License Agreement.


CWI LICENSE AGREEMENT FOR PYTHON 0.9.0 THROUGH 1.2
Copyright © 1991 - 1995, Stichting Mathematisch Centrum Amsterdam, The
Netherlands.  All rights reserved.

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted, provided that
the above copyright notice appear in all copies and that both that copyright
notice and this permission notice appear in supporting documentation, and that
the name of Stichting Mathematisch Centrum or CWI not be used in advertising or
publicity pertaining to distribution of the software without specific, written
prior permission.

STICHTING MATHEMATISCH CENTRUM DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
EVENT SHALL STICHTING MATHEMATISCH CENTRUM BE LIABLE FOR ANY SPECIAL, INDIRECT
OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
SOFTWARE.
"""

        self.about_window = tk.Toplevel()
        self.about_window.title("About LifeTracker")
        about_box = tk.Text(self.about_window, height=50, width=60, wrap='word')
        about_box.insert('1.0', "LifeTracker is currently in active development.\n")
        about_box.insert('end', "Find the project's repository at https://github.com/cranndarach/lifetracker\n\n")
        about_box.insert('end', mit_text)
        about_box.insert('end', "\n\nProgrammed in Python® 3.5.\n")
        about_box.insert('end', "\"Python\" is a registered trademark of the Python Software Foundation.\n")
        about_box.insert('end', "This executable was bundled using pyinstaller v3.2\
        (http://www.pyinstaller.org/) with Anaconda Python.\n\n")
        about_box.insert('end', conda_text)
        about_box.insert('end', "\n\n")
        about_box.insert('end', py_text)
        about_box.config(state='disabled')
        about_box.grid(row=0, padx=15, pady=15)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("LifeTracker")
    app = App(root)
    root.mainloop()
