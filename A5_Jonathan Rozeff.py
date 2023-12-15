#Jonathan Rozeff
#Assignment number: 
#Date: 3/9/18
#Section: 2-3:30pm
#This program allows the pizza shop owner to print and or update sales. 


#Main Function
def main():
    loop = 'Y' or 'y'
    while loop == 'Y' or loop =='y':
        welcome()
        choice = getChoice()
        if choice == 'P' or choice =='p':
            pizza_t = openFile()
            if pizza_t == '':
                loop = str(input('Do you want to continue? (Y or y - yes'))
                if loop == 'Y' or loop == 'y':
                    continue
            else:
               if pizza_t != '':
                   printReport(pizza_t)
            
                
        elif choice == 'U' or choice == 'u':
            print('Open input file:')
            input_fileV = openFile()
            print('Open output file:')
            output_fileV = openFile()
            updateFile()
        else:
            print('Invalid choice')
            print()
            loop = str(input('Do you want to continue? (Y or y - yes)'))
            print()

#This funtion displays the welcome message and option choices
def welcome():
    print('Welcome to the file program')
    print('=============================')
    print('To print report, press P o p')
    print('To update file, press U or u.')
    
def getChoice():
    choice = str(input('Please enter your choice:'))
    return choice


def openFile():
    file_name = str(input('What is the name of the file:'))
    file_mode = str(print('Please enter file mode:'))
    print('(r - reading, w - writing)')
    try: 
        if file_mode == 'r':
            pizza_t = open(file_name, file_mode)
            return pizza_t
        elif file_mode == 'w':
            pizza_profit = open(file_name, file_mode)
        return pizza_profit
            
    except Exception as Err:
        print('An exception has occurred, the system message is: [Errno 2] No such file or directory:', "'"+file_name+"'", Err)
        loop = str(input('Do you want to continue? (Y or y - yes'))
        

def printReport(file):
    pizza_count = 0
    total_profit = 0

    pizza = file.readline().rstrip('\n')
    while pizza != '':
        print('Pizza:', pizza)
        price = float(file.readline())
        print('Price:', '$'+price)
        cost = float(file.readline())
        print('Cost:', '$'+cost)
        profit = price - cost
        pizza_count += 1
        total_profit += profit
        print('Profit:', format('$'+profit, '.2f'))
    print()
    file.close()
    print('End of file!')
    print('A total of', pizza_count, 'pizza(s) have been processed.')
    print('The average profit is', '$'+(profit/pizza_count))


def updateFile(input_fileV, output_fileV):
    record_number = int(input('How many records?'))
    pizza = input_fileV.readline().rstrip('\n')
    for count in range(0, record_number):
        price = float(input_fileV.readline())
        cost = float(input_fileV.readline())
        pizza = input_fileV.readline().rstrip('\n')
        profit = price - cost

        
#The statement below calls main. 
main()
