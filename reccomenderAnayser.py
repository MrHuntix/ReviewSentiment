import os
import random
from nltk.probability import FreqDist
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from nltk import NaiveBayesClassifier, classify
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import pickle
import regex as re

p=open("positive.txt","r").read()
n=open("negative.txt","r").read()
all_reviews=[]

for i in p.split("\n"):
    all_reviews.append((i,"pos"))

for i in n.split("\n"):
    all_reviews.append((i,"neg"))

random.shuffle(all_reviews)

print("a")

reviews=[]

for word,value in all_reviews:
    reviews.append((re.tok_rem(word),value))

save_all_reviews=open("all_reviews.pickle","wb")
pickle.dump(reviews,save_all_reviews)
save_all_reviews.close()
print("b")
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

def train(features,samples_proportion):
    train_size = int(len(features) * samples_proportion)
    train_set, test_set = features[:train_size], features[train_size:]
    print ('Training set size = ' + str(len(train_set)) + ' reviews')
    print ('Test set size = ' + str(len(test_set)) + ' reviews')
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier

wordList=get_words_in_reviews(reviews)
print("c")
wordFeatures=get_word_features(wordList)
Wfeatures=[k for k in wordFeatures]
save_all_features = open("word_features.pickle","wb")
pickle.dump(Wfeatures, save_all_features)
save_all_features.close()
print("d")
training_set=classify.apply_features(extract_features,reviews)
print("e")

train_set, test_set, classifier=train(training_set, 0.8)
save_classifier = open("originalnaivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
print("f")
print ('Accuracy on the training set = ' + str(classify.accuracy(classifier, train_set)*100))
print ('Accuracy of the test set = ' + str(classify.accuracy(classifier, test_set)*100))





