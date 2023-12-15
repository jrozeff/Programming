#Jonathan Rozeff
#Assignment number: 3
#Date: 2/13/18
#Section: 2-3:30
#This program was created for a Mrs. Rose, the owner of a small flower shop. Its purpose is to allow customers to place an order, or multiple if wanted.
#After an order is placed, the program will print out a business receipt for the customer. 


#The statement below creates a loop for multiple orders. 
More_Roses = 'Y' or 'y'

#The statements below are constant variables.
SALES_TAX = 0.075
REDROSE_PRICE = 2.00
YELLOWROSE_PRICE= 1.50
DISCOUNT = .05

#The statements below are the beginning values for red and yellow rose count (for the accumalator).
RRose_Count = 0
YRose_Count = 0

    
#The statement below is part of the loop that allows customers to place another order. 
while More_Roses == 'Y' or More_Roses == 'y':
    print('Welcome to The Little Flower Shop')
    print('**********************************')
    print('            ~Menu~')
    print('Flowers:')
    print('  Red Roses, $2.00')
    print('  Yellow Roses, $1.50')
    print()

#The statements below make up the input validation loop that prompts customers for rose color.
    Rose_Color = str(input('Which color rose would you like? (R or r-Red, Y or y-Yellow)'))
    while Rose_Color != 'R' and Rose_Color != 'r' and Rose_Color != 'Y' and Rose_Color != 'y':
         print('Invalid rose color entered.')
         print('Please try again.')
         Rose_Color = str(input('Which color rose would you like? (R or r-Red, Y or y-Yellow)'))

#The variables are the calculations for the total rose prices (per color). 
    TotalRR_Price = RRose_Count*REDROSE_PRICE
    TotalYR_Price = YRose_Count*YELLOWROSE_PRICE

#The statements below are nested decision-structures that specify how many of which rose color the customer wants.
#Inside there are also statements that prohibit negative numbers from being ordered.
    if Rose_Color == 'R' or Rose_Color == 'r':
        Red_Roses = int(input('How many red roses would you like to order?'))
        if RRose_Count<0:
             print('The count that you have entered is negative.')
             print('Transaction cannot be processed.')
        else:
             RRose_Count = RRose_Count + Red_Roses
             TotalRR_Price = RRose_Count*REDROSE_PRICE 
             print('You have ordered', RRose_Count, 'red rose(s). The price is', '$'+format(TotalRR_Price, '.2f'))
    else:
        Yellow_Roses = int(input('How many yellow roses would you like to order?'))
        if YRose_Count<0:
            print('The count that you have entered is negative.')
            print('Transaction cannot be processed.')
        else:
            YRose_Count = YRose_Count + Yellow_Roses
            TotalYR_Price = YRose_Count*YELLOWROSE_PRICE
            print('You have ordered', YRose_Count, 'yellow rose(s). The price is', '$'+format(TotalYR_Price, '.2f'))
    
 
#The statement below is part of the loop that can allow customers to place another order. 
    More_Roses = str(input('Would you like to make another purchase? (If so, enter: Y or y)'))
    print()

#The statements below the calculations for the total price of roses (without sales tax), the discount amount, the tax amount, and the total amount (including sales tax). 
TotalPrice = TotalRR_Price + TotalYR_Price
Discount_Amount = TotalPrice*DISCOUNT
Tax_Amount = TotalPrice*SALES_TAX
TotalPrice_Tax = TotalPrice + Tax_Amount


#The statements below produce the business receipt, they display the amount each type of rose purchased and their prices (without sales tax). 
print('Transaction Report')
print('==================')
print('You have purchased', RRose_Count, 'red rose(s).')
print('The price for red roses is', '$'+format(TotalRR_Price, '.2f'))
print('You have purchased', YRose_Count, 'yellow rose(s).')
print('The price for yellow roses is', '$'+format(TotalYR_Price, '.2f'))

#The statements below are a decision-structure that outputs the total amount of sales before discount, and if applicable, the discount amount.
if TotalPrice>20.00:
    print('The total amonunt of sales before discount', '$'+format(TotalPrice, '.2f'))
    print('The discount amount is', '$'+format(Discount_Amount))
else:
    print('The total amonunt of sales before discount', '$'+format(TotalPrice, '.2f'))
    print('The sale is less than $20.00, no discount can be applied.')
print('The tax amount is', '$'+format(Tax_Amount, '.2f'))
print('The total amount with sales tax is', '$'+format(TotalPrice_Tax, '.2f'))
    





