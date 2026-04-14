# 📇 Contact Management System

## 🚀 Overview

This project is a **Contact Management System** built using **Python 🐍 and Tkinter 🖥️**.
It allows users to efficiently manage contacts by performing operations like adding, deleting, searching, and sorting.

The system demonstrates the use of **multiple data structures** to optimize performance.

---

## ✨ Features

* ➕ Add new contacts (name, phone, email)
* ❌ Delete existing contacts
* 🔍 Search contacts by name, phone, or email
* 🔤 Sort contacts alphabetically (A–Z)
* 📊 Display contacts in a user-friendly table
* 🚫 Prevent duplicate phone numbers
* ⚡ Real-time search filtering

---

## 🧠 Data Structures Used

### 📦 1. List (Array)

* Stores all contacts
* Used for display and iteration

### ⚡ 2. Hash Table

* Fast lookup using phone number
* Handles collisions using chaining
* ⏱️ Average Time: **O(1)**

### 🌳 3. Binary Search Tree (BST)

* Maintains sorted contacts by name
* Uses inorder traversal for A–Z display
* ⏱️ Average Time: **O(log n)**

---

## 🏗️ System Design

The system uses a hybrid architecture:

* 📦 List → stores all data
* ⚡ Hash Table → enables fast search
* 🌳 BST → enables sorting

This ensures efficient handling of different operations.

---

## ⏱️ Time Complexity

| ⚙️ Operation   | 📊 Structure      | ⏱️ Complexity         |
| -------------- | ----------------- | --------------------- |
| Add Contact    | List + Hash + BST | O(1) + O(log n)       |
| Delete Contact | List + Hash + BST | O(n)                  |
| Search Contact | Hash Table / Scan | O(1) avg / O(n) worst |
| Sort Contacts  | BST Inorder       | O(n)                  |

---

## 🖥️ User Interface

The GUI is built using **Tkinter** and includes:

* 🟦 Left Panel → Add Contact
* 🔍 Right Panel → Search & Display
* 📊 Bottom Panel → Statistics

The interface is simple, clean, and user-friendly.

---

## 🛡️ Error Handling & Validation

* ⚠️ Prevents empty inputs
* 🚫 Prevents duplicate phone numbers
* 📢 Shows warning messages for invalid actions
* ❗ Confirmation before deletion

---

## 🔧 Future Improvements

* ✏️ Add update/edit contact feature
* 💾 Add database (MongoDB/PostgreSQL)
* 📧 Validate email and phone formats
* ⚡ Optimize search further
* 🌳 Use balanced BST (AVL/Red-Black Tree)
* 🧪 Add unit testing

---

## ▶️ How to Run

### 1️⃣ Install Python

Make sure Python 3 is installed.

### 2️⃣ Save the file

Save your file as:

```bash
contact_manager.py
```

### 3️⃣ Run in Terminal

```bash
python3 contact_manager.py
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* 🧠 Practical use of data structures
* ⚡ Performance optimization
* 🖥️ GUI development with Tkinter
* 🏗️ System design thinking

---

## 📌 Conclusion

This project shows how combining **multiple data structures** improves performance and usability in real-world applications.


