import tkinter as tk
from tkinter import ttk, messagebox


# ─────────────────────────────────────────────────────
#  HASH TABLE  (Chapter 5 - Hashing)
#  Purpose: efficient search by phone number or email
#  Time complexity: O(1) average - Chapter 2 Algorithm Analysis
# ─────────────────────────────────────────────────────

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        # each bucket is a list to handle collisions via chaining
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash(self, key):
        # add up ascii value of each character then mod by capacity
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.capacity

    def insert(self, name, phone, email):
        # phone is the key for the hash table
        index = self._hash(phone)
        bucket = self.buckets[index]
        # check if phone already exists and update it
        for i in range(len(bucket)):
            if bucket[i][0] == phone:
                bucket[i] = (phone, name, email)
                return
        # otherwise append new entry to bucket
        bucket.append((phone, name, email))

    def remove(self, phone):
        index = self._hash(phone)
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == phone:
                bucket.pop(i)
                return

    def search_all(self, query):
        # search by name, phone, or email - O(n) worst case
        query = query.lower()
        matches = []
        seen = []
        for bucket in self.buckets:
            for phone, name, email in bucket:
                if query in name.lower() or query in phone or query in email.lower():
                    if phone not in seen:
                        matches.append((name, phone, email))
                        seen.append(phone)
        return matches


# ─────────────────────────────────────────────────────
#  BINARY SEARCH TREE  (Chapter 4 - Trees)
#  Purpose: sort contacts alphabetically by name
#  Time complexity: O(log n) average - Chapter 2 Algorithm Analysis
# ─────────────────────────────────────────────────────

class BSTNode:
    def __init__(self, name, phone, email):
        self.name  = name
        self.phone = phone
        self.email = email
        self.left  = None   # smaller names go left
        self.right = None   # bigger names go right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, name, phone, email):
        new_node = BSTNode(name, phone, email)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            # go left if name is alphabetically smaller
            if name.lower() < current.name.lower():
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            # go right if name is alphabetically bigger
            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right

    def delete(self, name):
        self.root = self._delete_node(self.root, name)

    def _delete_node(self, node, name):
        if node is None:
            return None
        if name.lower() < node.name.lower():
            node.left = self._delete_node(node.left, name)
        elif name.lower() > node.name.lower():
            node.right = self._delete_node(node.right, name)
        else:
            # case 1: no children - just remove the node
            if node.left is None and node.right is None:
                return None
            # case 2: one child - replace node with its child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # case 3: two children - find inorder successor
            # inorder successor is the leftmost node in the right subtree
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.name  = successor.name
            node.phone = successor.phone
            node.email = successor.email
            node.right = self._delete_node(node.right, successor.name)
        return node

    def inorder(self):
        # left -> root -> right gives A to Z alphabetical order
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node is None:
            return
        self._inorder_helper(node.left, result)
        result.append((node.name, node.phone, node.email))
        self._inorder_helper(node.right, result)


# ─────────────────────────────────────────────────────
#  CONTACT MANAGER UI
#  UI built by teammate - data structures integrated below
# ─────────────────────────────────────────────────────

class ContactManagerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("1000x680")
        self.root.minsize(900, 620)
        self.root.configure(bg="#eef4ff")

        # array to store contacts (Chapter 3 - Lists)
        self.contacts = []

        # hash table for fast search (Chapter 5 - Hashing)
        self.hash_table = HashTable()

        # bst for alphabetical sorting (Chapter 4 - Trees)
        self.bst = BinarySearchTree()

        self.view_mode = "all"

        # keeps track of which contact is being edited
        self.editing_phone = None
        self.editing_name = None

        self.setup_styles()
        self.build_ui()

    def _insert_all(self, name, phone, email):
        # add to array, hash table, and bst at the same time
        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.hash_table.insert(name, phone, email)
        self.bst.insert(name, phone, email)

    def _remove_all(self, name, phone):
        # remove from all three data structures
        self.contacts = [c for c in self.contacts if c["phone"] != phone]
        self.hash_table.remove(phone)
        self.bst.delete(name)

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

        # sort button - triggers BST inorder traversal
        ttk.Button(inner, text="Sort A-Z (BST)",
                   command=self.show_sorted).pack(fill="x", pady=(10, 0))

        # update button stays hidden until a contact is double-clicked
        self.update_button = ttk.Button(
            inner,
            text="Update Contact",
            style="Primary.TButton",
            command=self.update_contact
        )

    def build_search_card(self, parent):
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.grid(row=0, column=1, sticky="nsew", padx=(10, 0))

        inner = ttk.Frame(card, style="Card.TFrame", padding=20)
        inner.pack(fill="both", expand=True)
        inner.rowconfigure(2, weight=1)
        inner.columnconfigure(0, weight=1)

        ttk.Label(inner, text="Search Contacts",
                  style="CardTitle.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 16))

        # search bar - uses hash table on each keystroke
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.on_search)
        ttk.Entry(inner, textvariable=self.search_var).grid(
            row=1, column=0, sticky="ew", pady=(0, 14), ipady=6)

        list_frame = ttk.Frame(inner, style="Card.TFrame")
        list_frame.grid(row=2, column=0, sticky="nsew")
        list_frame.rowconfigure(0, weight=1)
        list_frame.columnconfigure(0, weight=1)

        columns = ("name", "phone", "email")
        self.tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=16)

        self.tree.heading("name",  text="Name")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("email", text="Email")

        self.tree.column("name",  width=170)
        self.tree.column("phone", width=130)
        self.tree.column("email", width=210)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.bind("<Double-1>", self.load_contact_for_edit)

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

        ttk.Button(button_row, text="Clear Search",
                   command=self.clear_search).grid(row=0, column=1, sticky="ew", padx=(6, 0))

    def build_stats_card(self, parent):
        card = tk.Frame(parent, bg="#ffffff", bd=1, relief="solid")
        card.pack(fill="x", pady=(16, 0))

        stats_inner = ttk.Frame(card, style="Card.TFrame", padding=18)
        stats_inner.pack(fill="x")

        self.stats_label = ttk.Label(stats_inner, text="Total Contacts: 0", style="Stats.TLabel")
        self.stats_label.pack()

        self.showing_label = ttk.Label(stats_inner, text="Showing: 0 results", style="Info.TLabel")
        self.showing_label.pack(pady=(6, 0))

    # ── Logic Functions ──

    def add_contact(self):
        name  = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name or not phone or not email:
            messagebox.showwarning("Missing Fields", "Please fill in all fields.")
            return

        # check for duplicate phone number
        for c in self.contacts:
            if c["phone"] == phone:
                messagebox.showwarning("Duplicate", "A contact with that phone number already exists.")
                return

        self._insert_all(name, phone, email)
        self.clear_form()

        self.view_mode = "all"
        self.update_table()

    def load_contact_for_edit(self, event):
        selected = self.tree.selection()
        if not selected:
            return

        values = self.tree.item(selected[0], "values")
        name, phone, email = values

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, name)

        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, phone)

        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, email)

        # stores the original contact so we know what to replace
        self.editing_name = name
        self.editing_phone = phone

        # update button appears under the sort button only while editing
        self.update_button.pack(fill="x", pady=(10, 0))

    def update_contact(self):
        if self.editing_phone is None:
            return

        new_name = self.name_entry.get().strip()
        new_phone = self.phone_entry.get().strip()
        new_email = self.email_entry.get().strip()

        if not new_name or not new_phone or not new_email:
            messagebox.showwarning("Missing Fields", "Please fill in all fields.")
            return

        # prevents changing to a phone number that already belongs to another contact
        for c in self.contacts:
            if c["phone"] == new_phone and c["phone"] != self.editing_phone:
                messagebox.showwarning("Duplicate", "A contact with that phone number already exists.")
                return

        # remove old contact from structures first
        self._remove_all(self.editing_name, self.editing_phone)

        # insert updated contact back in
        self._insert_all(new_name, new_phone, new_email)

        messagebox.showinfo("Updated", "Contact updated successfully.")

        self.clear_form()
        self.view_mode = "all"
        self.update_table()

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        self.editing_name = None
        self.editing_phone = None

        # hides update button again after edit is done
        self.update_button.pack_forget()

    def delete_contact(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select a contact to delete.")
            return

        values = self.tree.item(selected[0], "values")
        name  = values[0]
        phone = values[1]

        if messagebox.askyesno("Confirm Delete", f"Delete {name}?"):
            self._remove_all(name, phone)

            # if the deleted contact was being edited, reset the form
            if self.editing_phone == phone:
                self.clear_form()

            self.view_mode = "all"
            self.update_table()

    def on_search(self, *args):
        # hash table search triggers on every keystroke
        query = self.search_var.get().strip()
        if query == "":
            self.view_mode = "all"
            self.update_table()
            return
        self.view_mode = "search"
        results = self.hash_table.search_all(query)
        self.populate_tree(results)
        self.showing_label.config(text=f"Showing: {len(results)} results")

    def show_sorted(self):
        # bst inorder traversal returns contacts A to Z
        self.view_mode = "sorted"
        self.search_var.set("")
        sorted_contacts = self.bst.inorder()
        self.populate_tree(sorted_contacts)
        self.showing_label.config(text=f"Showing: {len(sorted_contacts)} results (A-Z)")

    def clear_search(self):
        self.search_var.set("")
        self.view_mode = "all"
        self.update_table()

    def update_table(self):
        if self.view_mode == "sorted":
            data = self.bst.inorder()
        else:
            data = [(c["name"], c["phone"], c["email"]) for c in self.contacts]
        self.populate_tree(data)
        self.stats_label.config(text=f"Total Contacts: {len(self.contacts)}")
        self.showing_label.config(text=f"Showing: {len(data)} results")

    def populate_tree(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for name, phone, email in data:
            self.tree.insert("", "end", values=(name, phone, email))


# run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerUI(root)
    root.mainloop()
