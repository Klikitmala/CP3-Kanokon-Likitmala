#Build stars pyramid
#input = 5 
'''
    *
   ***
  *****
 *******
*********
'''
number = int(input("enter the number of rows ="))
for row in range(number) :
    for column in range(number-row-1) :
        print(" ",end="")
    for column in range(row*2+1) :
        print("*",end="")
    print()
