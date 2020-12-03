import json
from SPARQLWrapper import SPARQLWrapper, JSON
import requests
import urllib.parse
import pandas as pd

append_json=[]

data_2= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\initial_task_text\dbpedia_location\sparql_lat_lon\raw_tweet.csv",error_bad_lines=False)
for index, row in data_2.iterrows():
    a=(row['Tweet'])
    print(a)
    # initial consts
    BASE_URL = 'http://api.dbpedia-spotlight.org/en/annotate?text={text}&confidence={confidence}&support={support}&types={types}'
    TEXT = str(a)
    CONFIDENCE = '0.5'
    SUPPORT = '10'
    TYPES = 'DBpedia%3ALocation'
    REQUEST = BASE_URL.format(
        text=urllib.parse.quote_plus(TEXT), 
        confidence=CONFIDENCE, 
        support=SUPPORT,
        types=TYPES
    )
    HEADERS = {'Accept': 'application/json'}
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    all_urls = []

    r = requests.get(url=REQUEST, headers=HEADERS)
    response = r.json()
    print(response)
    append_json.append(response)
    #resources = response['Resources']
    # for res in resources:
    #     all_urls.append(res['@URI'])
    # print(all_urls)
with open(r'C:\Users\insan\OneDrive\Desktop\task_initial\initial_task_text\dbpedia_location1.json', 'w') as json_file:
        json.dump(append_json, json_file)