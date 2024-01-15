import requests
import sys

def search_user_by_letter(letter):
    try:
        #set up the payload
        data ={'q': letter}

        #send a POST request to the specified URL 
        response = requests.post('http://0.0.0.0:5000/search_user', data=data)
        response.raise_for_status() #Check for HTTP errors 

        #parse the JSON response 
        json_response = response.json()

        #check if the response is properly JSON formatted and not empty
        if isinstance(json_response, dict) and json_response:
            user_id = json_response.get('id', '')
            user_name = json_response.get('name', '')
            print(f"[{user_id}] {user_name}")
        else:
            if not json_response:
                print("No result")
            else:
                print("not a valid JSON")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    #check if a letter is provided
    if len(sys.argv) == 2:
        letter = sys.argv[1] 
    else:
        letter = ""

    search_user_by_letter(letter)      