# FastAPI Playlist – Video 1 Notes

## Why Learn FastAPI & What Are APIs?

### 🚀 Why This Playlist?

* Channel’s vision: help students master AI by covering essential topics.
* Already covered: Machine Learning, Deep Learning, NLP, etc.
* AI requires creating models **and exposing them to users** — this requires **APIs**.
* Most ML products in industry expose their models using **FastAPI**.
* **9 out of 10 companies** use FastAPI for ML model APIs because of:

  * High performance
  * Scalability
  * Production-ready features

---

### 🎯 Playlist Structure

| Part  | What You Learn             | Goal                                           |
| ----- | -------------------------- | ---------------------------------------------- |
| **1** | FastAPI Fundamentals       | Understand the framework using a small project |
| **2** | FastAPI + Machine Learning | Build an API around an ML model                |
| **3** | Deployment                 | Dockerize & deploy the API on AWS              |

**Total videos:** ~15
**Timeline:** 21–25 days

---

### 🧠 What is an API?

**API = A connector that allows two software components to communicate using defined rules.**

#### Simple Definition

An API is like a **bridge** between:

* **Frontend** → what the user interacts with
* **Backend** → business logic, database, ML model

#### Example Flow

Udemy course search:

```
Frontend → API → Backend → Database → Backend → API → Frontend
```

Response always comes in **JSON** format.

---

### 🍽️ Restaurant Analogy

| Real World      | Software        |
| --------------- | --------------- |
| Customer        | Frontend        |
| Waiter          | API             |
| Kitchen & Chefs | Backend         |
| Menu            | Rules/Protocols |
| Food Served     | JSON Response   |

API works like a **waiter** connecting the customer (frontend) to the kitchen (backend).

---

### 🔍 Why APIs Were Invented?

#### Before APIs → **Monolithic Architecture**

* Frontend + Backend together in one application
* Very **tightly coupled**
* Hard to share data or give external access
* Example: IRCTC **could not** give train info to MakeMyTrip directly

#### After APIs → **Decoupled Architecture**

* Backend becomes an **independent service**
* APIs expose **endpoints** like:

```
irctc.com/trains?from=Pune&to=Mumbai&date=2025-01-04
```

* External apps (MakeMyTrip, Yatra, Goibibo) can safely request data
* Backend logic stays protected

---

### 🌍 Standard Protocols & Data Format

| Concept  | Why Used                                                  |
| -------- | --------------------------------------------------------- |
| **HTTP** | Communication over the Internet                           |
| **JSON** | Universal data format readable by Python, Java, PHP, etc. |

Example JSON:

```json
{
  "train_name": "Shatabdi Express",
  "departure": "07:45"
}
```

---

### 📱 APIs Solve Another Huge Problem

Earlier, companies had to maintain **three separate applications**:

* Website
* Android App
* iOS App

Each required its own:

* Database
* Backend
* Team & cost

**With APIs:**

```
Single Backend + Single Database → Used by multiple frontends
```

---

### 🤖 ML Perspective: APIs in AI/ML

Only one thing changes:

| Software World | ML World |
| -------------- | -------- |
| Database       | ML Model |

* ML Model returns **predictions** instead of stored data
* API exposes **predict** or **generate** endpoints

Example endpoints used by models:

```
/predict
/generate
```

**ChatGPT** works this way — the model isn't exposed, only the API is.

---

### 🎯 Summary

* **API = Communication bridge**
* APIs solve two major problems:

  1. Sharing data/models safely between applications
  2. Using a single backend for multiple frontends
* Essential for deploying ML / DL / GenAI models
* **FastAPI** is the most widely-used framework today for ML-based APIs

---

# FastAPI – Deep Introduction (Video 2 Notes)

## 1. Recap of Previous Video

In the last session, we learned:

* What an API is
* Why APIs are required
* Why learning FastAPI is important for Data Science, Machine Learning, and AI students

## 2. What is FastAPI?

FastAPI is a modern, high-performance web framework for building APIs using Python.

**One-line definition:**
FastAPI is a Python framework that allows you to build industrial-grade, fast, and scalable APIs with minimal code.

### Why FastAPI is powerful

* Extremely fast (comparable to Node.js and Go)
* Easy to write and understand
* Used heavily in ML model deployment

## 3. FastAPI Internals – What is it built on?

