📌 FastAPI Playlist – Video 1 Notes
Why Learn FastAPI & What Are APIs?
🚀 Why This Playlist?

Channel’s vision: help students master AI by covering essential topics.

Already covered: Machine Learning, Deep Learning, NLP, etc.

AI requires creating models AND exposing them to users — this requires APIs.

Most ML products in industry expose their models using FastAPI.

9 out of 10 companies use FastAPI for ML model APIs due to:

High performance

Scalability

Production-ready features

🎯 Playlist Structure
Part	What You Learn	Goal
1	FastAPI Fundamentals	Understand the framework using a small project
2	FastAPI + Machine Learning	Build an API around an ML model
3	Deployment	Dockerize & deploy the API on AWS

Total videos: ~15
Timeline: 21–25 days

🧠 What is an API?

API = A connector that allows two software components to communicate using defined rules.

Simple Definition

API is like a bridge between front-end (what user sees) and back-end (business logic, database, models).

Example

You search for a course on Udemy:

Frontend sends request → API receives it → backend fetches data → response returned in JSON → frontend displays results

🍽️ Analogy: Restaurant
Real World	Software
Customer	Frontend
Waiter	API
Kitchen & Chefs	Backend
Menu	Rules/Protocols
Food served	JSON response
🔍 Why APIs Were Invented?
Before APIs (Monolithic Architecture)

Frontend + Backend code lived in a single application

Tightly coupled

Hard to share data or features with other platforms

Example: IRCTC wants to give its train data to MakeMyTrip — impossible directly

🏗️ After APIs (Decoupled Architecture)

Backend becomes an independent service

API exposes endpoints like:

irctc.com/trains?from=Pune&to=Mumbai&date=2025-01-04


MakeMyTrip / Yatra / Goibibo can now request train data safely

Backend logic remains protected

🌍 Standard Protocols & Data Format
Concept	Why Used
HTTP	For communication over the internet
JSON	Universal format readable by Python, Java, PHP etc.

Example JSON:

{
  "train_name": "Shatabdi Express",
  "departure": "07:45"
}

📱 APIs Solve Another Huge Problem

Earlier companies needed three separate full applications:

Website

Android App

iOS App

Each required its own:

Database

Backend

Maintenance team

With APIs → Single backend + multiple frontends

🤖 ML Perspective: APIs in AI/ML

Only one thing changes:

Software World	ML World
Database	ML Model

ML Model returns predictions instead of stored data

API exposes model's predict function

Allows external apps to use your model

Example:

ChatGPT’s model (GPT) is NOT directly exposed

Only API endpoints are public, such as:

/predict
/generate

🎯 Summary

API = Communication bridge

Solves two major problems:

Data/model sharing between systems

Multiple frontends using one backend

Essential for deploying ML/DL/GenAI models

FastAPI is the most popular framework for creating ML APIs today


