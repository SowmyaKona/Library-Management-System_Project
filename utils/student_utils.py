
"""
Student CRUD helpers. Students store dept, year, sem fields.
"""
from utils.file_handler import read_json, write_json
from config import STUDENTS_FILE
from typing import Dict, List

def get_students() -> List[Dict]:
    return read_json(STUDENTS_FILE)

def add_student(student: Dict) -> None:
    data = read_json(STUDENTS_FILE)
    data.append(student)
    write_json(STUDENTS_FILE, data)

def update_student(student_id, updated_data):
    student_id = student_id.strip().lower()
    data = read_json(STUDENTS_FILE)

    for s in data:
        if s.get("id", "").lower() == student_id:
            s.update(updated_data)
            break

    write_json(STUDENTS_FILE, data)


def delete_student(student_id):
    student_id = student_id.strip().lower()
    data = read_json(STUDENTS_FILE)

    new_data = [s for s in data if s.get("id", "").lower() != student_id]

    write_json(STUDENTS_FILE, new_data)
