import PySimpleGUI as sg
import math


savingsAccounts = ['Cash', 'Stocks', 'Crypto', 'Spender Account', 'Everyday Saver', 'Car Savings', 'House Savings', 'Travel Savings']
expensesAccounts = ['Travel', 'Entertainment', 'Food', 'Gaming', 'Misc', 'Health']
incomeAccounts = ['Side Hustle', 'Twitch', 'Salary']

accounts_balance = {
    f'{account}' : 0.00 for account in incomeAccounts + expensesAccounts + savingsAccounts
}

def income_Window(tabName, amount):  
    roundedNumber = round(accounts_balance[tabName], 2)
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
    window = sg.Window("Income Window", layout, modal=True)
    while True: 
        event, values = window.read()
        if event == sg.WINDOW_CLOSED: 
            break
        if event == "Close": 
            break
        if event == "Transfer":
            if float(values[0]) < 0: 
                sg.popup_error('Bad input')
                window.close()
                continue
            accounts_balance[tabName] = accounts_balance[tabName] + float(values[0])
            accounts_balance[values['Account ingoing']] = accounts_balance[values['Account ingoing']] + float(values[0])
            window.close()
    window.close()
        

def savings_Window(tabName, amount):
    roundedNumber = round(accounts_balance[tabName], 2)
    outGoing_layout = [ 
        [sg.Text("Please enter money outgoing"), sg.InputText()],
        [sg.OptionMenu(values=expensesAccounts + savingsAccounts, key='Account ingoing')],
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
            if float(values[0]) < 0: 
                sg.popup_error('Bad input')
                window.close()
                continue
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

    window = sg.Window("Expense Window", layout, modal=True,grab_anywhere=True  )
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
    [sg.Button(f"{account}") for account in incomeAccounts]]
    
Savings_Layout = [
    [sg.Button(f"{account}") for account in savingsAccounts]]

Expense_Layout = [
    [sg.Button(f"{account}") for account in expensesAccounts]]

layout = [
    [
    [sg.Text('Welcome to Simple Budget', justification='center')],
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

    for iAccount in incomeAccounts: 
        if event == iAccount: 
            income_Window(iAccount, accounts_balance[iAccount])
    for sAccount in savingsAccounts: 
        if event == sAccount: 
            savings_Window(sAccount, accounts_balance[sAccount])
    for eAccount in expensesAccounts: 
        if event == eAccount: 
            income_Window(eAccount, accounts_balance[eAccount])
window.close()