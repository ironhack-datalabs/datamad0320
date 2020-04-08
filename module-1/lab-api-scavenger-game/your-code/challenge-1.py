import requests
import json
import os 

from dotenv import load_dotenv
load_dotenv()

#Load the apikey
apiKey = os.getenv("GITHUB_APIKEY")

#Check if we have key
print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

def getFromGithub(path,queryParams=dict(),apiKey=""):
    
    # Construct the resource url
    url = f"https://api.github.com{path}"
    
    # If apiKey is defined, pass a header
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}

    # Perform the request
    res = requests.get(url, params=queryParams, headers=headers)
    print(res.status_code, res.url)
    
    # Extract json from body response
    return res.json()



forks = getFromGithub("/repos/ironhack-datalabs/madrid-oct-2018/forks", apiKey=apiKey)

language=[]
for f in forks:
    if f['language'] not in language:
        language.append(f['language'])

print(language)



