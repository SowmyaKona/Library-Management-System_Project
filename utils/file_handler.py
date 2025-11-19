
"""
Simple JSON read/write helpers.
"""
import json, os
from typing import Any

def read_json(path: str) -> Any:
    if not os.path.exists(path):
        # create as empty list
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w') as f:
            json.dump([], f)
        return []
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # if file empty or invalid, reset to empty list
            with open(path, 'w') as fw:
                json.dump([], fw)
            return []

def write_json(path: str, data: Any) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
