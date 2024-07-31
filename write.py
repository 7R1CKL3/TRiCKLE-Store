def distributor_file(dict,ser,qua):
    with open('stock.txt','w') as file:
        line_dict = 1
        dict[ser-1][3] = int(dict[int(ser-1)][3])+int(qua)
        for values in dict.values():
            file.write(str(values[0])+','+str(values[1])+','+str(values[2])+','+str(values[3])+','+str(values[4])+','+str(values[5]))
            file.write('\n')
            #print(values)
            
            
def distributor_bill_print(dict,sn,quantity,distributor,unique):
    filename = distributor + unique + '.txt'
    file_name = filename.replace(':','')
    with open(file_name,'w') as file:
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
        file.write(110*'-'+'\n')
        file.write('\t\t\t\t\tWELCOME TO TRiCKLE STORE\n')
        file.write('\tMode of Payment: Checque\n')
        file.write(f"{' Distributor Name: '+distributor,(50-len(distributor))*' '+'Date and Time: '+ unique}")
        
        file.write('  \n-------------------------------------------------------------------------------------------------------------\n')
    
        file.write(f"{'      '+S_No+5*' '+Pr+7*' '+Br+9*' '+R+7*' '+Qu+4*' '+CPU+4*' '+GPU+'   Amount'}")
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------')
        file.write('\n       ')
        file.write(f"{num}{(8-len(str(num)))*' '}")
        file.write(f"{product}{(14-len(str(product)))*' '}")
        file.write(f"{brand}{(14-len(str(brand)))*' '}")
        file.write(f"{price}{(13-len(str(price)))*' '}")
        file.write(f"{quantity}{(10-len(str(quantity)))*' '}")
        file.write(f"{cpu}{(13-len(cpu))*' '}")
        file.write(f"{gpu}{(16-len(gpu))*' '}")
        file.write(f"{Am}")
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------\n')
        file.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t      '+'Total Amount: '+str(total)+'\n'+'\t\t\t\t\t\t\t\t\t\t\t\t\t\t       '+'Vat Amount (13%): '+str(vat_am))
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------')
        file.write('\n')
        file.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t        '+'Nett Total: '+str(nett_total))
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------')
        

def customer_file(dict,ser,qua):
    with open('stock.txt','w') as file:
        line_dict = 1
        dict[ser-1][3] = int(dict[int(ser-1)][3]) - int(qua)
        for values in dict.values():
            file.write(str(values[0])+','+str(values[1])+','+str(values[2])+','+str(values[3])+','+str(values[4])+','+str(values[5]))
            file.write('\n')

def customer_bill_print(dictionary,sn,quantity,distributor,unique):
    filename = distributor + unique + '.txt'
    file_name = filename.replace(':','')
    with open(file_name,'w') as file:
        item = dictionary[sn-1]
        product = item[0]
        brand = item[1]
        price = item[2]
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
        file.write(110*'-')
        file.write('\t\t\t\t\tWELCOME TO TRiCKLE STORE\n')
        file.write('\tMode of Payment: Cash\n')
        file.write(f"{'Distributor Name: '+distributor,(50-len(distributor))*' '+'Date and Time: '+ unique}")
        
        file.write('  \n-------------------------------------------------------------------------------------------------------------\n')
    
        file.write(f"{'      '+S_No+5*' '+Pr+7*' '+Br+9*' '+R+7*' '+Qu+4*' '+CPU+4*' '+GPU+'   Amount'}")
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------')
        file.write('\n       ')
        file.write(f"{num}{(8-len(str(num)))*' '}")
        file.write(f"{product}{(14-len(str(product)))*' '}")
        file.write(f"{brand}{(14-len(str(brand)))*' '}")
        file.write(f"{price}{(13-len(str(price)))*' '}")
        file.write(f"{quantity}{(10-len(str(quantity)))*' '}")
        file.write(f"{cpu}{(13-len(cpu))*' '}")
        file.write(f"{gpu}{(16-len(gpu))*' '}")
        file.write(str(Am))
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------\n')
        file.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t      '+'Total Amount: '+str(total)+'\n'+'\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t          '+'Shipping: '+str(shipping))
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------')
        file.write('\n')
        file.write('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t        '+'Nett Total: '+str(nett_total))
        file.write('\n')
        file.write('  -------------------------------------------------------------------------------------------------------------')
        