import json, requests, pyttsx3

def speak(str):
	engine = pyttsx3.init()
	engine.say(str)
	engine.runAndWait()
	
if __name__ == "__main__":

	with open("keys.json") as f:
		text = json.load(f)
		key = text["News API key"]
		
	url = f"https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={key}"
	news = requests.get(url).text
	news_dict = json.loads(news)
	arts = news_dict['articles']
	
	a = 1
	n = 5
	speak("Today's news highlights are...")
	for article in arts:
		print(article['title'])
		speak(article['title'])
		if a==n:
			break
		else:
			speak("Moving on to the next news.")
			a += 1
			continue

	speak("Thanks for listening...")
