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


# FastAPI – Video 3 Notes (Simple English)

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


