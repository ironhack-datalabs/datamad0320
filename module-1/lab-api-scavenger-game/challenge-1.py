#Importing modules
import os
import json
import requests
from dotenv import load_dotenv

#loading and defining the environment variable stored at .env
load_dotenv()
apiKey = os.getenv("GITHUB_APIKEY")

#Making the request to the github api
url = "https://api.github.com/repos/ironhack-datalabs/datamad0320/forks"
res = requests.get(url,headers = {"Authorization":f"token {apiKey}"})

#Formating the response
forks = res.json()

#Creating the list with the unique languages of each fork
lst = list({e['language'] for e in forks})
print(lst)
