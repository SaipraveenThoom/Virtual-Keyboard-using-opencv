import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector
from PIL import ImageFont, ImageDraw, Image
import numpy as np
from pynput.keyboard import Controller
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 1280)
cap.set(4, 720)
font = ImageFont.truetype("C:\Windows\Fonts\Vanib", 18)
font2 = ImageFont.truetype("C:\Windows\Fonts\courbd", 14)
font8 = ImageFont.truetype("C:\Windows\Fonts\courbd", 24)
font3 = ImageFont.truetype("C:\Windows\Fonts\Vanib", 9)
font4 = ImageFont.truetype("C:\Windows\Fonts\Vanib", 14)
font6 = ImageFont.truetype("C:\Windows\Fonts\Vanib", 21)
font5 = ImageFont.truetype("C:\Windows\Fonts\Vanib", 28)
font7 = ImageFont.truetype("C:\Windows\Fonts\Vanib", 50)
detector = HandDetector(detectionCon=0.9)

keyboard = Controller()

def alphabets():


    draw.rounded_rectangle((35, 190, 120, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 200), "Tab", font=font2, fill="purple")

    draw.rounded_rectangle((35, 290, 140, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 300), "Shift", font=font2, fill="purple")

    draw.rounded_rectangle((35, 390, 170, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 400), "&౧౨౩", font=font4, fill="purple")

    draw.rounded_rectangle((190, 390, 240, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((200, 400), "Ctrl", font=font2, fill="purple")

    draw.rounded_rectangle((260, 390, 310, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((270, 400), "Win", font=font2, fill="purple")

    draw.rounded_rectangle((330, 390, 380, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((340, 400), "Alt", font=font2, fill="purple")

    draw.rounded_rectangle((400, 390, 770, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((550, 400), "Space", font=font2, fill="purple")

    draw.rounded_rectangle((790, 390, 840, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((805, 400), "Mic", font=font2, fill="purple")

    draw.rounded_rectangle((860, 390, 910, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 400), "\u02c2", font=font2, fill="white")

    draw.rounded_rectangle((930, 390, 980, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((940, 400), "\u02c3", font=font2, fill="white")

    draw.rounded_rectangle((1000, 390, 1050, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 400), "Tel", font=font2, fill="blue")

    draw.rounded_rectangle((35, 90, 85, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 115), "Esc", font=font4)

    draw.rounded_rectangle((105, 90, 155, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((110, 95), "1", font=font2)
    draw.text((125, 95), "ఔ", font=font4)
    draw.text((120, 110), "ౌ", font=font5)

    draw.rounded_rectangle((175, 90, 225, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((180, 95), "2", font=font2)
    draw.text((195, 95), "ఐ", font=font4)
    draw.text((190, 110), "ై", font=font6)

    draw.rounded_rectangle((245, 90, 295, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((250, 95), "3", font=font2)
    draw.text((265, 95), "ఆ", font=font4)
    draw.text((260, 110), "ా", font=font5)

    draw.rounded_rectangle((315, 90, 365, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 95), "4", font=font2)
    draw.text((335, 95), "ఈ", font=font4)
    draw.text((330, 110), "ీ", font=font7)

    draw.rounded_rectangle((385, 90, 435, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((390, 95), "5", font=font2)
    draw.text((405, 95), "ఊ", font=font4)
    draw.text((400, 110), "ూ", font=font5)

    draw.rounded_rectangle((455, 90, 505, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((460, 95), "6", font=font2)
    draw.text((475, 95), "భ", font=font4)
    draw.text((470, 110), "బ", font=font5)

    draw.rounded_rectangle((525, 90, 575, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((530, 95), "7", font=font2)
    draw.text((545, 95), "ఙ", font=font4)
    draw.text((540, 110), "హ", font=font5)

    draw.rounded_rectangle((595, 90, 645, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((600, 95), "8", font=font2)
    draw.text((615, 95), "ఘ", font=font4)
    draw.text((610, 110), "గ", font=font5)

    draw.rounded_rectangle((665, 90, 715, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 95), "9", font=font2)
    draw.text((685, 95), "ధ", font=font4)
    draw.text((680, 110), "ద", font=font5)

    draw.rounded_rectangle((735, 90, 785, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 95), "0", font=font2)
    draw.text((755, 95), "ఝ", font=font4)
    draw.text((750, 110), "జ", font=font5)

    draw.rounded_rectangle((805, 90, 855, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((825, 95), "ఢ", font=font4)
    draw.text((820, 110), "డ", font=font5)

    draw.rounded_rectangle((875, 90, 925, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((895, 95), "ఞ", font=font4)
    draw.text((895, 115), "\u0C55", font=font7)

    draw.rounded_rectangle((945, 90, 1050, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((960, 100), "Backspace", font=font4, fill="purple")

    draw.rounded_rectangle((140, 190, 190, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((160, 195), "ఓ", font=font4)
    draw.text((160, 210), "ో", font=font5)

    draw.rounded_rectangle((210, 190, 260, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((230, 195), "ఏ", font=font4)
    draw.text((230, 210), "ే", font=font5)

    draw.rounded_rectangle((280, 190, 330, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((300, 195), "అ", font=font4)
    draw.text((300, 210), "్", font=font5)

    draw.rounded_rectangle((350, 190, 400, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((370, 195), "ఇ", font=font4)
    draw.text((365, 205), "ి", font=font7)

    draw.rounded_rectangle((420, 190, 470, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((440, 195), "ఉ", font=font4)
    draw.text((435, 205), "ు", font=font5)

    draw.rounded_rectangle((490, 190, 540, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((510, 195), "ఫ", font=font4)
    draw.text((505, 205), "ప", font=font5)

    draw.rounded_rectangle((560, 190, 610, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((580, 195), "ఱ", font=font4)
    draw.text((575, 205), "ర", font=font5)

    draw.rounded_rectangle((630, 190, 680, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((650, 195), "ఖ", font=font4)
    draw.text((650, 205), "క", font=font5)

    draw.rounded_rectangle((700, 190, 750, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((720, 195), "థ", font=font4)
    draw.text((715, 205), "త", font=font5)

    draw.rounded_rectangle((770, 190, 820, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((790, 195), "ఛ", font=font4)
    draw.text((785, 205), "చ", font=font5)

    draw.rounded_rectangle((840, 190, 890, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((860, 195), "ఠ", font=font4)
    draw.text((855, 205), "ట", font=font5)

    draw.rounded_rectangle((910, 190, 960, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((930, 195), "త్ర", font=font4)
    draw.text((925, 205), "\u0C79", font=font5)

    draw.rounded_rectangle((980, 190, 1050, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((995, 200), "Enter", font=font4, fill="purple")

    draw.rounded_rectangle((160, 290, 210, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((180, 295), "ఒ", font=font4)
    draw.text((175, 310), "ొ", font=font5)

    draw.rounded_rectangle((230, 290, 280, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((250, 295), "ఎ", font=font4)
    draw.text((245, 310), "ె", font=font5)

    draw.rounded_rectangle((300, 290, 350, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 295), "ఁ", font=font4)
    draw.text((320, 300), "ం", font=font5)

    draw.rounded_rectangle((370, 290, 420, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((390, 295), "\u0C59", font=font4)
    draw.text((385, 300), "ృ", font=font5)

    draw.rounded_rectangle((440, 290, 490, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((460, 295), "ణ", font=font4)
    draw.text((450, 305), "మ", font=font5)

    draw.rounded_rectangle((510, 290, 560, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((530, 295), "ష", font=font4)
    draw.text((525, 305), "న", font=font5)

    draw.rounded_rectangle((580, 290, 630, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((600, 295), "జ్ఞ", font=font4)
    draw.text((590, 305), "వ", font=font5)

    draw.rounded_rectangle((650, 290, 700, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 295), "ళ", font=font4)
    draw.text((670, 305), "ల", font=font5)

    draw.rounded_rectangle((720, 290, 770, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 295), "శ", font=font4)
    draw.text((740, 305), "స", font=font5)

    draw.rounded_rectangle((790, 290, 840, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((810, 295), "ౘ", font=font4)
    draw.text((800, 305), "య", font=font5)

    draw.rounded_rectangle((860, 290, 910, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 295), "క్ష", font=font4)
    draw.text((880, 305), ",", font=font5)

    draw.rounded_rectangle((930, 290, 980, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((950, 295), "శ్ర", font=font4)
    draw.text((950, 305), ".", font=font5)

    draw.rounded_rectangle((1000, 290, 1050, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 310), "Shift", font=font3, fill="purple")

def symbol2():
    draw.rounded_rectangle((35, 190, 190, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 200), "Tab", font=font2, fill="purple")

    draw.rounded_rectangle((35, 290, 140, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 300), "Shift", font=font2, fill="purple")

    draw.rounded_rectangle((35, 390, 170, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 400), "&౧౨౩", font=font4, fill="purple")

    draw.rounded_rectangle((190, 390, 240, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((200, 400), "Ctrl", font=font2, fill="purple")

    draw.rounded_rectangle((260, 390, 310, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((270, 400), "Win", font=font2, fill="purple")

    draw.rounded_rectangle((330, 390, 380, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((340, 400), "Alt", font=font2, fill="purple")

    draw.rounded_rectangle((400, 390, 770, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((550, 400), "Space", font=font2, fill="purple")

    draw.rounded_rectangle((790, 390, 840, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((805, 400), ".", font=font2, fill="purple")

    draw.rounded_rectangle((860, 390, 910, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 405), "\u02c2", font=font2, fill="white")

    draw.rounded_rectangle((930, 390, 980, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((950, 405), "\u02c5", font=font2, fill="white")

    draw.rounded_rectangle((1000, 390, 1050, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 405), "\u02c3", font=font2)

    draw.rounded_rectangle((35, 90, 155, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 100), "Esc", font=font4, fill="purple")

    draw.rounded_rectangle((175, 90, 225, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((190, 100), "1", font=font5)

    draw.rounded_rectangle((245, 90, 295, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((260, 100), "2", font=font5)

    draw.rounded_rectangle((315, 90, 365, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((330, 100), "3", font=font5)

    draw.rounded_rectangle((385, 90, 435, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((400, 100), "4", font=font5)

    draw.rounded_rectangle((455, 90, 505, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((470, 100), "5", font=font5)

    draw.rounded_rectangle((525, 90, 575, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((540, 100), "6", font=font5)

    draw.rounded_rectangle((595, 90, 645, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((610, 100), "7", font=font5)

    draw.rounded_rectangle((665, 90, 715, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((680, 100), "8", font=font5)

    draw.rounded_rectangle((735, 90, 785, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((750, 100), "9", font=font5)

    draw.rounded_rectangle((805, 90, 855, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((820, 100), "0", font=font5)

    draw.rounded_rectangle((875, 90, 1050, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((960, 100), "Backspace", font=font4, fill="purple")

    draw.rounded_rectangle((210, 190, 260, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((230, 200), "%", font=font5)

    draw.rounded_rectangle((280, 190, 330, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((290, 200), "[", font=font5)

    draw.rounded_rectangle((350, 190, 400, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((365, 200), "]", font=font5)

    draw.rounded_rectangle((420, 190, 470, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((435, 200), "{", font=font5)

    draw.rounded_rectangle((490, 190, 540, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((505, 205), "}", font=font5)

    draw.rounded_rectangle((560, 190, 610, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((575, 205), "<", font=font5)

    draw.rounded_rectangle((630, 190, 680, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((650, 205), ">", font=font5)

    draw.rounded_rectangle((700, 190, 750, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((715, 205), "€", font=font5)

    draw.rounded_rectangle((770, 190, 820, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((785, 205), "£", font=font5)

    draw.rounded_rectangle((840, 190, 890, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((855, 205), "^", font=font5)

    draw.rounded_rectangle((910, 190, 1050, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((995, 200), "Enter", font=font4, fill="purple")

    draw.rounded_rectangle((160, 290, 210, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((175, 310), "\u25c4", font=font2)

    draw.rounded_rectangle((230, 290, 280, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((245, 310), "\u25ba", font=font2)

    draw.rounded_rectangle((300, 290, 350, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 300), "*", font=font5)

    draw.rounded_rectangle((370, 290, 420, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((385, 300), "`", font=font5)

    draw.rounded_rectangle((440, 290, 490, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((450, 305), "°", font=font5)

    draw.rounded_rectangle((510, 290, 560, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((525, 305), "×", font=font5)

    draw.rounded_rectangle((580, 290, 630, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((590, 305), "÷", font=font5)

    draw.rounded_rectangle((650, 290, 700, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 305), "~", font=font5)

    draw.rounded_rectangle((720, 290, 770, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 305), "|", font=font5)

    draw.rounded_rectangle((790, 290, 840, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((800, 305), "\\", font=font5)

    draw.rounded_rectangle((860, 290, 910, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((875, 310), "Home", font=font3, fill="purple")

    draw.rounded_rectangle((930, 290, 980, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((950, 305), "\u02c4", font=font2)

    draw.rounded_rectangle((1000, 290, 1050, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 310), "End", font=font3, fill="purple")

def small2():
    draw.rounded_rectangle((35, 190, 120, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 200), "Tab", font=font2, fill="purple")

    draw.rounded_rectangle((35, 290, 140, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 300), "Shift", font=font2, fill="purple")

    draw.rounded_rectangle((35, 390, 170, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 400), "&౧౨౩", font=font4, fill="purple")

    draw.rounded_rectangle((190, 390, 240, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((200, 400), "Ctrl", font=font2, fill="purple")

    draw.rounded_rectangle((260, 390, 310, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((270, 400), "Win", font=font2, fill="purple")

    draw.rounded_rectangle((330, 390, 380, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((340, 400), "Alt", font=font2, fill="purple")

    draw.rounded_rectangle((400, 390, 770, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((550, 400), "Space", font=font2, fill="purple")

    draw.rounded_rectangle((790, 390, 840, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((805, 400), "Mic", font=font2, fill="purple")

    draw.rounded_rectangle((860, 390, 910, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 400), "\u02c2", font=font2, fill="white")

    draw.rounded_rectangle((930, 390, 980, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((940, 400), "\u02c3", font=font2, fill="white")

    draw.rounded_rectangle((1000, 390, 1050, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 400), "Tel", font=font2, fill="blue")

    draw.rounded_rectangle((35, 90, 85, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 115), "Esc", font=font4)

    draw.rounded_rectangle((105, 90, 155, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((120, 110), "ౌ", font=font5)

    draw.rounded_rectangle((175, 90, 225, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((190, 110), "ై", font=font6)

    draw.rounded_rectangle((245, 90, 295, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((260, 110), "ా", font=font5)

    draw.rounded_rectangle((315, 90, 365, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((330, 110), "ీ", font=font7)

    draw.rounded_rectangle((385, 90, 435, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((400, 110), "ూ", font=font5)

    draw.rounded_rectangle((455, 90, 505, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((470, 110), "బ", font=font5)

    draw.rounded_rectangle((525, 90, 575, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((540, 110), "హ", font=font5)

    draw.rounded_rectangle((595, 90, 645, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((610, 110), "గ", font=font5)

    draw.rounded_rectangle((665, 90, 715, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((680, 110), "ద", font=font5)

    draw.rounded_rectangle((735, 90, 785, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((750, 110), "జ", font=font5)

    draw.rounded_rectangle((805, 90, 855, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((820, 110), "డ", font=font5)

    draw.rounded_rectangle((875, 90, 925, 140), fill="black", outline="yellow", width=2, radius=8)

    draw.rounded_rectangle((945, 90, 1050, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((960, 100), "Backspace", font=font4, fill="purple")

    draw.rounded_rectangle((140, 190, 190, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((160, 200), "ో", font=font5)

    draw.rounded_rectangle((210, 190, 260, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((230, 210), "ే", font=font5)

    draw.rounded_rectangle((280, 190, 330, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((300, 210), "్", font=font5)

    draw.rounded_rectangle((350, 190, 400, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((365, 205), "ి", font=font7)

    draw.rounded_rectangle((420, 190, 470, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((435, 205), "ు", font=font5)

    draw.rounded_rectangle((490, 190, 540, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((505, 205), "ప", font=font5)

    draw.rounded_rectangle((560, 190, 610, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((575, 205), "ర", font=font5)

    draw.rounded_rectangle((630, 190, 680, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((650, 205), "క", font=font5)

    draw.rounded_rectangle((700, 190, 750, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((715, 205), "త", font=font5)

    draw.rounded_rectangle((770, 190, 820, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((785, 205), "చ", font=font5)

    draw.rounded_rectangle((840, 190, 890, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((855, 205), "ట", font=font5)

    draw.rounded_rectangle((910, 190, 960, 240), fill="black", outline="yellow", width=2, radius=8)
    #draw.text((925, 205), "\u0C79", font=font5)

    draw.rounded_rectangle((980, 190, 1050, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((995, 200), "Enter", font=font4, fill="purple")

    draw.rounded_rectangle((160, 290, 210, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((175, 310), "ొ", font=font5)

    draw.rounded_rectangle((230, 290, 280, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((250, 300), "ె", font=font5)


    draw.rounded_rectangle((300, 290, 350, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 290), "ం", font=font5)

    draw.rounded_rectangle((370, 290, 420, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((385, 300), "ృ", font=font5)

    draw.rounded_rectangle((440, 290, 490, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((450, 290), "మ", font=font5)

    draw.rounded_rectangle((510, 290, 560, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((525, 290), "న", font=font5)

    draw.rounded_rectangle((580, 290, 630, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((590, 305), "వ", font=font5)

    draw.rounded_rectangle((650, 290, 700, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 305), "ల", font=font5)

    draw.rounded_rectangle((720, 290, 770, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 305), "స", font=font5)

    draw.rounded_rectangle((790, 290, 840, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((800, 305), "య", font=font5)

    draw.rounded_rectangle((860, 290, 910, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 305), ",", font=font5)

    draw.rounded_rectangle((930, 290, 980, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((950, 305), ".", font=font5)

    draw.rounded_rectangle((1000, 290, 1050, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 310), "Shift", font=font3, fill="purple")


def capitals():
    draw.rounded_rectangle((35, 190, 120, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 200), "Tab", font=font2, fill="purple")

    draw.rounded_rectangle((35, 290, 140, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 300), "Shift", font=font2, fill="purple")

    draw.rounded_rectangle((35, 390, 170, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 400), "&౧౨౩", font=font4, fill="purple")

    draw.rounded_rectangle((190, 390, 240, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((200, 400), "Ctrl", font=font2, fill="purple")

    draw.rounded_rectangle((260, 390, 310, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((270, 400), "Win", font=font2, fill="purple")

    draw.rounded_rectangle((330, 390, 380, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((340, 400), "Alt", font=font2, fill="purple")

    draw.rounded_rectangle((400, 390, 770, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((550, 400), "Space", font=font2, fill="purple")

    draw.rounded_rectangle((790, 390, 840, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((805, 400), "Mic", font=font2, fill="purple")

    draw.rounded_rectangle((860, 390, 910, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 400), "\u02c2", font=font2, fill="white")

    draw.rounded_rectangle((930, 390, 980, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((940, 400), "\u02c3", font=font2, fill="white")

    draw.rounded_rectangle((1000, 390, 1050, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 400), "Tel", font=font2, fill="blue")

    draw.rounded_rectangle((35, 90, 85, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 115), "Esc", font=font4)

    draw.rounded_rectangle((105, 90, 155, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((110, 95), "1", font=font2)
    draw.text((125, 95), "ఔ", font=font5)

    draw.rounded_rectangle((175, 90, 225, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((180, 95), "2", font=font2)
    draw.text((195, 95), "ఐ", font=font5)

    draw.rounded_rectangle((245, 90, 295, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((250, 95), "3", font=font2)
    draw.text((265, 95), "ఆ", font=font5)

    draw.rounded_rectangle((315, 90, 365, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 95), "4", font=font2)
    draw.text((335, 95), "ఈ", font=font5)

    draw.rounded_rectangle((385, 90, 435, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((390, 95), "5", font=font2)
    draw.text((405, 95), "ఊ", font=font5)

    draw.rounded_rectangle((455, 90, 505, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((460, 95), "6", font=font2)
    draw.text((475, 95), "భ", font=font5)

    draw.rounded_rectangle((525, 90, 575, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((530, 95), "7", font=font2)
    draw.text((545, 95), "ఙ", font=font5)

    draw.rounded_rectangle((595, 90, 645, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((600, 95), "8", font=font2)
    draw.text((615, 95), "ఘ", font=font5)

    draw.rounded_rectangle((665, 90, 715, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 95), "9", font=font2)
    draw.text((685, 95), "ధ", font=font5)

    draw.rounded_rectangle((735, 90, 785, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 95), "0", font=font2)
    draw.text((750, 95), "ఝ", font=font5)

    draw.rounded_rectangle((805, 90, 855, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((825, 95), "ఢ", font=font5)

    draw.rounded_rectangle((875, 90, 925, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((895, 95), "ఞ", font=font5)

    draw.rounded_rectangle((945, 90, 1050, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((960, 100), "Backspace", font=font4, fill="purple")

    draw.rounded_rectangle((140, 190, 190, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((160, 195), "ఓ", font=font5)

    draw.rounded_rectangle((210, 190, 260, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((230, 195), "ఏ", font=font5)

    draw.rounded_rectangle((280, 190, 330, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((300, 195), "అ", font=font5)

    draw.rounded_rectangle((350, 190, 400, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((370, 195), "ఇ", font=font5)

    draw.rounded_rectangle((420, 190, 470, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((440, 195), "ఉ", font=font5)

    draw.rounded_rectangle((490, 190, 540, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((510, 195), "ఫ", font=font5)

    draw.rounded_rectangle((560, 190, 610, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((580, 195), "ఱ", font=font5)

    draw.rounded_rectangle((630, 190, 680, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((650, 195), "ఖ", font=font5)

    draw.rounded_rectangle((700, 190, 750, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((720, 195), "థ", font=font5)

    draw.rounded_rectangle((770, 190, 820, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((790, 195), "ఛ", font=font5)

    draw.rounded_rectangle((840, 190, 890, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((860, 195), "ఠ", font=font5)

    draw.rounded_rectangle((910, 190, 960, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((920, 195), "త్ర", font=font5)

    draw.rounded_rectangle((980, 190, 1050, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((995, 200), "Enter", font=font4, fill="purple")

    draw.rounded_rectangle((160, 290, 210, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((180, 295), "ఒ", font=font5)

    draw.rounded_rectangle((230, 290, 280, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((250, 295), "ఎ", font=font5)

    draw.rounded_rectangle((300, 290, 350, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 295), "ఁ", font=font5)

    draw.rounded_rectangle((370, 290, 420, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((390, 295), "\u0C59", font=font5)

    draw.rounded_rectangle((440, 290, 490, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((460, 295), "ణ", font=font5)

    draw.rounded_rectangle((510, 290, 560, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((530, 295), "ష", font=font5)

    draw.rounded_rectangle((580, 290, 630, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((590, 295), "జ్ఞ", font=font5)

    draw.rounded_rectangle((650, 290, 700, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 295), "ళ", font=font5)

    draw.rounded_rectangle((720, 290, 770, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 295), "శ", font=font5)

    draw.rounded_rectangle((790, 290, 840, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((810, 295), "ౘ", font=font5)

    draw.rounded_rectangle((860, 290, 910, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((875, 295), "క్ష", font=font5)

    draw.rounded_rectangle((930, 290, 980, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((945, 295), "శ్ర", font=font5)

    draw.rounded_rectangle((1000, 290, 1050, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 310), "Shift", font=font3, fill="purple")

def symbols():
    draw.rounded_rectangle((35, 190, 190, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 200), "Tab", font=font2, fill="purple")

    draw.rounded_rectangle((35, 290, 140, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 300), "Shift", font=font2, fill="purple")

    draw.rounded_rectangle((35, 390, 170, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 400), "&౧౨౩", font=font4, fill="purple")

    draw.rounded_rectangle((190, 390, 240, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((200, 400), "Ctrl", font=font2, fill="purple")

    draw.rounded_rectangle((260, 390, 310, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((270, 400), "Win", font=font2, fill="purple")

    draw.rounded_rectangle((330, 390, 380, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((340, 400), "Alt", font=font2, fill="purple")

    draw.rounded_rectangle((400, 390, 770, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((550, 400), "Space", font=font2, fill="purple")

    draw.rounded_rectangle((790, 390, 840, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((805, 400), ".", font=font2, fill="purple")

    draw.rounded_rectangle((860, 390, 910, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((880, 405), "\u02c2", font=font2, fill="white")

    draw.rounded_rectangle((930, 390, 980, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((950, 405), "\u02c5", font=font2, fill="white")

    draw.rounded_rectangle((1000, 390, 1050, 440), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 405), "\u02c3", font=font2)

    draw.rounded_rectangle((35, 90, 155, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((45, 100), "Esc", font=font4, fill="purple")

    draw.rounded_rectangle((175, 90, 225, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((190, 100), "౧", font=font5)

    draw.rounded_rectangle((245, 90, 295, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((260, 100), "౨", font=font5)

    draw.rounded_rectangle((315, 90, 365, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((330, 100), "౩", font=font5)

    draw.rounded_rectangle((385, 90, 435, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((400, 100), "౪", font=font5)

    draw.rounded_rectangle((455, 90, 505, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((470, 100), "౫", font=font5)

    draw.rounded_rectangle((525, 90, 575, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((540, 100), "౬", font=font5)

    draw.rounded_rectangle((595, 90, 645, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((610, 100), "౮", font=font5)

    draw.rounded_rectangle((665, 90, 715, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((680, 100), "౭", font=font5)

    draw.rounded_rectangle((735, 90, 785, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((750, 100), "౯", font=font5)

    draw.rounded_rectangle((805, 90, 855, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((820, 100), "౦", font=font5)

    draw.rounded_rectangle((875, 90, 1050, 140), fill="black", outline="yellow", width=2, radius=8)
    draw.text((960, 100), "Backspace", font=font4, fill="purple")

    draw.rounded_rectangle((210, 190, 260, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((230, 200), "!", font=font5)

    draw.rounded_rectangle((280, 190, 330, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((290, 200), "@", font=font5)

    draw.rounded_rectangle((350, 190, 400, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((365, 200), "#", font=font5)

    draw.rounded_rectangle((420, 190, 470, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((435, 200), "$", font=font5)

    draw.rounded_rectangle((490, 190, 540, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((505, 205), "\u20b9", font=font5)

    draw.rounded_rectangle((560, 190, 610, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((575, 205), "&", font=font5)

    draw.rounded_rectangle((630, 190, 680, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((650, 205), "_", font=font5)

    draw.rounded_rectangle((700, 190, 750, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((715, 205), "-", font=font5)

    draw.rounded_rectangle((770, 190, 820, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((785, 205), "=", font=font5)

    draw.rounded_rectangle((840, 190, 890, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((855, 205), "+", font=font5)

    draw.rounded_rectangle((910, 190, 1050, 240), fill="black", outline="yellow", width=2, radius=8)
    draw.text((995, 200), "Enter", font=font4, fill="purple")

    draw.rounded_rectangle((160, 290, 210, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((175, 310), "\u25c4", font=font2)

    draw.rounded_rectangle((230, 290, 280, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((245, 310), "\u25ba", font=font2)

    draw.rounded_rectangle((300, 290, 350, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((320, 300), ";", font=font5)

    draw.rounded_rectangle((370, 290, 420, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((385, 300), ":", font=font5)

    draw.rounded_rectangle((440, 290, 490, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((450, 305), "(", font=font5)

    draw.rounded_rectangle((510, 290, 560, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((525, 305), ")", font=font5)

    draw.rounded_rectangle((580, 290, 630, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((590, 305), "\u002f", font=font5)

    draw.rounded_rectangle((650, 290, 700, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((670, 305), "'", font=font5)

    draw.rounded_rectangle((720, 290, 770, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((740, 305), "\"", font=font5)

    draw.rounded_rectangle((790, 290, 840, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((800, 305), "?", font=font5)

    draw.rounded_rectangle((860, 290, 910, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((875, 310), "Home", font=font3, fill="purple")

    draw.rounded_rectangle((930, 290, 980, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((950, 305), "\u02c4", font=font2)

    draw.rounded_rectangle((1000, 290, 1050, 340), fill="black", outline="yellow", width=2, radius=8)
    draw.text((1010, 310), "End", font=font3, fill="purple")

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    fontpath = "C:\Windows\Fonts\Vanib"
    font = ImageFont.truetype(fontpath)
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    alphabets()
    if lmList:
        l, _, _ = detector.findDistance(8, 4, img, draw=False)
        if l<35:
            symbols()

        if lmList:
            l, _, _ = detector.findDistance(4, 16, img, draw=False)
            if l < 35:
                symbol2()

        if lmList:
            l, _, _ = detector.findDistance(4, 20, img, draw=False)
            if l < 35:
                small2()

        if lmList:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            if l < 35:
                capitals()

        if 35 < lmList[8][0] < 170 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)

            if l<35:
                symbols()
    if lmList:
        if 35 < lmList[8][0] < 120 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                pyautogui.press("tab")

    if lmList:
        if 945 < lmList[8][0] < 1050 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                pyautogui.press("backspace")

    if lmList:
        if 910 < lmList[8][0] < 1050 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                pyautogui.press("enter")

    if lmList:
        if 105 < lmList[8][0] < 155 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ౌ")

    if lmList:
        if 175 < lmList[8][0] < 225 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ై")

    if lmList:
        if 245 < lmList[8][0] < 295 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ా")

    if lmList:
        if 315 < lmList[8][0] < 365 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ీ")

    if lmList:
        if 385 < lmList[8][0] < 435 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ూ")

    if lmList:
        if 455 < lmList[8][0] < 505 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("బ")


    if lmList:
        if 525 < lmList[8][0] < 575 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("హ")

    if lmList:
        if 595 < lmList[8][0] < 645 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("గ")

    if lmList:
        if 665 < lmList[8][0] < 715 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ద")

    if lmList:
        if 735 < lmList[8][0] < 785 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("జ")

    if lmList:
        if 805 < lmList[8][0] < 855 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("డ")

    if lmList:
        if 875 < lmList[8][0] < 925 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("\u0c55")

    if lmList:
        if 140 < lmList[8][0] < 210 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ో")

    if lmList:
        if 230 < lmList[8][0] < 280 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ే")

    if lmList:
        if 300 < lmList[8][0] < 350 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("్")

    if lmList:
        if 370 < lmList[8][0] < 420 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ి")

    if lmList:
        if 440 < lmList[8][0] < 490 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ు")

    if lmList:
        if 510 < lmList[8][0] < 560 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ప")

    if lmList:
        if 580 < lmList[8][0] < 630 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ర")

    if lmList:
        if 650 < lmList[8][0] < 700 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("క")

    if lmList:
        if 720 < lmList[8][0] < 770 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("త")

    if lmList:
        if 790 < lmList[8][0] < 840 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("చ")

    if lmList:
        if 860 < lmList[8][0] < 910 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ట")

    if lmList:
        if 930 < lmList[8][0] < 980 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("\u0c79")

    if lmList:
        if  160 < lmList[8][0] < 210 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ొ")

    if lmList:
        if  230 < lmList[8][0] < 280 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ె")

    if lmList:
        if  300 < lmList[8][0] < 350 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ం")

    if lmList:
        if  370 < lmList[8][0] < 420 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ృ")

    if lmList:
        if  440 < lmList[8][0] < 490 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("మ")

    if lmList:
        if  510 < lmList[8][0] < 560 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("న")

    if lmList:
        if  580 < lmList[8][0] < 630 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("వ")

    if lmList:
        if  650 < lmList[8][0] < 700 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ల")

    if lmList:
        if  720 < lmList[8][0] < 770 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("స")

    if lmList:
        if  790 < lmList[8][0] < 840 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("య")

    if lmList:
        if  860 < lmList[8][0] < 910 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type(",")

    if lmList:
        if  930 < lmList[8][0] < 980 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type(".")

    if lmList:
        if  1000 < lmList[8][0] < 1050 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                capitals()

    if lmList:
        if  35 < lmList[8][0] < 140 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                capitals()

    if lmList:
        if  35 < lmList[8][0] < 170 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                symbols()

    if lmList:
        if  190 < lmList[8][0] < 240 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                symbol2()

    if lmList:
        if  260 < lmList[8][0] < 310 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                symbol2()

    if lmList:
        if  330 < lmList[8][0] < 380 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                small2()

    if lmList:
        if  400 < lmList[8][0] < 770 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                pyautogui.press('space')

    if lmList:
        if  790 < lmList[8][0] < 840 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("Can't record now ")

    if lmList:
        if 860 < lmList[8][0] < 970 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("right")

    if lmList:
        if 790 < lmList[8][0] < 910 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 12, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("left")

    if lmList:
        if 175 < lmList[8][0] < 225 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type("౧")

    if lmList:
        if  245 < lmList[8][0] < 295 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౨")

    if lmList:
        if  315 < lmList[8][0] < 365 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౩")

    if lmList:
        if  385 < lmList[8][0] < 435 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౪")

    if lmList:
        if  455 < lmList[8][0] < 505 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౫")

    if lmList:
        if  525 < lmList[8][0] < 575 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౬")

    if lmList:
        if  595 < lmList[8][0] < 645 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౭")

        if lmList:
            if 665 < lmList[8][0] < 715 and 90 < lmList[8][1] < 140:
                l, _, _ = detector.findDistance(8, 4, img, draw=False)
                print(l)
                if l < 35:
                    keyboard.type("౮")

    if lmList:
        if  735 < lmList[8][0] < 785 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౯")

    if lmList:
        if  805 < lmList[8][0] < 855 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("౦")

    if lmList:
        if  210 < lmList[8][0] < 260 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("!")

    if lmList:
        if  280 < lmList[8][0] < 330 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("@")

    if lmList:
        if  350 < lmList[8][0] < 400 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("#")

    if lmList:
        if  420 < lmList[8][0] < 470 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("$")

    if lmList:
        if  490 < lmList[8][0] < 540 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("\u20b9")

    if lmList:
        if  560 < lmList[8][0] < 610 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("&")

    if lmList:
        if  630 < lmList[8][0] < 680 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("_")

    if lmList:
        if  700 < lmList[8][0] < 750 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("-")

    if lmList:
        if  770 < lmList[8][0] < 820 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("=")

        if lmList:
            if 840 < lmList[8][0] < 890 and 190 < lmList[8][1] < 240:
                l, _, _ = detector.findDistance(8, 4, img, draw=False)
                print(l)
                if l < 35:
                    keyboard.type("+")

    if lmList:
        if 910 < lmList[8][0] < 1050 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press('enter')

    if lmList:
        if 300 < lmList[8][0] < 350 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type(';')

    if lmList:
        if 370 < lmList[8][0] < 420 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type(':')

    if lmList:
        if 440 < lmList[8][0] < 490 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('(')

    if lmList:
        if 510 < lmList[8][0] < 560 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type(')')

    if lmList:
        if 580 < lmList[8][0] < 630 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('/')

    if lmList:
        if 650 < lmList[8][0] < 700 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('\'')

    if lmList:
        if 720 < lmList[8][0] < 770 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('\"')

    if lmList:
        if 790 < lmList[8][0] < 840 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('?')

    if lmList:
        if 860 < lmList[8][0] < 910 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("home")

    if lmList:
        if 930 < lmList[8][0] < 980 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("pageup")

    if lmList:
        if 1000 < lmList[8][0] < 1050 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("end")

    if lmList:
        if 1000 < lmList[8][0] < 1050 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("right")

    if lmList:
        if 860 < lmList[8][0] < 910 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("left")

    if lmList:
        if 930 < lmList[8][0] < 980 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(8, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("pagedown")

    if lmList:
        if 35 < lmList[8][0] < 120 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                pyautogui.press("tab")

    if lmList:
        if 105 < lmList[8][0] < 155 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఔ")

    if lmList:
        if 175 < lmList[8][0] < 225 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఐ")

    if lmList:
        if 245 < lmList[8][0] < 295 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఆ")

    if lmList:
        if 315 < lmList[8][0] < 365 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఈ")

    if lmList:
        if 385 < lmList[8][0] < 435 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఊ")

    if lmList:
        if 455 < lmList[8][0] < 505 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("భ")

    if lmList:
        if 525 < lmList[8][0] < 575 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<50:
                keyboard.type("ఙ")

    if lmList:
        if 595 < lmList[8][0] < 645 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<50:
                keyboard.type("ఘ")

    if lmList:
        if 665 < lmList[8][0] < 715 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<50:
                keyboard.type("ధ")

    if lmList:
        if 735 < lmList[8][0] < 785 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<50:
                keyboard.type("ఝ")

    if lmList:
        if 805 < lmList[8][0] < 855 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<50:
                keyboard.type("ఢ")

    if lmList:
        if 875 < lmList[8][0] < 925 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<50:
                keyboard.type("ఞ")

    if lmList:
        if 140 < lmList[8][0] < 210 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఓ")

    if lmList:
        if 230 < lmList[8][0] < 280 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఏ")

    if lmList:
        if 300 < lmList[8][0] < 350 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("అ")

    if lmList:
        if 370 < lmList[8][0] < 420 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)

            if l<35:
                keyboard.type("ఇ")

    if lmList:
        if 440 < lmList[8][0] < 490 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఉ")

    if lmList:
        if 510 < lmList[8][0] < 560 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఫ")

    if lmList:
        if 580 < lmList[8][0] < 630 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఱ")

    if lmList:
        if 650 < lmList[8][0] < 700 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఖ")

    if lmList:
        if 720 < lmList[8][0] < 770 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("థ")

    if lmList:
        if 790 < lmList[8][0] < 840 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఛ")

    if lmList:
        if 860 < lmList[8][0] < 910 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఠ")

    if lmList:
        if 930 < lmList[8][0] < 980 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("త్ర")

    if lmList:
        if  160 < lmList[8][0] < 210 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఒ")

    if lmList:
        if  230 < lmList[8][0] < 280 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఎ")

    if lmList:
        if  300 < lmList[8][0] < 350 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ఁ")

    if lmList:
        if  370 < lmList[8][0] < 420 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("\u0c59")

    if lmList:
        if  440 < lmList[8][0] < 490 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ణ")

    if lmList:
        if  510 < lmList[8][0] < 560 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ష")

    if lmList:
        if  580 < lmList[8][0] < 630 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("జ్ఞ")

    if lmList:
        if  650 < lmList[8][0] < 700 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ళ")

    if lmList:
        if  720 < lmList[8][0] < 770 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("శ")

    if lmList:
        if  790 < lmList[8][0] < 840 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("ౘ")

    if lmList:
        if  860 < lmList[8][0] < 910 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("క్ష")

    if lmList:
        if  930 < lmList[8][0] < 980 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("శ్ర")

    if lmList:
        if  1000 < lmList[8][0] < 1050 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                capitals()

    if lmList:
        if  35 < lmList[8][0] < 140 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                capitals()

    if lmList:
        if  35 < lmList[8][0] < 170 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                symbols()

    if lmList:
        if  190 < lmList[8][0] < 240 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                symbol2()

    if lmList:
        if  260 < lmList[8][0] < 310 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                symbol2()

    if lmList:
        if  330 < lmList[8][0] < 380 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                small2()

    if lmList:
        if  400 < lmList[8][0] < 770 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                pyautogui.press("space")

    if lmList:
        if  790 < lmList[8][0] < 840 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("Can't record now ")

    if lmList:
        if 860 < lmList[8][0] < 970 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("right")

    if lmList:
        if 790 < lmList[8][0] < 910 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(4, 12, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("left")

    if lmList:
        if  175 < lmList[8][0] < 225 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("1")

    if lmList:
        if  245 < lmList[8][0] < 295 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("2")

    if lmList:
        if  315 < lmList[8][0] < 365 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("3")

    if lmList:
        if  385 < lmList[8][0] < 435 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("4")

    if lmList:
        if  455 < lmList[8][0] < 505 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("5")

    if lmList:
        if  525 < lmList[8][0] < 575 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("6")

    if lmList:
        if  595 < lmList[8][0] < 645 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)

            if l<35:
                keyboard.type("7")

        if lmList:
            if 665 < lmList[8][0] < 715 and 90 < lmList[8][1] < 140:
                l, _, _ = detector.findDistance(16, 4, img, draw=False)
                print(l)
                if l < 35:
                    keyboard.type("8")

    if lmList:
        if  735 < lmList[8][0] < 785 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("9")

    if lmList:
        if  805 < lmList[8][0] < 855 and 90 < lmList[8][1] < 140:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("0")

    if lmList:
        if  210 < lmList[8][0] < 260 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("%")

    if lmList:
        if  280 < lmList[8][0] < 330 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("[")

    if lmList:
        if  350 < lmList[8][0] < 400 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("]")

    if lmList:
        if  420 < lmList[8][0] < 470 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("{")

    if lmList:
        if  490 < lmList[8][0] < 540 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("}")

    if lmList:
        if  560 < lmList[8][0] < 610 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("<")

    if lmList:
        if  630 < lmList[8][0] < 680 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type(">")

    if lmList:
        if  700 < lmList[8][0] < 750 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("€")

    if lmList:
        if  770 < lmList[8][0] < 820 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l<35:
                keyboard.type("£")

        if lmList:
            if 840 < lmList[8][0] < 890 and 190 < lmList[8][1] < 240:
                l, _, _ = detector.findDistance(16, 4, img, draw=False)
                print(l)
                if l < 35:
                    keyboard.type("^")

    if lmList:
        if 910 < lmList[8][0] < 1050 and 190 < lmList[8][1] < 240:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press('enter')

    if lmList:
        if 300 < lmList[8][0] < 350 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('*')

    if lmList:
        if 370 < lmList[8][0] < 420 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('`')

    if lmList:
        if 440 < lmList[8][0] < 490 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('°')

    if lmList:
        if 510 < lmList[8][0] < 560 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('×')

    if lmList:
        if 580 < lmList[8][0] < 630 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('÷')

    if lmList:
        if 650 < lmList[8][0] < 700 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('~')

    if lmList:
        if 720 < lmList[8][0] < 770 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('|')

    if lmList:
        if 790 < lmList[8][0] < 840 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                keyboard.type('\\')

    if lmList:
        if 860 < lmList[8][0] < 910 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("home")

    if lmList:
        if 930 < lmList[8][0] < 980 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("pageup")

    if lmList:
        if 1000 < lmList[8][0] < 1050 and 290 < lmList[8][1] < 340:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("end")

    if lmList:
        if 1000 < lmList[8][0] < 1050 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("right")

    if lmList:
        if 860 < lmList[8][0] < 910 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("left")

    if lmList:
        if 930 < lmList[8][0] < 980 and 390 < lmList[8][1] < 440:
            l, _, _ = detector.findDistance(16, 4, img, draw=False)
            print(l)
            if l < 35:
                pyautogui.press("pagedown")

    img = np.array(img_pil)
    cv2.imshow("output", img)
    cv2.waitKey(1)