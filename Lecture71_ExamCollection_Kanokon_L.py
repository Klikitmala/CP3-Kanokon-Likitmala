menuList = []
priceList = []

def showBill():
    print("---- My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        totalPrice = totalPrice + int(priceList[number])
    print("Total Price : $",totalPrice)
while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : $")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()        

