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
            classes_list = list(data)
    return classes_list

#function to write out the data to csv
def set_class(classes_list):
    with open(YOGA_PATH, mode ='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CLASSES_KEYS)
        writer.writeheader()
        for yoga in classes_list:
            writer.writerow(yoga)
@app.route('/')
def index():
    
    return render_template('index.html')
    
@app.route('/classes')

def classes():
        #fill in the logic for the 3 routes
    classes=get_class()
    return render_template('classes.html', classes=classes)

@app.route("/classes/<class_id>")
def view_class(class_id=None):
    if class_id:
        classes = get_class()
        return render_template('class.html',class_id = class_id, yoga_class = classes[class_id])


@app.route("/classes/create", methods=['GET', 'POST'])
def add_class():
#     # if POST request received (form submitted)
   if request.method == 'POST':
       # get dinosaurs.csv data
       classes = get_class()
       # create new dict to hold dino data from form
       newClass={}
       # add form data to new dict
       
      
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
