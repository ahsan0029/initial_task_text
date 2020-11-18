import pandas as pd
data = pd.read_json(r"C:\Users\insan\OneDrive\Desktop\task_initial\initial_task_text\tweet_data\all_data.json")
data_1 = pd.DataFrame([])
for key, value in data.items():
    if key == "text" :
        print (value)
        #select the tweet data from json 
        data_1 = data_1.append(pd.DataFrame({'Tweet': value}))
#print(data_1)
data_1['Tweet'] = data_1['Tweet'].replace(r'http\S+', '', regex=True)
data_2=data_1.head(50)
#print(data_2)

data_2.to_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\initial_task_text\Tweet_data\raw_tweet.csv",index = None)
