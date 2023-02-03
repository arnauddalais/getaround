import uvicorn
import pandas as pd 
from pydantic import BaseModel, Field
from typing import Literal, List
from fastapi import FastAPI
import joblib

description = """
Welcome to the getaround API! (jedha's data fullstack project)


Check out documentation below 👇 for more information on each endpoint. 

## Machine Learning

This is the endpoint of Machine Learning who predict the price for your car's rental.

* `/predict` This endpoint accept POST method with JSON input data

example : {'model_key': 'Peugeot', 'mileage' : '70000', 'engine_power':'100', 'fuel': 'diesel', 'paint_color' :  'grey', 'car_type' : 'suv',
'private_parking_available' : True, 'has_gps' : False, 'has_air_conditioning' : True, 'automatic_car' : False,
'has_getaround_connect' : False, 'has_speed_regulator' : True, 'winter_tires' : True}




"""

tags_metadata = [
    
    {
        "name": "Machine_Learning",
        "description": "Prediction Endpoint."
    }
]

app = FastAPI(
    title="📱 Getaround API",
    description=description,
    version="0.1",
    openapi_tags=tags_metadata
)


class PredictionFeatures(BaseModel):
    model_key : Literal ['Citroën', 'Renault', 'BMW', 'Peugeot', 'Audi ', 'Nissan', 'Mitsubishi', 'Mercedes', 'Volkswagen',
                          'Toyota', 'SEAT', 'Opel', 'PGO', 'Ferrari', 'Subaru', 'Maserati', 'Porsche', 'Ford', 'KIA Motors',
                            'Alfa Romeo', 'Lamborghini', 'Fiat', 'Suzuki'] = Field(example='Peugeot')
    mileage : int = Field(example=70000)
    engine_power : int = Field(example= 100)
    fuel : Literal ['diesel', 'petrol', 'hybrid_petrol', 'electro'] = Field(example='diesel')
    paint_color : Literal ['black', 'grey', 'blue', 'white', 'brown', 'silver', 'red', 'beige', 'green', 'orange'] = Field(example= 'grey')
    car_type : Literal ['estate', 'sedan', 'suv', 'hatchback', 'subcompact', 'coupe', 'convertible', 'van'] = Field(example='suv')
    private_parking_available: Literal[True, False] = Field(example=True)
    has_gps: Literal[True, False] = Field(example=False)
    has_air_conditioning: Literal[True, False] = Field(example=True)
    automatic_car: Literal[True, False] = Field(example=False)
    has_getaround_connect: Literal[True, False] = Field(example=False)
    has_speed_regulator: Literal[True, False] = Field(example=True)
    winter_tires: Literal[True, False] = Field(example=True)

@app.get("/")
async def index():

    message = "Hello world! If you want to know how to use the API, check out documentation at `/docs`"

    return message

@app.post("/predict", tags=["Machine_Learning"])
async def predict(predictionFeatures: PredictionFeatures):
    """
    Predict the price for car's rental per day in US$ 
    """
        
    # Read data
    model_key_pred = predictionFeatures.model_key
    mileage_pred = predictionFeatures.mileage
    engine_power_pred = predictionFeatures.engine_power
    fuel_pred = predictionFeatures.fuel
    paint_color_pred = predictionFeatures.paint_color
    car_type_pred = predictionFeatures.car_type
    private_parking_available_pred = predictionFeatures.private_parking_available
    has_gps_pred = predictionFeatures.has_gps
    has_air_conditioning_pred = predictionFeatures.has_air_conditioning
    automatic_car_pred =predictionFeatures.automatic_car
    has_getaround_connect_pred = predictionFeatures.has_getaround_connect
    has_speed_regulator_pred = predictionFeatures.has_speed_regulator
    winter_tires_pred = predictionFeatures.winter_tires
   

    features_list = ['model_key', 'mileage', 'engine_power', 'fuel', 'paint_color',
       'car_type', 'private_parking_available', 'has_gps',
       'has_air_conditioning', 'automatic_car', 'has_getaround_connect',
       'has_speed_regulator', 'winter_tires']
    features_values = [model_key_pred, mileage_pred, engine_power_pred, fuel_pred, paint_color_pred, car_type_pred, 
                       private_parking_available_pred, has_gps_pred, has_air_conditioning_pred, automatic_car_pred, 
                       has_getaround_connect_pred, has_speed_regulator_pred, winter_tires_pred]
    X_topredict = pd.DataFrame([features_values], columns = features_list)

    # Load model
    loaded_model = joblib.load('xgboost_r.joblib')
    
    #prediction 
    prediction = round(loaded_model.predict(X_topredict).tolist()[0], 0)
   
    # Format response
    response = {"prediction": prediction}

    return response

#   loading the api on powershell
#    uvicorn run api:app --reload
