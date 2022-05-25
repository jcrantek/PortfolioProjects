#!/usr/bin/env python -W ignore::DeprecationWarning
# coding: utf-8

# ### Project 5 - Identify Fraud from Enron Email
# Jeremy Crantek<br>
# Western Governor's University<br>
# September 29, 2020

import sys
import pickle
sys.path.append("../tools/")
import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV, train_test_split
#from sklearn.cross_validation import train_test_split
from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

print ("\n")
print ("************************")
print ("Project 5 - Identify Fraud from Enron Email")
print ("************************\n")

### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
financial_features = ['salary', 
                     'deferral_payments', 
                     'total_payments', 
                     'loan_advances', 
                     'bonus', 
                     'restricted_stock_deferred', 
                     'deferred_income', 
                     'total_stock_value', 
                     'expenses', 
                     'exercised_stock_options', 
                     'other', 
                     'long_term_incentive', 
                     'restricted_stock', 
                     'director_fees']

email_features = ['to_messages', 
                 'email_address', 
                 'from_poi_to_this_person', 
                 'from_messages', 
                 'from_this_person_to_poi', 
                 'shared_receipt_with_poi'] 

poi_label = ['poi']
features_list = poi_label + email_features + financial_features

print ("Removing email addresses from the feature list...\n")
features_list.remove('email_address')

# Load the dictionary containing the dataset
print ("Loading dictionary into data_dict")
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)


# Total number of data points
print ("\nThe total number of data points: {0}".format(len(data_dict)))

# Investigating POIs in dataaset
poi = 0
for name in data_dict:
    if data_dict[name]['poi'] == True:
        poi+=1

print ("\nThe total number of POI is: {0}".format(poi))
print ("\nThe total number of non POI is: {0}".format(len(data_dict)-poi))
print ("\nThe number of features currently: {0}".format(len(features_list)))
print ("\n")
print (features_list)

### Task 2: Remove outliers

# ## Remove Outliers

# A simple scatterplot ought to show us how our data is grouped.
data = featureFormat(data_dict, ['total_payments', 'total_stock_value'])

for point in data:
    x = point[0]
    y = point[1]
    plt.scatter(x, y)

plt.title("Before TOTAL Removal")
plt.xlabel("Total Payments")
plt.ylabel("Total Stock Value")
plt.show()

# That's quite the outlier in that scatterplot. 
# Let's find out what it is and remove it so we can get a better look at our overall data grouping.

# What is the outlier?
#outlier = max([int(i['salary']) for i in data_dict.values()])
#outlier = max(data_dict["salary"], key=data_dict.get)

print ("\nRemoving Outliers...\n")

outlier_detect = []

for emp in data_dict:
    if data_dict[emp]['total_payments'] != "NaN":
        outlier_detect.append((emp, data_dict[emp]['total_payments']))

outlier = sorted(outlier_detect, key = lambda x: x[1], reverse=True)[0:1]

print ("\nThe outlier is {}".format(outlier))
print ("\nLet's remove TOTAL.\n")

#Now let's remove or drop TOTAL so our data is distributed better
print ("Removing TOTAL from our data...\n")
data_dict.pop("TOTAL", 0)

# Update our scatterplot
data = featureFormat(data_dict, ['total_payments', 'total_stock_value'])
for point in data:
    x = point[0]
    y = point[1]
    plt.scatter(x, y)

plt.title("After TOTAL Removal")
plt.xlabel("Total Payments")
plt.ylabel("Total Stock Value")
plt.show()

print ("\nAdding 2 new features (ratio_from_poi and ratio_to_poi)...\n")

# ratio_from_poi added to data_dict
for emp in data_dict:
    message_from_poi = data_dict[emp]['from_poi_to_this_person']
    to_message = data_dict[emp]['to_messages']
    if to_message != 'NaN' and message_from_poi != 'NaN':
       data_dict[emp]['ratio_from_poi'] = (message_from_poi*1.0)/(to_message*1.0)
    else:
       data_dict[emp]['ratio_from_poi'] = 0

