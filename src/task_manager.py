import json
DATA_FILE = "data/tasks.json"

def load_tasks():
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks():
    tasks = load_tasks()
    print("\n=== Daftar Seluruh Task ===")
    
    if not tasks:
        print("Belum ada task yang terdaftar.")
        return

    for task in tasks:
        # Menampilkan ID, Judul, Status, dan PIC sesuai modul
        print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")