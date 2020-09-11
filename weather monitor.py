def speak(str):
	from win32com.client import Dispatch
	speak=Dispatch("SAPI.SpVoice")
	speak.Speak(str)

print("This is the weather forecaster!")
import requests, json

if __name__ == "__main__":
	speak("Where do you live? ")
	place = input("Where do you live? ")

	url = f"http://api.weatherapi.com/v1/current.json?key=2f081a6878a747a5be135553200709&q={place.capitalize()}"

	r = requests.get(url).text
	a = json.loads(r)

	current_weather = a.get('current')
	condition = current_weather['condition']
	text = condition['text']

	if current_weather['is_day'] == 0:
		speak(f"It is currently night in {place} with current temeprature being{current_weather['temp_c']}, though it feels like {current_weather['feelslike_c']}")
		speak(f"The weather condition in {place} is {text}")
		speak("Thanks for listening!")

	elif current_weather['is_day'] == 1:
		speak(f"It is currently day in {place} with current temeprature being{current_weather['temp_c']}, though it feels like {current_weather['feelslike_c']}")
		speak(f"The weather condition in {place} is {text}")
		speak("Thanks for listening!")