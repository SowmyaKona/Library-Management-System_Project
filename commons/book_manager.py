"""
High-level borrow/return logic that updates available_copies.
Uses simple loops and write_json to persist changes.
"""

from utils.book_utils import get_books, update_book
from utils.file_handler import read_json, write_json
from config import BOOKS_FILE
from datetime import datetime, timedelta

HISTORY_FILE = "database/history.json"

# Borrow limits
STUDENT_LIMIT = 3
TEACHER_LIMIT = 5

def get_history():
    return read_json(HISTORY_FILE)

def save_history(data):
    write_json(HISTORY_FILE, data)

# Count currently borrowed books
def count_user_borrowed(user_id):
    history = get_history()
    return len([
        h for h in history
        if h["user_id"] == user_id and h["return_date"] is None
    ])


def borrow_book_by_title(book_title, user_id, user_type):
    book_title = book_title.strip().lower()
    books = get_books()

    # CHECK BORROW LIMIT
    already = count_user_borrowed(user_id)
    if user_type == "student" and already >= STUDENT_LIMIT:
        return "limit"
    if user_type == "teacher" and already >= TEACHER_LIMIT:
        return "limit"

    for book in books:
        if book["title"].lower() == book_title:

            # check availability
            if book["available_copies"] <= 0:
                return False

            # decrease count
            book["available_copies"] -= 1
            update_book(book["id"], {"available_copies": book["available_copies"]})

            # add to history
            history = get_history()
            history.append({
                "user_id": user_id,
                "user_type": user_type,
                "book_title": book["title"],
                "borrow_date": datetime.now().strftime("%Y-%m-%d"),
                "due_date": (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d"),
                "return_date": None,
                "fine": 0
            })
            save_history(history)

            return True

    return False


def return_book_by_title(book_title, user_id):
    book_title = book_title.strip().lower()
    books = get_books()
    history = get_history()

    # find matching borrow entry
    for entry in history:
        if (
            entry["book_title"].lower() == book_title
            and entry["user_id"] == user_id
            and entry["return_date"] is None
        ):
            # increase available copies
            for b in books:
                if b["title"].lower() == book_title:
                    if b["available_copies"] < b["total_copies"]:
                        b["available_copies"] += 1
                        update_book(b["id"], {"available_copies": b["available_copies"]})

            # calculate fine
            due = datetime.strptime(entry["due_date"], "%Y-%m-%d")
            today = datetime.now()

            late_days = (today - due).days
            fine = 5 * late_days if late_days > 0 else 0

            entry["return_date"] = today.strftime("%Y-%m-%d")
            entry["fine"] = fine

            save_history(history)
            return fine  # return fine amount

    return None  # invalid return


def get_user_borrowed_books(user_id):
    history = get_history()
    return [
        h for h in history
        if h["user_id"] == user_id and h["return_date"] is None
    ]
