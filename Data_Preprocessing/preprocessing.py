#Data Preprocessing


# importing required libraries

import logging
import re
import itertools
import json
import csv
from autocorrect import Speller
import pandas as pd
from wordsegment import load, segment
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from html.parser import HTMLParser
logging.basicConfig(level=logging.INFO)
spell = Speller(lang='en')

# preprocessing the input data
def preprocess(fp):

    corpus = []
    load()
    stopWords = set(stopwords.words('english'))
    data = {'Text': []};

    with open(fp, 'rt', encoding='utf-8') as data_in:
        csv_reader = csv.reader(data_in, delimiter=',')
        for line in csv_reader:
            # discarding first line
            if not 'Text' in line[0]:
                
                tweet = line[0]
                tweet = re.sub(r'RT','', tweet)
                print(tweet)

                 # remove url
                tweet = re.sub(r'(http|https?|ftp)://[^\s/$.?#].[^\s]*', '', tweet, flags=re.MULTILINE)
                tweet = re.sub(r'[http?|https?]:\\/\\/[^\s/$.?#].[^\s]*', '', tweet, flags=re.MULTILINE)

                # remove mentions
                remove_mentions = re.compile(r'(?:@[\w_]+)')
                tweet = remove_mentions.sub('',tweet)

                # remove emoticons
                try:
                    emoji_pattern = re.compile("["
                        u"\U0001F600-\U0001F64F" # emoticons
                        u"\U0001F650-\U0001F67F" # ornamental dingbats
                        u"\U0001F300-\U0001F5FF" # symbols & pictographs
                        u"\U0001F680-\U0001F6FF" # transport & map symbols
                        u"\u2600-\u26FF\u2700-\u27BF" # mislaneous
                        u"\U00002702-\U000027B0" 
                        u"\U000024C2-\U0001F251"
                        u"\U0001F1E0-\U0001F1FF" # flags (iOS)
                        "]+", flags=re.UNICODE)
                    tweet = emoji_pattern.sub(r'', tweet)
                except Exception:
                    pass


                # remove unicode
                try:
                    tweet = tweet.encode('ascii').decode('unicode-escape').encode('ascii','ignore').decode("utf-8")
                except Exception:
                    pass

             

                # Standardising words
                tweet = ''.join(''.join(s)[:2] for _, s in itertools.groupby(tweet))

                # applying contractions
                words = tweet.split()
                tweet = [apoDict[word] if word in apoDict else word for word in words]
                tweet = " ".join(tweet)

                hashWords =  re.findall(r'(?:^|\s)#{1}(\w+)', tweet)
                # replace #word with word
                tweet = re.sub(r'(?:^|\s)#{1}(\w+)', r' \1', tweet)

                # word segmentation
                token_list =  word_tokenize(tweet)
                segmented_word = []
                for i in token_list:
                    if i in hashWords:
                        seg = segment(i)
                        segmented_word.extend(seg)
                    else:
                        segmented_word.append(i)

                tweet = ' '.join(segmented_word)

                # remove special symbols
                tweet = re.sub('[@#$._|:,``!;]', ' ', tweet)

                # remove extra whitespaces
                tweet = re.sub('[\s]+', ' ', tweet)


                # creating a dictionary
                data['Text'].append(tweet)
            
    #creating a dataframe
    df = pd.DataFrame(data)
    print(df.to_string)

    #to order the columns in the csv file (while copying from dataframes to a CSV file)
    df_reorder = df[['Text']]


    #writing dataframe to a csv file
    df_reorder.to_csv(r'C:\Users\insan\OneDrive\Desktop\task_initial\Data_Preprocessing\tweet_pre.csv',encoding='utf-8', index= False)

    return corpus

# Contractions with the
def loadAppostophesDict(fp_contraction):
    apoDict = json.load(open(fp_contraction))
    return apoDict

if __name__ == "__main__":

    # function calls to contractions and preprocessing
    DATASET_FP = r"C:\Users\insan\OneDrive\Desktop\task\raw_tweet.csv"
    APPOSTOPHES_FP = r"C:\Users\insan\OneDrive\Desktop\task\Data_Preprocessing\appos_dict.txt"
    apoDict = loadAppostophesDict(APPOSTOPHES_FP)
    corpus = preprocess(DATASET_FP)