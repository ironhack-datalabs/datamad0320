#Importing modules
import os
import json
import requests
from dotenv import load_dotenv

#loading and defining the environment variable stored at .env
load_dotenv()
apiKey = os.getenv("GITHUB_APIKEY")

#Making the request to the github api
url = "https://api.github.com/repos/ironhack-datalabs/datamad0320/commits"
res = requests.get(url,params = {'since':'2020-03-30T00:00:01Z'},headers = {"Authorization":f"token {apiKey}"})

#Formating the response
commits = res.json()
print(f'{len(commits)} were made last week in this repository')

#Making the request to the github api
url = "https://api.github.com/repos/ironhack-datalabs/datamad0320/commits"
res = requests.get(url,params = {'until':'2020-03-30T00:00:01Z'},headers = {"Authorization":f"token {apiKey}"})

#Formating the response
commits = res.json()
print(f'{len(commits)} were made before last week in this repository')
print('by:')

for e in commits:
    print(e['commit']['author']['name'])