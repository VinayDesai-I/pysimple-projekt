# billing GUI
import PySimpleGUI as gui
# BASIC WORKING?  ILL INPUT (PRODUCT) ID AND QUANTIT
import tabulate as t
def billing_table():
    data = [['banana','20','5'],['bottles','200','50'],['blah','10000','6']]
    a = "y"
    table = []
    while a == "y" or a == "Y":
        i = int(input("Enter the Product ID:"))
        q = int(input("Enter the Quantity:")) 
        a = input("Do you want to continue? Press y to continue and n to stop")
        table = table.append(data[i])
        table = table.append(q)
    print(t(table))
print(billing_table())
