import encrypt_decrypt, datetime
"""
A full fledged bike rental system implemented in Python using object oriented programming.

Customers can:
See available bikes on the shop. done
Rent bikes on hourly basis $5 per hour. done 
Rent bikes on daily basis $20 per day.  done
Rent bikes on weekly basis $60 per week. done
Family Rental, a promotion that can include from 3 to 5 Rentals (of any type) with a discount of 30% of the total price. done

The bike rental shop can:
Issue a bill when customer decides to return the bike. done
Display available inventory. done
Take requests on hourly, daily and weekly basis by cross verifying stock. done

For simplicity we assume that:
Any customer requests rentals of only one type i.e hourly, monthly or weekly. done
Is free to choose the number of bikes he/she wants. done
Requested bikes should be less than available stock. done
"""

class BikeRental:
    """
    A class which packs all the functions including renting and issuing bills.
    """
    def __init__(self, name, no_of_bikes) -> None:
        self.name = name
        self.no_of_bikes = no_of_bikes
        self.users = {}

    def rent_bike_hourly(self, name:str, bikes:int):
        """
        Allots bikes to a person on hourly basis.
        Takes name of the person and number of bikes to rent as inputs.
        """
        if bikes > self.no_of_bikes:
            print(f"Bike shortage! You can have max {self.no_of_bikes} bikes.")

        else:
            self.users.update({name:{"hourly":bikes}})
            print("Bike rented successfully!")
            self.no_of_bikes -= bikes

    def rent_bike_daily(self, name:str, bikes:int):
        """
        Allots bikes to a person on daily basis.
        Takes name of the person and number of bikes to rent as inputs.
        """
        if bikes > self.no_of_bikes:
            print(f"Bike shortage! You can have max {self.no_of_bikes} bikes.")

        else:
            self.users.update({name:{"daily":bikes}})
            print("Bike rented successfully!")
            self.no_of_bikes -= bikes

    def rent_bike_weekly(self, name:str, bikes:str):
        """
        Allots bikes to a person on weekly basis.
        Takes name of the person and number of bikes to rent as inputs.
        """
        if bikes > self.no_of_bikes:
            print(f"Bike shortage! You can have max {self.no_of_bikes} bikes.")

        else:
            self.users.update({name:{"weekly":bikes}})
            print("Bike rented successfully!")
            self.no_of_bikes -= bikes


    def issue_bill(self, name:str):
        """
        Issues bill to the customer on basis of the customer name.
        """
        if name in self.users.keys():

            for i in self.users[name].keys():
                if i == 'hourly':
                    print(f"{name.capitalize()}, you rented {self.users.get(name).get('hourly')} bikes on hourly basis.")
                    if self.users[name]['hourly'] > 3 and self.users[name]['hourly'] < 6:
                        print("You also got the family discount of 30%!")
                        bill = 0.7 * (5 * self.users[name]['hourly'])
                    else:
                        bill = 5 * self.users[name]['hourly']
                    print(f"Therefore, total amount payable: {bill}$")
                    self.no_of_bikes += self.users[name]['hourly']
                    check = input("Press any key to continue. ")
                    print("Bike returned successfully!")
                    self.users.pop(name)
                
                elif i == 'daily':
                    print(f"{name.capitalize()}, you rented {self.users.get(name).get('daily')} bikes on daily basis.")
                    if self.users[name]['daily'] > 3 and self.users[name]['daily'] < 6:
                        print("You also got the family discount of 30%!")
                        bill = 0.7 * (20 * self.users[name]['daily'])
                    else:
                        bill = 20 * self.users[name]['daily']
                    print(f"Therefore, total amount payable: {bill}$")
                    self.no_of_bikes += self.users[name]['daily']
                    print("Bike returned successfully!")
                    self.users.pop(name)
    
                elif i == 'weekly':
                    print(f"{name.capitalize()}, you rented {self.users.get(name).get('weekly')} bikes on weekly basis.")
                    if self.users[name]['weekly'] > 3 and self.users[name]['weekly'] < 6:
                        print("You also got the family discount of 30%!")
                        bill = 0.7 * (60 * self.users[name]['weekly'])
                    else:
                        bill = 60 * self.users[name]['weekly']
                    print(f"Therefore, total amount payable: {bill}$")
                    self.no_of_bikes += self.users[name]['weekly']
                    print("Bike returned successfully!")
                    self.users.pop(name)
    
                else:
                    print("ERROR")

        else:
            print("Put proper name!")


if __name__ == "__main__":
    Nagpur_Bikes = BikeRental("Nagpur Bike Rental Service", 20)
    while 1:
        task = int(input("What to do:\n 1. See available bikes\n 2. Rent a bike\n 3. Return a bike\n"))

        if task == 1:
            print(Nagpur_Bikes.no_of_bikes)


        elif task == 2:
            type = int(input("On what basis would you like to rent a bike:\n 1. Hourly basis - 5$ per hour\n 2. Daily basis - 20$ per day\n 3. Weekly basis - 60$ per week\n"))

            if type == 1:
                name = input("Enter your name: ")
                bikes = int(input("How many bikes do you want to rent? "))
                Nagpur_Bikes.rent_bike_hourly(name, bikes)

            elif type == 2:
                name = input("Enter your name: ")
                bikes = int(input("How many bikes do you want to rent? "))
                Nagpur_Bikes.rent_bike_daily(name, bikes)

            elif type == 3:
                name = input("Enter your name: ")
                bikes = int(input("How many bikes do you want to rent? "))
                Nagpur_Bikes.rent_bike_weekly(name, bikes)

            else:
                print("Invalid input!")


        elif task == 3:
            if len(Nagpur_Bikes.users) != 0:
                for i in Nagpur_Bikes.users.keys():
                    print(f"Customer name: {i}")
                name = input("Who are you from the above list? ")
                Nagpur_Bikes.issue_bill(name)
            else:
                print("No one has rented a bike yet!")

        else:
            print("Invalid input!")


        print("\n----------------------------------------------------\n")