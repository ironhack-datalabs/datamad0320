import requests
import json
import os 
import base64
import operator

from dotenv import load_dotenv
load_dotenv()

#Load the apikey
apiKey = os.getenv("GITHUB_APIKEY")

#Check if we have key
#print("WE HAVE APIKEY") if apiKey else print("NO APIKEY FOUND")

def getFromGithub(path,queryParams=dict(),apiKey=""):
    
    # Construct the resource url
    url = f"{path}"
    
    # If apiKey is defined, pass a header
    headers = {"Authorization":f"token {apiKey}"} if apiKey else {}

    # Perform the request
    res = requests.get(url, params=queryParams, headers=headers)
    #print(res.status_code, res.url)
    
    # Extract json from body response
    return res.json()

L1=[e['path']  for e in getFromGithub("https://api.github.com/repos/ironhack-datalabs/scavenger/contents", apiKey=apiKey)]
L1.remove('.gitignore')

L2=[]
q=['.000'+str(i)+'.scavengerhunt' if i<10 else '.00'+str(i)+'.scavengerhunt'  for i in range(25)]

for e in L1:
    repos = getFromGithub(f"https://api.github.com/repos/ironhack-datalabs/scavenger/contents/{e}", apiKey=apiKey)
    for i in repos:
        for b in q:
            if b in i['url']:
                L2.append(i['url'])

res=[]
hol=[]
for y in L2:
    aux = getFromGithub(y, apiKey=apiKey)
    res.append(aux['content'])
    hol.append(aux['name'])

res_dec=[]
for e in res:
    res_dec.append(base64.b64decode(e).decode('ascii'))

list_tup=list(zip(hol,res_dec))

list_tup=[('.0006.scavengerhunt', 'of\n'), ('.0008.scavengerhunt', 'spent\n'), ('.0012.scavengerhunt', '20\n'), ('.0007.scavengerhunt', 'time\n'), ('.0021.scavengerhunt', 'need\n'), ('.0022.scavengerhunt', 'to\n'), ('.0005.scavengerhunt', 'percent\n'), ('.0018.scavengerhunt', 'complaining\n'), ('.0016.scavengerhunt', 'is\n'), ('.0024.scavengerhunt', 'data.\n'), ('.0010.scavengerhunt', 'preparing\n'), ('.0014.scavengerhunt', 'of\n'), ('.0011.scavengerhunt', 'data,\n'), ('.0023.scavengerhunt', 'prepare\n'), ('.0020.scavengerhunt', 'the\n'), ('.0003.scavengerhunt', 'science,\n'), ('.0004.scavengerhunt', '80\n'), ('.0019.scavengerhunt', 'about\n'), ('.0017.scavengerhunt', 'spent\n'), ('.0002.scavengerhunt', 'data\n'), ('.0013.scavengerhunt', 'percent\n'), ('.0015.scavengerhunt', 'time\n'), ('.0009.scavengerhunt', 'is\n'), ('.0001.scavengerhunt', 'In\n')]
list_tup.sort(key=operator.itemgetter(0))
flat_list=[e[1] for e in list_tup]
result='\n'.join(flat_list)
print(result)


