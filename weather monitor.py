import requests, json, pyttsx3
import tkinter as tk

def speak(str):
    engine = pyttsx3.init()
    engine.say(str)
    engine.runAndWait()


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Weather Forecaster!")
    root.geometry("500x500")

    lplace = tk.Label(root, text="Where do you live?")
    lplace.config(font=("Arial", 16))
    lplace.pack()

    tplace = tk.Text(root, height=1, width=100)
    tplace.config(font=("Arial", 16), bg="#dddddd")
    tplace.pack(padx=10, pady=10)

    speak("Where do you live? ")

    def forecaster():

        btn1.config(state="disabled")

        place = tplace.get("1.0", "end").capitalize()
        with open("keys.json") as f:
            text = json.load(f)
            key = text["Weather API Key"]

        url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={place}"

        r = requests.get(url).text
        a = json.loads(r)

        current_weather = a.get('current')
        condition = current_weather['condition']
        text = condition['text']

        if current_weather['is_day'] == 0:
            
            l_day = tk.Label(root, text="Day/Night:")
            l_day.config(font=("Arial", 16))
            l_day.pack()

            tday = tk.Text(root, height=1, width=100)
            tday.config(font=("Arial", 16), bg="#dddddd")
            tday.insert("1.0", f"It is currently night in {place}")
            tday.config(state="disabled")
            tday.pack(padx=10, pady=10)

            
            speak(f"It is currently night in {place} with current temperature being{current_weather['temp_c']}, though it feels like {current_weather['feelslike_c']}")
            speak(f"The weather condition in {place} is {text}")
            

        elif current_weather['is_day'] == 1:

            l_day = tk.Label(root, text="Day/Night:")
            l_day.config(font=("Arial", 16))
            l_day.pack()

            tday = tk.Text(root, height=1, width=100)
            tday.config(font=("Arial", 16), bg="#dddddd", state="normal")
            tday.insert("1.0", f"It is currently day in {place}")
            tday.config(state="disabled")
            tday.pack(padx=10, pady=10)

            speak(f"It is currently day in {place} with current temperature being{current_weather['temp_c']}, though it feels like {current_weather['feelslike_c']}")
            speak(f"The weather condition in {place} is {text}")
        
        ctemp_l = tk.Label(root, text="Current Temperature:")
        ctemp_l.config(font=("Arial", 16))
        ctemp_l.pack()

        ctemp_t = tk.Text(root, height=1, width=100)
        ctemp_t.config(font=("Arial", 16), bg="#dddddd")
        ctemp_t.insert("1.0", f"{current_weather['temp_c']}")
        ctemp_t.config(state="disabled")
        ctemp_t.pack(padx=10, pady=10)


        feel_temp_l = tk.Label(root, text="Feels like:")
        feel_temp_l.config(font=("Arial", 16))
        feel_temp_l.pack()

        feel_temp_t = tk.Text(root, height=1, width=100)
        feel_temp_t.config(font=("Arial", 16), bg="#dddddd")
        feel_temp_t.insert("1.0", f"{current_weather['feelslike_c']}")
        feel_temp_t.config(state="disabled")
        feel_temp_t.pack(padx=10, pady=10)

        weather_cond_l = tk.Label(root, text=f"Weather condition in {place}:")
        weather_cond_l.config(font=("Arial", 16), wraplength=500)
        weather_cond_l.pack()

        weather_cond_t = tk.Text(root, height=1, width=100)
        weather_cond_t.config(font=("Arial", 16), bg="#dddddd")
        weather_cond_t.insert("1.0", f"{text}")
        weather_cond_t.config(state="disabled")
        weather_cond_t.pack(padx=10, pady=10)

        speak("Thanks for listening!")

    btn1 = tk.Button(root, text="SUBMIT", command=forecaster)
    btn1.config(font=("Arial", 12))
    btn1.pack()

    root.mainloop()



    
    

    
