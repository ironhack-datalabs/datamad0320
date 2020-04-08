import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv('GITHUB_APIKEY')

def get_github(path,queryParams=dict(),apikey=""):
    
    # Construct the resource url
    url = f"https://api.github.com{path}" #schema https://api.github.com
    
    # If apiKey is defined, pass a header
    headers = {"Authorization":f"token {apikey}"} if apikey else {}
    
    # Perform the request
    res = requests.get(url, params=queryParams, headers=headers)
    print(res.status_code, res.url)
    
    # Extract json from body response
    return res.json()

# 1. Obtain the full list of forks created from the main lab repo via Github API.

# GET /repos/:owner/:repo/forks

path_forks = "/repos/ironhack-datalabs/datamad0320/forks"
forks = get_github(path_forks)
len(forks)

# 2.Loop the JSON response to find out the language attribute of each fork. 
# Use an array to store the language attributes of each fork.

lang = []
for f in forks:
    if f["language"] not in lang:
        lang.append(f["language"])
        

# 3. Print the language array.

print(lang)