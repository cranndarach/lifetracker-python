# LifeTracker
### Keep track of events and trends in your life

## Known issues

* Date/time fields default to AM regardless of time
* "Save as preset" is not yet functional (it is recommended that you do not use it as-is)

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

* If you run the program by clicking on the file (as opposed to from the command line), a terminal window will open while the program is running. This is normal. Closing it will close the program.

* Every entry is assigned a universally unique identifier (UUID), and is saved in its own file named `data-[uuid]` in a directory called `data/`, sibling to the `py/` directory. From the "File" menu in the program, you can export all of this data to a .CSV file and save it wherever you would like. That way, you can analyze it using R, Excel, SciPy, etc. Eventually, there may be some analysis options built into the program (see issue #3), but this is not an immediate priority.

* There is no form validation, making every field in an entry optional. Some are specified as "optional" because they will likely only apply in very limited circumstances. Nonetheless, you can leave anything blank (with the exception of sliders, which you can leave at 0). This is to allow for optimal flexibility, so that you can worry less about the requirements and labels and just record any data you feel is relevant.

* Similarly, individual entries are not labeled as "event" or "mood," etc. Only "field: data" pairs are saved. You should worry more about which form has the fields that you need, than about whether it is called the right thing.
