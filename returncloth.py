import Date
import list
def Bookreturn():  # creating function to return cloth
    name = input("Enter your firstname: ")
    lastname = input("Enter your lastname: ")
    rent = "rent" + name + ".txt"
    datas=""
    try:
        with open(rent, "r") as f:
            lines = f.readlines()
            lines = [a.strip("$") for a in lines]
        with open(rent, "r") as f:
            datas = f.read()
            print(datas)
    except:
        print("The information is incorrect so, please write a firstname and lastname used at a time of borrow")
        Bookreturn()

    retur = "Return" + name + ".txt"  # creating return file name
    with open(retur, "w+") as f:
        '''write the given information'''
        f.write(
            "*******************************Beige Nepal******************************* \n\n")
        f.write("Name of Returner: " + name + "\n")
        f.write("Date of Return  : " + Date.getDate() + "\n")
        f.write("Time of Return  : " + Date.getTime() + "\n\n\n")
        f.write(
            " S.N.            cloth Name                                      Brand                      Cost of Cloth\n")
        f.write(
            "------  ---------------------------------------------      --------------------------      -------------------\n")
        unitprice=0.0


    for i in range(len(list.ClothName)):
        if list.ClothName[i] in datas:
            with open(retur, "a") as f:
                f.write(str(i + 1) + "\t\t\t" + list.ClothName[i] + "\t\t\t\t\t\t\t\t\t" + list.Brand[i] + "\t\t\t\t\t$" + list.Price[i] + "\n")
            list.QuantityAvailable[i] = int(list.QuantityAvailable[i]) + rent.noOfQuantity+rent.b
            unitprice += float(list.Price[i])

            with open(retur, "a") as f:
                f.write("Unit cost: $" + str(unitprice) + "\n")
                f.write("Total: $"+str(rent.sum)+"\n")
                print("Total cost altogether:" + "$" + str(rent.sum))
                print("Is your  return date expired?")
                print("Press Y if it is expired for Yes and N if not expired for No")
                stat = input()
                if (stat.upper() == "Y"):
                    a=list.sum
                    print("How many days was the book returned late?")
                    day = int(input())  # input user to enter expired day
                    fine = 1.5 * day  # calculate fine
                    with open(retur, "a") as f:
                        f.write("Fine amount: $" + str(fine) + "\n")
                    a+= fine  # calculate book cost and fine amount
                    print("Fine amount=", fine)

                print("Total amount paid with fine: " + "$" + str(a))
                with open(retur, "a") as f:
                    f.write("Total amount paid with fine: $" + str(a))

                with open("stock.txt", "w+") as f:
                    for i in range(len(list.ClothName)):
                        f.write(
                            list.ClothName[i] + "," + list.Brand[i] + "," + str(list.QuantityAvailable[i]) + "," + "$" +
                            list.Price[i] + "\n")

