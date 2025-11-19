
from commons.menu import main_menu, admin_menu, student_menu, teacher_menu
from commons.display import display_list
from commons.auth import login_with_mp
from commons.book_manager import borrow_book_by_title, return_book_by_title,get_user_borrowed_books

from utils.admin_utils import ensure_default_admin
from utils.student_utils import get_students, add_student, update_student, delete_student
from utils.teacher_utils import get_teachers, add_teacher, update_teacher, delete_teacher
from utils.book_utils import get_books, add_book, update_book, delete_book

from assets.data import DEPTS, YEARS, SEMS
from config import BOOKS_FILE

import uuid

ensure_default_admin()
def input_text(msg):
    text = input(msg).strip()
    while text == "":
        text = input("Required! " + msg).strip()
    return text

def choose_from_list(prompt, choices):
    print(prompt)
    for i, c in enumerate(choices, start=1):
        print(f"{i}. {c}")
    idx = input("Choose number: ").strip()
    try:
        idxi = int(idx)
        if 1 <= idxi <= len(choices):
            return choices[idxi-1]
    except Exception:
        pass
    return None

def admin_manage_students():
    while True:
        print("""
--- Student Management ---
1. List Students
2. Add student
3. Update Student
4. Delete Student
5. Back
""")
        op = input("Choose: ").strip()
        if op == "1":
            display_list("Students", get_students())
        elif op == "2":
            sid = "S" + uuid.uuid4().hex[:6]
            rec = {
                "id": sid,
                "username": input_text("Username: "),
                "password": input_text("Password: "),
                "name": input_text("Name: "),
                "dept": choose_from_list("Select Department:", DEPTS),
                "year": choose_from_list("Select Year:", YEARS),
                "sem": choose_from_list("Select Semester:", SEMS)
            }
            add_student(rec)
            print("Student added.")
        elif op == "3":
            sid = input_text("Student ID: ")
            name = input("New name (blank to skip): ").strip()
            upd = {}
            if name: upd["name"] = name
            update_student(sid, upd)
            print("Updated.")
        elif op == "4":
            sid = input_text("Student ID: ")
            delete_student(sid)
            print("Deleted if existed.")
        elif op == "5":
            break
        else:
            print("Invalid choice")


def admin_manage_teachers():
    while True:
        print("""
--- Teacher Management ---
1. List Teachers
2. Add Teacher
3. Update Teacher
4. Delete Teacher
5. Back
""")
        op = input("Choose: ").strip()
        if op == "1":
            display_list("Teachers", get_teachers())
        elif op == "2":
            tid = "T" + uuid.uuid4().hex[:6]
            rec = {
                "id": tid,
                "username": input_text("Username: "),
                "password": input_text("Password: "),
                "name": input_text("Name: "),
                "dept": choose_from_list("Select Department:", DEPTS),
                "subject": input_text("Subject taught: ")
            }
            add_teacher(rec)
            print("Teacher added.")
        elif op == "3":
            tid = input_text("Teacher ID: ")
            name = input("New name (blank to skip): ").strip()
            upd = {}
            if name: upd["name"] = name
            update_teacher(tid, upd)
            print("Updated.")
        elif op == "4":
            tid = input_text("Teacher ID: ")
            delete_teacher(tid)
            print("Deleted if existed.")
        elif op == "5":
            break
        else:
            print("Invalid choice")


def admin_manage_books():
    while True:
        print("""
--- Book Management ---
1. List Books
2. Add Book
3. Update Book
4. Delete Book
5. Back
""")
        op = input("Choose: ").strip()
        if op == "1":
            display_list("Books", get_books())
        elif op == "2":
            bid = "B" + uuid.uuid4().hex[:6]
            total = None
            while total is None:
                try:
                    total = int(input_text("Total copies: "))
                    if total < 1:
                        print("Total must be >= 1"); total = None
                except Exception:
                    print("Enter a valid number")
            rec = {
                "id": bid,
                "title": input_text("Title: "),
                "author": input_text("Author: "),
                "total_copies": total,
                "available_copies": total
            }
            add_book(rec)
            print("Book added.")
        elif op == "3":
            bid = input_text("Book ID: ")
            title = input("New Title (blank to skip): ").strip()
            author = input("New Author (blank to skip): ").strip()
            upd = {}
            if title: upd["title"] = title
            if author: upd["author"] = author
            update_book(bid, upd)
            print("Updated.")
        elif op == "4":
            bid = input_text("Book ID: ")
            delete_book(bid)
            print("Deleted if existed.")
        elif op == "5":
            break
        else:
            print("Invalid choice")


