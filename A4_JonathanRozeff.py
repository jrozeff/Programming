#Jonathan Rozeff
#Assignment number: 4
#Date: 2/28/18
#Section: 2-3:30
#This assignemnt was created for users to be able to purchase t-shirts.

def main():
#Main function main
    
    PRICE_RED = 8.00
    PRICE_YELLOW = 8.00
    PRICE_BLUE = 18.00
    TAX_RATE = .0725
    MAX_RED = 8
    MAX_BLUE = 19
    MAX_YELLOW = 8
    CHARITY_RATE = 0.01
    #Above are all the constant variables
    
    start_loop = 0
    amount = 0
    Red_amount = 0
    Blue_amount = 0
    Yellow_amount = 0
    number_ordered = 0
    #Above are the variable initializations

    begin = str(input('Would you like to begin the program?'))
    while begin == 'Y' or begin == 'y':
    #Above is the loop for when customers want to make another purchase
        
        print()
        choice = getCustomerChoice()
        
        while choice == 'A' or choice == 'a' or choice == 'B' or choice == 'b' or choice == 'C' or choice == 'c':
        #Above is the choice loop
         
            if choice == 'A' or choice == 'a':
                Max_Number = MAX_RED
                price = PRICE_RED
                charge = calculateCharge(price, amount, TAX_RATE)
                amount = getTShirtNumber(MAX_RED)

                Red_amount = Red_amount + amount

                
            elif choice == 'B' or choice == 'b':
                Max_Number = MAX_BLUE
                price = PRICE_BLUE
                charge = calculateCharge(price, amount, TAX_RATE)
                amount = getTShirtNumber(MAX_BLUE)
                
                Blue_amount = Blue_amount + amount
                
            else:
                Max_Number = MAX_YELLOW
                price = PRICE_YELLOW
                charge = calculateCharge(price, amount, TAX_RATE)
                amount = getTShirtNumber(MAX_YELLOW)
            
                Yellow_amount = Yellow_amount + amount
             #Above is the decision structure for each t-shirt choice

            
        print('You have purchased a total of', amount, 'shirt(s).')
        total_amount = Red_amount + Blue_amount + Yellow_amount
        buy_more = buyMore(total_amount)
        begin = str(input('Do you want to continue shopping? (Y or y - Yes)'))
        print()
        choice = 'stop loop'
        #The statements above show the total t-shirt amount purchased and the input for another purchase loop

        total_order_charge = calculateCharge(PRICE_RED, Red_amount, TAX_RATE) + calculateCharge(PRICE_BLUE, Blue_amount, TAX_RATE) + calculateCharge(PRICE_YELLOW, Yellow_amount, TAX_RATE)
        donation_amount = total_order_charge * CHARITY_RATE


def display_menu(): #Function 1
    print('Welcome to Beautiful and Handsom T-Shirts')
    print('-----------------------------------------')
    print('(A) - Red t-shirt: $8.00')
    print('(B) - Blue t-shit: $18.00')
    print('(C) - Yellow t-shirt: $8.00')
    print()
    

def getCustomerChoice(): #Function 2
    display_menu()
    getCustomerChoice=str(input('Please select a choice (A or a for Red, B or b for blue, C or c for Yellow):'))
    while getCustomerChoice !='A' and getCustomerChoice !='a' and getCustomerChoice !='B' and getCustomerChoice !='b' and getCustomerChoice !='C' and getCustomerChoice !='c':
            print('Invalid choice!')
            getCustomerChoice=str(input('Please select a choice:'))
    return getCustomerChoice
    
    

def getTShirtNumber(Max_Number): #Function 3
    amount = int(input('How many t-shirts would you like to order?000'))

    while amount > Max_Number or amount < 0:
        if amount > Max_Number:
            print('Invalid Number! Exceeded maximum number')
            print('The maximum number you can buy at one time is', Max_Number)
            amount = int(input('How many t-shirts would you like to order?111'))
            return amount
            
        elif amount < 0:
            print('Invalid Number!')
            print('You have to enter 0 or a positive number!')
            amount = int(input('How many t-shirts would you like to order?222'))
            return amount
            
        else:
            return amount
#The above statements show the def for getTShirtNumber, prompt for t-shirt number,  include a nested decision structure for the maximum number ordered and negative shirts ordered with a loop
#that has a decision structure that prints invalid number (either for negative or exceeding maximum numbers)


def calculateCharge(price, amount, TAX_RATE): #Function 4
    total_price = price*amount
    sales_tax = total_price*TAX_RATE
    charge = total_price + sales_tax
    return charge
#The above statements show the def for calculateCharge and the calculations for total price, sales tax, and charge


def buyMore(): #Function 5
    total_amount = Red_amount + Blue_amount + Yellow_Amount
    if total_amount >=0 and total_amount<3:
        print('If you buy', format(3-total_amount, '.0f'), 'more, you will qualify for a free Green t-shirt.')
    else:
        print('Yay! You will receive a free Green t-shirt!')
    return total_amount
#The above statements show the def for buyMore, the calculation for total amount, and a decision structure that will prompt to buy more t-shirts or let the user know
#they are eligible for a green t-shirt


main()