FastAPI is built using two key Python libraries:

| Library   | What it does                                     |
| --------- | ------------------------------------------------ |
| Starlette | Handles HTTP requests, routing, response sending |
| Pydantic  | Performs data validation and type checking       |

**Meaning:**

* **Starlette** = receives HTTP request and sends HTTP response
* **Pydantic** = checks if the input data is valid (correct type, format, etc.)

So, **FastAPI = Starlette (request handling) + Pydantic (validation)**

## 4. Why do we need data validation?

APIs accept data from users, which might be:

* Wrong format
* Wrong datatype
* Invalid or missing

Without validation, your system may crash.
**Pydantic** automatically validates input data, saving developers a lot of effort.

**Example:** If API expects a string `station name`, Pydantic ensures it is not a number or empty value.

## 5. Core Philosophies of FastAPI

### Philosophy 1 – Fast to Run

FastAPI APIs are extremely fast due to:

| Component         | Old Frameworks        | FastAPI                      |
| ----------------- | --------------------- | ---------------------------- |
| Gateway Interface | WSGI (synchronous)    | ASGI (asynchronous)          |
| Server            | Gunicorn              | Uvicorn                      |
| Execution         | One request at a time | Multiple concurrent requests |

**Why ASGI makes FastAPI faster**

* ASGI supports async/await
* Multiple requests can be processed in parallel
* No blocking waits

### Philosophy 2 – Fast to Code

FastAPI reduces development time because:

* **Automatic Input Validation** using Pydantic
* No extra code for checking datatypes
* **Auto-Generated Documentation** at `/docs` and `/redoc`

**Modern Library Support**
Works smoothly with:

* Scikit-Learn, TensorFlow, PyTorch (ML)
* SQLAlchemy (database)
* OAuth (authentication)
* Docker & Kubernetes (deployment)

## 6. Understanding WSGI vs ASGI

| Feature     | WSGI (Flask)         | ASGI (FastAPI)         |
| ----------- | -------------------- | ---------------------- |
| Nature      | Synchronous          | Asynchronous           |
| Requests    | One at a time        | Many at once           |
| Performance | Slower               | Faster                 |
| Use Case    | Traditional web apps | Real-time & ML systems |

**Summary:**

* **Flask** = Waiter who handles one order at a time
* **FastAPI** = Waiter who takes multiple orders and processes efficiently

## 7. How does an API work internally?

```
Client (browser/Postman)
↓ sends HTTP request
Web Server
↓
Gateway Interface (WSGI/ASGI)
↓ converts request format
API Code (Python)
↓ executes business logic / ML model
Response → Client
```

ASGI enables non-blocking processing, leading to speed and scalability.

## 8. Installing FastAPI and Uvicorn

```
python -m venv myenv
myenv\Scripts\activate
pip install fastapi uvicorn pydantic
```

**Uvicorn** = server that runs FastAPI apps

## 9. Writing Your First FastAPI App

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
```

Run using:

```
uvicorn main:app --reload
```

Visit:

```
http://127.0.0.1:8000
```

Response:

```
{"message": "Hello World"}
```

## 10. Creating Another Endpoint

```python
@app.get("/about")
def about():
    return {"message": "CampusX is an education platform to learn AI"}
