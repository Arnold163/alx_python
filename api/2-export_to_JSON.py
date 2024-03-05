import requests
import sys
import json


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
    """
    Exports data to a JSON file.

    Args:
        data (dict): The data to be exported.
        filename (str): The name of the file to export data to.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Get the employee ID from command-line argument
    employee_id = sys.argv[1]

    # Fetch todo list progress for the employee
    data = fetch_todo_list_progress(employee_id)

    # Define the filename for the JSON file
    filename = f"{employee_id}.json"

    # Export data to JSON file
    export_to_json(data, filename)

    # Print confirmation message
    print(f"Data exported to {filename}.")