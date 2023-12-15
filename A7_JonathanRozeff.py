#Jonathan Rozeff & Madeline Deal
#Assignment Number: 8
#Date: 4/09/18
#Section: 2-3:30pm
#This program was created to store emloyee's and their information in a dictionary, add new employee's, 
#and be able to print a report. 


#Imports employee.py file 
import employee

#Declares ADD and PRINT as global variables
ADD = 'A'
PRINT = 'P'

#Main Function
def main():

    #Below is an exception handling statement
    try:
        
        #Creates an empty dictionary 
        employee_dict = {}

        #Instantiates two employee objects  
        employee1 = employee.Employee('Mary Walles', 31.00, 26)
        employee2 = employee.Employee('Jay Watson', 38.00, 40)

        #Assigns objects to the empty dictionary 
        employee_dict[employee1.get_name()] = employee1
        employee_dict[employee2.get_name()] = employee2

        #Below is the Exception handling statement for the main function
        
        #Below is the input statement that asks if you want to being the program
        begin = input('Do you want to begin the Employee program? Yes to start: ')
        begin = begin.upper()
        
        #Below is one loop that contain the getMenuChoice function 
        while begin == 'YES':
            
            choice = getMenuChoice()

            #Below is a decision structure to process the choice given 
            if choice == ADD:
                addEmployee(employee_dict)
                #Below is the input statement that asks if you want to continue the program 
                begin = input('Do you want to continue the program? Yes to continue: ')
                begin = begin.upper()
            elif choice == PRINT:
                printEmployee(employee_dict)
                begin = input('Do you want to continue the program? Yes to continue: ')
                begin = begin.upper()
                
    except Exception as Error:
        print(Error)
        begin = input('Do you want to continue the program? Yes to continue: ')
        begin = begin.upper()


#getMenuChoice Function (displays menu in beginning)
def getMenuChoice():
    print()
    print('Welcome to the Employee Program')
    print('===============================')
    print('A - Add a new contact')
    print('P - Print employees report')
    print()

    #The statement below gets the choice input
    choice = input('Please enter your choice: ')

    #The loop below process invalid choice inputs
    while choice != 'A' and choice != 'a' and choice != 'P' and choice != 'p':
        choice = input('Invalid choie! Please re-enter: ')
    
    #The decision structure below processes valid choice inputs 
    if choice == 'A' or choice == 'a':
        choice = 'A'
        return choice
        
    elif choice == 'P' or choice == 'p':
        choice = 'P'
        return choice 

#addEmployee Function (with the dictionary as the parameter)
def addEmployee(employee_dictionary):
    
    #Below is the input statement that prompts for the employee name 
    new_name = input('Please enter employee name: ')

    #Below is the Exception handling statement for the main function
    try:
        
        #The statement below is the input for the new_rate and also contains a
        #decision structure that assigns a value of 0 to new_rate if an invalid value is entered 
        new_rate = float(input('Please enter the hourly rate: '))
        if new_rate < 7.50 or new_rate > 70.00:
            print('Rate is not between 7.5 and 70. It will be set to 0.')
            new_rate = 0
            
        #The statement below is the input for the new_hours and also contains a
        #decision structure that assigns a value of 0 to the new_hours if an invalid value is entered. 
        new_hours = float(input('Pleae enter the hours worked: '))
        if new_hours < 5.00 or new_hours > 40.00:
            print('Hours worked is not between 5 and 40. It will be set to 0.')
            new_hours = 0
            
        
        #Instantiates employee object 
        employee3 = employee.Employee(new_name, new_rate, new_hours)

        #The statement below is a decision structure that prompts for a new rate and or hours if
        #given; in this decision structure, there is also another decision structure that will process if the
        #newly entered rate is valid or not. 
        if new_rate == 0:
            new_rate = float(input('Please enter the rate again: '))
            employee3.set_rate(new_rate)
            
            if new_rate < 7.50 or new_rate > 70.00:
                print('The new hourly rate is out of range! Value not updated')
                new_rate = 0
            else:
                employee3.set_rate(new_rate)

        #This decision structure process if the newly entered hours worked are valid or not. 
        if new_hours == 0:
            new_hours = float(input('Please enter the hours worked again: '))
            employee3.set_hours(new_hours)

        #Creates a new employee
        employee_dictionary[new_name] = employee3
        print()
        
    except ValueError:
        print('Inavlid entry! Numberic value must be entered.')


#printEmployee Function (with the dictionary as a paramter)
def printEmployee(employee_dictionary):
    print()
    print('Display All Employees')
    print('=====================')
    
    #Iterates through the dictionary 
    for key in employee_dictionary:
        print(employee_dictionary[key])
        
#Calls the Main Function 
main()

       




        
