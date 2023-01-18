import Date
fileName=""
def invoice():
    global fileName
    while True:
        print("Enter your first name")
        firstName = input()
        if firstName.isalpha():
            break
        else:
            print("Name cannot be in number")
    while True:
        print("Enter your last name")
        lastName = input()
        if lastName.isalpha():
            break
        else:
            print("LastName also cannot be number")
    fileName = "Rent" + firstName+" "+lastName + ".txt"
    with open(fileName, "w+") as f:
        f.write("************************Beige Nepal************************ \n\n")
        f.write("Name of customer who rented : " + firstName + " " + lastName + "\n")
        f.write("Date of Renting: " + Date.getDate() + "\n")
        f.write("Time of Renting" + Date.getTime() + "\n\n")
        f.write("S.N.              Cloth Name                                        Brand                   Price            Quantity\n")
        f.write("------  -----------------------------------------------   -------------------------   -------------------   ---------- \n")