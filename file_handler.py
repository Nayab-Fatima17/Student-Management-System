import json
import os

FILE_PATH = "projects/students.json"

def load_students():
    if not os.path.exists(FILE_PATH):
        return []

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        print("Error reading file. Starting with empty data.")
        return []

def save_students(students):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(students, file, indent=4)
    except:
        print("Error saving data!") 