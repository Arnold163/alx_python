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

    # Collecting tasks owned by the employee
    employee_tasks = []
    for task in todo_data:
        employee_tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    # Returning data
    return {employee_id: employee_tasks}


def export_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    data = fetch_todo_list_progress(employee_id)
    filename = f"{employee_id}.json"
    export_to_json(data, filename)
    print(f"Data exported to {filename}.")