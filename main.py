import requests
from datetime import datetime
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = "youir nutritionix app id"
NUTRITIONIX_APP_KEY = "your nutritionix app key"

GENDER = "your gender"
WEIGHT_KG = "your weight"
HEIGHT_CM = "your height"
BEARER = "your bearer token"
AGE = "your agegi"
query_text = input("What exercises you did today:")

params = {
    "query": query_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}
response = requests.post(url=exercise_endpoint, json=params, headers=headers).json()
print(response)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_endpoint = "your sheety endpoint"
for exercise in response["exercises"]:
    sheety_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_input, headers=headers)
    print(sheety_response.text)