# ratio_to_poi added to data_dict
for emp in data_dict:
    message_to_poi = data_dict[emp]['from_this_person_to_poi']
    from_message = data_dict[emp]['from_messages']
    if  from_message != 'NaN' and message_to_poi != 'NaN':
        data_dict[emp]['ratio_to_poi'] = (message_to_poi*1.0)/(from_message*1.0)
    else:
        data_dict[emp]['ratio_to_poi'] = 0

# from heapq import nlargest 
  
# threehighest = nlargest(3, data_dict, key = data_dict.get) 
  
# print("New features are now in the data_dict...\n") 
# print("Keys: Values") 
  
# for val in threehighest:
#     if val == "SKILLING JEFFREY K"
#     print(val, ":", data_dict.get(val)) 
        
features_list_new = features_list + ['ratio_to_poi'] + ['ratio_from_poi']
print ("\nHere is the new features list: \n")
print ("There are now {0} features in our list.".format(len(features_list_new)))
print (features_list_new)

print ("Checking for missing values...\n")
missingvals = {}
total_features = data_dict[data_dict.keys()[0]].keys()
for feature in total_features:
    missingvals[feature] = 0
for emp in data_dict:
    for feature in data_dict[emp]:
        if data_dict[emp][feature] == "NaN":
            missingvals[feature] += 1
print("The total number of missing values for each feature: ")

for feature in missingvals:
    print(feature + " : " + str(missingvals[feature]))

print ("\nChecking for NaN values and replacing with zeroes...\n")
for emp in data_dict:
    for f in data_dict[emp]:
        if data_dict[emp][f] == 'NaN':
            data_dict[emp][f] = 0

print ("Checking for missing values again...\n")
missingvals = {}
total_features = data_dict[data_dict.keys()[0]].keys()
for feature in total_features:
    missingvals[feature] = 0
for emp in data_dict:
    for feature in data_dict[emp]:
        if data_dict[emp][feature] == "NaN":
            missingvals[feature] += 1

print("After removing NaN, the total number of missing values for each feature: ")

for feature in missingvals:
    print(feature + " : " + str(missingvals[feature]))

print ("\nLoading updated data_dict into my_dataset...\n")
my_dataset = data_dict

print ("Extracting features and labels for local testing...\n")
data = featureFormat(my_dataset,features_list_new, sort_keys = True)
labels, features = targetFeatureSplit(data)

# print ("Using VarianceThreshold to remove more than 85 percent of samples\n")
# from sklearn.feature_selection import VarianceThreshold
# var = VarianceThreshold(threshold=(.85 * (1 - .85)))
# features = var.fit_transform(features)

# print ("Length of features after Variance Threshold: {0}\n".format(len(features)))

print ("Use Univariate Feature Selection to select features...\n")
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(f_classif, k=19)
selector.fit(features, labels)
scores = zip(features_list_new[1:], selector.scores_)
sort_scores = sorted(scores, key = lambda x: x[1], reverse = True)
print ("Use SelectKBeast to score features...\n")
print ("Feature Scores: \n")
print (sort_scores)

# A bar graph to show the scores side by side
# figure, axes = plt.subplots(figsize=(10,11))
# axes.barh(sort_scores, width = 15, color = "green")
# axes.set_title("Feature Scores", fontsize = 14)
# axes.set_xlabel("KBest Scores")
# axes.set_ylabel("Features")
# plt.show()

# labels, ys = zip(*sort_scores)
# xs = np.arange(len(labels)) 
# width = 15

# fig = plt.figure()                                                               
# ax = fig.gca()  #get current axes
# ax.barh(xs, ys, width)

# #Remove the default x-axis tick numbers and  
# #use tick numbers of your own choosing:
# ax.set_xticks(xs)
# #Replace the tick numbers with strings:
# ax.set_xticklabels(labels)
# #Remove the default y-axis tick numbers and  
# #use tick numbers of your own choosing:
# ax.set_yticks(ys)


