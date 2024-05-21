systemMenu = {"Cali roll":6,"Lava roll":12,"Salmon roll":8}
menuList = []

def showBill():
    print("---- My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        totalPrice = totalPrice + int(menuList[number][1])
    print("Total Price : $",totalPrice)

while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

print(menuList)
showBill()        