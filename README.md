# PresidentialAPI

## Instructions:
* Install requirements:
    > pip install flask
* Running the Servers:
    > python request.py
    
    > python get_data.py
* Make a GET request to get the csv file:
    > GET http://127.0.0.1:5001/data/all
    or
    > GET http://127.0.0.1:5001/data/all?format=csv
* Make a GET request to get a customized JSON:
    > GET http://127.0.0.1:5001/data/all?format=json
    
## About the code:
* The project makes use of two different servers to get data and process it to return a file specified
* The user can choose the customized file format in query - CSV (default if not specified) or JSON 
* The project is segregated into the different classes and uses Object Oriented Approach for better code reusabilty, clarity and understanding 

## Improvements
* Ability to pass JSON data in `RequestBody`, so the program can return the processed CSV
* Making use of standard logic that can convert any JSON data into a CSV
* Make use of queries to get certain results without having to stick to entire data
