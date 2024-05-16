def tax_calculate(total_price) :
    result = total_price+total_price*7/100
    return result
price_input = int(input("enter your total price = "))
print(tax_calculate(price_input))
