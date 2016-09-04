# LifeTracker
### Keep track of events and trends in your life

## tl;dr

The very short version of how to download and use the program. Each step is elaborated below.

* Clone or download the repository
* Run `py/main.py` (Double click on the file, or from the command line in the project's root directory run `python py/main.py` (Linux/Mac), or `py\main.py` (Windows), or see below)
* When you want to explore the data, go to "File -> Export data to CSV..." and choose a place to save it.
* If you want to add or edit forms, see the [wiki](https://github.com/cranndarach/lifetracker/wiki) for a tutorial.

## Known issues

* Date/time fields default to AM regardless of time &mdash; until this is fixed, be sure to keep an eye on the time input when adding an entry.
* ~~"Save as preset" is not yet functional (it is recommended that you do not use it as-is)~~ *"Save as preset" has been moved to the development branch "presets." Saving is functional, but the presets do not load yet.*

## Obtaining

Option 1) Download the .zip or tarball using the green "Clone or download" button

Option 2) Clone the repository:

```
git clone https://github.com/cranndarach/lifetracker.git
```

 if you **do not** plan on making changes to the files, update occasionally using

 ```
 git pull
 ```

 if you do plan on making changes, use

 ```
 git fetch
 ```

## Usage

Currently, there is no standalone application. To run, you will need Python 3 (it was written using 3.5).

Keeping the directory structure as is, run the file `main.py` to run the application. **You may need to edit the shebang lines**, depending on your OS.  
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

If you are unsure of what this should say, type into a terminal `which python` or `which python3`. Prepend the results with `#!` and use this as the shebang line. That is, if you type `which python` and the result is `/usr/bin/python`, make the first line of the files: `#!/usr/bin/python`.

### General usage notes

* If you run the program by clicking on the file (as opposed to from the command line), a terminal window will open while the program is running. This is normal. It will log any errors or messages from the code. Closing it will close the program.

* Your settings are saved in a file called `settings.json` in the `usrsettings/` directory, within the `py/` directory. So to be clear, that's `[LifeTracker]/py/usrsettings/settings.json`. This file will be created the first time your run the program, or any time it is not found.

* Every entry is assigned an identifier (UUID), and is saved in its own file named `data-[uuid].json` in a directory called `data/`, sibling to the `py/` directory. From the "File" menu in the program, you can export all of this data to a .CSV file and save it wherever you would like. That way, you can analyze it using R, Excel, SciPy, etc. Eventually, there may be some analysis options built into the program or distributed alongside it (see issue #3), but this is not an immediate priority.

* There is no form validation, making every field in an entry optional. Some are additionally specified as "optional" simply because they will likely only apply in very limited circumstances, but in reality you can leave anything blank (with the exception of sliders, which you can leave at 0). This is to allow for optimal flexibility, so that you can worry less about the requirements and labels and just record any data you feel is relevant.

* Similarly, individual entries are not labeled as "event" or "mood," etc. Only the actual data is saved. That way, you don't have to worry about which form has the right name for what you're entering, only that you can enter the right information.
