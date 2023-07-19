# billing GUI
import PySimpleGUI as gui
# BASIC WORKING?  ILL INPUT (PRODUCT) ID AND QUANTIT
import tabulate as t
def billing_table():
    data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
    table = []
    head=['ID','Product Name','Quantity','price']
    a = 'y'
    while a == "y" or a == "Y":
        i = int(input("Enter the Product ID:"))
        q = int(input("Enter the Quantity:")) 
        a = input("Do you want to continue? Press y to continue and n to stop")
        table.append([i,data[i][0],q,data[i][2]])
    print(t.tabulate(table,head))
billing_table()
#.append([data[i][0]]).append([q]).append([data[i][2]])

# GUI
def gui_table():
    headings
