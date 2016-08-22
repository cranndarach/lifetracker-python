# LifeTracker
### Keep track of events in your life and see how things relate to one another

## Usage

Currently, there is no standalone application. To run, you will need Python 3 (it was written using 3.5).

Keeping the directory structure as is, run the file `main.py` to run the application. **You may need to edit the shebang lines**, depending on your OS.  
The python files currently have the shebang line:

> #! python

### Windows
This will work iff one of the following conditions is met:

* Python 3 is the only version on your computer, or
* The environment variable PY_PYTHON = 3

Otherwise, you will need to either edit the shebang line to say:

>  #! python3

or explicitly run the file using Python 3 (e.g., by calling it from iPython 3)

### \*NIX
You will need to edit this line to point to Python 3 on your system. This will probably be something like:

> #!/usr/bin/python3

or

> #!/usr/bin/env python3

### General usage notes

If you do not run the program from the command line, a terminal window will open while the program is running. Closing it will close the program.

Every entry is assigned a universally unique identifier (UUID), and is saved in a separate file named `data-[uuid]` in a directory called `data/`, sibling to the `py/` directory. From the "File" menu in the program, you can export all of this data to a .CSV file and save it wherever you would like. That way, you can analyze it using R, Excel, SciPy, etc. Eventually, there may be some analysis options built into the program, but this is not an immediate priority.

There is no form validation, making every field in an entry optional. Some are specified as "optional" because they will likely only apply in very limited circumstances. Nonetheless, you can leave anything blank (with the exception of sliders, which you can leave at 0). This is to allow for optimal flexibility, so that you can worry less about the requirements and labels and just record any data you feel is relevant.
