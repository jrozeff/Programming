#Jonathan Rozeff & Madeline Deal
#Assignment Number: 6
#Date: 3/23/18
#Section: 2-3:30pm
#This program was created to read files, store them into one and two dimensional lists, process each record
#in the file, and output the information stored in the two dimensional list. 

#Below are the constant variables 
NUMFIELD = 5
ROW = 5
COL = 5


#Below is the main function. Here the file is opened, the (empty) twoDim list is created, the first line is read
#and maxRow is equal to zero.
def main():
    try:
        a6_file = open('HW6_PROD.txt', 'r')
        product_id = a6_file.readline().rstrip('\n')
        twoDim = []
        maxRow = 0

        #This while loop reads and appends lines into prodList (which is empty at first), it also appends twoDim (the two dimensional list) and contains an accumulator. 
        while product_id != '':
            prodList = []
            
            name = a6_file.readline().rstrip('\n')
            price = a6_file.readline().rstrip('\n')
            profit_margin = a6_file.readline().rstrip('\n')
            quantity = a6_file.readline().rstrip('\n')

        
            prodList.append(product_id)
            prodList.append(name)
            prodList.append(price)
            prodList.append(profit_margin)
            prodList.append(quantity)

            twoDim.append(prodList)
            maxRow = maxRow + 1
            
            #Below the first line of the next record is read. 
            product_id = a6_file.readline().rstrip('\n')


        #Below prodReport and printTwoDim are called, the main file (a6_file) is also closed.
        prodReport(prodList)
        printTwoDim(twoDim, maxRow)
        a6_file.close()
    
    except Exception as IOError:
        print('An error has occurred, please run program again.', IOError)
        
#The function below opens the file, reads the first line and goes into a loop.
def prodReport(PL):
    a6_file = open('HW6_PROD.txt', 'r')
    product_id = a6_file.readline().rstrip('\n')

    #In the loop lines are read, and also assigned float and int values.
    #The revenue and profit amount variables are created here, and all of the records along with the revenue and profit amounts are printed. 
    while product_id != '':
        
        name = a6_file.readline().rstrip('\n')
        price = float(a6_file.readline().rstrip('\n'))
        profit_margin = float(a6_file.readline().rstrip('\n'))
        quantity = int(a6_file.readline().rstrip('\n'))
        
        revenue = quantity*price
        profit_amount = revenue*profit_margin
        
        print(product_id)
        print(name)
        print(price)
        print(profit_margin)
        print(quantity)
        print('Revenue:', '$'+format(revenue, '.2f'))
        print('Profit Amount:', '$'+format(profit_amount, '.2f'))
        print()
        print()

        product_id = a6_file.readline().rstrip('\n')
    a6_file.close() 


#Here the printTwoDim function opens the file, prints out all of the records from the two dimensional list, and then closes the list. 
def printTwoDim(DL, mRow):
    a6_file = open('HW6_PROD.txt', 'r')
    a6_file.readline().rstrip('\n')
    print('The content of the two dimensional list:')
    for ROW in range(mRow):
        print()
        for COL in range(NUMFIELD):
            print(DL[ROW][COL])
    a6_file.close()

  


main()

