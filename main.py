import PySimpleGUI as sg
import math
import pickle
 
class Accounts():
    def __init__(self):
        self.income = ['Side Hustle', 'Twitch', 'Salary']
        self.savings = ['Cash', 'Stocks', 'Crypto', 'Spender Account', 'Everyday Saver', 'Car Savings', 'House Savings', 'Travel Savings']
        self.expenses = ['Travel', 'Entertainment', 'Food', 'Gaming', 'Misc', 'Health']
        self.accounts = {f'{account}' : 0.00 for account in self.income + self.expenses + self.savings}
        
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 

def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)

obj = load_object("data.pickle")
 
#print(obj.income)
#print(isinstance(obj, MyClass))


savingsAccounts = obj.savings
expensesAccounts = obj.expenses
incomeAccounts = obj.income

accounts_balance = obj.accounts
    #f'{account}' : 0.00 for account in incomeAccounts + expensesAccounts + savingsAccounts


def income_Window(tabName, amount):  
    roundedNumber = round(obj.accounts[tabName], 2)
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
            #accounts_balance[tabName] = accounts_balance[tabName] + float(values[0])
            #accounts_balance[values['Account ingoing']] = accounts_balance[values['Account ingoing']] + float(values[0])
            obj.accounts[tabName] = obj.accounts[tabName] + float(values[0])
            obj.accounts[values['Account ingoing']] = obj.accounts[values['Account ingoing']] + float(values[0])
            save_object(obj)
            window.close()
    window.close()
        

def savings_Window(tabName, amount):
    roundedNumber = round(obj.accounts[tabName], 2)
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
            obj.accounts[tabName] = obj.accounts[tabName] - float(values[0])
            obj.accounts[values['Account ingoing']] = obj.accounts[values['Account ingoing']] + float(values[0])
            save_object(obj)
            window.close()
    window.close()

def expense_Window(tabName, amount): 
    roundedNumber = round(obj.accounts[tabName], 2)
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
    layout = [ 
        [sg.Text("Resetting the values will require a application restart")],
        [sg.Button("Reset Values")],
    ]
    window = sg.Window("Settings Window", layout, modal=True,grab_anywhere=True)
    while True: 
        event, values = window.read()
        if event == "Reset Values": 
            obj = Accounts()
            save_object(obj)
            window.close()
            window_main.close()
            break
        if event == sg.WINDOW_CLOSED: 
            break
        if event == "Close": 
            break
    window.close()

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
    sg.Button("Settings"), 
    ]
]

window_main = sg.Window("Budget Tracker", layout, size=(1100,600))

while True: 
    window_main.refresh()
    event, values = window_main.read(timeout=10)
    if event == "Exit" or event == sg.WIN_CLOSED: 
        break
    if event == "Settings": 
        settings_Window()
    for iAccount in incomeAccounts: 
        if event == iAccount: 
            income_Window(iAccount, accounts_balance[iAccount])
    for sAccount in savingsAccounts: 
        if event == sAccount: 
            savings_Window(sAccount, accounts_balance[sAccount])
    for eAccount in expensesAccounts: 
        if event == eAccount: 
            expense_Window(eAccount, accounts_balance[eAccount])
window_main.close()