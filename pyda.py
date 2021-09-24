# app_id LRE6ER-4ELW4AL7R2
# app_name pyda.py

import pyttsx3
from tkinter.constants import FALSE
import wolframalpha
import wikipedia
import PySimpleGUI as sg

# wolfram accessing api
client = wolframalpha.Client("LRE6ER-4ELW4AL7R2")


sg.theme('Dark2')   # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Enter a question.' '\nBe as specific as possible'), sg.InputText()], [
    sg.Button('Ok'), sg.Button('Cancel')]]
window = sg.Window('Python Virtual Assistant', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    res = client.query(values[0])
    wolfram_res = next(res.results).text
    wiki_res = wikipedia.summary(values[0], sentences=2)
    engine = pyttsx3.init()
    sg.Popup("Wolfram Results: \n"+wolfram_res,
             "Wikipedia Results: \n"+wiki_res)
    engine.say(wolfram_res)
    engine.say(wiki_res)
    engine.runAndWait()

    print(values[0])


window.close()
