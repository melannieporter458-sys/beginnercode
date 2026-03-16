tasks =[]

def add_task():
	task = input("Enter task: ")
	if task:
		tasks.append(task)
		print(f"Task '{task}' added.")

def view_task():
	if not tasks:
		print("\nList is empty.")
	else:	
		print("\n--- Tasks ---")
		for i, task in enumerate(tasks, 1):
			print(f"{i}. {task}")
def delete_task():
	view_task()
	if tasks:
		try:
			idx = int(input("Delete #:"))-1
			print(f"'{tasks.pop(idx)}' removied.")
		except (ValueError, IndexError):
			print("Invalid number.")

while True:
	print("\n1. Add 2. View 3. Delete 4. Exit")
	choice = input("Choice: ")
	if choice == '1': add_task()
	elif choice == '2': view_task()
	elif choice == '3': delete_task()
	elif choice == '4': break 
