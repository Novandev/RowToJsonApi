
# Row To JSON

Row To Json is a JSON API that does the following
- Accepts a post request with the body being a CSV file
- Processes said CSV file and extracts just the columns that contains numerical(continuous) data
- From the columns that contain numerical data, it drops any and all null or NAN values.
- Returns a JSON file that contains the descriptive statitics of the numerical columns

## Getting Started

To run this project clone the repository, start a virtual environment using conda or mvenv (or any virtual environment for python) and run the following command:
```
python3 app.py
```
This will start a server on your system that wull allow you to perform a post request to obtain your statistics


### Prerequisites

Python3



## Deployment

This API can be used in any stack as it is publicly availible and returns JSON

## Built With

* [Flask](http://flask.pocoo.org/) - Python Web framework 
* [Pandas](https://pandas.pydata.org/) - For access to process and transform numerical data in a csv file




## Authors

* **Novan Adams** - *Initial work* - [Novandev](https://github.com/Novandev)

See also the list of [contributors](https://github.com/Novandev/RowToJson/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

