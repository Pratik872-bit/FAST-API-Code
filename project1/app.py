from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from typing import Literal,Annotated,Optional
from fastapi.responses import JSONResponse
import pickle
import pandas as pd

#import ML model
with open('project1/model.pkl','rb') as f:
    model=pickle.load(f)
    
app=FastAPI()

#create pydantic to validate incoming data 
class UserInput(BaseModel):
    sepal_length:Annotated[float,Field(...,description='sepal length of the flower')]
    sepal_width:Annotated[float,Field(...,description='sepal width of the flower')]
    petal_length:Annotated[float,Field(...,description='city where the patient living')]
    petal_width:Annotated[float,Field(...,gt=0,lt=120,description='Age of the patient')]
   

@app.post('/predict')
def prediction(data:UserInput):
    
    input_df=pd.DataFrame([{
        'sepal_length':data.sepal_length,
        'sepal_width':data.sepal_width,
        'petal_length':data.petal_length,
        'petal_width':data.petal_width
    }])
    
    prediction=int(model.predict(input_df)[0])
    return JSONResponse(status_code=200,content={'predicted_flower':prediction})
    
    
    
    
    