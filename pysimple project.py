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
    #layout FOR up SIDE
    layout0 = [[gui.Button("Get Information", size = (10,1))],  [gui.Button("List all Items", size = (10,1))], [gui.Button("Make BILL", size = (10,1))], [gui.Button("Admin Login", size = (10,1))], [gui.Button("Exit", size = (10,1))]
        ]
    #layout FOR down SIdE
    layout1 = [[gui.Text("You Have Chosen", key = "dtop0"), gui.Text(" ", key = "dtop")]
        ]


    layout2 = [[gui.Text("You Have Chosen", key = "dtop0"), gui.Text(" ", key = "dtop")],
        ]


    layout3 = [[gui.Text("You Have Chosen", key = "dtop0"), gui.Text(" ", key = "dtop")],
               [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False)],
               [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False)],
               [gui.Button("Add")],
               [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
               [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
               [gui.Exit()] 
        ]


    layout4 = [[gui.Text("You Have Chosen", key = "dtop0"), gui.Text(" ", key = "dtop")],
        ]


    #final layout PROBLEM POSSIBLE SOLUTION
                 #CREATE LAYOUT FOR EACH TASK IE MAKE BILL, ADMIN LOGIN STICK UPDATION
                 #NOW IN LAYOUT SET THE layout1 AS True AND OTHER ALL AS False (IMP: expand_x = true)

    #layout = [  [gui.Column(layout0, k='layout0', expand_x=True)], 
     #       [gui.pin(gui.Column( layout1, k=' layout1', visible=False, expand_x=True), expand_x=True)], 
      #      [gui.pin(gui.Column( layout2, k=' layout2', visible=False, expand_x=True), expand_x=True)], 
       #     [gui.pin(gui.Column(layout_acai, k='layout_acai', visible=False, expand_x=True), expand_x=True)], 
        #    [gui.pin(gui.Column(layout_bebida, k='layout_bebida', visible=False, expand_x=True), expand_x=True)]
#]
    layout = [  [gui.Column(layout0, k='layout0', expand_x=True, justification = "centre")], 
            [gui.pin(gui.Column( layout1, k=' layout1', visible=False, expand_x=True), expand_x=True)], 
            [gui.pin(gui.Column( layout2, k=' layout2', visible=False, expand_x=True), expand_x=True)], 
            [gui.pin(gui.Column(layout3, k='layout3', visible=False, expand_x=True), expand_x=True)], 
            [gui.pin(gui.Column(layout4, k='layout4', visible=False, expand_x=True), expand_x=True)]
]    

    window = gui.Window("PROMPT", layout,  size=(715,715))

    while True:
        event, values = window.read()

        if event == "Make BILL":
            sb = "Make BILL"
            window["dtop"].update(sb)
            window["layout3"].update(visible=True)

            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            try:
                price1 = int(values["QTY"]) * int(data[int(values["ID"])][2])
            except ValueError:
                pass
                
            
            try:
                infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price1])
            except ValueError:
                pass


            
            window["tablebill"].update(values = infotable)
            price2.append(price1)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)
                    

           

        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()
gui_prompt()


# WORKING!!!

#MAIN THINGS
price2 = []
infotable = []
head = ['ID','Product Name','Quantity','Price']
price1 = 0



import PySimpleGUI as gui
def gui_prompt():
    
    gui.theme("DarkAmber")
    
    #LAYOUT(S) AS PER REQUIREMENT
    layout1 = [
        ]


    layout2 = [
        ]


    layout3 = [
               [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False)],
               [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False)],
               [gui.Button("Add")],
               [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
               [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
               [gui.Exit()] 
        ]


    layout4 = [
        ]
    
    #FINAL LAYOUT
    layout = [  [gui.TabGroup([[gui.Tab("Get information", layout1),
                                gui.Tab("admin", layout2),
                                gui.Tab("Make BILL", layout3),
                                gui.Tab("Stock OPADAtION", layout4)]])
        ]
]    

    window = gui.Window("General Mavika Store", layout)

    while True:
        event, values = window.read()

        
        if event == "Add":
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
            price1 = int(float(values["QTY"]))*int(float(data[int(values["ID"])][2]))
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price1])
            price2.append(price1)
            window["tablebill"].update(values = infotable)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)

        #MORE if if STATEMENTS AS REQUIRE HOPEFULLY
        
        
        if event == "Exit" or event == gui.WIN_CLOSED:
            break

    window.close()
gui_prompt()

