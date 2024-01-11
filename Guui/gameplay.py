import PySimpleGUI as sg
from PIL import Image, ImageTk
import os

def rotate_and_resize_image(image_path, rotation_angle, size):
    original_image = Image.open(image_path)
    rotated_image = original_image.rotate(rotation_angle)
    resized_image = rotated_image.resize(size)
    return ImageTk.PhotoImage(resized_image)

sample_image = Image.open("karty\C2.png")

rotation_angle = 90
image_size = (15,100)

layout = [
    [sg.Image(key="-IMAGE-", size=image_size)]
]

window = sg.Window("Image Display", layout, resizable=True)

image = rotate_and_resize_image(sample_image, rotation_angle, image_size)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break

window.close