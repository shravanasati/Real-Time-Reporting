import requests, json, pyttsx3

def speak(str):
	engine = pyttsx3.init()
	engine.say(str)
	engine.runAndWait()


if __name__ == "__main__":
	print("This is the weather forecaster!")
	speak("Where do you live? ")
	place = input("Where do you live? ")

	url = f"http://api.weatherapi.com/v1/current.json?key="KEY HERE"&q={place.capitalize()}"

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
