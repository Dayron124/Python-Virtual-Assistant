# app_id LRE6ER-4ELW4AL7R2
# app_name pyda.py

from tkinter.constants import FALSE
import wolframalpha
import wikipedia
import PySimpleGUI as sg

client = wolframalpha.Client("LRE6ER-4ELW4AL7R2")


sg.theme('Dark2')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter a question'), sg.InputText()], [
    sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Python Virtual Assistant', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
    except:
        res = client.query(values[0])
        wolfram_res = next(res.results).text
    print(values[0])
    sg.Popup(wiki_res)  

window.close()
