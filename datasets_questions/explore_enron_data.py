#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# 
print "Data Observation Number:", len(enron_data)
total_keys = enron_data.keys()
print "[Debug] Total Keys:", total_keys

print "Feature Number:", len(enron_data[total_keys[0]])

# POI
poi_number = 0
for i in range(len(total_keys)):
    if enron_data[total_keys[i]]["poi"] == 1:
        poi_number += 1

print "POI Number:", poi_number

# Search for POI
# sys.argv settings
# regex search
import sys
import re
combStrList = list()
poi_search_file = sys.argv[1]
fid = open(poi_search_file, 'r')
for line in fid:
    if re.match(r'^\(.*', line):
        tmpArray = re.sub(',', '', line.strip()).split(' ')
        combStr = (tmpArray[1] + " " + tmpArray[2]).upper()
        combStrList.append(combStr)

fid.close()

tPoiNum = 0
for name in combStrList:
    for hashList in total_keys:
        if re.search(name, hashList):
            if enron_data[hashList]["poi"] == 1:
                print name, hashList
                tPoiNum += 1

print "Selected POI Number:", len(combStrList)

# James Prentice
print enron_data["PRENTICE JAMES"]

# Wesley Colwell
print enron_data["COLWELL WESLEY"]

# Jeffrey K Skilling
print enron_data["SKILLING JEFFREY K"]
