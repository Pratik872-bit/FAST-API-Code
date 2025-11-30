import json #package who help to load the json data 
from fastapi import FastAPI
app=FastAPI()

def load_data():
    with open('patients.json','r') as f:  #this function will read the data from the patients file 
        data=json.load(f)
    return data


@app.get("/") # home route 
def home():
    return {"message":"Patients management system"} 

@app.get("/about")
def about():
    return {"a fully functional api to manage patients"}


@app.get("/view")
def view():
    data=load_data()# here the data will expose to this view route using load data function
    
    return data




