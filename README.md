# getaround



Curl example (copy/paste into notebook)

import requests\n
import json\n
response = requests.post("PUBLIC_URL/predict", json={'model_key': 'Peugeot', 'mileage' : '70000', 'engine_power':'100', 'fuel': 'diesel', 'paint_color' :  'grey', 'car_type' : 'suv',
'private_parking_available' : True, 'has_gps' : False, 'has_air_conditioning' : True, 'automatic_car' : False,
'has_getaround_connect' : False, 'has_speed_regulator' : True, 'winter_tires' : True}
print(response.json())