import requests
import sys

def get_github_user_id(username, password):
    # GitHub API endpoint for the authenticated user
    api_url = 'https://api.github.com/user'

    # Prepare the authentication header using basic authentication
    auth_header = f"{username}:{password}"
    encoded_auth_header = "Basic " + auth_header.encode('utf-8').strip().decode('latin-1')

    # Set up the request headers
    headers = {
        'Authorization': encoded_auth_header,
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        # Make a GET request to the GitHub API
        response = requests.get(api_url, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            print(f"Github User ID: {user_id}")
        else:
            print(f"Failed to retrieve user data. Status code: {response.status_code}")
            print(response.text)  # Print additional details for debugging
    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Check if the expected number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <github_username> <github_password>")
        sys.exit(1)

    # Get GitHub credentials from command line arguments
    github_username = sys.argv[1]
    github_password = sys.argv[2]

    # Call the function to get and display GitHub user ID
    get_github_user_id(github_username, github_password)