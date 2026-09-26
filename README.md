# Worthly

Worthly is a Django web application that predicts a laptop's estimated price based on its specifications.

The prediction is made using a Random Forest model trained on laptop specification and price data.

## Features

- User registration and login
- Profile management
- Laptop price prediction

## Tech Stack

- Python
- Django
- Scikit-learn
- Pandas
- NumPy
- HTML/CSS
- SQLite

## Run Locally

Create and activate a virtual environment:

```bash
python -m venv myenv
myenv\Scripts\activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

## How Prediction Works

The user enters laptop specifications such as brand, RAM, storage, processor, GPU, display and weight.

Django validates the input and calculates the display PPI. The processed values are then passed to the trained model, which returns the estimated laptop price.

## Model

The deployed model is a Random Forest Regressor.

The model achieved an R² score of approximately **0.89** on the holdout test data.

The prediction is an estimate based on the training dataset and should not be considered a live market price.
