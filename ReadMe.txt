# Contact Management System

## Overview

This project is a **Contact Management System** developed using Python and Tkinter. It allows users to efficiently manage contact information by adding, deleting, searching, and sorting contacts.

The system integrates multiple data structures to optimize performance and demonstrate real-world applications of algorithms.


## Features

* Add new contacts (name, phone, email)
* Delete existing contacts
* Search contacts by name, phone, or email
* Sort contacts alphabetically (A–Z)
* Display contacts in a user-friendly table
* Prevent duplicate entries based on phone number
* Real-time search filtering


## Data Structures Used

### 1. List (Array)

* Stores all contacts in memory
* Used for iteration and display

### 2. Hash Table

* Enables efficient lookup by phone number
* Uses chaining to handle collisions
* Average time complexity: **O(1)**

### 3. Binary Search Tree (BST)

* Maintains contacts in sorted order by name
* Supports inorder traversal for A–Z display
* Average time complexity: **O(log n)**


## System Design

The system uses a hybrid approach:

* Contacts are stored in a list for general access
* A hash table is used for efficient searching
* A binary search tree is used for sorting

This design ensures that different operations are optimized for performance.

---

## Time Complexity

| Operation      | Data Structure          | Complexity            |
| -------------- | ----------------------- | --------------------- |
| Add Contact    | List + Hash Table + BST | O(1) + O(log n)       |
| Delete Contact | List + Hash Table + BST | O(n)                  |
| Search Contact | Hash Table / Scan       | O(1) avg / O(n) worst |
| Sort Contacts  | BST Inorder             | O(n)                  |

---

## User Interface

The application provides a graphical user interface built with Tkinter:

* Left panel: Add new contact
* Right panel: Search and display contacts
* Bottom section: Statistics (total contacts, results shown)

The interface is designed to be simple and intuitive.

---

## Error Handling and Validation

The system includes:

* Validation for empty input fields
* Duplicate phone number prevention
* User prompts for invalid actions (e.g., deleting without selection)
* Confirmation dialogs for deletion

## Possible Improvements

* Add update/edit contact functionality
* Implement persistent storage (database or file system)
* Improve search efficiency for partial matches
* Add input format validation (email and phone)
* Balance BST using AVL or Red-Black Tree
* Add unit and integration testing



## How to Run

1. Ensure Python 3 is installed
2. Save the file as `contact_manager.py`
3. Open terminal and navigate to the file location
4. Run:

```bash
python3 contact_manager.py
```

## Conclusion

This project demonstrates the practical use of:

* Data structures (List, Hash Table, BST)
* Algorithm optimization
* GUI development using Tkinter

It highlights how combining multiple data structures can improve system performance and usability.


