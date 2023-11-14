"""TypeSpeedTest Desktop App"""
from tkinter import *
from tkinter import ttk
from data import EXAMPLE


class TypeTest:
    """Application class."""

    def __init__(self, root, text, user_input):

        # Title
        root.title("Type speed test")

        # Frame
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        # Text for text tp write
        ttk.Label(mainframe, text="Text to type:").grid(column=0, row=0)
        text_window = Text(mainframe, height=5, width=35, wrap="word")

        # Letter options
        text_window.tag_configure("default", font="Arial 12")
        text_window.tag_configure("next", font="Arial 14 bold", foreground="green")
        text_window.tag_configure("correct", font="Arial 12", background="green")

        # Insert default text
        text_window.insert("end", text.get()[0], "next")
        text_window.insert("end", text.get()[1:], "default")
        text_window.configure(state="disabled")
        text_window.grid(column=0, row=1, sticky=(W, E))

        # Text entry
        ttk.Label(mainframe, text="User input:").grid(column=0, row=2)
        user_input_window = ttk.Entry(mainframe, textvariable=user_input, width=35)
        user_input_window .grid(column=0, row=3, sticky=(W, E))

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        user_input_window.focus()


    def check_text(self, *args):
        """Check user input."""
        # for count, char in enumerate(user_input.get()):
        #     if char == text.get()[count]:
        #         pass
        


root = Tk()
text = StringVar(value=EXAMPLE)
user_input = StringVar()
app = TypeTest(root, text, user_input)
user_input.trace_add("write", TypeTest.check_text)
root.mainloop()
