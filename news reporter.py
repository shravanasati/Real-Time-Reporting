import json, newsapi

def speak(str):
	  from win32com.client import Dispatch
	  speak=Dispatch("SAPI.SpVoice")
	  speak.Speak(str)

if __name__ == "__main__":
	from newsapi import NewsApiClient
	speak("How many news articles do you want to hear? ")
	pag = int(input("How many news articles do you want to hear? "))

	newsapi = NewsApiClient(api_key='YOUR NEWS API KEY')

	news = newsapi.get_top_headlines(q="tech", language='en', country='in', category='technology', page_size=pag, page=pag)

	a = json.dumps(news)

	n = json.loads(a)
	arts = n['articles']

	speak("Today's news highlights are...")
	for articles in arts:
		print(articles.get('title'))
		speak(articles.get('title'))
	speak("Thanks for listening!")
