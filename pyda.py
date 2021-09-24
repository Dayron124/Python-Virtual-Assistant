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
layout = [[sg.Text('Enter a question.'), [sg.Input()]], [
    sg.Button('Ok'), sg.Button('Cancel')]]
[sg.Button('Submit, visible=False, bind_return_key=True')]
window = sg.Window('Python Virtual Assistant', layout)

# Event Loop to process "events" and get the "values" of the inputs
engine = pyttsx3.init()
engine.setProperty('volume', 0.5)
while True:
    event, values = window.read()

    if event in (None, 'Cancel'):  # if user closes window or clicks cancel
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Results: \n"+wolfram_res,
                            "Wikipedia Results: \n"+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)
    engine.runAndWait()

    print(values[0])


window.close()
