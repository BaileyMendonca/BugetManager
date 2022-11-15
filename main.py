import PySimpleGUI as sg
import math


accounts_balance = {
    'Side Hustle' : 23.40,
    'Twitch' : 8.90,
    'Salary' : 263.40,
    'Stocks' : 0.00,
    'Crypto' : 0.00,
    'Spender Account' : 0.00,
    'Everyday Saver' : 0.00,
    'Car Savings' : 0.00,
    'House Savings' : 0.00,
    'Travel Savings' : 0.00,
    'Travel' : 0.00,
    'Entertainment' : 0.00,
    'Food' : 0.00,
    'Gaming' : 0.00,
    'Misc' : 0.00,
    'Health' : 0.00,
}

savingsAccounts = ['Stocks', 'Crypto', 'Spender Account', 'Everyday Saver', 'Car Savings', 'House Savings', 'Travel Savings']
expensesAccounts = ['Travel', 'Entertainment', 'Food', 'Gaming', 'Misc', 'Health']
incomeAccounts = ['Side Hustle', 'Twitch', 'Salary']

def income_Window(tabName, amount):  
    roundedNumber = round(accounts_balance[tabName], 3)
    outGoing_layout = [ 
        [sg.Text("Please enter money outgoing"), sg.InputText()],
        [sg.OptionMenu(values=savingsAccounts, key='Account ingoing')],
    ]
    button_layout = [ 
        [sg.Button("Transfer")],
        [sg.Button("Close")],
    ]
    layout = [ 
        [sg.Text(tabName + " Income window")],
        [sg.Text("You currently have made: $" + str(roundedNumber) + " through this revune")],
        [outGoing_layout],
        [button_layout], 

    ] 
    window = sg.Window("Income Window", layout, modal=True )
    while True: 
        event, values = window.read()
        if event == sg.WINDOW_CLOSED: 
            break
        if event == "Close": 
            break
        if event == "Transfer":
            accounts_balance[tabName] = accounts_balance[tabName] + float(values[0])
            accounts_balance[values['Account ingoing']] = accounts_balance[values['Account ingoing']] + float(values[0])
            window.close()
    window.close()
        

def savings_Window(tabName, amount):
    roundedNumber = round(accounts_balance[tabName], 3)
    outGoing_layout = [ 
        [sg.Text("Please enter money outgoing"), sg.InputText()],
        [sg.OptionMenu(values=expensesAccounts, key='Account ingoing')],
    ]
    button_layout = [ 
        [sg.Button("Transfer")],
        [sg.Button("Close")],
    ]
    layout = [ 
        [sg.Text(tabName + " Income window")],
        [sg.Text("You currently have: $" + str(roundedNumber))],
        [outGoing_layout],
        [button_layout], 

    ] 
    window = sg.Window("Income Window", layout, modal=True )
    while True: 
        event, values = window.read()
        if event == sg.WINDOW_CLOSED: 
            break
        if event == "Close": 
            break
        if event == "Transfer":
            accounts_balance[tabName] = accounts_balance[tabName] - float(values[0])
            accounts_balance[values['Account ingoing']] = accounts_balance[values['Account ingoing']] + float(values[0])
            window.close()
    window.close()

def expense_Window(tabName, amount): 
    roundedNumber = round(accounts_balance[tabName], 2)
    layout = [ 
        [sg.Text(tabName + " Income window")],
        [sg.Text("You currently have spent: $" + str(roundedNumber) + " this month")], 
        [sg.Button("Close")],
    ]

    window = sg.Window("Expense Window", layout, modal=True )
    while True: 
        event, values = window.read()
        if event == sg.WINDOW_CLOSED: 
            break
        if event == "Close": 
            break
    window.close()

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
        income_Window("Side Hustle", accounts_balance["Side Hustle"])
    if event == "Salary": 
        income_Window(event, accounts_balance[event])
    if event == "Twitch": 
        income_Window(event, accounts_balance[event])
    if event == "Stock": 
        savings_Window(event, accounts_balance[event])
    if event == "Crypto": 
        savings_Window(event, accounts_balance[event])
    if event == "Spender Account": 
        savings_Window(event, accounts_balance[event])
    if event == "Everyday Saver": 
        savings_Window(event, accounts_balance[event])
    if event == "Car Savings": 
        savings_Window(event, accounts_balance[event])
    if event == "House Savings": 
        savings_Window(event, accounts_balance[event])
    if event == "Travel Savings": 
        savings_Window(event, accounts_balance[event])
    if event == "Travel": 
        expense_Window(event, accounts_balance[event])
    if event == "Entertainment": 
        expense_Window(event, accounts_balance[event])
    if event == "Food": 
        expense_Window(event, accounts_balance[event])
    if event == "Gaming": 
        expense_Window(event, accounts_balance[event])
    if event == "Misc": 
        expense_Window(event, accounts_balance[event])
    if event == "Health": 
        expense_Window(event, accounts_balance[event])

window.close()