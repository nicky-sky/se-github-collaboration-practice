from task_manager import load_tasks, save_tasks, show_tasks


def delete_task():
    tasks = load_tasks()

    if not tasks:
        print("Belum ada task yang terdaftar.")
        return

    show_tasks()

    try:
        task_id = int(input("\nMasukkan ID task yang ingin dihapus: "))
    except ValueError:
        print("✗ ID harus berupa angka.")
        return

    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        print("✗ Task dengan ID tersebut tidak ditemukan.")
        return

    confirm = input(f"Apakah Anda yakin ingin menghapus task '{task['title']}'? (y/n): ").lower()

    if confirm == "y":
        tasks.remove(task)
        save_tasks(tasks)
        print("✓ Task berhasil dihapus.")
    else:
        print("✗ Penghapusan dibatalkan.")


if __name__ == "__main__":
    delete_task()
