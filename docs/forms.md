# Forms: Creating, editing, moving, deleting

## Overview

The forms in LifeTracker are accessed via buttons, which are organized into
  separate tabs of a [tkinter]() notebook. Each tab has a dedicated file named for
  it, which is where the code for creating each form is housed. The main program
  then references those files in order to know what to put in the notebook.

This tutorial will show you how to add, edit, move and delete forms so that you
  can customize LifeTracker to work best for you.

## Creating a form

### 1) Open the page's file

First, decide what page the new form will go in (don't worry if you're not sure;
  you can change this later&mdash;see [Moving forms]() below).

Locate that page's file in the `py/` directory. It will probably be called
  `page_[page-name].py`.

Open the file in the text editor of your choice, such as [atom](http://atom.io),
  gedit, TextEdit, or Notepad. (Note: Do not open it in a word processor.)

### 2) Define the new form

For now, I am going to refer to the form type as "topic," but you can name it
  whatever you want.

Go to the bottom of the file (or wherever you'd like, as long as it's not in the
  middle of another method) and add the following lines of code: (explained below)

```{Python}
def update_topic(self):
    self.topic_window = tk.Toplevel()
    self.topic_window.title("Log Topic")
    topic = Form(self.topic_window)
```

Okay, let's break that down:

```
def update_topic(self):
```

This defines the method that makes the form. It makes it so that you can call
    `self.update_topic()` later and have all this code execute. **Make sure
    all the code from this form that follows this line is indented.**  
The "`self`" part means that it executes the code with respect to its object,
    in this case, the notebook page.

```
self.topic_window = tk.Toplevel()
```

This tells it to make a separate window (called a Toplevel) called topic_window
    for the form to be housed in.

```
self.topic_window.title("Log Topic")
```

This gives the window a title. You can change "Log Topic" to whatever you want.

```
topic = Form(self.topic_window)
```

This says that we are putting an object of class **Form** (as defined by
    form_general.py) in the window self.topic_window, and calling that Form "topic."

### 3) Add fields to your form

So now you have an empty form. You probably want to add some fields to it for
    collecting data. The **Form** class has several methods for adding fields to
    your form. These are currently: `add_entry`, `add_date_time`,
    `add_scale`, and `add_numeric`. You can add as many of these as you want, in
    whatever order you want. Just add one per line, and keep the same indentation
    level going from the previous lines.

They differ in function, but calling them is largely the same:

```
topic.add_FIELD_TYPE(label, name)
```

(Replace "FIELD_TYPE" with the actual type of field you're adding.)

`label` is the text that will appear in the form for the user to see  
`name` is what the field is called in the data output file. You may want to use
    names that are consistent across forms (e.g. 'when' or 'spoons'), so that
    you can use the data without much pre-processing.

#### The specific methods:

```
topic.add_entry(label, name)
```

This adds a one-line text box.

```
topic.add_date_time(label, name)
```

This adds a row of Spinboxes for recording the date and time. It defaults to the
    user's date/time.

```
topic.add_scale(label, name, min_=0, max_=100)
```

This adds a slider for picking a numeric value within a range. You do not need
    to include the `min_` and `max_` values unless you want the range to be
    something other than 0&ndash;100.

```
topic.add_numeric(label, name)
```

This adds a Spinbox for users to add a specific numeric value.


### 4) Finish up the form

After all of the fields, add one more line:

```
topic.populate()
```

This adds the fields and buttons that are at the bottom of every form: the notes
    box, the tags box, and the submit and close buttons.

### 5) Add a button for opening this form to the notebook page

Almost done! Go back up to the section called `def __init__(self, master)`.

Find the block of lines that say `self.new_button(...)`.

Either after this block, or somewhere in the middle (wherever you want your
    button to appear), add your own line:

```
self.new_button("Button Text", self.update_topic)
```

The "Button Text" is self-explanatory: this is what the button will say.  
The `self.update_topic` refers to the method you defined in step 2. This points
    it to the code that will run when someone clicks the button.

**That's all!**

### An example form

Here is an example of what the code for the form might look like, just to make
    all of this concrete. (Don't forget to add the button!)

```{Python}
def update_topic(self):
    self.topic_window = tk.Toplevel()
    self.topic_window.title("Log Topic")
    topic = Form(self.topic_window)
    topic.add_entry('Title:', 'title')
    topic.add_entry('Category:', 'category')
    topic.add_date_time('When:','when')
    topic.add_scale('Spoons:', 'spoons')
    topic.add_numeric('Exp. gained:', 'exp_gained')
    topic.populate()
```

## Editing, moving, or deleting a form

Once you have the creation down, the rest is easy.

Labels and output names can be edited simply by changing the values (the text)
    of the `label` and `name` arguments of the field.

Fields can be reordered by moving the lines around within the method.

Buttons can be reordered by moving the `new_button` lines around in the
    `__init__` method.

To delete a form, rememeber to delete (or, more typically, comment out) *both*
    its method and its `new_button` line.

To move a form to a different page, copy *both* its method and its `new_button`
    line from one file to the other, and delete/comment out the one in the original.
