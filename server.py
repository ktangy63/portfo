from flask import Flask, render_template, send_from_directory, request, redirect
import os
import csv

app = Flask(__name__)
print(__name__)

# Define your routes

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            # write_to_file(data)
            write_to_csv(data)
            # file.close()
            return redirect('/thankyou.html')
        except:
            return 'DB save failed'
    else:
        return 'Something went wrong'
    
# def write_to_file(data):
#     with open("database.txt", 'a') as f:  
#         for key, value in data.items():  
#             f.write('%s:%s\n' % (key, value))
#     return

def write_to_csv(data):
    with open("database.csv", newline='', mode='a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
    return

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
