import requests
import sys

def send_post_request(url, email):
    try:
        #setup data payload 
        data = {'email': email}

        #send a post request to the response 
        response = requests.post(url, data=data)
        response.raise_for_status() #check for HTTp errs

        #display the body of the response 
        print(response.text)

    except requests.RequestException as e:
        print(response.text)
        sys.exit(1)
if __name__== "__main__":
    #check if both URL and email are provided as command-line argumentd
    if len(sys.argv) !=3 :
        print("usage: python script.py <URL> <email>")
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)


        
        
