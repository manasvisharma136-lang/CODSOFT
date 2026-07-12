import tkinter as tk
from tkinter import messagebox


class TodoApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Modern To-Do List")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e")  # Sleek dark background
        self.root.resizable(False, False)

        # Title Label
        self.title_label = tk.Label(
            root,
            text="My To-Do List",
            font=("Helvetica", 24, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4",
        )
        self.title_label.pack(pady=20)

        # Input Frame (Entry field + Add button)
        self.input_frame = tk.Frame(root, bg="#1e1e2e")
        self.input_frame.pack(padx=20, pady=10, fill="x")

        self.task_entry = tk.Entry(
            self.input_frame,
            font=("Helvetica", 14),
            bg="#313244",
            fg="#cdd6f4",
            insertbackground="#cdd6f4",  # Cursor color
            bd=0,
            highlightthickness=1,
            highlightbackground="#45475a",
            highlightcolor="#89b4fa",
        )
        self.task_entry.pack(side="left", fill="x", expand=True, ipady=8, padx=(0, 10))
        # Bind the Enter key to automatically add a task
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = tk.Button(
            self.input_frame,
            text="Add Task",
            font=("Helvetica", 12, "bold"),
            bg="#a6e3a1",  # Soft pastel green
            fg="#11111b",
            bd=0,
            padx=15,
            cursor="hand2",
            command=self.add_task,
        )
        self.add_button.pack(side="right", ipady=6)

        # Tasks Listbox Frame
        self.list_frame = tk.Frame(root, bg="#1e1e2e")
        self.list_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Listbox for tasks
        self.task_listbox = tk.Listbox(
            self.list_frame,
            font=("Helvetica", 14),
            bg="#181825",
            fg="#cdd6f4",
            selectbackground="#45475a",
            selectforeground="#f5e0dc",
            bd=0,
            activestyle="none",
            highlightthickness=0,
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side="right", fill="y")

        # Link listbox and scrollbar together
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Action Buttons Frame (Complete & Delete)
        self.action_frame = tk.Frame(root, bg="#1e1e2e")
        self.action_frame.pack(padx=20, pady=20, fill="x")

        self.complete_button = tk.Button(
            self.action_frame,
            text="✓ Mark Completed",
            font=("Helvetica", 11, "bold"),
            bg="#89b4fa",  # Soft blue
            fg="#11111b",
            bd=0,
            cursor="hand2",
            command=self.complete_task,
        )
        self.complete_button.pack(side="left", fill="x", expand=True, padx=(0, 5), ipady=8)

        self.delete_button = tk.Button(
            self.action_frame,
            text="🗑 Delete Task",
            font=("Helvetica", 11, "bold"),
            bg="#f38ba8",  # Soft red
            fg="#11111b",
            bd=0,
            cursor="hand2",
            command=self.delete_task,
        )
        self.delete_button.pack(side="right", fill="x", expand=True, padx=(5, 0), ipady=8)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text != "":
            self.task_listbox.insert(tk.END, f"  ○ {task_text}")
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You cannot add an empty task!")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            current_text = self.task_listbox.get(selected_index)

            # Check if it's already completed to prevent duplicate checkmarks
            if "✓" not in current_text:
                # Remove the initial circle icon and add a checkmark + strikethrough effect via unicode
                clean_text = current_text.replace("  ○ ", "")
                strikethrough_text = "".join([c + "\u0336" for c in clean_text])
                completed_text = f"  ✓ {strikethrough_text}"

                # Update the listbox item
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, completed_text)
                # Apply a muted color to the completed item
                self.task_listbox.itemconfig(selected_index, fg="#6c7086")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()