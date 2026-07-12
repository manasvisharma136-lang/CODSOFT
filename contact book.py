import tkinter as tk
from tkinter import messagebox, ttk

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Modern Contact Book")
        self.root.geometry("650x450")
        self.root.configure(bg="#f5f6fa")
        
        # In-memory dictionary to store contacts
        self.contacts = {}
        
        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("Treeview", rowheight=25, font=("Arial", 10))
        self.style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        
        self.create_widgets()

    def create_widgets(self):
        # --- LEFT PANEL: Input Form ---
        form_frame = tk.Frame(self.root, bg="#ffffff", bd=1, relief=tk.SOLID, padx=15, pady=15)
        form_frame.place(x=20, y=20, width=240, height=410)
        
        tk.Label(form_frame, text="CONTACT INFO", font=("Arial", 12, "bold"), bg="#ffffff", fg="#2f3640").pack(anchor="w", pady=(0, 15))
        
        tk.Label(form_frame, text="Name:", bg="#ffffff", fg="#718093").pack(anchor="w")
        self.ent_name = tk.Entry(form_frame, font=("Arial", 10), bd=1, relief=tk.SOLID)
        self.ent_name.pack(fill="x", pady=(0, 10), ipady=4)
        
        tk.Label(form_frame, text="Phone:", bg="#ffffff", fg="#718093").pack(anchor="w")
        self.ent_phone = tk.Entry(form_frame, font=("Arial", 10), bd=1, relief=tk.SOLID)
        self.ent_phone.pack(fill="x", pady=(0, 10), ipady=4)
        
        tk.Label(form_frame, text="Email:", bg="#ffffff", fg="#718093").pack(anchor="w")
        self.ent_email = tk.Entry(form_frame, font=("Arial", 10), bd=1, relief=tk.SOLID)
        self.ent_email.pack(fill="x", pady=(0, 20), ipady=4)
        
        # Form Buttons
        btn_add = tk.Button(form_frame, text="Add / Update", bg="#4cd137", fg="white", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.add_contact)
        btn_add.pack(fill="x", pady=5, ipady=6)
        
        btn_delete = tk.Button(form_frame, text="Delete Selected", bg="#e84118", fg="white", font=("Arial", 10, "bold"), bd=0, cursor="hand2", command=self.delete_contact)
        btn_delete.pack(fill="x", pady=5, ipady=6)
        
        btn_clear = tk.Button(form_frame, text="Clear Fields", bg="#718093", fg="white", font=("Arial", 10), bd=0, cursor="hand2", command=self.clear_entries)
        btn_clear.pack(fill="x", pady=5, ipady=4)

        # --- RIGHT PANEL: Search & Table Display (The cut-off section) ---
        display_frame = tk.Frame(self.root, bg="#f5f6fa")
        display_frame.place(x=280, y=20, width=350, height=410)
        
        # Search Box
        search_frame = tk.Frame(display_frame, bg="#f5f6fa")
        search_frame.pack(fill="x", pady=(0, 10))
        
        tk.Label(search_frame, text="Search:", bg="#f5f6fa", font=("Arial", 10, "bold")).pack(side="left", padx=(0, 5))
        self.ent_search = tk.Entry(search_frame, font=("Arial", 10), bd=1, relief=tk.SOLID)
        self.ent_search.pack(side="left", fill="x", expand=True, ipady=3)
        self.ent_search.bind("<KeyRelease>", self.search_contact)
        
        # Table View Grid
        columns = ("name", "phone", "email")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings")
        self.tree.heading("name", text="Name")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("email", text="Email")
        
        self.tree.column("name", width=100)
        self.tree.column("phone", width=100)
        self.tree.column("email", width=140)
        
        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.get_selected_row)

    # --- ACTION METHODS ---
    def add_contact(self):
        name = self.ent_name.get().strip()
        phone = self.ent_phone.get().strip()
        email = self.ent_email.get().strip()
        
        if not name:
            messagebox.showwarning("Error", "Name field is required!")
            return
            
        # Add to local dictionary
        self.contacts[name] = {"phone": phone if phone else "N/A", "email": email if email else "N/A"}
        self.update_table_view()
        self.clear_entries()

    def update_table_view(self, data_dict=None):
        # Wipe current view clean
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        # Target either the filtered search data or all data
        target_dict = data_dict if data_dict is not None else self.contacts
        for name, details in target_dict.items():
            self.tree.insert("", "end", values=(name, details["phone"], details["email"]))

    def delete_contact(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Error", "Please select a contact from the list to delete.")
            return
            
        row_values = self.tree.item(selected_item)["values"]
        name_key = row_values[0]
        
        if messagebox.askyesno("Confirm", f"Are you sure you want to delete {name_key}?"):
            del self.contacts[name_key]
            self.update_table_view()
            self.clear_entries()

    def search_contact(self, event):
        query = self.ent_search.get().strip().lower()
        if not query:
            self.update_table_view()
            return
            
        # Filter logic
        filtered_contacts = {
            name: details for name, details in self.contacts.items()
            if query in name.lower() or query in details["phone"] or query in details["email"].lower()
        }
        self.update_table_view(filtered_contacts)

    def get_selected_row(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            row_values = self.tree.item(selected_item)["values"]
            self.clear_entries()
            self.ent_name.insert(0, row_values[0])
            self.ent_phone.insert(0, row_values[1])
            self.ent_email.insert(0, row_values[2])

    def clear_entries(self):
        self.ent_name.delete(0, tk.END)
        self.ent_phone.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()