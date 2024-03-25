import requests
import sys
import json

def fetch_todo_list_progress(employee_id):
    # Fetching employee details
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_data = employee_response.json()
    employee_name = employee_data['name']

    # Fetching todo list for the employee
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Prepare data in JSON format
    tasks = []
    for task in todo_data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        })

    # Writing data to JSON file
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump({employee_id: tasks}, json_file, indent=4)

    # Counting completed tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_data)

    # Printing employee todo list progress
    print(
        f"Employee {employee_name}{' '*(9-len(employee_name))} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    employee_id = sys.argv[1]
    fetch_todo_list_progress(employee_id)