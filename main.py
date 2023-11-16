"""TypeSpeedTest Desktop App"""
import tkinter as tk
from tkinter import ttk
from data import EXAMPLE


class Windows(tk.Tk):
    """Application class."""


    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.text_to_type = tk.StringVar(value=EXAMPLE)
        self.user_input = tk.StringVar()

        # Title
        self.title("Type speed test")

        # Frame
        self.mainframe = ttk.Frame(self, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky="nwes")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Text for text tp write
        ttk.Label(self.mainframe, text="Text to type:").grid(column=0, row=0)
        self.text_window = tk.Text(self.mainframe, height=5, width=35, wrap="word")
        self.text_window.configure(state="disabled")
        self.text_window.grid(column=0, row=1, sticky="we")

        # Text entry
        ttk.Label(self.mainframe, text="User input:").grid(column=0, row=2)
        self.user_input_window = ttk.Entry(self.mainframe, textvariable=self.user_input, width=35)
        self.user_input_window .grid(column=0, row=3, sticky="we")

        # Add padding to widget
        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.user_input_window.focus()

    def show_text_to_type(self):
        """Show text function"""

        # Enable window
        self.text_window.configure(state="normal")

        # Letter options
        self.text_window.tag_configure("default", font="Arial 12")
        self.text_window.tag_configure("next", font="Arial 14 bold", foreground="green")
        self.text_window.tag_configure("correct", font="Arial 12", background="green")

        # Insert default text
        self.text_window.insert("end", self.text_to_type.get()[0], "next")
        self.text_window.insert("end", self.text_to_type.get()[1:], "default")

        # Disable window
        self.text_window.configure(state="disabled")


    def check_text(self):
        """Check user input."""
        for count, char in enumerate(self.user_input.get()):
            if char == self.text_to_type.get()[count]:
                print("Hello")


def main():
    """Main function"""
    app = Windows()
    app.show_text_to_type()
    app.check_text()
    app.mainloop()


if __name__ == "__main__":
    main()
