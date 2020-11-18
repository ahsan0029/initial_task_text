import spacy
import pandas as pd
import xx_ent_wiki_sm #Multi-language
# import en_core_web_sm
en_model = xx_ent_wiki_sm.load()
# en_core_web_sm.load()
import csv
import json
df_2 = pd.DataFrame([])
a=''
sample_text=''
nlp =spacy.load ('xx_ent_wiki_sm')#('en_core_web_sm')
df= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\Tweet_data\raw_tweet.csv") 
for index, row in df.iterrows():
    #print(row['Tweet'])
    sample_text+=(row['Tweet'])
    a=row=['Tweet']

    def ner(text):
        ent_docs = en_model(text)
        return [(ent.text, ent.label_) for ent in ent_docs.ents]

    text_list, ne_list = map(list, zip(*ner(sample_text)))
    d = {'Tweet': text_list, 'Named Entity': ne_list}
   # df_2 = pd.DataFrame(data=d, columns=['Tweet','Named Entity'])
    df_2 = df_2.append(pd.DataFrame(data=d, columns=['Tweet','Named Entity']))
    print(df_2)
    doc=nlp(a)