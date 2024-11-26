import datetime

def read_tasks(filename):
    """Reads tasks from the given file and returns them as a list."""
    try:
        with open(filename, "r") as file:
            for line in file:
                if line.strip():
                    yield line.strip()
    except FileNotFoundError:
        return []
def write_tasks(filename, tasks):
    """Writes the list of tasks back to the given file."""
    with open(filename, "w") as file:
        file.writelines(tasks)
def add_task(description):
    if not description.strip():
        print("Task description cannot be empty.")
        return
    with open("ongoingTasks.txt", "a") as file:
        created_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{description}, {created_date}, \n")
    print(f"Task noted: {description}")

def list_tasks(filename, title):
    try:
        tasks = read_tasks(filename)

        if not tasks:
            print(f"\nNo tasks in {title}.")
            return

        print(f"\n{title}:")
        for i, task in enumerate(tasks, 1):
            task_parts = task.strip().split(",")
            description = task_parts[0]
            created_date = task_parts[1].strip()
            completed_date = task_parts[2].strip() if len(task_parts) > 2 else "Not completed"
            print(f"{i}. Description: {description} | Created: {created_date} | Completed: {completed_date}")


        else:
            print(f"\nNo files in {title}.")
            return
    except FileNotFoundError:
        print(f"\n{filename} not found.")

def list_all_tasks():
    print("\nAll tasks:")
    print("\n--- Ongoing Tasks ---")
    list_tasks("ongoingTasks.txt", "Ongoing Tasks")
    print("\n--- Completed Tasks ---")
    list_tasks("completedTasks.txt", "Completed Tasks")

def check_task(task_number):
    try:
        tasks = read_tasks("ongoingTasks.txt")

        if not tasks or task_number < 1 or task_number > len(tasks):
            print(f"Invalid task number. Please select a number between 1 and {len(tasks)}.")
            return

        completed_task = tasks.pop(task_number - 1)
        write_tasks("ongoingTasks.txt", tasks)

        with open("completedTasks.txt", "a") as file:
            completed_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task_parts = completed_task.strip().split(",")
            if len(task_parts) < 2:
                print(f"Task format invalid: {completed_task.strip()}. Skipping.")
                return
            task_parts[2] = completed_date
            file.write(",".join(task_parts) + "\n")

        print(f"Task marked as completed: {task_parts[0]}")
    except FileNotFoundError:
        print("ongoingTasks.txt not found.")

def uncheck_task(task_number):
    try:
        tasks = read_tasks("completedTasks.txt")

        if not tasks or task_number < 1 or task_number > len(tasks):
            print(f"Invalid task number. Please select a number between 1 and {len(tasks)}.")
            return

        unchecked_task = tasks.pop(task_number - 1)
        write_tasks("completedTasks.txt", tasks)

        with open("ongoingTasks.txt", "a") as file:
            task_parts = unchecked_task.strip().split(",")
            task_parts[2] = ""  # Remove completion date
            file.write(",".join(task_parts) + "\n")

        print(f"Task unchecked and moved back to ongoing: {task_parts[0]}")
    except FileNotFoundError:
        print("completedTasks.txt not found.")

def delete_task(filename, task_number):
    try:
        tasks = read_tasks(filename)
        if not tasks:
            print("The file is empty. No tasks to delete.")
            return

        if not tasks or task_number < 1 or task_number > len(tasks):
            print(f"Invalid task number. Please enter a number between 1 and {len(tasks)}.")
            return

        delete_task = tasks.pop(task_number -1)
        write_tasks(filename, tasks)

        print(f"Task deleted: {delete_task.strip()}")
    except FileNotFoundError:
        print(f"{filename} not found.")

def main():
    while True:
        command = input("\nEnter a command (add, list ongoing, list completed, list all, check, uncheck, delete, quit): ").strip().lower()
        if command == "add":
            description = input("Enter the task description: ").strip()
            add_task(description)
        elif command == "list ongoing":
            list_tasks("ongoingTasks.txt", "Ongoing Tasks")
        elif command == "list completed":
            list_tasks("completedTasks.txt", "Completed Tasks")
        elif command == "list all":
            list_all_tasks()
        elif command == "check":
            list_tasks("ongoingTasks.txt", "Ongoing Tasks")
            try:
                task_number = int(input("Enter the task number to check: "))
                check_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == "uncheck":
            list_tasks("completedTasks.txt", "Completed Tasks")
            try:
                task_number = int(input("Enter the task number to uncheck: "))
                uncheck_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == "delete":
            list_all_tasks()
            filename = input("Delete from (ongoing/completed): ").strip().lower()
            try:
                task_number = int(input("Enter the task number to delete: "))
                if filename == "ongoing":
                    delete_task("ongoingTasks.txt", task_number)
                elif filename == "completed":
                    delete_task("completedTasks.txt", task_number)
                else:
                    print("Invalid file name. Use 'ongoing' or 'completed'.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again. Valid commands: add, list ongoing, list completed, list all, check, uncheck, delete, quit.")

if __name__ == "__main__":
    main()