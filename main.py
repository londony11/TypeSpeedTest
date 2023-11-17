"""TypeSpeedTest Desktop App"""
import tkinter as tk
from tkinter import ttk
import time
from data import EXAMPLE


class Windows(tk.Tk):
    """Application class."""

    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None
        ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.text_to_type = tk.StringVar(value=EXAMPLE)
        self.user_input = tk.StringVar()
        self.t0 = time.time()
        self.t1 = self.t0

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

        # Letter options for text window
        self.text_window.tag_configure("default", font="Arial 12")
        self.text_window.tag_configure("next", font="Arial 14 bold", foreground="pink")
        self.text_window.tag_configure("correct", font="Arial 14 bold", foreground="green")
        self.text_window.tag_configure("wrong", font="Arial 14 bold", foreground="red")

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

        # Insert default text, if empty, else update
        self.text_window.insert("end", self.text_to_type.get()[0], "next")
        self.text_window.insert("end", self.text_to_type.get()[1:], "default")

        # Disable window
        self.text_window.configure(state="disabled")


    def check_text(self, *args):
        """Check user input."""

        # Start timer
        if self.t0 == self.t1:
            self.t0 = time.time()

        # Enable window
        self.text_window.configure(state="normal")

        # Update text window
        for count, char in enumerate(self.user_input.get()):

            # Check if finished typing
            if count < len(self.text_to_type.get())-1:
                # Delete actual character for update
                self.text_window.delete(f"1.{count}", f"1.{count+2}")

                # Evaluate user input and insert result
                if char == self.text_to_type.get()[count]:
                    self.text_window.insert(f"1.{count}", char, "correct")
                else:
                    self.text_window.insert(f"1.{count}", self.text_to_type.get()[count], "wrong")

                # Highlight next character
                self.text_window.insert(f"1.{count+1}", self.text_to_type.get()[count+1], "next")
                self.text_window.delete(f"1.{count+2}", "end")
                self.text_window.insert(
                    f"1.{count+2}",
                    self.text_to_type.get()[count+2:],
                    "default"
                    )
            elif count == len(self.text_to_type.get())-1:
                # Delete actual character for update
                self.text_window.delete(f"1.{count}", "end")

                # Evaluate user input and insert result
                if char == self.text_to_type.get()[count]:
                    self.text_window.insert(f"1.{count}", char, "correct")
                    self.text_window.insert("end", "\n\nFinished", "default")
                    self.t1 = time.time()
                else:
                    self.text_window.insert(f"1.{count}", self.text_to_type.get()[count], "wrong")
            else:
                self.text_window.insert("end", char, "wrong")


        # Disable window
        self.text_window.configure(state="disabled")



def main():
    """Main function"""
    app = Windows()
    app.show_text_to_type()
    app.user_input.trace_add("write", app.check_text)
    app.mainloop()


if __name__ == "__main__":
    main()
