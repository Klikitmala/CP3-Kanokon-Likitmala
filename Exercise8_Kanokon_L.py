usernameInput = input("Username :")
passwordInput = input("Password :")

if usernameInput == "Kanokon" and passwordInput == "1234" :
    print("Welcome Y'All !!!!")
    print("<<<<<<  Nanny Shop >>>>>>")

    print("1. Squishmello : 13.99 $")
    print("2. Kids Jean : 10.99 $")
    print("3. Kids T-shirt : 4.99 $")
    
    price1 = 13.99 #1. Squishmello : 13.99 $
    price2 = 10.99 #2. Kids Jean : 10.99 $
    price3 = 4.99  #3. Kids T-shirt : 4.99 $

    userSelected = int(input("Please Select item's number >>"))

    if userSelected == 1:
        print("1. Squishmello : 13.99 $")
        quantity1 = int(input("Quantity ="))
        totalPrice1 = price1*quantity1
        print("Total Price :",totalPrice1,"quantity:",quantity1)
    elif userSelected == 2:
        print("2. Kids Jean : 10.99 $")
        quantity2 = int(input("Quantity ="))
        totalPrice2 = price2*quantity2
        print("Total Price :",totalPrice2,"quantity:",quantity2)
    elif userSelected == 3:
        print("3. Kids T-shirt : 4.99 $")
        quantity3 = int(input("Quantity ="))
        totalPrice3 = price3*quantity3
        print("Total Price :",totalPrice3,"quantity:",quantity3)
else :
    print("Could not find your Username or Password, please try again")