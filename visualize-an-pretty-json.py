import json
from urllib.request import urlopen

url = "https://raw.githubusercontent.com/suttacentral/sc-data/master/structure/tree/sutta/an-tree.json"
response = urlopen(url)
json_data = json.loads(response.read())

print(json.dumps(json_data, indent=4))


                       
