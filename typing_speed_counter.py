import time, random

with open("typing_speed_phrases.txt") as p:
    ps = p.read()
    phrase_list = ps.split("\n")

def save_history(name:str, wpm, mistakes:int):
    """
    Saves the result of the typing speed test.
    """
    txt = f"{name.capitalize()} had an average typing speed of {wpm} wpm with {mistakes} mistakes commited.\n"
    try:
        with open('typing_speed_history.txt', 'a') as f:
            f.write(txt)
    except Exception as e:
        print(e)

def read_history():
    """
    Reads the typing speed test history.
    """
    with open('typing_speed_history.txt', 'r') as f:
        fc = f.read()
        print(fc)
        

def typing_speed(name:str):
    """
    Main code
    """
    sum_wpm = 0
    already_asked = []
    mistakes = 0

    for i in range(5):
        while True:
            phrase = random.choice(phrase_list)
            if phrase in already_asked:
                continue
            else:
                print(f"Phrase: {phrase}")
                phrase_ques = (phrase.split(" "))
                already_asked.append(phrase)
                break

        while 1:
            check = input("Press enter and start typing the phrase immidiately and again press enter once you've written the phrase.")
            init = time.time()
            user_ans = input()
            finish = time.time()

            user_ans = user_ans.split(" ")

            if len(user_ans) == len(phrase_ques):
                difference = finish - init
                wpm = (len(phrase_ques)*60)//difference
                sum_wpm += wpm
                for i in range(len(user_ans)):
                    if user_ans[i] == phrase_ques[i]:
                        pass
                    else:
                        mistakes += 1
                break
            else:
                print("You didn't typed the phrase wholly!")

        print("\n---------------------------------------------\n")
                
    average_wpm = sum_wpm/5
    result = f"Hey {name.capitalize()}, your average words per minute(WPM) counts {average_wpm} with {mistakes} mistakes commited.\n"

    save_history(name, average_wpm, mistakes)
    return result


if __name__ == "__main__":
    print("WELCOME TO THE TYPING SPEED COUNTER!\n")
    name = input("Enter your name: ")
    if name == "shravan-1908":
        read_history()
        quit()
    else:
        print(f"\n{typing_speed(name)}")