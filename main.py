import requests
import os
from datetime import datetime
APP_ID = "5612fed8"
API_KEY = "457ee18b748d5a3314a302708f2154e3"

os.environ["APP_ID"] = APP_ID

GENDER = "MALE"
WEIGHT = 75
HEIGHT = 165
AGE = 17

query = input("What exercises did you do: ")

#------------------ENDPOINTS-----------------------#
excerciseEndpoinnt = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheetyEndpoint = "https://api.sheety.co/a48fb1e93befc632435ea9cb60aaf1e4/myWorkouts/workouts"
deleteEndpoint = "https://api.sheety.co/a48fb1e93befc632435ea9cb60aaf1e4/myWorkouts/workouts/10"


#------------------PARAMETERS----------------------#
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
sheetyHeader = {
    "Authorization": "Basic Rm9yaSBEYW5pZWw6MWJveDJib3hlcw=="
}
params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
deleteParams = {
    "method": "DELETE"
}


excerciseResponse = requests.post(url=excerciseEndpoinnt, json=params, headers=headers)
exercises = excerciseResponse.json()["exercises"]


today = datetime.now()

sheetyParams = {
        "workout": {
            "date": today.strftime('%d/%m/%Y'),
            "time": str(today)[10:][:9],
            "exercise": f"{exercises[0]['user_input']}".title(),
            "duration": f"{exercises[0]['duration_min']}",
            "calories": f"{exercises[0]['nf_calories']}"
    }
}

response = requests.post(url=sheetyEndpoint, json=sheetyParams, headers=sheetyHeader)
print(response)


#deleteResponse = requests.delete(url=deleteEndpoint, json=deleteParams)
#print(deleteResponse)