```

Visit:

```
/about
```

## 11. Auto-Documentation

FastAPI generates interactive docs automatically.
Open:

```
http://127.0.0.1:8000/docs
```

You can:

* View API endpoints
* Test them
* Send requests without Postman

This makes API testing incredibly easy.

## 12. Summary of Video 2

You learned:
✔️ What FastAPI is
✔️ How it is built internally
✔️ Why FastAPI is faster than Flask
✔️ What ASGI and Uvicorn are
✔️ Why FastAPI reduces coding effort
✔️ How to install and build your first FastAPI API
✔️ How auto-documentation works


# FastAPI – Video 3 Notes 

## 1. Project Begins

In the previous videos, we learned what APIs are and got an introduction to FastAPI. From this video onwards, we start building a real project using FastAPI.

## 2. Project Overview

### Problem

Doctors give handwritten prescriptions on paper. Patients must carry these papers during every visit, which leads to issues:

* Papers can get lost
* Records can be misplaced
* Hard to maintain for years

### Solution Idea

Create a digital Patient Management System where:

* Doctor has an app
* They can create a profile for every patient
* Patient details like name, age, city, height, weight, and BMI are stored online

## 3. What Will Our API Do?

We will not build the frontend app, only the backend API.

### Features of our API:

| Operation       | What it does                     |
| --------------- | -------------------------------- |
| Create          | Add a new patient record         |
| Retrieve (View) | See all patient details          |
| Retrieve single | View one patient’s data using ID |
| Update          | Modify patient data              |
| Delete          | Remove patient from system       |

Data will be stored temporarily in a `patients.json` file instead of a database.

## 4. CRUD Operations

Every dynamic software performs four actions:

| Name | Full Form | Meaning              |
| ---- | --------- | -------------------- |
| C    | Create    | Add something new    |
| R    | Retrieve  | View existing data   |
| U    | Update    | Change existing data |
| D    | Delete    | Remove data          |

Examples:

* Instagram post → Create
* View profile → Retrieve
* Edit profile → Update
* Delete post → Delete

## 5. Websites and HTTP Methods

Websites use HTTP requests to communicate.

| CRUD     | HTTP Method | Meaning              |
| -------- | ----------- | -------------------- |
| Create   | POST        | Send data to server  |
| Retrieve | GET         | Get data from server |
| Update   | PUT         | Change existing data |
| Delete   | DELETE      | Remove data          |

These methods tell the server what operation to perform.

## 6. Our First Endpoint – View All Patients

### Step 1: JSON File

`patients.json` stores dummy patient records.

### Step 2: Helper Function

A function `load_data()` will:

* Open `patients.json`
* Read data
* Return patient records

### Step 3: Create GET Endpoint `/view`

When someone visits `/view`:

* API loads data from JSON file
* Returns all patient records

This is our Retrieve (GET) operation.

## 7. Running the App

Start the server using:

```
uvicorn main:app --reload
```

Then open:

```
http://127.0.0.1:8000/view
```

This shows all patient data.

Open docs at:

```
http://127.0.0.1:8000/docs
```

Test API using auto-generated documentation.

## 8. Summary of Video 3

You learned:

* Project idea (Patient Management System)
* Meaning and importance of CRUD
* HTTP methods: GET, POST, PUT, DELETE
* CRUD and HTTP mapping
* Created first API endpoint for viewing data
* Loaded patient data from JSON file


# FastAPI – Video 4 Notes

## What We Will Learn

In this video, we continue our FastAPI project and learn two very important concepts:

* **Path Parameters**
* **Query Parameters**

Both are used to send information to an API using the URL, but they serve different purposes.

---

## 1. Path Parameters

### What are Path Parameters?

Path parameters are dynamic parts of a URL that help us identify a specific resource.

**Example from last video:**

```
http://localhost:8000/view
```

This showed all patients.

To get only one specific patient:

```
http://localhost:8000/patient/P003
```

Here:

* `patient` → endpoint name
* `P003` → path parameter (patient ID)

### When to Use Path Parameters?

Use them when you want to:
✔ View one specific object
✔ Update one specific object
✔ Delete one specific object

**Examples in real apps:**

| App       | Path Parameter Example |
| --------- | ---------------------- |
| Instagram | /profile/rahul         |
| Zomato    | /order/12345           |

### Path Parameter in Code

```python
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str):
```

`{patient_id}` is the path parameter. The user must provide it.

If patient exists → return details
If not → return an error

### Improving Path Parameters

FastAPI provides a function called **Path()** to:
✔ Add description
✔ Add example values
✔ Add constraints

```python
patient_id: str = Path(..., description="ID of the patient", example="P01")
```

This improves the API documentation.

---

## HTTP Status Codes

Every server response contains a 3-digit status code.

**Ranges:**

| Code Range | Meaning      |
| ---------- | ------------ |
| 2xx        | Success      |
| 3xx        | Redirection  |
| 4xx        | Client error |
| 5xx        | Server error |

**Common Codes:**

| Code | Meaning             |
| ---- | ------------------- |
| 200  | Request successful  |
| 201  | Resource created    |
| 204  | Success but no data |
| 400  | Bad request         |
| 401  | Unauthorized        |
| 403  | Forbidden           |
| 404  | Resource not found  |
| 500  | Server error        |

**Fixing Response Code Issue**
Earlier, even if patient did not exist, API returned `200`.

We corrected it:

```python
raise HTTPException(status_code=404, detail="Patient not found")
```

Now it returns the correct `404`.

---

## 2. Query Parameters

### What are Query Parameters?

These are extra details added after the main URL.
Used for search, sorting, filtering, pagination.

Format:

```
/endpoint?key=value&key2=value2
```

**Example:**

```
/sort?sort_by=height&order=descending
```

| Parameter | Meaning                          |
| --------- | -------------------------------- |
| sort_by   | field to sort on (height/weight) |
| order     | ascending or descending          |

### Why Query Parameters?

They allow features without making new endpoints.

Use cases:
✔ Sort data
✔ Filter data
✔ Search data
✔ Limit records

### Query Parameter in Code

```python
@app.get("/sort")
def sort_patients(
    sort_by: str = Query(...),
    order: str = Query("ascending")
):
```

* `sort_by` is required (because of `...`)
* `order` is optional, default is `ascending`

We validated:

```python
valid_fields = ["height", "weight", "BMI"]
if sort_by not in valid_fields:
    raise HTTPException(400, "Invalid field")
