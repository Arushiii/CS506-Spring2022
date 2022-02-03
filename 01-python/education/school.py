import PySimpleGUI as sg
import os
import tkinter
import io
import os
from PIL import Image, ImageDraw
def draw_school():
    #from lab's example
    print(os.getcwd())
    img = Image.open(os.getcwd() + "\\BUschool.jpg")
    img.thumbnail((1200, 800))
    bio = io.BytesIO()
    img.save(bio, format="PNG")

    layout = [[[sg.Text("School:", font= ("Arial", 25))], 
    [sg.Image(data=bio.getvalue())]],
    [sg.Button("Don't Show Me Anymore")]]

    window = sg.Window("Image", layout, size=(1200, 800))
#closing the window:
    while True:
        event, values = window.read()
        if event == "Don't Show Me Anymore" or event == sg.WIN_CLOSED:
            break
#draw_school()

#Nathan Vollertsen, zhitao gan, Jason Chow, Peng Huang, Ji Zhao