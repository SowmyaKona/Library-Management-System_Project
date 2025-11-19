"""
# Validation helpers.
"""

def id_exists(data_list, id_val):
    return any(item["id"] == id_val for item in data_list)