# plt.barh(ys, xs, width, align='center', color="green")
# plt.xticks(xs, labels)
# plt.yticks(ys)
# plt.show()


# Now we have a newer feature list...
feature_list_updated = poi_label + [(i[0]) for i in sort_scores[0:8]]
print ("\nRevised features list...\n")
print feature_list_updated

print ("Use MinMaxScaler to scale necessary features...\n")
from sklearn.preprocessing import MinMaxScaler
data = featureFormat(my_dataset, feature_list_updated, sort_keys = True)
labels, features = targetFeatureSplit(data)
scaler = MinMaxScaler()
features = scaler.fit_transform(features)

### Task 4: Try a varity of classifiers
print ("Applying Algorithms...")

from sklearn.model_selection import train_test_split, GridSearchCV 

# Split the data into 70% train data and 30% test data
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

print ("\nfeatures_train: {0}".format(len(features_train)))
print ("features_test: {0}".format(len(features_test)))
print ("labels_train: {0}".format(len(labels_train)))
print ("labels_test: {0}".format(len(labels_test)))
print ("features: {0}".format(len(features)))
print ("labels: {0}\n".format(len(labels)))


### Decision Tree Classifier

# import the decisiontreeclassifier from sklearn
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# apply some random parameters
clf = DecisionTreeClassifier(max_depth = 5, random_state = 45)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

# Now let's see those metrics
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test,pred)
print ("\n")
print ("*******************************")
print ("Decision Tree Classifier: \n")
print "Accuracy: \n" + str(accuracy)
print "Precision Score: \n" + str(precision_score(labels_test,pred))
print "Recall Score: \n" + str(recall_score(labels_test,pred))
print "F1 Score: \n" + str(f1_score(labels_test,pred))


### Naive Bayes Classifier

# import NaiveBayes from sklearn
from sklearn.naive_bayes import GaussianNB

# default parameters
clf = GaussianNB()
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

# Now let's see those metrics
accuracy = accuracy_score(labels_test,pred)
print ("\n")
print ("*******************************")
print("Naive Bayes Classifier: \n")
print "Accuracy: \n" + str(accuracy)
print "Precision Score: \n" + str(precision_score(labels_test,pred))
print "Recall Score: \n" + str(recall_score(labels_test,pred))
print "F1 Score: \n" + str(f1_score(labels_test,pred))

### Random Forest Classifier

# import RandomForest from sklearn
from sklearn.ensemble import RandomForestClassifier

# put in some random parameters
clf = RandomForestClassifier(random_state = 45, n_estimators = 150)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test,pred)

# Now let's see those metrics
print ("\n")
print ("*******************************")
print ("Random Forest Classifier: \n")
print "Accuracy: \n" + str(accuracy)
print "Precision Score: \n" + str(precision_score(labels_test,pred))
print "Recall Score: \n" + str(recall_score(labels_test,pred))
print "F1 Score: \n" + str(f1_score(labels_test,pred))


### Ada Boost Classifier

# import AdaBoost from sklearn
from sklearn.ensemble import AdaBoostClassifier

# default parameters
clf = AdaBoostClassifier(n_estimators = 50, learning_rate = 0.1)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test,pred)

# Now let's see those metrics
print ("\n")
print ("*******************************")
print ("AdaBoost Classifier: \n")
print "Accuracy: \n" + str(accuracy)
print "Precision Score: \n" + str(precision_score(labels_test,pred))
print "Recall Score: \n" + str(recall_score(labels_test,pred))
print "F1 Score: \n" + str(f1_score(labels_test,pred))


### K-Nearest Neighbors Classifier

# import KNN from sklearn
from sklearn.neighbors import KNeighborsClassifier

# parameter of 3
clf = KNeighborsClassifier(3)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)
accuracy = accuracy_score(labels_test,pred)

