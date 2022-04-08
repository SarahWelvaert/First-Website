from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv
app = Flask(__name__)
#global variable for accessing the csv data file
YOGA_PATH = app.root_path + '/classes.csv'
#global variable for classes headers
CLASSES_KEYS = ['slug', 'name', 'type', 'level', 'date', 'duration', 'trainer', 'description']
#function to read in classes.csv
def get_class():
    with open(YOGA_PATH, 'r') as csvfile:
            data = csv.DictReader(csvfile)
            classes_list = {}
            for yoga in data:
                classes_list[yoga['slug']] = yoga
    return classes_list
def sort_by_dates(classes_list):
        
#function to write out the data to csv
def set_class(classes_list):
    with open(YOGA_PATH, mode ='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CLASSES_KEYS)
        writer.writeheader()
        for yoga in classes_list.values():
            writer.writerow(yoga)