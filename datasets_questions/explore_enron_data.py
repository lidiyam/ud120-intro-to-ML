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

count = 0
for user in enron_data:
    if enron_data[user]['poi'] == 1:
        count+=1
print "count poi: " + str(count)

# James Prentice's stock
print "James Prentice stock: " + str(enron_data["PRENTICE JAMES"]["total_stock_value"])

# Wesley Colwell, # of emails to POI
print "# of emails to POI: " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

# value of stock options exercised by Jeffrey K Skilling
print "Jeffrey K Skilling stock options exercised: " + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

# How many folks in this dataset have a quantified salary? What about a known email address?
count_salary = 0
count_emails = 0
for user in enron_data:
	if enron_data[user]["salary"] != "NaN":
		count_salary+=1
	if enron_data[user]["email_address"] != "NaN":
		count_emails+=1
print "Known salary:"
print count_salary
print "Known emails:"
print count_emails
