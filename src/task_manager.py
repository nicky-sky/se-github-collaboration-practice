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
# Pastikan def add_task sejajar dengan def lainnya (paling kiri)
def add_task():
    tasks = load_tasks()
    
    if not tasks:
        new_id = 1
    else:
        new_id = max(task["id"] for task in tasks) + 1
        
    print(f"\n--- Tambah Task Baru (ID: {new_id}) ---")
    title = input("Judul task: ")
    description = input("Deskripsi: ")
    priority = input("Priority (low/medium/high): ")
    assignee = input("Assignee: ")

    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "todo", 
        "priority": priority,
        "assignee": assignee
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print("✓ Task berhasil ditambahkan.")
