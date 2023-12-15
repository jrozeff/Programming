#Jonathan Rozeff & Madeline Deal
#Assignment Number: 8
#Date: 4/23/18
#Section: 2-3:30pm
#This program was created to be able to store information of books and audiobooks.
#Users will be able to print and change the price of the different books. 


#Imports file with Book and AudioBook classes
import A8


#Main function 
def main():

    #The statement below is part of an exception handling statement
    try:

        #The statements below instantiate objects
        book1 = A8.Book('123-12-12345-12-1','Magic Kitten', 'Miss Muffet', 'Sunshine Publishing', 7.50)
        book2 = A8.Book('234-23-23456-23-2','The Lost Puppy', 'Lucy Carter', 'Moonlight Publishing', 6.90)
        AudioBook1 = A8.AudioBook('345-34-34567-34-3','Giant Peach Tree', 'Jane Stone', 'Starlight Publishing', 11.88, 'John Voice')
        AudioBook2 = A8.AudioBook('456-45-45678-45-4','The Pink Balloon', 'Jenny Herme', 'Sunshine Publishing', 12.99, 'Karen Vokal')

        #The statement below adds the objects to a list
        book_list = [book1, book2, AudioBook1, AudioBook2]

        #The statement below begins the program 
        begin = input('Do you want to begin the program? (YES or yes to begin): ')

        #The statement below starts a loop when user inputs 'YES'/'yes'
        while begin == 'YES' or begin == 'yes':

            #The print statements below display the menu
            print()
            print('Welcome to the book program!')
            print('============================')
            print('P - Print book information')
            print('C - Change the price of a book')
            print()

            #The statements below set the flag (wrongChoice) to 0, and allow users to input their
            #choice with no error (choice.upp())
            wrongChoice = 0
            choice = input('Please enter menu choice (P for print, C for change): ')
            choice = choice.upper()

            #The statements below is a decision structure the processes the choice entered
            if choice == 'P' or choice == 'p':
                PrintList(book_list)
            elif choice == 'C' or choice == 'c':
                ChangePrice(book_list)
            else:
                wrongChoice = 88888

            #The statement below checks to see if the choice entered is incorrect. If it is
            #users will be given another chance to re-enter the choice
            if wrongChoice == 88888:
                begin = input('Incorrect choice entered! Please re-enter choice: ')

            #The statement below prompts the user if they want to continue the program 
            begin = input('Do you want to continue with the program? (YES or yes to continue): ')

    #The statment below is part of an exception handling statement 
    except:
        begin = input('Do you want to continue with the program? (YES or yes to continue): ')


                
#Below is the function that prints the list of items
def PrintList(book_list):
    for item in book_list:
        print(item)


#Below is the function that changes the price
def ChangePrice(book_list):

    #The statements below prompt the user for the ISBN and new price
    ISBN = input('Please enter ISBN with dashes: ')
    new_price = float(input('Please enter new price: '))

    #The statement below sets a flag (Found_ISBN)
    Found_ISBN = 0

    #The statements below iterate through the list, tries to locate the ISBN,
    #if found sets the flag value to 1 and updates the price, and then breaks out of the loop
    for item in book_list:
        if item.get_ISBN() == ISBN:
            Found_ISBN = 1
            item.set_price(new_price)
        break

    #The statement below checks to see if the ISBN entered is valid
    if Found_ISBN == 0:
        print('The ISBN was not located! The price has not been updated!')
        print()

    #The statement below is a loop that processes incorrect inputs that are
    #are entered for the new price
    while new_price < 0.00 or new_price > 10.00:
            print('The new price must be between 0 and 100.00!')
            new_price = float(input('Please re-enter the new price: '))
            item.set_price(new_price)
            if new_price >= 0 or new_price <= 10.00:
                print('The price has been updated!')
                print()


#Calls Main function 
main()






    

    
