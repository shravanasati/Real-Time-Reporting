import json, requests, pyttsx3
import tkinter as tk


def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()
    
if __name__ == "__main__":

    root = tk.Tk()
    root.title("News Reporter!")
    root.geometry("500x500")
    
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
    news_title = tk.Label(root, text="Today's news highlights are...")

    for article in arts:
        
        news_title.config(font=("Arial", 16))
        news_title.pack()

        news = tk.Text(root, height=1, width=100)
        news.config(font=("Arial", 16), bg="#dddddd")
        news.insert("1.0", article['title'])
        news.config(state="disabled")
        news.pack(padx=10, pady=10)
        
        speak(article['title'])
        if a==n:
            break
        else:
            speak("Moving on to the next news.")
            a += 1
            
    speak("Thanks for listening...")
    root.mainloop()
