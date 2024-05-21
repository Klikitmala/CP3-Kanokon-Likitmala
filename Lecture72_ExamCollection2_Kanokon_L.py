menuList = []

def showBill():
    print("---- My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number])
        totalPrice = totalPrice + int(menuList[number][1])
    print("Total Price : $",totalPrice)
while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : $")
        menuList.append([menuName,menuPrice])

showBill()        