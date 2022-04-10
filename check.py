
from datetime import datetime
import csv

#global variable for accessing the csv data file

#global variable for classes headers
CLASSES_KEYS = ['name', 'type', 'level', 'date', 'duration', 'trainer', 'description']
#function to read in classes.csv
def get_class():
    with open('classes.csv','r') as csvfile:
            data = csv.DictReader(csvfile)
            classes_list = list(data)
            dates = sorted(data, key = lambda row: datetime.strptime(row[3], "%d-%b-%y"))
            print(dates)
            
    return classes_list

get_class()