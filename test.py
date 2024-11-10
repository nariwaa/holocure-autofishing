from PIL import ImageGrab
import pyautogui

# ⇐⇑⇒⇓⊙
count = 0

def GetPixelColor(axeX, axeY):
    px = ImageGrab.grab().load()
    for y in (axeY, axeY):
        for x in (axeX, axeX):
            color = px[x, y]
            return color

def ColorCheck(color):
    global count
    count = count + 1
    if color == (174, 49, 208): 
        # ⊙ Purple
        print(f"Detected: ⊙ purple {color} ({count})")
        return " "
    elif color == (225, 50, 50): 
        # ⇑ Red
        print(f"Detected: ⇑ Red {color} ({count})")
        return "w"
    elif color == (52, 145, 247): 
        # ⇓ Blue
        print(f"Detected: ⊙ ⇓ Blue {color} ({count})")
        return "s"
    elif color == (245, 197, 67): 
        # ⇐ Yellow
        print(f"Detected: ⇐ Yellow {color} ({count})")
        return "a"
    elif color == (45, 235, 43): 
        # ⇒ Green
        print(f"Detected: ⇒ Green {color} ({count})")
        return "d"
    else:
        return "x"
    

def main():
    # get pixel
    pixel = GetPixelColor(1193, 755)
    # compare with colors and return 
    a = ColorCheck(pixel)
    if a == "x":
        pass
    else:
        pyautogui.keyDown(a)
        pyautogui.sleep(0.2)
        pyautogui.keyUp(a)
    
    # if the color is a match, input the key

while True:
    main()