"""
All printing and display formatting.
"""

"""Pretty printing helpers used for menus and data display."""
def display_list(title: str, data):
    print("\n" + "="*60)
    print(title)
    print("="*60)
    if not data:
        print("No records found.")
        return
    for item in data:
        for k, v in item.items():
            print(f"{k} : {v}")
        print("-"*40)
