import pandas as pd
from sklearn import preprocessing
from nltk import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from collections import defaultdict
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.stem import WordNetLemmatizer

class ConversationalEngine():
    def __init__(self, app, lemmatize_data=True, filepath=None):
        df = pd.read_csv(filepath)
        df.sort_values(by='intent_name')
        self.labels = []
        for i in df['intent_name']:
            if i not in self.labels:
                self.labels.append(i)
        self.trainingData = df['sample_utterance'].apply(str)
        if lemmatize_data==True:
            tag_map = defaultdict(lambda : wn.NOUN)
            tag_map['J'] = wn.ADJ
            tag_map['V'] = wn.VERB
            tag_map['R'] = wn.ADV
            lemmatizer = WordNetLemmatizer()
            df['sample_utterance'] = df['sample_utterance'].apply(self._lemmatize, tagMap=tag_map, ignoreStopWords=True, lemmatizer=lemmatizer)
        df['sample_utterance'] = [word_tokenize(entry) for entry in df['sample_utterance']]
        # vectorize the data
        Tfidf_vectored = TfidfVectorizer(max_features=5000)
        Tfidf_vectored.fit(self.trainingData)
        Train_X_Tfidf = Tfidf_vectored.transform(self.trainingData)
        self.Naive = naive_bayes.MultinomialNB()
        self.Naive.fit(Train_X_Tfidf, df['intent_name'])

    def getIntent(self, utterance):
        vectorizer = TfidfVectorizer(max_features=5000)
        vectorizer.fit(self.trainingData)
        vectored_transformed = vectorizer.transform([utterance])
        predictions_NB = self.Naive.predict(vectored_transformed)
        score = self.Naive.predict_proba(vectored_transformed)
        probability_matrix = sorted(zip(self.Naive.classes_, score[0]), key= lambda x: x[1], reverse=True)
        return {
            'intent' : predictions_NB[0],
            'probability' : sorted(score[0], reverse=True)[0],
            'probability_matrix' : probability_matrix
        }

    def _lemmatize(self, value, tagMap, ignoreStopWords, lemmatizer):
        outputList = []
        word = str(value).strip("'[]")
        word = word_tokenize(value)
        for word, tag in pos_tag(word):
            if (word not in stopwords.words('english') or ignoreStopWords==False) and word.isalpha():
                word_Final = lemmatizer.lemmatize(word, tagMap[tag[0]])
                outputList.append(word_Final)
        return str(outputList)





