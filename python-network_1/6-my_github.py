import requests
import sys

def get_github_user_id(username, token):
    # GitHub API endpoint for the authenticated user
    api_url = 'https://api.github.com/user'

    # Prepare the authentication header using Basic Authentication with personal access token
    auth_header = f"{username}:{token}"
    encoded_auth_header = "Basic " + (auth_header.encode('utf-8').decode('latin-1').encode('base64')).strip()

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
            print(user_id)
        else:
            print("None")

    except requests.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    # Get GitHub credentials from command line arguments
    github_username = sys.argv[1]
    github_token = sys.argv[2]

    # Call the function to get and display GitHub user ID
    get_github_user_id(github_username, github_token)