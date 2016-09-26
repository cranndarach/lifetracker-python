# Creating new Pages

The main LifeTracker interface is held by a
  [tkinter](https://docs.python.org/3/library/tkinter.html) Notebook, with separate
  pages for different categories.

This tutorial will show you how to add a new page to the notebook.

### 1) Create a new file for the page

For the sake of example, let's call the page "MyPage."

Create a file in the `py/` folder called `page_mypage.py`. Technically you do
    not have to use the "page_*" style, but it makes it easier to organize.

### 2) Create the page's class

Add the following lines of code to the file:

```{Python}
import tkinter as tk
from form_general import Form
from page import Page

class MyPage(Page):
    def __init__(self, master):
        super(MyPage, self).__init__()
        self.master = master
```

Make sure to replace both occurrences of "MyPage" with the page's actual name.

### 3) Add some forms

See the "Creating a form" section of the [Forms]() page if you need help with this.

### 4) Add it to the notebook

Now you have a page, but you haven't actually put it in the notebook yet.

Go over to `py/main.py`.

First, import the module you just created. Under the "import" lines, add:

```{Python}
from page_mypage import MyPage
```

Make sure you update that to reflect the file name and the class name (the
    page's name).

Now, go to the `__init__` method, and find the chunk of code that starts with

```{Python}
self.nb = ttk.Notebook(self.master)
self.main = MainPage(self.nb)
...
```

Instantiate the page by adding the following line (with the usual name modifications):

```{Python}
self.mypage = MyPage(self.nb)
```

Then jump to the next chunk and add it to the notebook with:

```{Python}
self.nb.add(self.mypage, text='My Page')
```

The `text` argument is the title of the tab.

**And you're done!**
