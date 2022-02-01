from PIL import Image, ImageDraw
import PySimpleGUI as sg
import os
import tkinter
import io

def draw_school():
    #from lab's example
    img = Image.open("BUschool.jpg")
    img.thumbnail((1200, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    layout = [[[sg.Text("School:", font= ("Arial", 25))], 
    [sg.Image(Data=bio.getvalue())]],
    [sg.Button("Don't Show Me Anymore")]]

    window = sg.Window("Image", layout, size=(1200, 800))

    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break

    window.close()
    return
