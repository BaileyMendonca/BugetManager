import PySimpleGUI as sg

layout = [
    [sg.Text("Welcome Bailey to your budget tracker")], 
    [sg.Button("Exit")]
]

window = sg.Window("Budget Tracker", layout)

while True: 
    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED: 
        break

window.close()