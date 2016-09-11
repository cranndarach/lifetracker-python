# LifeTracker
### Keep track of events and trends in your life

### License information

Except where otherwise noted, this project is copyright (c) 2016 R Steiner and licensed under the terms of the MIT license.  

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Except where otherwise noted, images in this project are licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/cranndarach/lifetracker" property="cc:attributionName" rel="cc:attributionURL">R Steiner</a>.

Spread the love!

## [LifeTracker v0.1.0](https://github.com/cranndarach/lifetracker/releases) is current as of Sept. 10, 2016

![The main page of LifeTracker](https://github.com/cranndarach/lifetracker/blob/master/screenshots/main_page.PNG)

> [ The main page of LifeTracker. A window with three visible tabs. The active one is labeled "Main." The other two are labeled "Influences" and "Status." There are two rows of buttons. The first row's buttons are labeled "Add Event," "Add Task," and "Add EXP Gained." The second row's buttons are labeled "Add Simple Entry" and "Add Generic." ]

![The "Log Mood" entry](https://github.com/cranndarach/lifetracker/blob/master/screenshots/log_mood.PNG)

> [ A window with a form for logging your mood. There are seven sliders, one per row, labeled: "Valence (higher for better mood)," "Worry/anxiety," "Tension (emotional or physical)," "Focus," "Intensity of mood," "Energy," and "Spoons." The next row is labeled "When" and allows the user to enter a date and time. The last three rows of the form are text entries labeled "Location," "Notes," and "Tags (separated by commas)." At the bottom are two buttons. The one on the left is labeled "Close," and the one on the right is labeled "Submit." ]

![A successful submission](https://github.com/cranndarach/lifetracker/blob/master/screenshots/med_success.PNG)

> [ A set of three windows depicting a successfully submitted entry. In the back is a window labeled "Log Medicine Taken." The fields are labeled "Medicine name," "Category," "Dosage," "Reason for taking (optional)," "Start of dose," "End of dose (set to same as start if not applicable)," "Benefit/improvement" (with a mostly unobstructed slider), "Notes," and "Tags (separated by commas)." In the middle is the main window with the "Influences" tab open. The four buttons (three in the first row) read "Add Sleep Entry," "Add Coping Mechanism," "Record Medicine Taken," and "Add Misc. Influence." In the front is a dialog box labeled "Success" with the message, "Your entry has been saved," and a focused button that says "OK." ]

## Windows binaries

If you are a Windows user and you do not have Python installed on your computer, you can download the standalone program from the [releases](https://github.com/cranndarach/lifetracker/releases) page. See General Usage Notes for tips on making the most of LifeTracker.

If you do have Python 3.5, you may want to use the source code, because the binary is significantly bigger.

## From Source: tl;dr

The condensed version of how to download and use LifeTracker from the source code. Each step is elaborated below.

* Clone or download the repository
* Run `py/main.py` (Double click on the file, or from the command line in the project's root directory run `python py/main.py` (Linux/Mac), or `py\main.py` (Windows), or see below)
* When you want to explore the data, go to "File -> Export data to CSV..." and choose a place to save it.
* If you want to add or edit forms, see the [wiki](https://github.com/cranndarach/lifetracker/wiki) for a tutorial.

## Obtaining

Option 1) Download the .zip or tarball using the green "Clone or download" button

Option 2) Clone the repository:

```
git clone https://github.com/cranndarach/lifetracker.git
```

Update occasionally using

 ```
 git pull
 ```

 or

 ```
 git fetch
 ```

## Running LifeTracker

The Windows .exe file should run as-is. Just save it somewhere and double-click. You may want to have it in its own directory so that you can keep the data files nearby by default.

Currently, there is no standalone application for Mac or Linux. To run LifeTracker, you will need Python 3 (specifically, it was written using 3.5).

Keeping the directory structure as is, run the file `main.py` to run the application. **You may need to edit the shebang lines**, depending on your OS and method of execution.  
The python files currently have the shebang line:

```
#! python
```

### Windows
This will work iff one of the following conditions is met:

* Python 3 is the only version on your computer, or
* The environment variable PY_PYTHON = 3

Otherwise, you will need to either edit the shebang line to say:

```
#! python3
```

or explicitly run the file using Python 3.

### \*NIX (including Mac)
You will need to edit this line to point to Python 3 on your system. This will probably be something like:

```
#!/usr/bin/python3
```

or

```
#!/usr/bin/env python3
```

If you are unsure of what it should say, type into a terminal `which python` or `which python3`. Prepend the results with `#!` and use this as the shebang line. That is, if you type `which python3` and the result is `/usr/bin/python3`, make the first line of the files: `#!/usr/bin/python3`.

## General usage notes

* If you run the program by clicking on the file (as opposed to from the command line), a terminal window will open while the program is running. This is normal. It will log any errors or messages from the code. Closing it will close the program.

* Your settings are saved in a file called `settings.json` in the `usrsettings/` directory, within the `py/` directory. So to be clear, that's `[LifeTracker]/py/usrsettings/settings.json`. This file will be created the first time your run the program, or any time it is not found.

* Every entry is assigned an identifier (UUID), and is saved in its own file named `data-[uuid].json` in a directory called `data/`, sibling to the `py/` directory. From the "File" menu in the program, you can export all of this data to a .CSV file and save it wherever you would like. That way, you can analyze it using R, Excel, SciPy, etc. Eventually, there may be some analysis options built into the program or distributed alongside it (see issue #3), but this is not an immediate priority.

* There is no form validation, making every field in an entry optional. Some are additionally specified as "optional" simply because they will likely only apply in very limited circumstances, but in reality you can leave anything blank (with the exception of sliders, which you can leave at 0). This is to allow for optimal flexibility, so that you can worry less about the requirements and labels and just record any data you feel is relevant.

* Similarly, individual entries are not labeled as "event" or "mood," etc. Only the actual data is saved. That way, you don't have to worry about which form has the right name for what you're entering, only that you can enter the right information.

## Questions, comments, suggestions, bugs...

First, check the existing [issues](https://github.com/cranndarach/lifetracker/issues) (both open and closed) to see if anyone else has brought it up. If not, please submit an issue!

When doing so, please try to be as descriptive as possible. If it is a bug, please note whether you are using a source build or a binary. If it was from source, please do your best to include your operating system, version of Python, and the traceback, if applicable.

**"Beginner questions" are welcome!** The same goes for all types of issues, really. It's okay if you aren't sure how to run the file, what version of Python you have, etc. Official documentation can be hard to sort through if you don't already know what you're doing. This program is supposed to make your life easier, and so it is important to make sure as many people as possible can take an active role in its development if they so choose. Similarly, if you have an idea for a feature but have no idea how or even if it could be implemented, feel free to suggest it anyway. Creativity is an important part of any project's development.

## Known issues

* Date/time fields default to AM regardless of time &mdash; until this is fixed, be sure to keep an eye on the time input when adding an entry.
* ~~"Save as preset" is not yet functional (it is recommended that you do not use it as-is)~~ *"Save as preset" has been moved to the development branch "presets." Saving is functional, but the presets do not load yet.*
