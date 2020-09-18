# TO DO:::::
# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

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
            print("***Book lended successfully!! Return it within a week :) ***")
        else:
            print("No such game available in the directory!")

    def returnb(self, name):
        if name.lower() in self.lenders.keys():
            self.booklist.append(self.lenders[name.lower()])
            self.lenders.pop(name.lower())
            print("***Book returned successfully!***")
        else:
            print("Input proper name!")

    def donate(self, kindname, newbook):
        print("Thanks", kindname, "a lot!!!")
        self.booklist.append(newbook)
        self.donors.update({kindname.capitalize():newbook})
    
Shravan_Lib = Library(["Factfulness", "The Code of Extraordinary Mind", "The 5AM Club", "Rich Dad Poor Dad"], "Central Library", {}, {})

if __name__ == "__main__":
    while True:
        print("This is the", Shravan_Lib.libname, "library!")
        op = int(input("What would you like to do:\n1. See the book list\n2. Rent a book\n3. Donate a book\n4. Return a book\n(1/2/3/4) "))

        if op==1:
            print(Shravan_Lib.books)
            if len(Shravan_Lib.donors)>0:
                print(f"Some kind men who donated us books: {Shravan_Lib.donors}")
            else:
                pass      

        elif op==2:
            print(Shravan_Lib.books)
            if len(Shravan_Lib.donors)>0:
                print(Shravan_Lib.donors)
            else:
                pass
            name = input("Your name: ")
            book = input("Book name: ")
            Shravan_Lib.lend(book, name)

        elif op==3:
            name = input("Your name: ")
            book = input("Book name: ")
            Shravan_Lib.donate(name, book)
        
        elif op==4:
            if len(Shravan_Lib.lenders)>0:
                print(Shravan_Lib.lenders.keys())
                name = input("Your name: ")
                Shravan_Lib.returnb(name)
            else:
                print("No borrowers currently in the system!")

        else:
            print("Invalid input!")