```

### Example Outputs

```
/sort?sort_by=height&order=descending
```

→ Patients sorted from tallest to shortest

If order is missing:

```
/sort?sort_by=weight
```

→ Sorted in ascending order by default

---

### Example 
# FastAPI – Sorting Patients Endpoint

## 📌 What is This Endpoint?

This API endpoint allows you to sort patient data based on **height**, **weight**, or **BMI**. You can also choose the sorting order — either **ascending** or **descending**.

This is useful when doctors or system users want to quickly view patients in a particular order, such as tallest to shortest, lowest BMI to highest, etc.

---

## 🧠 How It Works

The `/sort` endpoint accepts two query parameters:

| Parameter | Type | Required | Description                                    |
| --------- | ---- | -------- | ---------------------------------------------- |
| `sort_by` | str  | Yes      | Field to sort by: `height`, `weight`, or `bmi` |
| `order`   | str  | No       | Sorting order: `asc` (default) or `desc`       |

Example usage:

```
http://localhost:8000/sort?sort_by=height
http://localhost:8000/sort?sort_by=bmi&order=desc
```

---

## 📝 Code for Sorting Patients

```python
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
```

---

## 🔍 Code Explanation 

### 1️⃣ Route Definition

```python
@app.get('/sort')
```

This creates a GET endpoint at `/sort`.

### 2️⃣ Query Parameters

```python
sort_by: str = Query(...)
order: str = Query('asc')
```

* `sort_by` is mandatory — you **must** choose one attribute.
* `order` is optional — if not given, it defaults to `asc`.

### 3️⃣ Validations

```python
valid_fileds=['height','weight','bmi']
```

The API checks if the `sort_by` value is valid. If not, it returns a **404 error**.

### 4️⃣ Loading Data

```python
data = load_data()
```

Fetches patient data stored in memory or a file.

### 5️⃣ Sorting Logic

```python
sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)
```

* Uses Python's `sorted()` function.
* Sorts based on the field mentioned in `sort_by`.
* If `order` is `desc`, it sorts in reverse.

### 6️⃣ Return Output

The API returns a list of sorted patient records in JSON format.

---


## Summary

| Feature   | Path Parameter             | Query Parameter        |
| --------- | -------------------------- | ---------------------- |
| Purpose   | Identify a specific entity | Add filters/options    |
| Required? | Yes                        | Optional               |
| Location  | URL path                   | After `?` in URL       |
| Example   | /patient/P01               | /sort?order=descending |

---

## Final Takeaway

In this video, you learned:
✔ What Path Parameters are and how to use them
✔ What Query Parameters are and when to use them
✔ How to improve API documentation using `Path()` and `Query()`
✔ How to use `HTTPException` and return correct status codes
✔ How to build endpoints using both Path and Query Parameters


🚀 FastAPI Playlist – (Video 5)
**Topic:** Create Endpoint (POST request + Request Body + Pydantic Model)

---

## 📌 What Have We Learned So Far?

### Previous Videos Covered:

| Video | Topic                                                                            |
| ----- | -------------------------------------------------------------------------------- |
| 1     | What are APIs? Why do we use them?                                               |
| 2     | Fundamentals of FastAPI, strengths/weaknesses, comparison with Flask             |
| 3     | Started project → Patient Management System                                      |
| 4     | GET endpoints: view, patient/<id>, sort using Path Parameters & Query Parameters |

### CRUD Progress

✔️ Retrieve (GET) completed
⏳ Create (POST) → covered in THIS video
🔜 Next → Update & Delete

---

## 🎯 Goal of This Video

Create a **POST endpoint** named `/create` that allows a client to add a new patient to our database stored in a **JSON file**.

---

## 🧠 Important Concept: Request Body

**Definition:** The data sent by the client to the server inside an HTTP POST/PUT request.

### Example request body JSON:

```json
{
  "id": "P006",
  "name": "Rahul Gupta",
  "city": "Hyderabad",
  "age": 19,
  "gender": "male",
  "height": 1.74,
  "weight": 55
}
```

➡️ The server will use this data to create a new patient.

---

## 🧰 Tech Used Behind The Scenes

| Library       | Purpose                               |
| ------------- | ------------------------------------- |
| **Starlette** | ASGI framework, routing               |
| **Pydantic**  | Data validation & settings management |

📌 If you don’t understand Pydantic, the Create API won't make sense.

---

## 🏗️ Step-by-Step Process of Create Endpoint

| Step | Description                                   |
| ---- | --------------------------------------------- |
| 1    | Client sends a POST request with patient data |
| 2    | Server validates data using Pydantic Model    |
| 3    | If valid → add new patient to JSON database   |
| 4    | Return success message                        |

---

## 🔑 Step 1: Creating the Pydantic Model

### Install Pydantic (if not installed)

```bash
pip install pydantic
```

### Patient Model with Validations + Computed Fields

```python
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

