import list
import invoice


def Rent() :
    a = True  # first while loop to infinity
    invoice.invoice()
    yesOrNo = True  # second while loop to infinity

    while a == True :

        print("choose a cloth you like to rent")
        for i in range(len(list.ClothName)) :
            print("Choose", i, "to Rent Clothes:", list.ClothName[i])

        try :
            choiceOfUser = int(input())
            sum = 0.0
            try:
                if (int((list.QuantityAvailable[choiceOfUser])) > 0) :

                    print("We have ", list.QuantityAvailable[choiceOfUser], "pieces remaining")
                    print("How many do you want to book")
                    noOfQuantity = int(input())
                    sum = float(list.Price[choiceOfUser]) * float(noOfQuantity)

                    if (int((list.QuantityAvailable[choiceOfUser])) >= noOfQuantity) :
                        yesOrNo = True
                        with open(invoice.fileName, "a") as f :
                            f.write("1. \t\t\t" + list.ClothName[choiceOfUser] + "\t\t\t\t\t\t\t\t\t\t" + list.Brand[
                                choiceOfUser] + "\t\t\t\t\t\t$" + list.Price[choiceOfUser] + "\t\t\t\t\t" + str(
                                noOfQuantity) + "\n")
                        list.QuantityAvailable[choiceOfUser] = int(list.QuantityAvailable[choiceOfUser]) - noOfQuantity
                        with open("stock.txt", "w+") as f :
                            for i in range(len(list.ClothName)) :
                                f.write(list.ClothName[i] + "," + list.Brand[i] + "," + str(
                                    list.QuantityAvailable[i]) + "," + "$" + list.Price[i] + "\n")
                        count = 1
                    else :
                        print("Sorry we only have" + list.QuantityAvailable[choiceOfUser] + "peices left")
                        yesOrNo = False
                else :
                    print("Not in stock please select another cloth")
                    yesOrNo = False

                while yesOrNo == True :


                    More = input('''Do you want to continue shopping?,
                            Y for continue
                            N for stopping''')
                    if (More.upper() == "Y") :
                        sum1 = 0.0

                        print("Choose any clothes you want to purchase \n")
                        for i in range(len(list.ClothName)) :
                            print("choose", i, "to rent clothes:", list.ClothName[i])
                        try :
                            a = int(input())  # to choose which cloth

                            try :
                                if (int(list.QuantityAvailable[a]) > 0) :

                                    print("Clothes available in our shops" + str(list.QuantityAvailable[a]) + "left")
                                    print("how many do you want to rent")
                                    b = int(input())  # no of quantity purchased of a particular cloth
                                    sum1 = float(list.Price[a]) * float(b)
                                    sum = float(sum1) + sum

                                    if (int((list.QuantityAvailable[a])) > b) :
                                        yesOrNo = True
                                        count = count + 1

                                        with open(invoice.fileName, "a") as f :
                                            f.write(
                                                str(count) + ". \t\t\t" + list.ClothName[a] + "\t\t\t\t\t\t\t\t\t " +
                                                list.Brand[a] + "\t\t\t\t\t\t\t$" + list.Price[a] + "\t\t\t\t" + str(
                                                    b) + "\n")
                                            list.QuantityAvailable[a] = int(list.QuantityAvailable[a]) - b
                                        with open("stock.txt", "w+") as f :
                                            for i in range(len(list.ClothName)) :
                                                f.write(list.ClothName[i] + "," + list.Brand[i] + "," + str(
                                                    list.QuantityAvailable[i]) + "," + "$" + list.Price[i] + "\n")



                                    else :
                                        print("sorry we only have" + list.QuantityAvailable[a] + 'left')
                                else :
                                    print("not in stock")




                            except IndexError :
                                print("")
                                print("Pleasechoose according to thier number")

                        except ValueError :
                            print("")
                            print("Please choose according to suggestion.")
                    elif (More.upper() == "N") :
                        b = False
                        print(" Rented  succesfully.\n")
                        print("Thank you. ")
                        print("")
                        # if count == 1 :
                        with open(invoice.fileName, "a") as f :
                            f.write('''\n-----------------------------------------------------------------------------------------------------
                                     Total price:''' + "$" + str(sum)
                                    )

                        a = False
                        break
                    else :
                        print("please enter either y or n")

            except IndexError :
                print("")
                print("Pleasechoose according to thier number")
        except ValueError :
            print("")
            print("Please choose according to suggestion.")
