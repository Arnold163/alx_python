import requests
import sys

def get_x_request_id(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the value of the X-Request-Id header
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    # Get URL from command line arguments
    url = sys.argv[1]

    # Call the function to get and display X-Request-Id
    get_x_request_id(url)
    
