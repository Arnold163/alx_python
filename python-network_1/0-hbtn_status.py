import requests

url = "https://alu-intranet.hbtn.io/status"

try: 
    response = requests.get(url)
    response.raise_for_status() # Raise an exception for HTTP errors 

    # displaying the response 
    print("Body response:")
    print("\t- type:" , type(response.text))
    print("\t- content:" , response.text)



except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")