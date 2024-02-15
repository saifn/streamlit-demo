import PySimpleGUI as sg

# Layout definition
layout = [[sg.Text("Enter your name:")],
          [sg.InputText()],
          [sg.Button("Click me!")],
          [sg.Text("", key="output")]]

# Create the window
window = sg.Window("My Simple Demo App", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Click me!":
        window["output"].update(f"Hello, {values[0]}!")

# Close the window
window.close()
