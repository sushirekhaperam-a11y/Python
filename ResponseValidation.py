import requests
from requests.auth import HTTPBasicAuth

try:
    data = {
        "category": "Platform",
        "name": "Mario",
        "rating": "Mature",
        "releaseDate": "2012-05-04",
        "reviewScore": 85
    }
    # make a get request to endpoint api
    response  = requests.get("https://videogamedb.uk:443/api/v2/videogame",json=data)
    print (response)

    #
    if response.status_code == 200:
        print("Status code is 200 k")

        #parse the jso file
        data = response.json()
        #text of the response file
        print(response.text)
        # content of the response file
        print(response.content)
        # status of the response file
        print(response.status_code)
        # headers of the response file
        print(response.headers)
        # url of the response file
        print(response.url)
        # history of the response file
        print(response.history)
        #fetch the single header
        content_type = response.headers.get('Content-Type')
        print(content_type)



    else: print(f"Error:Received status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error has occurred:{e}")