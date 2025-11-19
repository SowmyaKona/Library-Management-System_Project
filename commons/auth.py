
"""Authentication logic using multiprocessing.
Admin -> filter()
Student/Teacher -> for loop
"""
from utils.file_handler import read_json
from config import ADMIN_FILE, STUDENTS_FILE, TEACHERS_FILE
import multiprocessing

def admin_login(username, password):
    admins = read_json(ADMIN_FILE)
    res = list(filter(lambda a: a.get("username") == username and a.get("password") == password, admins))
    return len(res) > 0

def student_login(username, password):
    for s in read_json(STUDENTS_FILE):
        if s.get("username") == username and s.get("password") == password:
            return True
    return False

def teacher_login(username, password):
    for t in read_json(TEACHERS_FILE):
        if t.get("username") == username and t.get("password") == password:
            return True
    return False

def _mp_login(user_type, username, password, conn):
    try:
        if user_type == "admin":
            conn.send(admin_login(username, password))
        elif user_type == "student":
            conn.send(student_login(username, password))
        elif user_type == "teacher":
            conn.send(teacher_login(username, password))
        else:
            conn.send(False)
    except Exception:
        conn.send(False)
    finally:
        conn.close()

def login_with_mp(user_type, username, password, timeout=3):
    parent, child = multiprocessing.Pipe()
    p = multiprocessing.Process(target=_mp_login, args=(user_type, username, password, child))
    p.start()
    p.join(timeout)
    result = False
    if parent.poll():
        result = parent.recv()
    if p.is_alive():
        p.terminate()
    parent.close()
    return result
