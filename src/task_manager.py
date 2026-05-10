import json
DATA_FILE = "data/tasks.json"

def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)