'''
    This server returns a json response from csv files at diffrent api endpoints

'''
# OS Import section
import os
# Flask import section
from flask import Flask, request #import main Flask class and request object
from flask import render_template
from flask import Response,redirect, url_for,send_from_directory
from flask import json
from werkzeug import secure_filename
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

# Stats import section
import pandas as pd

app = Flask(__name__)       #create the Flask app
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





@app.route('/')
def home():
    '''-----Renders the home route-----'''
    return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


'''-----Api route-----'''
@app.route('/api',methods = ['POST'])
def api_return():
    '''-----File reading section-----'''
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # print(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            csv_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            original_file_df = pd.read_csv(csv_file)
            response_file_df_numeric =original_file_df._get_numeric_data()  # creates a datafram of only numeric values
            response_file_df_numeric.dropna(inplace=True)  # Drops to handle the na values


            '''-----Conversions to variables section for Json file-----'''
            csv_file_name =filename     # Takes the file name of the file
            original_columns = list(original_file_df.columns)   # The original colums list
            numeric_only_columns = list(response_file_df_numeric.columns)   # This takes only the numeric data
            print(response_file_df_numeric.head())


            '''---------Dictionary that will be converted to a json object and returned---------'''

            return_json_dict = {
            "fileName":csv_file_name,
            "originalColumns":original_columns,
            "numericColumns":numeric_only_columns,
            "stats":{
                "mean":dict(),
                "median":dict(),
                "mode": dict(),
                "max":dict(),
                "std": dict(),
                "skew": dict()
            },
            }
            '''-----Stats conversion section-----'''

            '''Mean'''

            for column in response_file_df_numeric:
                 return_json_dict['stats']['mean'][column]= response_file_df_numeric[column].mean()


            '''Median'''
            for column in response_file_df_numeric:
                 return_json_dict['stats']['median'][column]= response_file_df_numeric[column].median()

            '''Mode'''
            for column in response_file_df_numeric:
                 return_json_dict['stats']['mode'][column] = list(response_file_df_numeric[column].mode())
            '''Max'''
            for column in response_file_df_numeric:
                 return_json_dict['stats']['max'][column] = float(response_file_df_numeric[column].max())
            '''STD'''
            for column in response_file_df_numeric:
                 return_json_dict['stats']['std'][column] = float(response_file_df_numeric[column].std())

            '''Skew'''
            for column in response_file_df_numeric:
                 return_json_dict['stats']['skew'][column] = float(response_file_df_numeric[column].skew())


            '''-----JSON CONVERSION-----'''

            json_object = json.dumps(return_json_dict)
            response_json = Response(json_object, status=200, mimetype='application/json')
            response_json.headers['Link'] = 'http://github.com/Novandev'
            # return  response_json
            return response_json




# run the application
if __name__ == "__main__":
    app.run(debug=True, port=5000)