# Now let's see those metrics
print ("\n")
print ("*******************************")
print ("K-Nearest Neighbors Classifier: ")
print "Accuracy: \n" + str(accuracy)
print "Precision Score: \n" + str(precision_score(labels_test,pred))
print "Recall Score: \n" + str(recall_score(labels_test,pred))
print "F1 Score: \n" + str(f1_score(labels_test,pred))


### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

print ("\nHyperparameter Tuning Naive Bayes...\n")

# Setting NaiveBayes to an object called nb, necessary for GridSearchCV to work
nb = GaussianNB()

# test parameters to feed the GridsearchCV and return the highest NaiveBayes accuracy score
#search_grid={'n_estimators':[500,1000,2000],'learning_rate':[.001,0.01,.1]}
from random import seed
np.random.seed(999)
nb_param = {'var_smoothing': np.logspace(0,-9, num=100)}

# Apply StratifiedShuffleSplit to run our numerous algorithm folds
from sklearn.model_selection import StratifiedShuffleSplit

# Running 3 random folds, with a test size of 35%
cv = StratifiedShuffleSplit(n_splits=10, test_size=0.35, random_state=42)
search = GridSearchCV(estimator = nb, param_grid = nb_param, scoring = 'accuracy', n_jobs = 1, cv=cv)
#search = GridSearchCV(estimator = ada, param_grid = search_grid, scoring = 'accuracy', cv=cv)

# This will return the overall best parameters to use in another DecisionTree algorithm 
# to return the highest accuracy score
print ("Our best parameters to boost the accuracty of the Naive Bayes Classifier...\n")
search.fit(features,labels)
print (search.best_params_)
print ("\n")

# This is the best possible score using the parameters we fed the GridSearch
print ("Our best possible precision after running several splits...\n")
print (search.best_score_)

# Now we'll apply our newly fine tuned parameters to an Naive Bayes algorithm
from sklearn.model_selection import cross_val_score
print ("Using cross validation to find the mean accuracy of a few splits of our data...\n")
score = np.mean(cross_val_score(nb,features, labels, scoring = 'accuracy', cv=cv , n_jobs = 1))
print(score)
print ("\n")


# Our hypertuned parameters are now applied
clf = GaussianNB(var_smoothing=1.0)
clf.fit(features_train,labels_train)
pred = clf.predict(features_test)

# print ("Now we'll run our hypertuned parameters against our original AdaBoost Classifier...\n")
# print ("*******************************")
# print ("Our hypertuned results...\n")
# print "AdaBoost Classifier: \n"
# print "Accuracy: \n" + str(accuracy)
# print "Precision Score: \n" + str(precision_score(labels_test,pred))
# print "Recall Score: \n" + str(recall_score(labels_test,pred))
# print "F1 Score: \n" + str(f1_score(labels_test,pred))

print ("Now we'll run our hypertuned parameters against our original Naive Bayes Classifier...\n")
accuracy = accuracy_score(labels_test,pred)
print ("\n")
print ("*******************************")
print("Naive Bayes Classifier: \n")
print "Accuracy: \n" + str(accuracy)
print "Precision Score: \n" + str(precision_score(labels_test,pred))
print "Recall Score: \n" + str(recall_score(labels_test,pred))
print "F1 Score: \n" + str(f1_score(labels_test,pred))

# print ("\nListing out the most important features...")
# importances = clf.feature_importances_
# for index, item in enumerate(importances):
#     if item > 0.3:        
#         print '\nThe index of the most powerful feature is = {0} and the importance is = {1} '.format(index, item)

# indices = np.argsort(importances)[::-1]
# print "\nFeature Ranking: "
# for i in range(10):
#     print "{} Feature no.{} ({})".format(i+1,indices[i],importances[indices[i]])

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.
print ("\nDumping all of the data for local testing...\n")
dump_classifier_and_data(clf, my_dataset, features_list)
