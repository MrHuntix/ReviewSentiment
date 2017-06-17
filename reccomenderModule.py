import os
import random
from nltk.probability import FreqDist
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import NaiveBayesClassifier, classify
from sklearn.feature_extraction.text import CountVectorizer
import pickle

def get_words_in_reviews(reviews):
    all_words=[]
    for (words,sentiment) in reviews:
        all_words.extend(words)
    return(all_words)

def get_word_features(wordList):
    wordList=FreqDist(wordList)
    word_features=wordList.keys()
    return word_features

def extract_features(document):
    document_words=set(document)
    features={}
    for word in Wfeatures:
        features["contains(%s)" % word]=(word in document_words)
    return features

def train(features, samples_proportion):
    train_size = int(len(features) * samples_proportion)
    train_set, test_set = features[:train_size], features[train_size:]
    print ('Training set size = ' + str(len(train_set)) + ' reviews')
    print ('Test set size = ' + str(len(test_set)) + ' reviews')
    return train_set, test_set

all_reviewsf=open("all_reviews.pickle","rb")
reviews=pickle.load(all_reviewsf)
all_reviewsf.close()

word_featuresf=open("word_features.pickle","rb")
Wfeatures=pickle.load(word_featuresf)
word_featuresf.close()

training_set=classify.apply_features(extract_features, reviews)
train_set, test_set=train(training_set, 0.8)

classifierf=open("originalnaivebayes.pickle","rb")
classifier=pickle.load(classifierf)
classifierf.close()

def PosOrNeg(text):
    a=[e.lower() for e in text.split()]
    feats=extract_features(a)
    return classifier.classify(feats)
