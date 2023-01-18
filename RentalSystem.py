import list
import rent
import returning


def RentalSystem():
    while (True):  # checking the condition to display, borrow ,return or exit
        print("------------------------------------------------------------------------------")
        print("          Beige Nepal     ")
        print("------------------------------------------------------------------------------")

        print("Enter 1. To Display Clothes we have")
        print("Enter 2. To Rent a Cloth as per needed")
        print("Enter 3. To return a  cloth")
        print("Enter 4. To exit")

        try:
            choose = int(input("Select a choice from 1-4 as per your needed: "))

            print()

            if (choose == 1):
                with open("stock.txt", "r") as f:
                    lines = f.read()# read bookstock.txt
                    print(lines)
                    print()

            elif (choose == 2):
                list.list()  # calling list function
                rent.Rent()  #calling rent function from rent module
                print("Note: Please, return our cloth within  5 day if you return late then you have to pay fine 1.5 per day.")
            elif (choose == 3):
                list.list()  # calling list function
                returning.Rentreturn()# calling return function

            elif (choose == 4):
                print("------------------------------------------------------------------------------")
                print("    Thank you  ")
                print("-------------------------------------------------------------------------------")
                break  # exit loop process
            else:
                print("Please enter a valid choice i.e 1-4")

        except ValueError:
            print("Please select from the choices given to you")
RentalSystem()