# billing GUI
import PySimpleGUI as gui
# BASIC WORKING?  ILL INPUT (PRODUCT) ID AND QUANTIT
import tabulate as t
def billing_table():
    data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
    table = []
    head=['ID','Product Name','Quantity','Price']
    a = 'y'
    while a == "y" or a == "Y":
        i = int(input("Enter the Product ID:"))
        q = int(input("Enter the Quantity:")) 
        a = input("Press y to continue and n to stop:")
        table.append([i,data[i][0],q,data[i][2]])
    print(t.tabulate(table,head))
billing_table()
#.append([data[i][0]]).append([q]).append([data[i][2]])

#form gui not for project
#1 to set a theme
gui.theme("DarkAmber")

#2 to create a layout
layout = [
    [gui.Text("Enter name")],   # 1st row
    [gui.InputText()],           #  (To take input)
    [gui.Button("OKAY"),gui.Button("CANCEL")] # 2nd row (Buttons)
]
# pysimple functions = .theme , .text , .Button , .window , .WIN_CLOSE

#3 to create window
window = gui.Window("Form input",layout)

#4 to create a event loop
while True:
    event,values = window.read()
    if event == "CANCEL" or event == gui.WIN_CLOSED:
        break
    print(values[0])

#5 to close the window
window.close()

# GUI
def gui_table():
    
    #WINDOW TO GET INPUT ID AND QUANTITY
    layout = [gui.Text("Enter ID"), gui.Input(key = "ID")],
        [gui.Text("Enter Quantity"), gui.Input(key = "QTY")],
        [gui.Button("Show BILL"), gui.Button("Exit")]]
    window = gui.Window("KINDLY ENTER", layout)
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == "Exit":
            break
        else:
            infotable = []
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            infotable.append([values["ID"], data[int(values["QTY"])][0],values["QTY"],data[int(values["ID"])][1]])
            gui.theme("AmberDark")
            head = ['ID','Product Name','Quantity','price']
            # DATA IS table
            layout = [
                [gui.Table(values = infotable, headings = head)]
                ]
            window = gui.Window("BILL",layout)
            while True:
                event , values = window.read()
                if event == "Exit" or event == gui.WIN_CLOSED:
                    break
            window.close()
