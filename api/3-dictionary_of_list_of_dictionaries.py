"""dictionary  of list dictionaries"""
import json
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """
    Fetches todo list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        dict: A dictionary containing tasks owned by the employee, formatted as specified.
    """
    # Fetching employee details
    employee_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    
    # Check if the user ID is valid
    if employee_response.status_code != 200:
        print("Invalid USER_ID. Please provide a valid employee ID.")
        sys.exit(1)

    employee_data = employee_response.json()
    employee_name = employee_data['username']

    # Fetching todo list for the employee
    todo_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")
    todo_data = todo_response.json()

    # Collecting tasks owned by the employee
    employee_tasks = []
    for task in todo_data:
        employee_tasks.append({
            "username": employee_name,
            "task": task['title'],
            "completed": task['completed']
        })

    # Returning data
    return employee_tasks


def export_to_json(data, filename):
    """
    Exports data to a JSON file.

    Args:
        data (dict): The data to be exported.
        filename (str): The name of the file to export data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    all_employee_data = {}

    # Loop through employee IDs and fetch todo list progress for each
    for employee_id in range(1, 11):
        # Fetch todo list progress for the employee
        employee_tasks = fetch_todo_list_progress(employee_id)
        all_employee_data[str(employee_id)] = employee_tasks

    # Export data to JSON file
    export_to_json(all_employee_data, "todo_all_employees.json")

    # Print confirmation message
    print("Data exported to todo_all_employees.json.")