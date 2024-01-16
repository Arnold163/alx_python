import requests
import sys

def get_github_user_id(username, password):
    #GitHub API endpoint for the authenticated user
    api_url = 'https://api.github.com/user'

    #prepare the authentication header using basic authentication
    auth_header = f"{username} : {password}"
    encoded_auth_header = f"Basic {auth_header.encode('utf-8').b64encode().decode('utf-8')}"

    #set up the request headers
    headers = {
        'Authorization': encoded_auth_header,
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        #make a GET request to the Github API
        response = requests.get(api_url, headers=headers)

        #Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_data = response.json()
            user_id = user_data['id']
            print(f"Failed to retrieve user data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        
if __name__ == "__main__":
    #get github credentials from command line argument
    github_username = sys.argv[1]
    github_password = sys.argv[2]

    #call the function to get and display GitHub user ID
    get_github_user_id(github_username, github_password)
    
