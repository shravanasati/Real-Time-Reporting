import smtplib, pyautogui, time, os
pyautogui.FAILSAFE = True
cwd = os.getcwd()

class Spammer:
    """
    Spammer class which has functions to spam in file, email and other ways.
    """

    def spam_script_file(self, filepath, filename):
        try:
            os.chdir(filepath)
            f = open(f"{filename}", 'a')
            script_file = open('kungfu_panda.txt', 'r')
            script = script_file.read()
            f.write(script)
            f.close()
            script_file.close()

        except Exception as e:
            print(e)

        finally:
            os.chdir(cwd)


    def spam_file(self, filepath, filename, keyword, times):
        try:
            os.chdir(filepath)
            with open(f"{filename}", 'a') as f:
                for i in range(times):
                    f.write(f"{keyword}\n")

        except Exception as e:
            print(e)

        finally:
            os.chdir(cwd)


    def spam_email(self, keyword, times):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            host = input("Enter email address to spam: ")
            your_email = input("Enter your email: ")
            password = input("Enter your password: ")
            server.login(your_email, password)
            subject = input("Enter spam mail subject: ")
            body = keyword * times
            server.sendmail(your_email, host, f"Subject: {subject}\n{body}")
            server.quit()
            print("Spam email has been sent successfully!")

        except Exception as e:
            print(f"Following error occured:\n{e}")
            

    def spam_other(self, keyword, times):
        print("Starting spamming in 10 seconds...")
        time.sleep(10)
        for i in range(times):
            pyautogui.typewrite(keyword)


    def main(self):
        print("!!!!!This is the ultimate spammer!!!!!")
        app = int(input("\nWhere to spam?\n1.File\n2.Email\n3.Youtube Live Comments\n4.Other\n"))


        # TEXT FILE
        if app==1:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())

            if meme==1:
                file = input("Enter file name: ")
                path = input("Enter the directory path where this file is located: ")
                self.spam_script_file(path, file)

            elif meme==2:
                file = input("Enter file name: ")
                path = input("Enter the directory path where this file is located: ")
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                self.spam_file(path, file, keyword, times)

            else:
                raise Exception("Access denied!")

        
        # EMAIL SPAM
        elif app==2:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())

            if meme == 1:
                script_file = open(r'C:\\Users\\Lenovo\\Documents\\Python Codes\\kungfu_panda.txt', 'r')
                script = script_file.read()
                self.spam_email(script, 1)

            elif meme==2:
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                self.spam_email(f"{keyword}\n", times)

            else:
                raise Exception("Access denied!")


        # YOUTUBE COMMENT SPAM
        elif app==3:
            print("Open the youtube video (on browser) with comment section on.")
            keyword = input("Enter your keyword: ")
            times = int(input("How many times: "))
            print("It will wait for 10 seconds before sending the spam because of youtube live comment rules.")
            for i in range(times):
                self.spam_other(keyword, times)
                time.sleep(10)


        # OTHER SPAM
        elif app==4:
            print("\nWhat to spam?\n1. Kungfu Panda script\n2. Custom keyword or phrase")
            meme = int(input())
            
            if meme == 1:
                check = input("Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                with open(r'C:\\Users\\Lenovo\\Documents\\Python Codes\\kungfu_panda.txt') as f:
                    script = f.read()
                self.spam_other(script, 1)

            elif meme == 2:
                keyword = input("Enter your custom keyword: ")
                times = int(input("How many times: "))
                check = input("Open the application where you want to spam. Press enter once you've done it and then switch to that application and place the cursor to the 'type message' box.")
                self.spam_other(keyword+"\n", times)

            else:
                raise Exception("Access denied!")
            

        else:
            raise Exception("Access denied!")

        print("!!!!Spamming task successfuly executed!!!!")



if __name__=='__main__':
    sp = Spammer()
    sp.main()
