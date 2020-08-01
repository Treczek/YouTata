import tkinter as tk


class TextInfo:
    def __init__(self, parent, window_title='window', text='a text field', label=None):

        self.top = tk.Toplevel(parent)
        self.parent = parent
        self.window_title = window_title
        self.textfield = text

        # set window title
        if window_title:
            self.top.title(window_title)

        # add label if given
        if label:
            tk.Label(self.top, text=window_title).grid(row=0)

        # create the text field
        self.textField = tk.Text(self.top, width=20, height=2, wrap=tk.NONE)
        if text:
            self.textField.insert(1.0, text)
        self.textField.grid(row=1)

        # create the ok button
        b = tk.Button(self.top, text="OK", command=self.ok)
        b.grid(row=2)

    def ok(self):
        self.top.destroy()