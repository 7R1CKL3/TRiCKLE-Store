from datetime import datetime

from operation import *

from read import *

from write import *



unique = str(datetime.now())





welcome()
def userlist():
    print("================================================")
    print("ENTER 1: TO BUY PRODUCTS AND ADD IN THE STOCK")
    print("ENTER 2: TO SELL PRODUCTS AND PRINT THE BILL")
    print("ENTER 3: TO VIEW INVENTORY")
    print("ENTER 4: TO EXIT")
    print("================================================\n")

dictionary,line = dict()

loop = True
while loop == True:
    l = False
    while l == False:
        try:
            userlist()
            enter = int(input("\nEnter your choice here : "))
            if enter == 1:
                distributor = input("\nEnter the name of the Distributor: ")
                inventory()
                s_n = item(line)
                quantity_no= quantity(s_n)
                distributor_file(dictionary,s_n,quantity_no)
                distributor_bill_print(dictionary,s_n,quantity_no,distributor,unique)
                bill_distrib(dictionary,s_n,quantity_no,distributor,unique)
                
            elif enter == 2:
                print()
                customer = input("\nEnter the name of the Customer: ")
                inventory()
                s_n_customer = sell(line)
                quantity_n= sell_quantity(s_n_customer)
                filename = customer + unique + '.txt'
                file_name = filename.replace(':','')
                customer_file(dictionary,s_n_customer,quantity_n)
                customer_bill_print(dictionary,s_n_customer,quantity_n,customer,unique)
                customer_bill(dictionary,s_n_customer,quantity_n,customer,unique)
        
            elif enter == 3:
                inventory()
                again()
            elif enter == 4:
                loop = False
                end()
            else:
                print("\nPlease input only the number present in the menu!!\n")
            l = True
        except ValueError:
            print("\n--------------------------------------------!!!!----------------------------------------------\n")
            print("Sorry! The data you have entered is not correct. Please enter a numerical value.\n")
            print("--------------------------------------------!!!!----------------------------------------------\n")
