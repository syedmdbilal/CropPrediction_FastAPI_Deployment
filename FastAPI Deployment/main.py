import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
from typing import List

class crop(BaseModel):
    nitrogen: float 
    phosphorus: float 
    potasium: float 
    temperature: float
    humidity: float 
    ph: float 
    rainfall: float

app = FastAPI()

model = joblib.load('rfc.pkl')

@app.get('/')
def index():
    return {'message': 'Welcom to Pinaca Group'}

@app.post('/predict')

def predict(data: List[crop]):
    input_data = [data.dict() for data in data]
    predictions = model.predict([(data['nitrogen'], data['phosphorus'], data['potasium'], data['temperature'], data['humidity'], data['ph'], data['rainfall']) for data in input_data])

    if predictions== 0:
        predictions='APPLE'
    elif predictions== 1:
        predictions='BANANA'
    elif predictions== 2:
        predictions='BLACK GRAM'
    elif predictions== 3:
        predictions='CHICKPEA'
    elif predictions== 4:
        predictions='COCONUT'
    elif predictions== 5:
        predictions='COFFEE'
    elif predictions== 6:
        predictions='COTTON'
    elif predictions== 7:
        predictions='GRAPES'
    elif predictions== 8:
        predictions='JUTE'
    elif predictions== 9:
        predictions='KIDNEY BEANS'
    elif predictions== 10:
        predictions='LENTIL'
    elif predictions== 11:
        predictions='MAIZE'
    elif predictions== 12:
        predictions='MANGO'
    elif predictions==13:
        predictions='MOTH BEANS'
    elif predictions== 14:
        predictions='MUNG BEAN'
    elif predictions== 15:
        predictions='MUSK MELON'
    elif predictions== 16:
        predictions='ORANGE'
    elif predictions== 17:
        predictions='PAPAYA'
    elif predictions== 18:
        predictions='PIGEON PEAS'
    elif predictions== 19:
        predictions='POMEGRANATE'
    elif predictions== 20:
        predictions="RICE"
    else:
        output="WATER MELON"
                                     
    return {'predictions': predictions}
                                     
                                     
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
