def getdate():
    import datetime
    return datetime.datetime.now()


import datetime


def gettime():
    return datetime.datetime.now()


var1 = int(input("1:log and 2:see:: "))
if var1 == 1:
    var2 = int(input("1:Mahin 2:Harry 3:Fahim:: "))
    var3 = int(input("1:Food 2:excrise:: "))
    # Mahin
    if var2 == 1 and var3 == 1:
        print('WHAT FOOD YOU EAT  ')
        var4 = input()
        f = open("mahinfood.txt", "a")
        a = f.write("\n"+var4 +str(getdate()))
        f.close()
    elif var2 == 1 and var3 == 2:
        var4 = input("what excrice you do \n")
        f = open("mahinExcrice.txt", "a")
        a = f.write("\n"+var4 + str(getdate()))
        f.close()
    # Harry
    if var2 == 2 and var3 == 1:
        var4 = input("what Food you eat \n")
        f = open("harryfood.txt", "a")
        a = f.write("\n"+var4 + str(getdate()))
        f.close()
    elif var2 == 2 and var3 == 2:
        var4 = input("what Excrice you do ")
        f = open("harryExcrise.txt", "a")
        a = f.write("\n"+var4 + str(getdate()))
        f.close()
    # fahim
    if var2 == 3 and var3 == 1:
        var4 = input("what Food you eat ")
        f = open("fahimfood.txt", "a")
        a = f.write("\n"+var4 + str(getdate()))
        f.close()
    elif var2 == 3 and var3 == 2:
        var4 = input("what Excrice you do ")
        f = open("fahimExcrise.txt", "a")
        a = f.write("\n"+var4 + str(getdate()))
        f.close()

else:
    var2 = int(input("1:Mahin 2:Harry 3:Fahim:: "))
    var3 = int(input("1:Food 2:excrise:: "))
    # Mahin
    if var2 == 1 and var3 == 1:
        f = open("mahinfood.txt", "r+")
        print(f.read())
        f.close()
    elif var2 == 1 and var3 == 2:
        f = open("mahinExcrice.txt", "r+")
        print(f.read())
        f.close()
    # harry
    if var2 == 2 and var3 == 1:
        f = open("harryfood.txt", "r+")
        print(f.read())
        f.close()
    elif var2 == 2 and var3 == 2:
        f = open("harryExcrise.txt")
        print(f.read())
        f.close()
    # fahim
    if var2 == 3 and var3 == 1:
        f = open("fahimfood.txt")
        print(f.read())
        f.close()
    elif var2 == 3 and var3 == 2:
        f = open("fahimExcrise.txt", "r+")
        print(f.read())
        f.close()
