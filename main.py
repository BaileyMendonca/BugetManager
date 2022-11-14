import PySimpleGUI as sg


def income_Window(tabName): 
    Deposit_Layout = [
        [sg.Input(key= "-IN-")], 
        [sg.Button("Confirm")], 
        [sg.Button("Go Back")],
    ]
    mainIncomelayout = [ 
        [sg.Text(tabName + " Income window")], 
        [sg.Button("Deposit")],
        [sg.Button("Transfer")],
        [sg.Button("Close")],
    ]
    window = sg.Window("Income Window", mainIncomelayout, modal=True )
    while True: 
        event, values = window.read()
        if event == sg.WINDOW_CLOSED: 
            break
        if event == "Close": 
            break
    window.close()
        

def savings_Window(): 
    print('yo')

def expense_Window(): 
    print('yo')

def settings_Window(): 
    print('yo')

Income_Layout = [
    [sg.Button("Side Hustle")],
    [sg.Button("Twitch")],  
    [sg.Button("Salary")],   
]

Savings_Layout = [
    [sg.Button("Stocks")], 
    [sg.Button("Crypto")], 
    [sg.Button("Side Hustle")],
    [sg.Button("Spender Account")],
    [sg.Button("Everyday Saver")],
    [sg.Button("Car Savings")],
    [sg.Button("House Savings")],
    [sg.Button("Travel Savings")],

]

Expense_Layout = [
    [sg.Button("Travel")], 
    [sg.Button("Entertainment")], 
    [sg.Button("Food")],
    [sg.Button("Gaming")],  
    [sg.Button("Misc")],
    [sg.Button("Health")],
]

layout = [
    [
    [sg.Text('Welcome to Simple Budget')],
    [Income_Layout],
    sg.HSeparator(),
    [Savings_Layout],
    sg.HSeparator(),
    [Expense_Layout],
    sg.HSeparator(),
    sg.Button("Exit"), 
    ]
]

window = sg.Window("Budget Tracker", layout, size=(1100,600))

while True: 
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED: 
        break

    if event == "Side Hustle": 
        income_Window("Side Hustle")

window.close()