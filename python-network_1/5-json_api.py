import requests
import sys

def search_user_by_letter(letter):
    try:
        # Set up the payload
        data = {'q': letter}

        # Send a POST request to the specified URL
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)
        response.raise_for_status()  # Check for HTTP errors

        # Check if the response is not empty
        if response.text.strip():
            # Parse the JSON response
            json_response = response.json()

            # Check if the response is properly JSON formatted and not empty
            if isinstance(json_response, dict) and json_response:
                print(f"[{json_response.get('id', '')}] {json_response.get('name', '')}")
            else:
                print("Not a valid JSON")
        else:
            print("No result")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if a letter is provided
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    search_user_by_letter(letter)