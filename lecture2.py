from fastapi import FastAPI
app=FastAPI()

@app.get("/") # home route 
def home():
    return {"message":"hello world"} # create basic server 

@app.get("/aboutpratik")
def pratik():
    return {"hi my name is pratik naik"}

@app.get("/prediction")
def predict():
    return {"dog"}

