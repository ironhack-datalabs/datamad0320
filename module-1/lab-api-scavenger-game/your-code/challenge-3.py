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

#Me creo una lista con el nombre de los repositorios contenidos en ironhack-datalabs/scavenger
L1=[e['path']  for e in getFromGithub("https://api.github.com/repos/ironhack-datalabs/scavenger/contents", apiKey=apiKey)]
L1.remove('.gitignore')

#Me creo una lista con el nombre de los archivos que quiero buscar
L2=[]
q=['.000'+str(i)+'.scavengerhunt' if i<10 else '.00'+str(i)+'.scavengerhunt'  for i in range(25)]

#Busco las URLs de las APIs de los archivos .00XX.scavengerhunt y las meto en una lista
for e in L1:
    repos = getFromGithub(f"https://api.github.com/repos/ironhack-datalabs/scavenger/contents/{e}", apiKey=apiKey)
    for i in repos:
        for b in q:
            if b in i['url']:
                L2.append(i['url'])

#Con la URL de las APIs de los archivos .00XX.scavengerhunt, extraigo la info, es decir, nombre y contenido
res=[]
hol=[]
for y in L2:
    aux = getFromGithub(y, apiKey=apiKey)
    res.append(aux['content'])
    hol.append(aux['name'])

#Decodifico a ASCII el contennido de cada archivo .00XX.scavengerhunt
res_dec=[]
for e in res:
    res_dec.append(base64.b64decode(e).decode('ascii'))

#Uno el nombre con el contenido para hacer un SORT ascendente de los contenidos: .0000,.0001,.0002,.0003...
list_tup=list(zip(hol,res_dec))
list_tup.sort(key=operator.itemgetter(0))

#Preparo el string resultado para imprimir directamente por terminal 
flat_list=[e[1] for e in list_tup]
result='\n'.join(flat_list)
print(result)


