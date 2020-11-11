import spacy
import pandas as pd
# import xx_ent_wiki_sm #Multi-language
import en_core_web_sm
en_model = en_core_web_sm.load()#xx_ent_wiki_sm.load()
import csv
import json
sample_text=''

nlp =spacy.load ('en_core_web_sm')#('en_core_web_sm')
df= pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\Tweet_data\raw_tweet.csv") 
for index, row in df.iterrows():
    sample_text+=(row['Text'])
    #print(row['Text'])

#defining a function so that we can use it later at the end while tokenizing the complete dataset

# Tokenization
# We would be doing word tokenization, which is splitting the text in single words. We can also split the text into sentences, i.e. sentence tokenization.

# Let's do the tokenization of sample_text we extracted above
def tokenize(text):
    my_doc = nlp(text)
    token_list = []
    for token in my_doc:
        token_list.append(token.text)
    return token_list

json_token=json.dumps(tokenize(sample_text))
# print(tokenize(sample_text))
with open(r'C:\Users\insan\OneDrive\Desktop\task_initial\tokenization\tweet-tokenized-data.csv', 'w') as json_file:
    json.dump(tokenize(sample_text), json_file)


#POS Tagging
# Let's do POS tagging of the sample_text we extracted above.
def pos_tag(text):
    pos_tagged_list = []
    pos_tagged_docs = en_model(text)
    for word in pos_tagged_docs:
        pos_tagged_list.append((word.text,word.pos_))
    return pos_tagged_list

text_list, pos_list = map(list, zip(*pos_tag(sample_text)))
d = {'Text': text_list, 'POS Tag': pos_list}
df_1 = pd.DataFrame(data=d, columns=['Text','POS Tag'])
# print(df_1)
df_1.to_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\tokenization\tweet-POS-Tag-data.csv",index = None)

#Chunking
# Detecting the Noun Phrases: NP from the sample_text extracted above
def chunking(text):
    chunked_text_list = []
    doc = en_model(text)
    for chunk in doc.noun_chunks:
        chunk_piece = {}
        chunk_piece['chunk'] = chunk.text
        chunk_piece['NP'] = chunk.root.text
        chunked_text_list.append(chunk_piece)
    return chunked_text_list

json_token=json.dumps(chunking(sample_text))
print(chunking(sample_text))


with open(r'C:\Users\insan\OneDrive\Desktop\task_initial\tokenization\tweet-chunked-data.csv', 'w') as json_file:
    json.dump(chunking(sample_text), json_file)

# Named Entity Recognition
# Now we find Named entities

def ner(text):
    ent_docs = en_model(text)
    return [(ent.text, ent.label_) for ent in ent_docs.ents]

text_list, ne_list = map(list, zip(*ner(sample_text)))
d = {'Text': text_list, 'Named Entity': ne_list}
df_2 = pd.DataFrame(data=d, columns=['Text','Named Entity'])
# print(df_2)
df_2.to_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\tokenization\tweet-spacy-ner_data.csv",index = None)



# output_files = []

# #used to create the output files required i.e. for tokenized data, POS tagged data, chunked data and ner data.
# #for each of the three datasets, we need to do these steps, hence defining a separate reusable method
# def open_out_files(dataset_filename, nlp_toolkit):
    
#     #Tokenization
#     #creating an output file to write Tokenized tagged data for the input dataset
#     tokenized_out_file = open(dataset_filename+"-[with-"+nlp_toolkit+"]"+"-tokenized_data.csv","w+")
#     output_files.append(tokenized_out_file) #adding the opened file in the output_files list, so that we can keep track of files we need to close.
#     #creating csv writer for Tokenized output file
#     tokenized_csv = csv.writer(tokenized_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     tokenized_csv.writerow(['Tweet', 'tokens'])
    
#     #POS Tagging
#     #creating an output file to write POS tagged data for the input dataset
#     pos_out_file = open(dataset_filename+"-[with-"+nlp_toolkit+"]"+"-pos_tagged_data.csv","w+")
#     output_files.append(pos_out_file) #adding the opened file in the output_files list, so that we can keep track of files we need to close.
#     #creating csv writer for POS tagged output file
#     pos_tag_csv = csv.writer(pos_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     pos_tag_csv.writerow(['Tweet', 'pos_tagged_text'])
    
#     #Chunking
#     #creating an output file to write chunked data for the input dataset
#     chunk_out_file = open(dataset_filename+"-[with-"+nlp_toolkit+"]"+"-chunked_data.csv","w+")
#     output_files.append(chunk_out_file) #adding the opened file in the output_files list, so that we can keep track of files we need to close.
#     #creating csv writer for output file for chunked data
#     chunked_csv = csv.writer(chunk_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     chunked_csv.writerow(['Tweet', 'chunks'])
    
#     #NER
#     #creating an output file to write NER data for the input dataset
#     ner_out_file = open(dataset_filename+"-[with-"+nlp_toolkit+"]"+"-ner_data.csv","w+")
#     output_files.append(ner_out_file) #adding the opened file in the output_files list, so that we can keep track of files we need to close.
#     #creating csv writer for output file for NER
#     ner_csv = csv.writer(ner_out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     ner_csv.writerow(['Tweet', 'ner'])
    
#     return tokenized_csv, pos_tag_csv, chunked_csv, ner_csv

# #defining a separate method for closing all the files we open for creation, hence reducing number of lines
# def close_out_files():
#     for output_file in output_files:
#         output_file.close()


