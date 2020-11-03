import spotlight
import json
import pandas as pd
b=[]
location_filter = {
    'policy': "whitelist",
    'types': "DBpedia:Location",
    'coreferenceResolution': False
}
data_2= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task\Data_Preprocessing\tweet_pre.csv") 
for index, row in data_2.iterrows():
    a=(row['Text'])
    annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate', a,
                                    filters=location_filter)
    b+=annotations
print(b)
# jsondata = json.dumps(annotations)

# with open(r"C:\Users\insan\OneDrive\Desktop\initial_task/location.json", "w") as f:
#         f.write(jsondata)
#         f.close()