# Lifestat

A small machine learning project that predicts life satisfaction from GDP per capita using a Linear Regression model served through FastAPI.

## Overview

The project demonstrates a simple machine learning deployment workflow:

1. A Linear Regression model is trained using a life satisfaction dataset.
2. The trained model is saved as `lifesat_model.pkl`.
3. FastAPI loads the saved model.
4. A GDP per capita value is submitted to the application.
5. The model returns a predicted life satisfaction score.

## API

The FastAPI application provides the following endpoints:

### `GET /`

Returns a basic response from the application.

### `GET /template`

Displays the HTML form used to interact with the model.

### `POST /model`

Accepts a GDP per capita value through a form submission and uses the trained model to generate a life satisfaction prediction.

## Project Structure

~~~text
lifestat/
├── lifesat_model.pkl
├── main.py
├── model.ipynb
├── train.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
~~~

## Technologies

- Python
- FastAPI
- Scikit-learn
- Joblib
- Jinja2
- HTML
- Jupyter Notebook

## Running the Project

Install the dependencies:

~~~bash
pip install -r requirements.txt
~~~

Start the FastAPI application:

~~~bash
uvicorn main:app --reload
~~~

The application will be available at:

~~~text
http://127.0.0.1:8000
~~~

Open the template page at:

~~~text
http://127.0.0.1:8000/template
~~~

## Machine Learning Model

The trained model is stored in:

~~~text
lifesat_model.pkl
~~~

The FastAPI application loads this model with Joblib and uses it to generate predictions.

The repository also includes `model.ipynb` for machine learning experimentation and `train.py` for the training workflow.

## Purpose

This project was created to practice integrating a machine learning model with a Python backend and serving predictions through a web application.