def admin_operations():
    while True:
        admin_menu()
        ch = input("Enter option: ").strip()
        if ch == "1":
            admin_manage_students()
        elif ch == "2":
            admin_manage_teachers()
        elif ch == "3":
            admin_manage_books()
        elif ch == "4":
            break
        else:
            print("Invalid choice")

def student_operations(username):
    students = get_students()
    sid = None
    for s in students:
        if s["username"] == username:
            sid = s["id"]
            break

    while True:
        student_menu()
        ch = input("Choose: ").strip()

        if ch == "1":
            display_list("Books", get_books())

        elif ch == "2":
            title = input_text("Book Name to borrow: ")
            result = borrow_book_by_title(title, sid, "student")

            if result == "limit":
                print("Borrow limit reached (max 3 books).")
            elif result:
                print("Borrow successful!")
            else:
                print("Book not available.")

        elif ch == "3":
            title = input_text("Book Name to return: ")
            fine = return_book_by_title(title, sid)

            if fine is None:
                print("You did not borrow this book.")
            elif fine > 0:
                print(f"Returned late! Fine: ₹{fine}")
            else:
                print("Returned successfully.")

        elif ch == "4":
            borrowed = get_user_borrowed_books(sid)
            if not borrowed:
                print("You have no borrowed books.")
            else:
                print("\nBorrowed Books:")
                for b in borrowed:
                    print(f"- {b['book_title']} (Due: {b['due_date']})")

        elif ch == "5":
            break

        else:
            print("Invalid choice")

def teacher_operations(username):
    teachers = get_teachers()
    tid = None
    for t in teachers:
        if t["username"] == username:
            tid = t["id"]
            break

    while True:
        teacher_menu()
        ch = input("Choose: ").strip()

        if ch == "1":
            display_list("Books", get_books())

        elif ch == "2":
            title = input_text("Book Name to borrow: ")
            result = borrow_book_by_title(title, tid, "teacher")

            if result == "limit":
                print("Borrow limit reached (max 5 books).")
            elif result:
                print("Borrow successful!")
            else:
                print("Book not available.")

        elif ch == "3":
            title = input_text("Book Name to return: ")
            fine = return_book_by_title(title, tid)

            if fine is None:
                print("Invalid return.")
            elif fine > 0:
                print(f"Returned late. Fine: ₹{fine}")
            else:
                print("Returned successfully.")

        elif ch == "4":
            borrowed = get_user_borrowed_books(tid)
            if not borrowed:
                print("You have no borrowed books.")
            else:
                print("\nBorrowed Books:")
                for b in borrowed:
                    print(f"- {b['book_title']} (Due: {b['due_date']})")

        elif ch == "5":
            break

        else:
            print("Invalid choice")


def main():
    print("Welcome to the LMS Project")
    while True:
        main_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            u = input_text("Admin username: ")
            p = input_text("Admin password: ")
            if login_with_mp("admin", u, p):
                print("Admin login success.")
                admin_operations()
            else:
                print("Invalid admin credentials.")
        elif choice == "2":
            u = input_text("Student username: ")
            p = input_text("Student password: ")
            if login_with_mp("student", u, p):
                print("Student login success.")
                student_operations(u)
            else:
                print("Invalid student credentials.")
        elif choice == "3":
            u = input_text("Teacher username: ")
            p = input_text("Teacher password: ")
            if login_with_mp("teacher", u, p):
                print("Teacher login success.")
                teacher_operations(u)
            else:
                print("Invalid teacher credentials.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
