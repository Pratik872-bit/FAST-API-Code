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

