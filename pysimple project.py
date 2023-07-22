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
        [gui.Button("Show BILL"), gui.Button("CANCEL")]]
    window = gui.Window("KINDLY ENTER", layout)
    while True:
        event, values = window.read()
        if event == "CANCEL" or event == gui.WIN_CLOSED:
            break
        else:
            infotable = []
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],data[int(values["ID"])][1]])
            gui.theme("DarkAmber")
            head = ['ID','Product Name','Quantity','Price']
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
    window.close()
#GUI for prompt
def gui_prompt():
    #GUI PROMPT WITH vseparator()

    gui.theme("DarkAmber")
    #layout FOR LEFT SIDE
    layout1 = [[gui.Button("Get Information", size = (10,1))],
              [gui.Button("List all Items", size = (10,1))],
              [gui.Button("Make BILL", size = (10,1))],
              [gui.Button("Admin Login", size = (10,1))],
              [gui.Button("Exit", size = (10,1))]
        ]
    #layout FOR RIGHT SIdE
    layout2 = [[gui.Text("You Have Chosen", key = "dtop0"), gui.Text(" ", key = "dtop")],
               [gui.In(size = (70, 30), key = "display")]
        ]

    #final layout PROBLEM POSSIBLE SOLUTION
                 #CREATE LAYOUT FOR EACH TASK IE MAKE BILL, ADMIN LOGIN STICK UPDATION
                 #NOW IN LAYOUT SET THE layout1 AS True AND OTHER ALL AS False (IMP: 1 event_= Ttue 2 Invisible = True 3 expand_x = true)
       #layout = [  [sg.Column(layout_principal, k='layout_principal', expand_x=True)], 
     #       [sg.pin(sg.Column(layout_suco, k='layout_suco', visible=False, expand_x=True), expand_x=True)], 
      #      [sg.pin(sg.Column(layout_lanche, k='layout_lanche', visible=False, expand_x=True), expand_x=True)], 
       #     [sg.pin(sg.Column(layout_acai, k='layout_acai', visible=False, expand_x=True), expand_x=True)], 
        #    [sg.pin(sg.Column(layout_bebida, k='layout_bebida', visible=False, expand_x=True), expand_x=True)]
#]
    layout = [[gui.Column(layout1),
               gui.VSeparator(),
               gui.Column(layout2)]
        ]

    window = gui.Window("PROMPT", layout)

    while True:
        event, values = window.read()

        if event == "Make BILL":
            sb = "Make BILL"
            window["dtop"].update(sb)

            
            p = gui_table()
            window[f"display"].p

        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()
gui_prompt()
