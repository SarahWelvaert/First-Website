#libraries
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import csv

app = Flask(__name__)
#global variable for accessing the csv data file
YOGA_PATH = app.root_path + '/classes.csv'
#global variable for classes headers
CLASSES_KEYS = ['name', 'type', 'level', 'date', 'duration', 'trainer', 'description']
#function to read in classes.csv
def get_class():
    with open(YOGA_PATH) as csvfile:
            data = csv.DictReader(csvfile)
            #Sorts by date and then turns csv data into a list of dictionaries
            data = sorted(data, key = lambda row: datetime.strptime(row['date'], "%m/%d/%y"))
            classes_list = list(data)
    return classes_list

#function to write out the data to csv
def set_class(classes_list):
    with open(YOGA_PATH, mode ='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CLASSES_KEYS)
        writer.writeheader()
        for yoga in classes_list:
            writer.writerow(yoga)

#routes
@app.route('/')
def index():
    
    return render_template('index.html')
   
@app.route('/classes/')
def classes():
    classes=get_class()
    return render_template('classes.html', classes=classes)

@app.route("/classes/<class_id>/")
def view_classes(class_id=None):
    #if a class id exists, then go to that class page otherwise go to the classes page
    if class_id:
        classes = get_class()
        class_id = int(class_id)
        return render_template('class.html',class_id = class_id, yoga_class = classes[class_id])
    else:
        return render_template('classes.html', classes=classes)

@app.route("/classes/create", methods=['GET', 'POST'])
def add_class():
    # if POST request received (form submitted)
   if request.method == 'POST':
       # get csv data
       classes = get_class()
       # add form data to new dict
       newClass={}
       #store from data
       newClass['name'] = request.form['name']
       newClass['type'] = request.form['type']
       newClass['level'] = request.form['level']
       newClass['date'] = request.form['date']
       newClass['duration'] = request.form['duration']
       newClass['trainer'] = request.form['trainer']
       newClass['description'] = request.form['description']
       # add new dict to csv data
       classes.append(newClass)
       # write csv data back out to csv file
       set_class(classes)
       # since POST request, redirect after Submit (we want the display to change so user knows form went through)
       return redirect(url_for('classes'))
   # if GET request received (display form)
   else:
       return render_template('class_form.html')

@app.route('/classes/<class_id>/edit', methods=['GET', 'POST'])
def edit_class(class_id = None):
    #get csv data
    classes = get_class()
    #dict to store form data
    update_class = {}
    #class id to integer, integer is index of class in list of dictionaries classes_list
    class_id = int(class_id)
    #store data from form
    if request.method == 'POST':
       update_class['name'] = request.form['name']
       update_class['type'] = request.form['type']
       update_class['level'] = request.form['level']
       update_class['date'] = request.form['date']
       update_class['duration'] = request.form['duration']
       update_class['trainer'] = request.form['trainer']
       update_class['description'] = request.form['description']
      
    #replace any old data with the new data from the form    
       classes[class_id]['name']= update_class['name']
       classes[class_id]['type']= update_class['type']
       classes[class_id]['level']= update_class['level']
       classes[class_id]['date']= update_class['date']
       classes[class_id]['duration']= update_class['duration']
       classes[class_id]['trainer']= update_class['trainer']
       classes[class_id]['description']= update_class['description']

       # write csv data back out to csv file
       set_class(classes)
       # since POST request, redirect after Submit 
       return render_template('class.html',class_id = class_id, yoga_class = classes[class_id])
    else: #go to form for first time
        if class_id:
            classes = get_class()
            class_id = int(class_id)
            class_name = classes[class_id]
        return render_template('class_form.html',classes=classes,class_id = class_id, yoga_class = classes[class_id])

   
