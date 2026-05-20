import json
import os

DATA_FILE = "data/tasks.json"

def load_tasks(file_path=DATA_FILE):
    if not os.path.exists(file_path):
        return []
    with open(file_path, "r") as file:
        return json.load(file)

def save_tasks(tasks, file_path=DATA_FILE):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        json.dump(tasks, file, indent=4)

# =====================================================================
#  FUNGSI BACKEND (Wajib Ada untuk Lolos Testing GitHub Actions/Pytest)
# =====================================================================

def get_all_tasks(tasks):
    return tasks

def add_task_backend(tasks, title, description, priority, assignee):
    new_id = tasks[-1]["id"] + 1 if tasks else 1
    new_task = {
        "id": new_id,
        "title": title,
        "description": description,
        "status": "todo",
        "priority": priority,
        "assignee": assignee
    }
    tasks.append(new_task)
    return tasks

def update_task_status(tasks, task_id, new_status):
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            break
    return tasks

def delete_task_backend(tasks, task_id):
    return [task for task in tasks if task["id"] != task_id]

def search_task_by_assignee(tasks, assignee_name):
    return [task for task in tasks if task["assignee"].lower() == assignee_name.lower()]

# Alias fungsi agar nama yang diimport sesuai persis dengan kebutuhan file test_task_manager.py
add_task = add_task_backend
delete_task = delete_task_backend



#  FUNGSI CLI INTERAKTIF 
def show_tasks():
    tasks = load_tasks()
    print("\n=== Daftar Seluruh Task ===")
    if not tasks:
        print("Belum ada task yang terdaftar.")
        return
    for task in tasks:
        print(f"{task['id']}. {task['title']} | Status: {task['status']} | PIC: {task['assignee']}")

def add_task_cli():
    tasks = load_tasks()
    new_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    print(f"\n--- Tambah Task Baru (ID: {new_id}) ---")
    title = input("Judul task: ")
    description = input("Deskripsi: ")
    priority = input("Priority (low/medium/high): ")
    assignee = input("Assignee: ")
    
    tasks = add_task_backend(tasks, title, description, priority, assignee)
    save_tasks(tasks)
    print("✓ Task berhasil ditambahkan.")

def update_status():
    tasks = load_tasks()
    if not tasks:
        print("Belum ada task yang terdaftar.")
        return
    show_tasks()
    try:
        task_id = int(input("\nMasukkan ID task yang ingin diubah statusnya: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if not task:
            print("✗ Task dengan ID tersebut tidak ditemukan.")
            return
        print(f"\nTask saat ini: {task['title']}")
        print(f"Status saat ini: {task['status']}")
        print("Pilih status baru:\n1. todo\n2. in_progress\n3. done")
        status_choice = input("Pilih status (1/2/3): ")
        status_map = {"1": "todo", "2": "in_progress", "3": "done"}
        if status_choice not in status_map:
            print("✗ Pilihan tidak valid.")
            return
        
        tasks = update_task_status(tasks, task_id, status_map[status_choice])
        save_tasks(tasks)
        print(f"✓ Status task berhasil diubah.")
    except ValueError:
        print("✗ ID harus berupa angka.")

def delete_task_cli():
    tasks = load_tasks()
    if not tasks:
        print("Belum ada task yang terdaftar.")
        return
    show_tasks()
    try:
        task_id = int(input("\nMasukkan ID task yang ingin dihapus: "))
        task = next((t for t in tasks if t["id"] == task_id), None)
        if not task:
            print("✗ Task dengan ID tersebut tidak ditemukan.")
            return
        confirm = input(f"Apakah Anda yakin ingin menghapus task '{task['title']}'? (y/n): ").lower()
        if confirm == "y":
            tasks = delete_task_backend(tasks, task_id)
            save_tasks(tasks)
            print("✓ Task berhasil dihapus.")
        else:
            print("✗ Penghapusan dibatalkan.")
    except ValueError:
        print("✗ ID harus berupa angka.")

def search_by_assignee():
    tasks = load_tasks()
    if not tasks:
        print("Belum ada task yang terdaftar.")
        return
    assignee_name = input("\nMasukkan nama assignee yang ingin dicari: ")
    found_tasks = search_task_by_assignee(tasks, assignee_name)
    if not found_tasks:
        print(f"✗ Tidak ada task yang ditugaskan kepada '{assignee_name}'.")
        return
    print(f"\n=== Task untuk {assignee_name} ===")
    for task in found_tasks:
        print(f"{task['id']}. {task['title']} | Status: {task['status']} | Priority: {task['priority']}")