import requests
import sys

def fetch_and_display_body(url):
    try:
        response = requests.get(url)
        #display the body of the response 
        print(response.text)

        #check if the HTTP status code is greater than or equal to 400
        if response.status_code >=400:
            print(f"Error code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__== "__main__":
    #check if URL is provided as command
    if len(sys.argv) != 2:
        print("usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_and_display_body(url)
