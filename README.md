# LMS Project
A modular Python LMS (Library Management System) sample project.

📘 Overview

This LMS is designed with a modular Python architecture that organizes all library-related operations into dedicated components.
Admins can manage users and books, while Students and Teachers can borrow and return books seamlessly.
The system integrates enhanced functionalities like automated due-date assignment, fine calculation, and user-specific borrow tracking.


 Features
👨‍💼Admin Features
 - Add / View / Update / Delete Students
 - Add / View / Update / Delete Teachers
 - Add / View / Update / Delete Books
 - Track book availability
 - Manage total & available copies

🎓Student Features
 - View all available books
 - Borrow books by name
 - Return books with auto fine system
 - Borrow limit: 3 books
 - View My Borrowed Books

👨‍🏫Teacher Features 
 - View all books
 - Borrow books
 - Return books
 - Borrow limit: 5 books
 - View My Borrowed Books

🔥 Advanced Features Implemented
1️⃣ Issued Books History
Tracks Every borrow & return is logged with:
 - user id
 - book title
 - borrow date
 - due date
 - return date
 - fine
 - Stored in: database/history.json

2️⃣ Due Date & Fine System
 - Each book is due in 7 days
 - Fine of ₹5 per late day

3️⃣ Show Books Borrowed by User
 - Students & teachers can view only their borrowed books

4️⃣ Borrow Limit
 - Students → 3 books
 - Teachers → 5 books

 Folder Structure:

 LMS_Project/
│
├── assets/
│   ├── __init__.py
│   └── data.py              # constants (departments, years, semesters)
│
├── commons/
│   ├── auth.py              # login system
│   ├── menu.py              # menu printing
│   ├── display.py           # data display utils
│   └── book_manager.py      # borrow/return + fine system + history
│
├── utils/
│   ├── file_handler.py      # read/write JSON
│   ├── validations.py       # validations
│   ├── student_utils.py     # student CRUD
│   ├── teacher_utils.py     # teacher CRUD
│   ├── admin_utils.py       # admin utilities
│   └── book_utils.py        # book CRUD
│
├── database/
│   ├── admins.json
│   ├── students.json
│   ├── teachers.json
│   ├── books.json
│   └── history.json         # issued books history
│
├── config.py
├── main.py                  # application entry point
└── README.md


Example Usage :

========= STUDENT MENU =========
1. View Books
2. Borrow Book
3. Return Book
4. My Borrowed Books
5. Logout
================================

Choose: 2
Book Name to borrow: Python Programming
Borrow successful!

Choose: 3
Book Name to return: Python Programming
Returned late. Fine: ₹15

## To Run
- open terminal 
python main.py

Default admin login: 
username = admin 
password = admin
