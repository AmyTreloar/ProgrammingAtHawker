The word "widget" is often used as an abstract name for an object, most often for something manufactured.
Modern GUI toolkits, tkinter included, are comprised of components that are referred to as "widgets."
All tkinter widgets have a lot in common, even though they may not look alike.

There aren't a lot of widgets in the tkinter toolkit, but using them wisely will allow you to create a variety of
useful graphical interfaces. Below are some important ones that you should know about now:

| Widget Type| Purpose|
|---|:--|
|Frame	|A container for other widgets. You can set the border and background color, and place other widgets inside of it|
|Toplevel	|A special kind of Frame that interacts directly with the windows manager. Toplevels will usually have a title bar, and features to interact with the window manager. The windows you see on your screen are mostly top-level windows, and your application can create additional Toplevel windows if it is set to do that|
|Button	|Users click on buttons to trigger some action. As you already know from the sample program you just entered and ran, clicks on the button can be translated into actions taken by your program (this is actually true of many widgets). Buttons usually have text inside of them, but they can also show graphics.|
|Checkbutton	|A special type of button that has two states; clicking change the state of the button from one to the other.|
|Label	|Labels are used to display pieces of text or images, usually ones that won't change during the execution of the application.|
|Entry	|Used to enter single lines of text and all kinds of input.|
|Listbox	|Used to display a set of choices. The user can select a single item or multiple items from the list. The Listbox can also be rendered as a set of radio buttons or checkboxes.|
|Scale	|Lets the user set numerical values by dragging a slider.|
|Text	|A multi-line formatted text widget, it allows the textual content to be "rich." It may also contain embedded images and Frames.|
|Message	|Similar to a Text, but can automatically wrap text to a particular width, or width and height.|
|Menu	|This is the base widget that you use to put a menu in your window (not all programs need one). It corresponds to the menu bar along the top of your program window, and can also be used to implement "popup" or "context" menus.|
|Menubutton	|Adds choices to your Menus.|
|Radiobutton	|Represents one of a set of mutually exclusive choices. Selecting one Radiobutton from a set, deselects any others.|
|Scrollbar	|Implements scrolling on a larger widget such as a Canvas, Listbox, or Text.|
|Canvas	|A surface on which you can draw graphs and/or plots, and also use as the basis of your own widgets.|

![Kitchen sink of widgets](https://github.com/carteras/testing/blob/master/Python/GUI/GUIElements/Widgets/kitchenSink.png)

# Problem

You need the user to select some sort of action.

## Solution

Use a button!

## Discussion

The Button widget is a standard tkinter widget used to implement various kinds of buttons. Buttons can contain text or images, and you can associate a Python function or method with each button. When the button is pressed, tkinter automatically calls that function or method.

The button can only display text in a single font, but the text may span more than one line. In addition, one of the characters can be underlined, for example to mark a keyboard shortcut. By default, the Tab key can be used to move to a button widget.

### When to use a button?

Simply put, button widgets are used to let the user say “do this now!,” where this is either given by the text on the button, or implied by the icon displayed in the button. Buttons are typically used in toolbars, in application windows, and to accept or dismiss data entered into a dialog box.

### Patterns

Plain buttons are pretty straightforward to use. All you have to do is to specify the button contents (text, bitmap, or image) and what function or method to call when the button is pressed:

```python
from tkinter import *

master = Tk()

def callback():
    print "click!"

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()
```

A button without a callback is pretty useless; it simply doesn’t do anything when you press the button. You might wish to use such buttons anyway when developing an application. In that case, it is probably a good idea to disable the button to avoid confusing your beta testers:

`b = Button(master, text="Help", state=DISABLED)`

If you don’t specify a size, the button is made just large enough to hold its contents. You can use the padx and pady option to add some extra space between the contents and the button border.

You can also use the height and width options to explicitly set the size. If you display text in the button, these options define the size of the button in text units. If you display bitmaps or images instead, they define the size in pixels (or other screen units). You can specify the size in pixels even for text buttons, but that requires some magic. Here’s one way to do it (there are others):

```python
f = Frame(master, height=32, width=32)
f.pack_propagate(0) # don't shrink
f.pack()

b = Button(f, text="Sure!")
b.pack(fill=BOTH, expand=1)
```

# Problem

You want the user to enter a single line of input

## Solution

Use the Entry widget!

## Discussion

The Entry widget is a standard tkinter widget used to enter or display a single line of text.

###When to use the Entry Widget

The entry widget is used to enter text strings. This widget allows the user to enter one line of text, in a single font.

To enter multiple lines of text, use the Text widget.

### Patterns

To add entry text to the widget, use the insert method. To replace the current text, you can call delete before you insert the new text.
```python
e = Entry(master)
e.pack()

e.delete(0, END)
e.insert(0, "a default value")
```

To fetch the current entry text use the get method:

`s = e.get()`

You can also bind the entry widget to a StringVar instance, and set or get the entry text via that variable:

```python
v = StringVar()
e = Entry(master, textvariable=v)
e.pack()

v.set("a default value")
s = v.get()
```

# Problem

## Solution

## Discussion