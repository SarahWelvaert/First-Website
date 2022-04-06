from flask import Flask, render_template, request, redirect, url_for
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
#function to write out the dinosaurs data to csv
def set_class(classes_list):
    with open(YOGA_PATH, mode ='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=CLASSES_KEYS)
        writer.writeheader()
        for yoga in classes_list.values():
            writer.writerow(yoga)
@app.route('/')
def index():
    
    return render_template('index.html')
    
@app.route('/classes')
@app.route('/class_id')
@app.route('/classes/<class_id>')
def classes(class_id=None):
        #fill in the logic for the 3 routes
    classes=get_class()
    
    if class_id and class_id in classes.keys():
       y_class = classes[class_id]
       return render_template('class.html', y_class=y_class, classes =classes)
    
    else:
        return render_template('classes.html', classes=classes)


# @app.route('/classes/<class_id>')
# def class_id():
#     return render_template('class.html')
@app.route("/classes/create", methods=['GET', 'POST'])
def add_class():
#     # if POST request received (form submitted)
    if request.method == 'POST':
#        # get classes.csv data
        classes = get_class()
#        # create new dict to hold class data from form
        newClass={}
#        
    else:
        return render_template('class_form.html')
