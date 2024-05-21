menuList = []
priceList = []
totalPrice = 0
def showBill():
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])

while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : $")
        menuList.append(menuName)
        priceList.append(menuPrice)
        totalPrice = totalPrice + int(menuPrice)

showBill()        
print("Total Price : $",totalPrice)
