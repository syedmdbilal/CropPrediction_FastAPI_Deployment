from pydantic import BaseModel
class Crop(BaseModel):
    nitrogen: float 
    phosphorus: float 
    potasium: float 
    temperature: float
    humidity: float 
    ph: float 
    rainfall: float
    