def list():
    global ClothName
    global Brand
    global Price
    global QuantityAvailable
    ClothName = []
    Brand = []
    Price = []
    QuantityAvailable = []
    with open("stock.txt",'r') as f:

        lines=f.readlines()
        b=[]
        for x in lines:
            a=x.strip('\n')
            b.append(a)
        lines=b
        for i in range(len(lines)):
            index=0
            for c in lines[i].split(','):

                if(index==0):
                    ClothName.append(c)
                elif(index==1):
                    Brand.append(c)
                elif(index==2):
                    QuantityAvailable.append(c)
                elif(index==3):
                    Price.append(c.strip(" $"))
                index=index+1












