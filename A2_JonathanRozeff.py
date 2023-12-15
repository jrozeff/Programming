#Name: Jonathan Rozeff
#Assignment number: 2
#Date: 2/6/17
#Section: 2-3:30
#This program was created for a company named Gourmet Foods. Its purpose is to allow customers to order meal packages and also upgrade from an Ordinary to a Premium membership, if they have not done so already. 
#It also prints a Business Receipt for the cusomter.


#The statements below are constants and also the flag.  
SALESTAX = .075
PACKAGEPRICE_O = 5.95
PACKAGEPRICE_P = 5.20
MEMBERSHIP_FEE = 9.00
Error = 0

#The statements below display a welcome message along with inputs for a name and membership type. 
print('Welcome to Gourmet Food pre-packaged meals ordering program')
print('**************************************************************')
Name = str(input('Please enter your name:'))
Membership_type = str(input('Please enter your membership type (O or o-Ordinary; P or p-Premium):'))


#The decision structure below inlcudes inputs prompting for the amount of regular or premium packages wanted for the order. It also includes the decision structure to process the amount of free meals.
#A flag (Error) is also set withinin the structure in order to prohibit the customers from ordering 200 or more packages, as well as entering the wrong membership type. 
if Membership_type == 'O' or Membership_type == 'o':
    Package_Amount = int(input('How many packages do you want to order?'))
    if Package_Amount>=0 and Package_Amount<6:
        Free_Packages = 0
    elif Package_Amount>=6 and Package_Amount<=12:
        Free_Packages = 1
    elif Package_Amount>12 and Package_Amount<=200:
        Free_Packages = 2
    else:
        Error = 99
        print('You cannot order more than 200 packages! Transaction will not be conducted.')
 
elif Membership_type == 'P' or Membership_type == 'p':
    Package_Amount = int(input('How many packages do you want to order?'))
    if Package_Amount<4:
        Free_Packages = 0
    elif Package_Amount>=4 and Package_Amount<=8:
        Free_Packages = 1
    elif Package_Amount>8 and Package_Amount<=200:
        Free_Packages = 2
    else:
        Error = 99
        print('You cannot order more than 200 packages! Transaction will not be conducted.')
else:
    Error = 99
    print('Incorrect membership type entered, please try again.')

if Error != 99:

#The statements below are variables.    
    Total_O = (PACKAGEPRICE_O*Package_Amount)
    Total_P = (PACKAGEPRICE_P*Package_Amount)
    SalesTax_O = (Total_O*SALESTAX)
    SalesTax_P = (Total_P*SALESTAX)
    TaxTotal_O = (Total_O+SalesTax_O)
    TaxTotal_P = (Total_P+SalesTax_P)
    
#The statements below contain a decision structure which only displays the current charge for ordinary customers as well as prompts them if they want to upgrade to a premium membership.
#If customers do not respond with 'Y', they are not charged for a premium membership on the business receipt. 
    if Membership_type == 'O' or Membership_type == 'o':
        print('Your current charge is', '$'+format((TaxTotal_O), '.2f'))
        print('You can save more on pre-package price if you upgrade to premium membership!')
        Upgrade = str(input('Would you like to upgrade? (Y for Yes):'))
    else:
        Upgrade = 'n'
        
    print()


#The statements below display the business receipt. The receipt contains: customer name, membership type, total packages ordered, total price, sales tax, and new membership fee price (if customers decided to upgrade).
    print('Business Receipt')
    print('==================')
    print('Customer name:', Name)
    if Membership_type == 'O' or Membership_type == 'o':
        print('Membership Type: Ordinary')
    else:
        print('Membership Type: Premium')
    print('Total packages ordered:', Package_Amount)
    print('Total free packages:', Free_Packages)


    if Membership_type == 'O' or Membership_type == 'o':
        print('Total price:', '$'+format(Total_O, '.2f'))
    else:
        Membership_type == 'P' or Membership_type == 'p'
        print('Total price:', '$'+format(Total_P, '.2f'))
    
    if Membership_type == 'O' or Membership_type == 'o':
        print('Sales tax:', '$'+format(SalesTax_O, '.2f'))
    else:
        Membership_type == 'P' or Membership_type == 'p'
        print('Sales tax:', '$'+format(SalesTax_P, '.2f'))
  
    if Upgrade == 'Y':
        print('New membership fee:', '$'+format(MEMBERSHIP_FEE, '.2F'))

#The statements below are a continuation of the business receipt display. They show the total amount due. 
    if Upgrade == 'Y':
        print('Total amount due:', '$'+format(TaxTotal_O+MEMBERSHIP_FEE, '.2f'))
    elif Membership_type == 'P' or Membership_type == 'p':
        print('Total amount due:', '$'+format(TaxTotal_P,'.2f'))
    elif Upgrade != 'Y':
        print('Total amount due:', '$'+format(TaxTotal_O, '.2f'))


