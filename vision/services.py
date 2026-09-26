from functools import lru_cache
from pathlib import Path
import pickle
import numpy as np
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parent / 'laptop_price_model.pkl'
FEATURES = ['Company','TypeName','Ram','Weight','Touchscreen','Ips','ppi','HDD','SSD','Cpu brand','Gpu brand','os']

@lru_cache(maxsize=1)
def get_model():
    with MODEL_PATH.open('rb') as file:
        return pickle.load(file)

def predict_price(cleaned_data):
    inches = float(cleaned_data['screen_size'])
    width = int(cleaned_data['resolution_width'])
    height = int(cleaned_data['resolution_height'])
    ppi = ((width ** 2 + height ** 2) ** 0.5) / inches

    row = pd.DataFrame([{
        'Company': cleaned_data['Company'],
        'TypeName': cleaned_data['TypeName'],
        'Ram': int(cleaned_data['Ram']),
        'Weight': float(cleaned_data['Weight']),
        'Touchscreen': int(cleaned_data['Touchscreen']),
        'Ips': int(cleaned_data['Ips']),
        'ppi': ppi,
        'HDD': int(cleaned_data['HDD']),
        'SSD': int(cleaned_data['SSD']),
        'Cpu brand': cleaned_data['cpu_brand'],
        'Gpu brand': cleaned_data['gpu_brand'],
        'os': cleaned_data['os'],
    }], columns=FEATURES)

    log_price = float(get_model().predict(row)[0])
    return float(np.exp(log_price)), round(ppi, 1)
