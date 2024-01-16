import requests
import sys

def search_user(letter):
    # Set the URL for the POST request
    url = 'http://0.0.0.0:5000/search_user'

    # Set the parameter 'q' with the provided letter or an empty string if no letter is given
    params = {'q': letter}

    try:
        # Send a POST request with the parameters
        response = requests.post(url, data=params)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Parse the JSON in the response
        json_data = response.json()

        # Check if the JSON is properly formatted and not empty
        if isinstance(json_data, dict) and json_data:
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            if not json_data:
                print("No result")
            else:
                print("Not a valid JSON")

    except requests.RequestException as e:
        print(f"Error making the request: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Get the letter from the command line argument or set it to an empty string if no argument is given
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Call the function to search for a user and display the result
    search_user(letter) 