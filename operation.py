from read import *

def welcome():
    print("-------------------------------------------------------------------------------")
    print("Hello Admin!!!\n")
    print("Welcome to TRiCKLE Store. Hope you enjoy it!")
    print("-------------------------------------------------------------------------------\n")     



def end():
    print("     **THANK YOU**     ")
    print("| HAVE A NICE DAY AHEAD |")
    print("-------------------------------------------------------------------------------")     
    print("The program has been termiated by the user")
    print("-------------------------------------------------------------------------------")     

def again():
    print("\n")
    input ("Enter any key to continue: ")
    print("\n")



def item(line_no):
    while True:
        try:
            s_n = int(input("\nEnter the S.No. of the product you want to buy here : "))
            if s_n < 1 or s_n > line_no:
                print("\n--------------------------------------------!!!!----------------------------------------------")
                print("Please enter a valid S.No. present in the inventory!!")
                print("--------------------------------------------!!!!----------------------------------------------\n")
                
            else:
                break
        except ValueError:
            print("\n--------------------------------------------!!!!----------------------------------------------")
            print("S.No. can only b numbers!!.")
            print("--------------------------------------------!!!!----------------------------------------------\n")
    return s_n

def quantity(s_n):
    while True:
        try:
            with open("stock.txt","r") as file:
                stock_dict = {}
                line_dict = 1
                for line in file:
                    line = line.replace("\n","")
                    value = line.split(",")
                    stock_dict.update({line_dict:value})
                    line_dict = line_dict + 1
                    if line_dict-1 == s_n:
                        print('\n'+line)
                        max_quantity = int(value[3])          
                quantity = int(input("\nEnter the quantity of the product you want to buy here : "))
                if quantity < 1 or quantity > 1000:
                    print("\n--------------------------------------------!!!!----------------------------------------------")
                    print("Sorry!! The distributor doesn't deliver more than 1000 products of same item at once.Try ordering a maximum of 1000 at once.")
                    print(" --------------------------------------------!!!!----------------------------------------------\n")    
                else:
                    break
        except ValueError:
            print("\n--------------------------------------------!!!!----------------------------------------------")
            print("Quantity can only be numbers!!.")
            print("--------------------------------------------!!!!----------------------------------------------\n")
    again1 = input("\nDo you want to buy more items from suppliers (Y/N) ")  
    if again1.lower() == "y":
        item(5)
    else:
        False
        again()
    return quantity     


def bill_distrib(dict,sn,quantity,distributor,unique):
    item = dict[sn-1]
    product = item[0]
    brand = item[1]
    price = int(item[2])-(int(item[2])*0.2)
    cpu = item[4]
    gpu = item[5]
    S_No = "S.No"
    Br = "Brand"
    Pr = "Product"
    R = "Rate"
    Qu = "Quantity"
    CPU = "Processor"
    GPU = "Graphics Card"
    vat = 0.13
    num = 1
    Am = int(price) * int(quantity)
    total = Am
    vat_am = Am * vat
    nett_total = int(Am) + int(Am) * vat
    print(110*'-'+'\n')
    print('\t\t\t\t\tWELCOME TO TRiCKLE STORE\n')
    print('\tMode of Payment: Checque')
    print('Distributor Name: '+distributor,(50-len(distributor))*' ','Date and Time: '+ unique)
    print('  -------------------------------------------------------------------------------------------------------------')
    print('      ',S_No,3*' ',Pr,6*' ',Br,8*' ',R,5*' ',Qu,4*' ',CPU,3*' ',GPU,'   Amount')
    print('  -------------------------------------------------------------------------------------------------------------')
    print('       ',end='')
    print(num,(8-len(str(num)))*' ',end="")
    print(product,(14-len(str(product)))*' ',end="")
    print(brand,(14-len(str(brand)))*' ',end="")
    print(price,(13-len(str(price)))*' ',end="")
    print(quantity,(10-len(str(quantity)))*' ',end="")
    print(cpu,(13-len(cpu))*' ',end="")
    print(gpu,(16-len(gpu))*' ',end="")
    print(Am)
    print('\n')
    print('  -------------------------------------------------------------------------------------------------------------')
    print('\t\t\t\t\t\t\t\t\t\t      ','Total Amount: ',total,'\n','\t\t\t\t\t\t\t\t\t          ','Vat Amount (13%): ',vat_am)
    print('  -------------------------------------------------------------------------------------------------------------')
    print('\t\t\t\t\t\t\t\t\t\t        ','Nett Total: ', nett_total)
    print('  -------------------------------------------------------------------------------------------------------------')



