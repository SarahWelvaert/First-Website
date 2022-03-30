from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)
#global variable for accessing the csv data file
# DINO_PATH = app.root_path + '/dinosaurs.csv'
#global variable for dinosaur headers
# DINO_KEYS = ['slug', 'name', 'description', 'image', 'image-credit', 'source-url', 
# 'source-credit']
#function to read in dinosaurs.csv
# # def get_dinos():
#     with open(DINO_PATH, 'r') as csvfile:
#             data = csv.DictReader(csvfile)
#             dinosaurs = {}
#             for dino in data:
#                 dinosaurs[dino['slug']] = dino
#     return dinosaurs
#function to write out the dinosaurs data to csv
# def set_dinos(dinosaurs):
#     with open(DINO_PATH, mode ='w', newline='') as csv_file:
#         writer = csv.DictWriter(csv_file, fieldnames=DINO_KEYS)
#         writer.writeheader()
#         for dino in dinosaurs.values():
#             writer.writerow(dino)
@app.route('/')

def index():
    #fill in the logic for the 3 routes
    
    #if dino exists and it is in the list of dino names, render dino.html and pass the specific dinosaur dictionary
    # if dino and dino in dinosaurs.keys():
    #    dinosaur = dinosaurs[dino]
    #    return render_template('dino.html', dinosaur=dinosaur)
    #else, render the index.html template per normal
    # else:
    return render_template('index.html')
@app.route('/classes')
def classes():
    return render_template('classes.html')
@app.route("/classes", methods=['GET', 'POST'])
def add_dino():
    # if POST request received (form submitted)
   if request.method == 'POST':
       # get dinosaurs.csv data
       dinosaurs = get_dinos()
       # create new dict to hold dino data from form
       newDino={}
       # add form data to new dict
       newDino['slug'] = request.form['slug']
       newDino['name'] = request.form['name']
       newDino['description'] = request.form['description']
       newDino['image'] = request.form['image']
       newDino['image-credit'] = request.form['image-credit']
       newDino['source-url'] = request.form['source-url']
       newDino['source-credit'] = request.form['source-credit']
       # add new dict to csv data
       dinosaurs[request.form['name']] = newDino
       # write csv data back out to csv file
       set_dinos(dinosaurs)
       # since POST request, redirect after Submit (we want the display to change so user knows form went through)
       return redirect(url_for('index'))
   # if GET request received (display form)
   else:
       return render_template('add-dino.html')
@app.route("/classes", methods=['GET', 'POST'])
def dino_quiz():
    #do we have post data from the quiz?
    if request.method == 'POST':
               # get quiz data
        quizGuesses = {}
        quizGuesses['Question 1'] = request.form['continents']
        quizGuesses['Question 2'] = request.form.get('eggs', 'false')
        quizGuesses['Question 3'] = request.form.getlist('herbivores')
        quizGuesses['Question 4'] = request.form['extinct']
        quizGuesses['Question 3'] = " and ".join(quizGuesses["Question 3"])
        #save the correct answers
        quizAnswers = {
           'Question 1' : 'North America',
           'Question 2' : 'true',
           'Question 3' : 'Stegosaurus and Triceratops',
           'Question 4' : '66'
       }
       # check the data by printing it to the console
        print(quizGuesses)
       # for now, just go back home when done
        return render_template("quiz-results.html", quizGuesses = quizGuesses, 
quizAnswers=quizAnswers)
    #if GET, we are loading the page for the first time
    else:
       return render_template('dino-quiz.html')