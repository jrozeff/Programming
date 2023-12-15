#Name: Jonathan Rozeff
#Assignment Number: 1
#Date: 1/29/18
#Section: 2-3:30
#This program was created for the owner of DC (Delicious Cookies) and it's owner Mrs. Cookie. The program's purpose was to calculate how much Mrs. Cookie should charge her customers, see her profit amount, and update her on her inventory after each transaction. 

print('Welcome to Delicious Cookies!')
print('********************************')
print('           ~Menu~')
print('Cookies:')
print(' Vanilla Cookie, $1.20')
print(' Chocolate Cookie, $1.30')
print('Toppings:')
print(' Strawberry Cream per scoop, $0.50')
print(' Chocolate Chips per ounce, $0.20')
print(' Crushed Almonds per ounce, $0.40')
#Above includes the title, menu, and listing of cookies, toppings, and their prices. 
print()
VcookCount = float(input('How many Vanilla cookies?'))
CcookCount = float(input('How many Chocolate cookies?'))
topp1Count = float(input('How many scoops of Strawberry Cream?'))
topp2Count = float(input('How many ounces of Chocolate Chips?'))
topp3Count = float(input('How many ounces of Crushed Almonds?'))
#Above is the prompting for how many of each cookie/topping.
print()
VcookPrice = 1.20
CcookPrice = 1.30
topp1Price = 0.50
topp2Price = 0.20
topp3Price = 0.40
#Above shows the named constants and prices for the cookies/toppings.
print()
print('Customer Report for Mrs. Cookie')
print('********************************')
CRvanilla = (VcookCount*VcookPrice)
CRchocolate = (CcookCount*CcookPrice)
CRtopp1 = (topp1Count*topp1Price)
CRtopp2 = (topp2Count*topp2Price)
CRtopp3 = (topp3Count*topp3Price)
#Above is the Customer Report. Also show are the calculations for the amount owed for each cookie/topping ordered and the variables they are stored in. 
print('The price for', format(VcookCount, '.0f'), 'Vanilla cookies is', '$'+format(CRvanilla, '.2f'))
print('The price for', format(CcookCount, '.0f'), 'Chocolate cookies is', '$'+format(CRchocolate, '.2f'))
print('The price for', format(topp1Count, '.0f'), 'scoops of Strawberry is', '$'+format(CRtopp1, '.2f'))
print('The price for', format(topp2Count, '.0f'), 'ounces of Chocolate Chips is', '$'+format(CRtopp2, '.2f'))
print('The price for', format(topp3Count, '.0f'), 'ounces of Crushed Almonds is', '$'+format(CRtopp3, '.2f'))
#Above shows the prices for the total amount of cookies/toppings chosen. 
print()
sum = (CRvanilla + CRchocolate + CRtopp1 + CRtopp2 + CRtopp3)
salesTax = 0.0725
profitAmount = 0.30
print('The total price for this order is', '$'+format((sum+(sum*salesTax)), '.2f'))
print('The pre-sales tax profits are:', '$'+format(((sum*profitAmount)), '.2f'))
#Above are statements showing the sum of all cookies/toppings prices, the amounts for sales tax and profit, the total price for the order (including sales tax), and pre-sales tax profit. 
print()
VCstartInv = 70
CCstartInv = 70
StrCstartInv = 60
ChChstartInv = 50
CrAlstartInv = 40
#Above are the starting inventory amounts stored in variables. 
print('The current inventory of Vanilla cookies is:', format((VCstartInv-VcookCount), '.0f'))
print('The current inventory of Chocolate cookies is:', format((CCstartInv-CcookCount), '.0f'))
print('The total number of scoops of Strawberry Cream:',  format((StrCstartInv-topp1Count), '.0f'))
print('The total amount of Chocolate Chips left:', format((ChChstartInv-topp2Count), '.0f'), 'ounce(s)')
print('The total amount of Crushed Almonds left:', format((CrAlstartInv-topp3Count), '.0f'), 'ounce(s)')
#Above are the inventory amounts after subtracting the cookies/toppings purchased. 