class Patient(BaseModel):
    id: Annotated[str, Field(description="Patient ID", examples=["P01"])]
    name: Annotated[str, Field(description="Name of the patient")]
    city: Annotated[str, Field(description="City where patient lives")]
    age: Annotated[int, Field(gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal["male", "female", "others"], Field(description="Gender of the patient")]
    height: Annotated[float, Field(gt=0, description="Height in meters")]
    weight: Annotated[float, Field(gt=0, description="Weight in kg")]

    @computed_field
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        return "Obese"
```

✔️ `bmi` and `verdict` are computed automatically
❌ Client does NOT send them

---

## 📂 Step 2: Create Endpoint

### `POST /create` → adds new patient

```python
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import json

app = FastAPI()

def load_data():
    with open("patients.json") as f:
        return json.load(f)

def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f, indent=4)

@app.post("/create")
def create_patient(patient: Patient):
    data = load_data()

    # Check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")

    # Convert model to dict & add to DB
    data[patient.id] = patient.model_dump(exclude={"id"})
    save_data(data)

    return JSONResponse(
        status_code=201,
        content={"message": "Patient created successfully"}
    )
```

---

## 🧪 Testing the Endpoint

### Run the FastAPI app:

```bash
uvicorn main:app --reload
```

### Visit Swagger Docs:

```
http://localhost:8000/docs
```

Use the UI → enter patient data → click **Execute**

💡 FastAPI auto-shows model rules & examples in docs!

---

## 🎉 Output Example

After adding a new patient:

```json
{
  "P006": {
    "name": "Rahul Gupta",
    "city": "Hyderabad",
    "age": 19,
    "gender": "male",
    "height": 1.74,
    "weight": 55,
    "bmi": 18.17,
    "verdict": "Underweight"
  }
}
```

---

## 🏁 Summary

| Feature             | Status        |
| ------------------- | ------------- |
| GET View Patients   | ✔️ Done       |
| GET Patient by ID   | ✔️ Done       |
| GET Sorted Patients | ✔️ Done       |
| POST Create Patient | ✅ Completed   |
| PUT Update Patient  | ⏳ Next Video  |
| DELETE Patient      | ⏳ Coming Soon |

---

## 👍 Why Pydantic Makes Life Easy

Without Pydantic you would manually:
❌ Check age ≥ 0
❌ Restrict gender values
❌ Calculate BMI & verdict
❌ Validate request body

**Pydantic = Automatic validation + clean code + great docs**


# 🚀 FastAPI – Patient Management System

## Video 6 Notes: Update & Delete Endpoints

We are building a CRUD API for a **Patient Management System**.

### 📌 Progress So Far

| Feature         | Status           |
| --------------- | ---------------- |
| CREATE (POST)   | ✔️ Done          |
| RETRIEVE (GET)  | ✔️ Done          |
| UPDATE (PUT)    | 🟡 In this video |
| DELETE (DELETE) | 🟡 In this video |

---

## 🎯 Goal of This Video

Implement two new endpoints:
1️⃣ **/edit/{patient_id}** → Update details of an existing patient
2️⃣ **/delete/{patient_id}** → Remove a patient from our database

---

## 🛠 Update Endpoint – How It Works

### 📥 What will the client send?

The client must send two things:

| Type                | What it contains?                              |
| ------------------- | ---------------------------------------------- |
| Path Parameter      | Patient ID to update                           |
| Request Body (JSON) | Updated values like new city, new weight, etc. |

### ❓ Why do we need a NEW Pydantic Model?

Our main Patient model requires **all fields**.
But during update, the user may send **only a few fields**.
Therefore, we create an **update model** where all fields are **optional**.

---

## 🧾 Update Pydantic Model

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal

class PatientUpdate(BaseModel):
    name: Optional[str] = Field(None)
    city: Optional[str] = Field(None)
    age: Optional[int] = Field(None)
    gender: Optional[Literal["male", "female", "others"]] = Field(None)
    height: Optional[float] = Field(None)
    weight: Optional[float] = Field(None)
```

