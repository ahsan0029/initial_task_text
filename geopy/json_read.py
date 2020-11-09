import json
import pandas as pd 
data_1 = pd.DataFrame([])


# data = pd.read_json(r"C:\Users\insan\OneDrive\Desktop\task_initial\dbpedia_location\dbpedia_location.json")
# for row in data.iterrows():
#     #print(row)
#     for nums in row:
#         print(type(nums))
#         for key, value in data.items():
#             for a in value.items():
#                 for b in a:
#                     ab+=b
with open(r"C:\Users\insan\OneDrive\Desktop\task_initial\dbpedia_location\dbpedia_location.json") as input_file:
    data = json.load(input_file)
    #print(data)
for x in data:
    print(x)
    for c in x:
        #print(type(c))
        for key, value  in c.items():
            if key=='surfaceForm':
                #print(value)
                merge=list(value)
                loc=[''.join(merge[:])]
                #print(loc)
                data_1 = data_1.append(pd.DataFrame({'Location': loc}),ignore_index=False)
                

print(data_1) 
  
data_1.to_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\dbpedia_location\dbpedia_location.csv",index = None) 
    

