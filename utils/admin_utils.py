
"""
Admin utilities. Creates a default admin if none exist.
"""

from utils.file_handler import read_json, write_json
from config import ADMIN_FILE
from typing import Dict, List

def get_admins() -> List[Dict]:
    return read_json(ADMIN_FILE)

def add_admin(admin: Dict) -> None:
    data = read_json(ADMIN_FILE)
    data.append(admin)
    write_json(ADMIN_FILE, data)

def ensure_default_admin() -> None:
    data = read_json(ADMIN_FILE)
    if not data:
        default_admin = {"id": "A1", "username": "admin", "password": "admin", "name": "Super Admin"}
        write_json(ADMIN_FILE, [default_admin])
