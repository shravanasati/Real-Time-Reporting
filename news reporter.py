import json, requests, newsapi

def speak(str):
	  from win32com.client import Dispatch
	  speak=Dispatch("SAPI.SpVoice")
	  speak.Speak(str)

if __name__ == "__main__":
	# url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=fbddfcc479954110ba532f7b45dc41d2"
	# news = requests.get(url).text
	# print(type(news))
	# news_dict = json.loads(news)
	# arts = news_dict['articles']

	# speak("Enter number of articles you want")
	# n = int(input("Enter number of articles you want: "))
	# a = 1

	# speak("Today's news highlights are...")
	# for article in arts:
	# 	print(article['title'])
	# 	speak(article['title'])
	# 	if a==n:
	# 		break
	# 	else:
	# 		speak("Moving on to the next news.")
	# 		a += 1
	# 		continue

	# speak("Thanks for listening...")


	# my alt 
	from newsapi import NewsApiClient
	speak("How many news articles do you want to hear? ")
	pag = int(input("How many news articles do you want to hear? "))

	newsapi = NewsApiClient(api_key='fbddfcc479954110ba532f7b45dc41d2')

	news = newsapi.get_top_headlines(q="tech", language='en', country='in', category='technology', page_size=pag, page=pag)

	a = json.dumps(news)

	n = json.loads(a)
	arts = n['articles']

	speak("Today's news highlights are...")
	for articles in arts:
		print(articles.get('title'))
		speak(articles.get('title'))
	speak("Thanks for listening!")