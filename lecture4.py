from doctest import Example
from email import message
import json
from os import path #package who help to load the json data 
from fastapi import FastAPI ,Path ,HTTPException,Query #to handle the 404 status code
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

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of the patient in the db',example='P001')):
    #load data
    data=load_data()
    
    if patient_id in data: # patient data madhe aahe ka nahi te check karate  if found then retun the patient data from the data 
        return data[patient_id] 
    raise HTTPException(status_code=404,detail='patient not found')

@app.get('/sort')
def sorted_patients(sort_by:str=Query(...,description='sort on the basis of height and weight or bmi'),order:str=Query('asc',description='sort in desc order')):
    valid_fileds=['height','weight','bmi']
    if sort_by not in valid_fileds:
        raise HTTPException(status_code=404,detail=f'Invalid filed select from {valid_fileds}')
    if order not in ['asc','desc']:
        raise HTTPException(status_code=404,detail='invalid order select between asc and desc')
    data=load_data()
    sort_order=True if order=='desc' else False
    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)
    return sorted_data


    

