"""
Teacher CRUD helpers. Teacher records include dept and subject.
"""
from utils.file_handler import read_json, write_json
from config import TEACHERS_FILE
from typing import Dict, List

def get_teachers() -> List[Dict]:
    return read_json(TEACHERS_FILE)

def add_teacher(teacher: Dict) -> None:
    data = read_json(TEACHERS_FILE)
    data.append(teacher)
    write_json(TEACHERS_FILE, data)

def update_teacher(teacher_id, updated_data):
    teacher_id = teacher_id.strip().lower()
    data = read_json(TEACHERS_FILE)

    for t in data:
        if t.get("id", "").lower() == teacher_id:
            t.update(updated_data)
            break

    write_json(TEACHERS_FILE, data)


def delete_teacher(teacher_id):
    teacher_id = teacher_id.strip().lower()
    data = read_json(TEACHERS_FILE)

    new_data = [t for t in data if t.get("id", "").lower() != teacher_id]

    write_json(TEACHERS_FILE, new_data)
