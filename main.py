'''
    This server returns a json response from csv files at diffrent api endpoints

'''


from flask import Flask, request #import main Flask class and request object
from flask import render_template


app = Flask(__name__)       #create the Flask app




@app.route('/')
def home():
    return render_template('index.html')

# run the application
if __name__ == "__main__":
    app.run(debug=True, port=5000)