def sell(line_no):
    while True:
        try:
            s_n = int(input("\nEnter the S.No. of the product you want to Sell : "))
            #print(s_n)
            #print(line_no)
            a = line_no

            if s_n < 1 or s_n > 5:
                print("\n--------------------------------------------!!!!----------------------------------------------\n")
                print("Please enter a valid S.No. present in the inventory!!\n")
                print("--------------------------------------------!!!!----------------------------------------------\n")
                
            else:
                break
        except ValueError:
            print("\n--------------------------------------------!!!!----------------------------------------------\n")
            print("S.No. can only be numbers!!.\n")
            print("--------------------------------------------!!!!----------------------------------------------\n")
    return s_n

def sell_quantity(s_n):
    while True:
        try:
            with open("stock.txt","r") as file:
                stock_dict = {}
                line_dict = 1
                for line in file:
                    line = line.replace("\n","")
                    value = line.split(",")
                    stock_dict.update({line_dict:value})
                    line_dict = line_dict + 1
                    if line_dict-1 == s_n:
                        print('\n'+line)
                        max_quantity = int(value[3])          
                quantity = int(input("\nEnter the quantity of the product you want to sell : "))
                if quantity < 1 or quantity > max_quantity:
                    print("\n--------------------------------------------!!!!----------------------------------------------\n")
                    print("Sorry!! That much quantity of this item is not available right now.\n")
                    print(" --------------------------------------------!!!!----------------------------------------------\n")    
                else:
                    break
        except ValueError:
            print("\n--------------------------------------------!!!!----------------------------------------------\n")
            print("Quantity can only be numbers!!.\n")
            print("--------------------------------------------!!!!----------------------------------------------\n")
    again2 = input("\nDo you want to sell more items to this customer (Y/N) ")   
    if again2.lower == 'y':
        item()
    else:
        False
        again()
    return quantity 


def customer_bill(dict,sn,quantity,customer,unique):
    item = dict[sn-1]
    product = item[0]
    brand = item[1]
    price = int(item[2])-(int(item[2])*0.2)
    cpu = item[4]
    gpu = item[5]
    S_No = "S.No"
    Br = "Brand"
    Pr = "Product"
    R = "Rate"
    Qu = "Quantity"
    CPU = "Processor"
    GPU = "Graphics Card"
    num = 1
    Am = int(price) * int(quantity)
    total = Am
    shipping = 100
    nett_total = int(Am) + shipping
    print(110*'-'+'\n')
    print('\t\t\t\t\tWELCOME TO TRiCKLE STORE\n')
    print('\tMode of Payment: Cash')
    print('Customer Name: '+customer,(50-len(customer))*' ','Date and Time: '+ unique)
    print('  -------------------------------------------------------------------------------------------------------------')
    print('      ',S_No,3*' ',Pr,6*' ',Br,8*' ',R,5*' ',Qu,4*' ',CPU,3*' ',GPU,'   Amount')
    print('  -------------------------------------------------------------------------------------------------------------')
    print('       ',end='')
    print(num,(8-len(str(num)))*' ',end="")
    print(product,(14-len(str(product)))*' ',end="")
    print(brand,(14-len(str(brand)))*' ',end="")
    print(price,(13-len(str(price)))*' ',end="")
    print(quantity,(10-len(str(quantity)))*' ',end="")
    print(cpu,(13-len(cpu))*' ',end="")
    print(gpu,(16-len(gpu))*' ',end="")
    print(Am)
    print('\n')
    print('  -------------------------------------------------------------------------------------------------------------')
    print('\t\t\t\t\t\t\t\t\t\t       ','Total Amount: ',total,'\n','\t\t\t\t\t\t\t\t\t             ','Shipping Price: ',shipping)
    print('  -------------------------------------------------------------------------------------------------------------')
    print('\t\t\t\t\t\t\t\t\t\t         ','Nett Total: ', nett_total)
    print('  -------------------------------------------------------------------------------------------------------------')