✔️ No `id` because patient ID comes from URL
✔️ All fields optional → User may update **any single** field

---

## 🔧 Update Logic (Concept)

| Step | Action                                             |
| ---- | -------------------------------------------------- |
| 1    | Load existing patients data                        |
| 2    | Check if patient exists, else 404                  |
| 3    | Convert incoming update to dictionary              |
| 4    | Update only provided fields                        |
| 5    | Recalculate BMI & Verdict if height/weight changed |
| 6    | Save updated record                                |
| 7    | Return success message                             |

---

## ✨ Update Endpoint Code

```python
from fastapi import HTTPException

@app.put("/edit/{patient_id}")
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_info = data[patient_id]
    updated_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_info.items():
        existing_info[key] = value

    existing_info["id"] = patient_id
    patient_obj = Patient(**existing_info)

    data[patient_id] = patient_obj.model_dump(exclude={"id"})
    save_data(data)

    return {"message": "Patient updated successfully"}
```

### 🧪 Testing Update API

**Example Request:**

```
PUT /edit/P004
{
  "city": "Mumbai",
  "weight": 90
}
```

✔️ City updated → Bengaluru ➝ Mumbai
✔️ Weight updated → BMI recalculated
✔️ Verdict updated automatically

---

## 🗑 DELETE Endpoint – How It Works

Only one input: **patient_id**

### Steps

1️⃣ Load data
2️⃣ Check if ID exists
3️⃣ Delete entry
4️⃣ Save data
5️⃣ Send confirmation

---

## ❌ Delete Endpoint Code

```python
from fastapi import HTTPException

@app.delete("/delete/{patient_id}")
def delete_patient(patient_id: str):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    del data[patient_id]
    save_data(data)

    return {"message": "Patient deleted successfully"}
```

### 🧪 Testing Delete API

**Example:**

```
DELETE /delete/P006
{
  "message": "Patient deleted successfully"
}
```

If patient doesn't exist:

```
{
  "detail": "Patient not found"
}
```

---

## 🎉 Project Completed!

We now support **full CRUD**:

| Action   | Method | Endpoint                    |
| -------- | ------ | --------------------------- |
| Create   | POST   | /create                     |
| Retrieve | GET    | /view, /patient/{id}, /sort |
| Update   | PUT    | /edit/{id}                  |
| Delete   | DELETE | /delete/{id}                |

---

✨ Your Patient API is now a complete CRUD system!


# 🚀 FastAPI + Machine Learning Model Serving (Video 7)

## Previous Progress

We have successfully created a **Patient Management System API** using FastAPI and completed these CRUD features:

| Feature  | Status  |
| -------- | ------- |
| Create   | ✔️ Done |
| Retrieve | ✔️ Done |
| Update   | ✔️ Done |
| Delete   | ✔️ Done |