#gui_prompt()
def gui_prompt2():
    #MAIN THINGS

    #from PIL import Image
    data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
    supdation = ['Add', 'Update', 'Delete']
    price2 = []
    infotable = []
    head = ['ID','Product Name','Quantity','Price']
    price1 = 0
    
    gui.theme("DarkAmber")

    # DIFFERENT LAYOUTS
    
    #MAIN MENU
    layout0 = [ [gui.Text("!!Welcome To Mavika store!!", size = (20, 1), font = ("Cooper Black", 20), expand_x = True, justification = "centre")],
                [gui.Image(filename = "cat.png", size = (150, 220),  expand_x = True, expand_y = True)],
                [gui.Button("Get Information"), gui.Button("List all Items"), gui.Button("Make BILL"), gui.Button("Admin Login"), gui.Button("Exit")]
        ]


    #GET INFORMATION 
    layout1 = [ [gui.Text("Welcome to Get Information", expand_x = "True", justification = "centre")],
                [gui.Text("Enter Item ID", size = (12,1)), gui.Input(key = "ITEMID", do_not_clear = False)],
                [gui.Text("Enter Item Name", size = (12,1)), gui.Input(key = "ITEMNAME", do_not_clear = False)],
                [gui.Button("Search"),
                [gui.Table(values =  data, headings = head, key = "infotable", justification = "centre")],
                [gui.Button("Back", key = "back_getinfo")]
        ]

   
    #ADMIN LOGIN
    layout2 = [ [gui.Text("Welcome to Admin Login", expand_x = "True", justification = "centre")],
                [gui.Text("Enter Name", size = (12,1)), gui.Input(key = "NAME", do_not_clear = False)],
                [gui.Text("Enter Password", size = (12,1)), gui.Input(key = "PASSWORD", do_not_clear = False)],
                [gui.Button("Enter"), gui.Button("Back", key = "back_login")]
        ]

   
    #UNDER ADMIN LOGIN - "STOCK UPDATION"
    layout21 = [ [gui.Text("Welcome to Stock Updation", expand_x = "True", justification = "centre")],
                 [gui.Text("Select your Choice")],[gui.Listbox(supdation, key = "stockupdation"],
                 [gui.Button("Back", key = "back_stock")]
        ]

  
    #MAKE BILL
    layout3 = [ [gui.Text("Welcome to Bill", expand_x = "True", justification = "centre")],
                [gui.Text("Enter ID", size = (10,1)), gui.Input(key = "ID", do_not_clear = False, justification = "left")],
                [gui.Text("Enter Quantity", size = (10,1)), gui.Input(key = "QTY", do_not_clear = False, justification = "left")],
                [gui.Button("Add")],
                [gui.Table(values =  infotable, headings = head, key = "tablebill", justification = "centre")],
                [gui.Text("Total Price:", size = (10,1)), gui.Text(" ", size = (10,1), key = "p")],
                [gui.Button("Back", key = "back_bill")] 
        ]      

    #LIST ALL ITEMS 
    layout4 = [ [gui.Text("Welcome to All Items", expand_x = "True", justification = "centre")],
                [gui.Table(values =  data, headings = head, key = "listbill", justification = "centre")],
                [gui.Button("Back", key = "back_allitems")]
        ]

    #MAIN LAYOUT
    layout = [ [gui.Column(layout0, key = "l0"),
                gui.Column(layout1, key = "l1", visible = False),
                gui.Column(layout2, key = "l2", visible = False),
                gui.Column(layout21, key = "l21", visible = False),
                gui.Column(layout3, key = "l3", visible = False),
                gui.Column(layout4, key = "l4", visible = False)]
        ]

    # WINDOW
    window = gui.Window("Mavika Store", layout, resizable = True)


    #while-event loop
    while True:
        event, values = window.read()

        if event in (gui.WIN_CLOSED, "Exit"):
            break
       
        #*Get Info* starts
        if event == "Get Information":
            window["l1"].update(visible = True)
            window["l0"].update(visible = False)


        if event == "Search" and values["ITEMID"] == '' and values["ITEMNAME"] == '':
            gui.Popup("Please Enter ID and NAME")


        if event == "Search" and values["ITEMID"] != '' and values["ITEMNAME"] != '':
            # mathew's code from make bILL
            


        if event == "back_getinfo":
            window["l0"].update(visible = True)
            window["l1"].update(visible = False)

        
        #*Get Info* ends



        # *Admin* start
        if event == "Admin Login":
            window["l2"].update(visible = True)
            window["l0"].update(visible = False)
        if event == "back_login":
            window["l0"].update(visible = True)
            window["l2"].update(visible = False)

        if event == "Enter":
            name = ["vinay", "kalpit", "mathew"]
            password = ["ayo", "akhila123", "yo"]
            if values["NAME"] in name and values["PASSWORD"] in password:
                window["l21"].update(visible = True)
                window["l2"].update(visible = False)
                #stock updation
            else:
                gui.Popup("YOU'RE NOT AUTHORISED PERSONNEl!!!")

        


        if event == "back_stock":
            window["l0"].update(visible = True)
            window["l21"].update(visible = False)
        # *Admin* end



        # *Bill*
        if event == "Make BILL":
            window["l3"].update(visible = True)
            window["l0"].update(visible = False)

        if event == "back_bill":
             window["l0"].update(visible = True)
             window["l3"].update(visible = False)

             
        if event == "Add" and values["ID"] == '' and values["QTY"] == '':
            gui.Popup("Please Enter ID and QUANTITY")


        if event == "Add" and values["ID"] != '' and values["QTY"] != '':

            
            data = [['banana',20,5],['bottles',200,4],['blah',10000,6]]
                
            price1 = int(float(values["QTY"]))*int(float(data[int(values["ID"])][2]))
            infotable.append([values["ID"], data[int(values["ID"])][0],values["QTY"],price1])
            price2.append(price1)
            window["tablebill"].update(values = infotable)
            price = 0
            for i in price2:
                price+=i
            window["p"].update(price)
        #^Bill^ end


        #*Items*starts
        if event == "List all Items":
            window["l4"].update(visible = True)
            window["l0"].update(visible = False)

            #sql backend code?
            
        if event == "back_allitems":
             window["l0"].update(visible = True)
             window["l4"].update(visible = False)
        #*Items*starts
    window.close()
gui_prompt2()

