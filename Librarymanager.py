# TO DO:::::
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)
# dictionary (books-nameofperson)
# create a main function and run an infinite while loop asking users for their input

class Library:
    def __init__(self, booklist, libname, lenders, donors):
        self.booklist = booklist
        self.libname = libname
        self.lenders = lenders
        self.donors = donors

    @property
    def books(self):
        return f"{self.booklist}"

    def lend(self, bookname, name):
        if bookname in self.booklist:
            self.booklist.remove(bookname)
            self.lenders.update({name.lower():bookname})
            print("***Game lended successfully!! Return it within a week :) ***")
        else:
            print("No such game available in the directory!")

    def returnb(self, name):
        if name.lower() in self.lenders.keys():
            self.booklist.append(self.lenders[name.lower()])
            self.lenders.pop(name.lower())
            print("***Game returned successfully!***")
        else:
            print("Put proper name!")

    def donate(self, kindname, newbook):
        print("Thanks", kindname, "a lot!!!")
        self.booklist.append(newbook)
        self.donors.update({kindname.capitalize():newbook})
    
Shravan_Lib = Library(["COD Mobile", "PUBG Mobile", "Free Fire", "Hopeless"], "Gamers", {}, {})

if __name__ == "__main__":
    while True:
        print("This is the", Shravan_Lib.libname, "library!")
        op = int(input("What would you like to do:\n1. See the game list\n2. Rent a game\n3. Donate a game\n4. Return a game\n(1/2/3/4) "))

        if op==1:
            print(Shravan_Lib.books)
            if len(Shravan_Lib.donors)>0:
                print(f"Some kind men who donated us games: {Shravan_Lib.donors}")
            else:
                pass      

        elif op==2:
            print(Shravan_Lib.books)
            if len(Shravan_Lib.donors)>0:
                print(Shravan_Lib.donors)
            else:
                pass
            name = input("Your name: ")
            book = input("Gamename: ")
            Shravan_Lib.lend(book, name)

        elif op==3:
            name = input("Your name: ")
            book = input("Gamename: ")
            Shravan_Lib.donate(name, book)
        
        elif op==4:
            if len(Shravan_Lib.lenders)>0:
                print(Shravan_Lib.lenders.keys())
                name = input("Your name: ")
                Shravan_Lib.returnb(name)
            else:
                print("No game borrowers currently in the system!")

        else:
            print("yOU aRE LOL!")