import tkinter as tk


class Calculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Modern Calculator")
        self.root.geometry("350x500")
        self.root.configure(bg="#17171c")  # Dark background
        self.root.resizable(False, False)

        self.equation = ""

        # Display Screen
        self.display = tk.Entry(
            root,
            font=("Arial", 28),
            bg="#17171c",
            fg="#ffffff",
            bd=0,
            justify="right",
        )
        self.display.pack(fill="both", ipadx=8, ipady=25, padx=10, pady=20)
        self.display.insert(0, "0")

        # Button Container
        self.grid_frame = tk.Frame(root, bg="#17171c")
        self.grid_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Configure grid rows and columns to expand equally
        for i in range(5):
            self.grid_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_frame.columnconfigure(i, weight=1)

        self.create_buttons()

    def create_buttons(self):
        # Layout layout: (Text, Row, Column, BG Color, FG Color)
        buttons = [
            ("C", 0, 0, "#4e505f", "#ffffff"),
            ("(", 0, 1, "#4e505f", "#ffffff"),
            (")", 0, 2, "#4e505f", "#ffffff"),
            ("/", 0, 3, "#ff9f0a", "#ffffff"),
            ("7", 1, 0, "#2e2f38", "#ffffff"),
            ("8", 1, 1, "#2e2f38", "#ffffff"),
            ("9", 1, 2, "#2e2f38", "#ffffff"),
            ("*", 1, 3, "#ff9f0a", "#ffffff"),
            ("4", 2, 0, "#2e2f38", "#ffffff"),
            ("5", 2, 1, "#2e2f38", "#ffffff"),
            ("6", 2, 2, "#2e2f38", "#ffffff"),
            ("-", 2, 3, "#ff9f0a", "#ffffff"),
            ("1", 3, 0, "#2e2f38", "#ffffff"),
            ("2", 3, 1, "#2e2f38", "#ffffff"),
            ("3", 3, 2, "#2e2f38", "#ffffff"),
            ("+", 3, 3, "#ff9f0a", "#ffffff"),
            ("0", 4, 0, "#2e2f38", "#ffffff"),
            (".", 4, 1, "#2e2f38", "#ffffff"),
            ("⌫", 4, 2, "#2e2f38", "#ffffff"),
            ("=", 4, 3, "#ff9f0a", "#ffffff"),
        ]

        for text, row, col, bg, fg in buttons:
            # Lambda keeps track of the specific character passed to the function
            action = lambda x=text: self.on_button_click(x)

            btn = tk.Button(
                self.grid_frame,
                text=text,
                bg=bg,
                fg=fg,
                font=("Arial", 18, "bold"),
                bd=0,
                relief="flat",
                activebackground="#424450",
                activeforeground="#ffffff",
                command=action,
            )
            # Sticky="nsew" makes the button fill the entire grid cell
            btn.grid(row=row, column=col, padx=3, pady=3, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.equation = ""
            self.update_display("0")
        elif char == "⌫":
            self.equation = self.equation[:-1]
            self.update_display(self.equation if self.equation else "0")
        elif char == "=":
            try:
                # Safely evaluate the string math expression
                result = str(eval(self.equation))
                # Truncate floats if they end in .0
                if result.endswith(".0"):
                    result = result[:-2]
                self.update_display(result)
                self.equation = result  # Allow continuing operations on the result
            except Exception:
                self.update_display("Error")
                self.equation = ""
        else:
            # Prevent leading zeros or consecutive operators depending on need
            if self.equation == "" and char in ["+", "*", "/", ")"]:
                return
            self.equation += str(char)
            self.update_display(self.equation)

    def update_display(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, value)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()