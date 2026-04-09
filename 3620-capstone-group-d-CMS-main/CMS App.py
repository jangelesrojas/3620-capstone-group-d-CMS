import tkinter as tk
from tkinter import ttk


class ContactManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("1000x680")
        self.root.minsize(900, 620)
        self.root.configure(bg="#eef4ff")

        #   array to hold contacts
        self.contacts = []

        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("App.TFrame", background="#eef4ff")
        style.configure("Card.TFrame", background="#ffffff")

        style.configure("Header.TLabel",
                        background="#eef4ff",
                        foreground="#132238",
                        font=("Segoe UI", 22, "bold"))

        style.configure("SubHeader.TLabel",
                        background="#eef4ff",
                        foreground="#5d6b82",
                        font=("Segoe UI", 10))

        style.configure("CardTitle.TLabel",
                        background="#ffffff",
                        foreground="#1d2b3a",
                        font=("Segoe UI", 13, "bold"))

        style.configure("FieldLabel.TLabel",
                        background="#ffffff",
                        foreground="#546273",
                        font=("Segoe UI", 10))

        style.configure("Info.TLabel",
                        background="#ffffff",
                        foreground="#5d6b82",
                        font=("Segoe UI", 10))

        style.configure("Stats.TLabel",
                        background="#ffffff",
                        foreground="#3d4a5c",
                        font=("Segoe UI", 11))

        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=10)
        style.configure("Danger.TButton", font=("Segoe UI", 9, "bold"), padding=6)

    def build_ui(self):
        outer = ttk.Frame(self.root, style="App.TFrame", padding=24)
        outer.pack(fill="both", expand=True)

        header_frame = ttk.Frame(outer, style="App.TFrame")
        header_frame.pack(fill="x", pady=(0, 18))

        ttk.Label(header_frame,
                  text="Contact Management System",
                  style="Header.TLabel").pack(anchor="w")

        ttk.Label(header_frame,
                  text="Manage and organize your contacts efficiently",
                  style="SubHeader.TLabel").pack(anchor="w", pady=(4, 0))

        content = ttk.Frame(outer, style="App.TFrame")
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)

        self.build_add_contact_card(content)
        self.build_search_card(content)
        self.build_stats_card(outer)

    def build_add_contact_card(self, parent):
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        inner = ttk.Frame(card, style="Card.TFrame", padding=20)
        inner.pack(fill="both", expand=True)

        ttk.Label(inner, text="Add New Contact", style="CardTitle.TLabel").pack(anchor="w", pady=(0, 16))

        ttk.Label(inner, text="Name", style="FieldLabel.TLabel").pack(anchor="w", pady=(0, 6))
        self.name_entry = ttk.Entry(inner)
        self.name_entry.pack(fill="x", pady=(0, 14), ipady=6)

        ttk.Label(inner, text="Phone Number", style="FieldLabel.TLabel").pack(anchor="w", pady=(0, 6))
        self.phone_entry = ttk.Entry(inner)
        self.phone_entry.pack(fill="x", pady=(0, 14), ipady=6)

        ttk.Label(inner, text="Email Address", style="FieldLabel.TLabel").pack(anchor="w", pady=(0, 6))
        self.email_entry = ttk.Entry(inner)
        self.email_entry.pack(fill="x", pady=(0, 20), ipady=6)

        ttk.Button(inner, text="Add Contact", style="Primary.TButton",
                   command=self.add_contact).pack(fill="x")

    def build_search_card(self, parent):
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        inner = ttk.Frame(card, style="Card.TFrame", padding=20)
        inner.pack(fill="both", expand=True)
        inner.rowconfigure(2, weight=1)
        inner.columnconfigure(0, weight=1)

        ttk.Label(inner, text="Search Contacts", style="CardTitle.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 16))

        ttk.Entry(inner).grid(row=1, column=0, sticky="ew", pady=(0, 14), ipady=6)

        list_frame = ttk.Frame(inner, style="Card.TFrame")
        list_frame.grid(row=2, column=0, sticky="nsew")
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

        columns = ("name", "phone", "email")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=16)

        self.tree.heading("name", text="Name")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("email", text="Email")

        self.tree.column("name", width=170)
        self.tree.column("phone", width=130)
        self.tree.column("email", width=210)

        self.tree.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scrollbar.set)

        button_row = ttk.Frame(inner, style="Card.TFrame")
        button_row.grid(row=3, column=0, sticky="ew", pady=(14, 0))
        button_row.columnconfigure(0, weight=1)
        button_row.columnconfigure(1, weight=1)

        ttk.Button(button_row, text="Delete Selected",
                   style="Danger.TButton",
                   command=self.delete_contact).grid(row=0, column=0, sticky="ew", padx=(0, 6))

        ttk.Button(button_row, text="Clear Search").grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def build_stats_card(self, parent):
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.pack(fill="x", pady=(16, 0))

        self.stats_inner = ttk.Frame(card, style="Card.TFrame", padding=18)
        self.stats_inner.pack(fill="x")

        self.stats_label = ttk.Label(self.stats_inner, text="Total Contacts: 0", style="Stats.TLabel")
        self.stats_label.pack()

    #  FUNCTIONS (ARRAY LOGIC)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if not name or not phone or not email:
            print("Fill all fields")
            return

        contact = {"name": name, "phone": phone, "email": email}
        self.contacts.append(contact)

        self.update_table()

        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def update_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for contact in self.contacts:
            self.tree.insert("", "end",
                             values=(contact["name"],
                                     contact["phone"],
                                     contact["email"]))

        self.stats_label.config(text=f"Total Contacts: {len(self.contacts)}")

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            return

        index = self.tree.index(selected[0])
        self.contacts.pop(index)

        self.update_table()


# run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerUI(root)
    root.mainloop()
