import tkinter as tk
from tkinter import ttk


class ContactManagerUI:
    def __init__(self, root):
        # basic window setup
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("1000x680")  # default size
        self.root.minsize(900, 620)  # dont let it get too small
        self.root.configure(bg="#eef4ff")  # background color

        # set styles and build UI
        self.setup_styles()
        self.build_ui()

    def setup_styles(self):
        # using ttk styles so everything looks a bit cleaner
        style = ttk.Style()
        style.theme_use("clam")  # looks nicer than default

        # app background
        style.configure("App.TFrame", background="#eef4ff")

        # card backgrounds
        style.configure("Card.TFrame", background="#ffffff")

        # main title
        style.configure(
            "Header.TLabel",
            background="#eef4ff",
            foreground="#132238",
            font=("Segoe UI", 22, "bold")
        )

        # subtitle under title
        style.configure(
            "SubHeader.TLabel",
            background="#eef4ff",
            foreground="#5d6b82",
            font=("Segoe UI", 10)
        )

        # card titles like "Add Contact"
        style.configure(
            "CardTitle.TLabel",
            background="#ffffff",
            foreground="#1d2b3a",
            font=("Segoe UI", 13, "bold")
        )

        # labels for inputs
        style.configure(
            "FieldLabel.TLabel",
            background="#ffffff",
            foreground="#546273",
            font=("Segoe UI", 10)
        )

        # smaller info text
        style.configure(
            "Info.TLabel",
            background="#ffffff",
            foreground="#5d6b82",
            font=("Segoe UI", 10)
        )

        # bottom stats text
        style.configure(
            "Stats.TLabel",
            background="#ffffff",
            foreground="#3d4a5c",
            font=("Segoe UI", 11)
        )

        # buttons
        style.configure("Primary.TButton", font=("Segoe UI", 10, "bold"), padding=10)
        style.configure("Danger.TButton", font=("Segoe UI", 9, "bold"), padding=6)

    def build_ui(self):
        # outer container (basically whole screen padding)
        outer = ttk.Frame(self.root, style="App.TFrame", padding=24)
        outer.pack(fill="both", expand=True)

        # header section
        header_frame = ttk.Frame(outer, style="App.TFrame")
        header_frame.pack(fill="x", pady=(0, 18))

        ttk.Label(
            header_frame,
            text="Contact Management System",
            style="Header.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header_frame,
            text="Manage and organize your contacts efficiently",
            style="SubHeader.TLabel"
        ).pack(anchor="w", pady=(4, 0))

        # main content area (2 columns)
        content = ttk.Frame(outer, style="App.TFrame")
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)
        content.rowconfigure(0, weight=1)

        # left = add contact
        self.build_add_contact_card(content)

        # right = search + list
        self.build_search_card(content)

        # bottom stats
        self.build_stats_card(outer)

    def build_add_contact_card(self, parent):
        # card container (left side)
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        inner = ttk.Frame(card, style="Card.TFrame", padding=20)
        inner.pack(fill="both", expand=True)

        # title
        ttk.Label(inner, text="Add New Contact", style="CardTitle.TLabel").pack(anchor="w", pady=(0, 16))

        # name input
        ttk.Label(inner, text="Name", style="FieldLabel.TLabel").pack(anchor="w", pady=(0, 6))
        ttk.Entry(inner).pack(fill="x", pady=(0, 14), ipady=6)

        # phone input
        ttk.Label(inner, text="Phone Number", style="FieldLabel.TLabel").pack(anchor="w", pady=(0, 6))
        ttk.Entry(inner).pack(fill="x", pady=(0, 14), ipady=6)

        # email input
        ttk.Label(inner, text="Email Address", style="FieldLabel.TLabel").pack(anchor="w", pady=(0, 6))
        ttk.Entry(inner).pack(fill="x", pady=(0, 20), ipady=6)

        # add button (no functionality yet)
        ttk.Button(inner, text="Add Contact", style="Primary.TButton").pack(fill="x")

    def build_search_card(self, parent):
        # card container (right side)
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        inner = ttk.Frame(card, style="Card.TFrame", padding=20)
        inner.pack(fill="both", expand=True)
        inner.rowconfigure(2, weight=1)
        inner.columnconfigure(0, weight=1)

        # title
        ttk.Label(inner, text="Search Contacts", style="CardTitle.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 16))

        # search bar
        ttk.Entry(inner).grid(row=1, column=0, sticky="ew", pady=(0, 14), ipady=6)

        # table area
        list_frame = ttk.Frame(inner, style="Card.TFrame")
        list_frame.grid(row=2, column=0, sticky="nsew")
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

        # table columns
        columns = ("name", "phone", "email")
        tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=16)

        # column headers
        tree.heading("name", text="Name")
        tree.heading("phone", text="Phone")
        tree.heading("email", text="Email")

        # column sizes
        tree.column("name", width=170)
        tree.column("phone", width=130)
        tree.column("email", width=210)

        tree.grid(row=0, column=0, sticky="nsew")

        # scrollbar for table
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=tree.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        tree.configure(yscrollcommand=scrollbar.set)

        # sample data so UI isnt empty taken directly from the figma
        sample_contacts = [
            ("Sarah Johnson", "(555) 123-4567", "sarah.j@example.com"),
            ("Michael Chen", "(555) 987-6543", "mchen@example.com"),
            ("Emily Davis", "(555) 555-0123", "emily.davis@example.com"),
        ]

        for contact in sample_contacts:
            tree.insert("", "end", values=contact)

        # buttons under table
        button_row = ttk.Frame(inner, style="Card.TFrame")
        button_row.grid(row=3, column=0, sticky="ew", pady=(14, 0))
        button_row.columnconfigure(0, weight=1)
        button_row.columnconfigure(1, weight=1)

        # delete button (no logic yet)
        ttk.Button(button_row, text="Delete Selected", style="Danger.TButton").grid(row=0, column=0, sticky="ew", padx=(0, 6))

        # clear search button (no logic yet)
        ttk.Button(button_row, text="Clear Search").grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def build_stats_card(self, parent):
        # bottom stats card
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.pack(fill="x", pady=(16, 0))

        inner = ttk.Frame(card, style="Card.TFrame", padding=18)
        inner.pack(fill="x")

        # static numbers for now (no logic)
        ttk.Label(inner, text="Total Contacts: 3", style="Stats.TLabel").pack()
        ttk.Label(inner, text="Showing: 3 results", style="Info.TLabel").pack(pady=(6, 0))


# run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerUI(root)
    root.mainloop()
