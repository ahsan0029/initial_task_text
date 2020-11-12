import spotlight
import json
import pandas as pd
b=[]
results = []
annotations=[]
location_filter = {
    'policy': "whitelist",
    'types': "DBpedia:Location",
    'coreferenceResolution': False
}

data_2= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\Data_Preprocessing\tweet_pre.csv") 
for index, row in data_2.iterrows():
    a=(row['Text'])
    
    # print(type(row['Text']))
    
    try:
        annotations = spotlight.annotate('https://api.dbpedia-spotlight.org/en/annotate?text={text}', str(a), filters=location_filter)
        #annotations.append({'text':row['Text']})
        print(annotations)
    except:
        print("Error occurred ")

    #print(annotations)
    results.append(annotations)
# with open(r'C:\Users\insan\OneDrive\Desktop\task_initial\dbpedia_location\dbpedia_location.json', 'w') as json_file:
#     json.dump(results, json_file)

    