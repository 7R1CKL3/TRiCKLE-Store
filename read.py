from operation import *


def dict():
    with open("stock.txt","r") as file:
        stock_dict = {}
        line_dict = 0
        for line in file:
            line = line.replace("\n","")
            value = line.split(",")
            stock_dict.update({line_dict:value})
            #print(value)
            line_dict = line_dict + 1
    return stock_dict,line_dict


    
def inventory():
    S_No = "S.No"
    Br = "Brand"
    Pr = "Product"
    R = "Rate"
    Qu = "Quantity"
    CPU = "Processor"
    GPU = "Graphics Card"
    print('  -------------------------------------------------------------------------------------------------------------')
    print('      ',S_No,3*' ',Pr,7*' ',Br,9*' ',R,7*' ',Qu,9*' ',CPU,3*' ',GPU)
    print('  -------------------------------------------------------------------------------------------------------------')
    file = open("stock.txt","r")
    
    i_d = 1
    print('       ',end='')     #for managing Spacing for 1st line products
    for line in file:
        doc = line.split(",")
        print(i_d,end="\t")
        for data in doc:
            print(data,(15-len(data))*' ',end="")
        
        i_d = i_d + 1
    file.close()
    print('\n  -------------------------------------------------------------------------------------------------------------')           

