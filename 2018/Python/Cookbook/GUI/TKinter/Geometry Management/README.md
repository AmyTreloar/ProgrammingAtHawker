### Problem:

You need to organise your interface in rows and/or columns

### Solution:

Use Pack Geometry Manager


### Discussion

The Pack geometry manager packs widgets in rows or columns. You can use options like fill, expand, and side to control this geometry manager.

The manager handles all widgets that are packed inside the same master widget. The packing algorithm is simple, but a bit tricky to describe in words; imagine a sheet of some elastic material, with a very small rectangular hole in the middle. For each widget, in the order they are packed, the geometry manager makes the hole large enough to hold the widget, and then place it against a given inner edge (default is the top edge). It then repeats the process for all widgets. Finally, when all widgets have been packed into the hole, the manager calculates the bounding box for all widgets, makes the master widget large enough to hold all widgets, and moves them all to the master.

### When to use the Pack Manager

Compared to the grid manager, the pack manager is somewhat limited, but it’s much easier to use in a few, but quite common situations:

Put a widget inside a frame (or any other container widget), and have it fill the entire frame
Place a number of widgets on top of each other
Place a number of widgets side by side

### Patterns

Using this code as a base.

 ```python
from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack()

for i in range(20):
    listbox.insert(END, str(i))

mainloop()
```

The default behaviour for a listbox is made large enough to show 10 items. But this listbox has twice as many of them.

If the user attempts to show them all by resizing the window, tkinter will add padding around the listbox.

To make the widget fill the entire parent, also if the user resizes the window, add fill and expand to the options:

```python
from tkinter import *

root = Tk()

listbox = Listbox(root)
listbox.pack(fill=BOTH, expand=1)

for i in range(20):
    listbox.insert(END, str(i))

mainloop()
```

####
Placing widgets on top of each other:

```python
from Tkinter import *

root = Tk()

w = Label(root, text="Red", bg="red", fg="white")
w.pack()
w = Label(root, text="Green", bg="green", fg="black")
w.pack()
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack()

mainloop()
```

Fill the width of the widgets to be as wide as the parent widget:

```python
from Tkinter import *

root = Tk()

w = Label(root, text="Red", bg="red", fg="white")
w.pack(fill=X)
w = Label(root, text="Green", bg="green", fg="black")
w.pack(fill=X)
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack(fill=X)

mainloop()
```

#### Placing a number of widgets side by side
To pack widgets side by side, use the side option. If you wish to make the widgets as high as the parent,
use the fill=Y option too:

```python
from Tkinter import *

root = Tk()

w = Label(root, text="Red", bg="red", fg="white")
w.pack(side=LEFT)
w = Label(root, text="Green", bg="green", fg="black")
w.pack(side=LEFT)
w = Label(root, text="Blue", bg="blue", fg="white")
w.pack(side=LEFT)

mainloop()
```

### Problem:

You want to create an interface that has a layer of 2-dimensional elements. Like nested tables.

### Solution:

Use Grid geometry manager!

### Discussion

The Grid geometry manager puts the widgets in a 2-dimensional table.
The master widget is split into a number of rows and columns, and each “cell” in the resulting table can hold a widget.

####When to use the Grid Manager

The grid manager is the most flexible of the geometry managers in Tkinter. If you don’t want to learn how and when to
use all three managers, you should at least make sure to learn this one.

The grid manager is especially convenient to use when designing dialog boxes. If you’re using the packer for that
purpose today, you’ll be surprised how much easier it is to use the grid manager instead. Instead of using lots of
extra frames to get the packing to work, you can in most cases simply pour all the widgets into a single container
widget, and use the grid manager to get them all where you want them.

Notice:

Never mix Grid and pack in the same master window. tkinter will happily spent the rest of your lifetime trying to
negotiate a solution that works for both managers.

#### Patterns

#### Simple grid:

Using the grid manager is easy. Just create the widgets, and use the grid method to tell the manager in which row and
column to place them. You don’t have to specify the size of the grid beforehand; the manager automatically determines
that from the widgets in it.

```python
    Label(master, text="First").grid(row=0)
    Label(master, text="Second").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
```
Empty rows and columns are ignored. The result would have been the same if you had placed the widgets in row 10 and 20
instead.

Note: that the widgets are centered in their cells. You can use the sticky option to change this; this option takes one
or more values from the set N, S, E, W. To align the labels to the left border, you could use W (west):

```python
    Label(master, text="First").grid(row=0, sticky=W)
    Label(master, text="Second").grid(row=1, sticky=W)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
```

You can also have the widgets span more than one cell. The columnspan option is used to let a widget span more than one
column, and the rowspan option lets it span more than one row. The following code creates the layout shown in the
previous section:

```python
    label1.grid(sticky=E)
    label2.grid(sticky=E)

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    checkbutton.grid(columnspan=2, sticky=W)

    image.grid(row=0, column=2, columnspan=2, rowspan=2,
               sticky=W+E+N+S, padx=5, pady=5)

    button1.grid(row=2, column=2)
    button2.grid(row=2, column=3)
```

There are plenty of things to note in this example. First, no position is specified for the label widgets. In this case,
the column defaults to 0, and the row to the first unused row in the grid. Next, the entry widgets are positioned as
usual, but the checkbutton widget is placed on the next empty row (row 2, in this case), and is configured to span two
columns. The resulting cell will be as wide as the label and entry columns combined. The image widget is configured to
span both columns and rows at the same time. The buttons, finally, is packed each in a single cell: