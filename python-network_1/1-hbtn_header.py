import requests
import sys

def fetch_and_display_request_id(url):
    try:
        response = requests.get(url)

        response.raise_for_status()  # Raise an exception for HTTP errors

        # Display the value of X-Request-Id in the response header
        request_id = response.headers.get('X-Request-Id')
        if request_id is not None:
            print(f"{request_id}")
        else:
            print("None")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Check if the URL is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    result = fetch_and_display_request_id(url)