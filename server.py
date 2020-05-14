
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hellooooooo'



@app.route('/')
def my_home():
    return render_template('index.html')



@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# Database data

# def write_to_file(data):
#   with open('database.txt', mode='a') as database:
#     email = data["email"]
#     subject = data["subject"]
#     message = data["message"]
#     file = database.write(f'\n{email},{subject},{message}')


# Database with csv::::

def write_to_csv(data):
  with open('database.csv', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return 'Something Went Wrong! Please try Again.'








# @app.route('/index.html')
# def my_home():
#     return render_template('index.html')

# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')

# @app.route('/work.html')
# def my_work_details():
#     return render_template('work.html')


# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')
