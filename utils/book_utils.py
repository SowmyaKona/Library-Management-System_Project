
"""
Book CRUD helpers. Books include total_copies and available_copies.
"""
from utils.file_handler import read_json, write_json
from config import BOOKS_FILE
from typing import Dict, List

def get_books() -> List[Dict]:
    return read_json(BOOKS_FILE)

def add_book(book: Dict) -> None:
    data = read_json(BOOKS_FILE)
    data.append(book)
    write_json(BOOKS_FILE, data)

def update_book(book_id, updated_data):
    book_id = book_id.strip().lower()
    data = read_json(BOOKS_FILE)

    for b in data:
        if b.get("id", "").lower() == book_id:
            b.update(updated_data)
            break

    write_json(BOOKS_FILE, data)


def delete_book(book_id):
    book_id = book_id.strip().lower()
    data = read_json(BOOKS_FILE)

    new_data = [b for b in data if b.get("id", "").lower() != book_id]

    write_json(BOOKS_FILE, new_data)