---

## 🎯 New Goal

Now, we are moving into the next phase:

**Serve a Machine Learning model using FastAPI** so users can send input data and receive predictions.

---

## 📌 Why Do We Need This?

* Data scientists train ML models inside **Jupyter Notebooks**, but users cannot access them directly.
* We need an **API** so users can send data from apps/websites and get predictions.

FastAPI helps us:
✔️ Load the ML model
✔️ Validate input
✔️ Run prediction
✔️ Return output as JSON
✔️ Connect frontend UI

---

## 🧭 Flow of the System

```
User → Frontend → FastAPI → ML Model → Prediction → FastAPI → Frontend → User
```

### Process Breakdown

| Part   | Description                    |
| ------ | ------------------------------ |
| Part 1 | Build Machine Learning Model   |
| Part 2 | Create API Endpoint in FastAPI |
| Part 3 | Build Frontend using Streamlit |

---

## 🧱 PART 1: Building the Machine Learning Model

### Problem Statement

Predict **Insurance Premium Category**:

* Categories → `Low`, `Medium`, `High`

### Based On These Features

| Feature      | Meaning          |
| ------------ | ---------------- |
| Age          | Age of user      |
| Weight       | Body weight      |
| Height       | Height in meters |
| Income (LPA) | Annual income    |
| Smoker       | True/False       |
| City         | User's city      |
| Occupation   | Job type         |

### Why Predict Premium Category?

* Insurance companies understand **customer risk**
* Users know whether they will pay **high or low** premium

---

## 🧪 Feature Engineering

We transformed raw inputs into useful features.

| New Feature    | Based On        | Purpose            |
| -------------- | --------------- | ------------------ |
| Age Group      | Age             | Categorize users   |
| BMI            | Weight & Height | Body Fat Indicator |
| Lifestyle Risk | BMI + Smoker    | Risk score         |
| City Tier      | City            | Tier-1/2/3 cities  |

### BMI Formula

```
bmi = weight / (height ** 2)
```

### Pandas Example

```python
df['BMI'] = df['weight'] / (df['height'] ** 2)
```

### Lifestyle Risk Logic

```python
if smoker and bmi > 30:
    risk = 'High'
elif smoker and bmi > 27:
    risk = 'Medium'
else:
    risk = 'Low'
```

---

## 🤖 ML Pipeline

We used **RandomForestClassifier** with **ColumnTransformer**.

```python
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('transformer', ColumnTransformer(...)),
    ('model', RandomForestClassifier())
])
```

### Save Model with Pickle

```python
import pickle
pickle.dump(pipeline, open('model.pkl', 'wb'))
```

File created: **model.pkl**

---

## 🔁 PART 2: FastAPI Prediction API

### Step 1 → Load Model

```python
import pickle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
```

### Step 2 → Create App

```python
from fastapi import FastAPI
app = FastAPI()
```

### Step 3 → Define Input Schema

```python
from pydantic import BaseModel, Field
from typing import Annotated, Literal

class UserInput(BaseModel):
    age: Annotated[int, Field(gt=0, le=120)]
    weight: float
    height: float
    income_lpa: float
    smoker: bool
    city: str
    occupation: Literal['Government Job', 'Business Owner', 'Private Job']
```

### Step 4 → Predict Endpoint

```python
@app.post("/predict")
def predict_premium(data: UserInput):
    input_df = pd.DataFrame([{
        "BMI": data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }])

    prediction = model.predict(input_df)[0]

    return {"predicted_category": prediction}
```

📌 **HTTP Method** = `POST`

---

## 🖥 PART 3: Streamlit Frontend

Install dependencies:

```bash
pip install streamlit requests
```

### Basic UI Code

```python
import streamlit as st
import requests

st.title("Insurance Premium Predictor")

age = st.number_input("Age", min_value=0, max_value=120)
# ... more fields ...

if st.button("Predict Premium Category"):
    data = {...}
    response = requests.post("http://localhost:8000/predict", json=data)
    st.write(response.json())
```

Run:

```bash
streamlit run front.py
```

---

## 🎉 Summary

You learned how to:
✔️ Build an ML model
✔️ Export and save it
✔️ Serve it with FastAPI
✔️ Connect Streamlit to consume predictions

This is exactly how **real-world ML deployment** works! 🚀

