from PIL import ImageGrab
import pyautogui
import time
from colorama import Fore, Style, just_fix_windows_console
just_fix_windows_console()

print(f"Starting...")
time.sleep(1.2397236962398347)
count = 0

def GetPixelColor(x1, y1, x2, y2):
    px = ImageGrab.grab().load()
    colors = []
    
    for y in range(y1, y2 + 1):
        row_colors = []
        for x in range(x1, x2 + 1):
            color = px[x, y]
            row_colors.append(color)
        colors.append(row_colors)
    
    return colors

def GetPixelWhiteState(axeX, axeY):
    px = ImageGrab.grab().load()
    for y in (axeY, axeY):
        for x in (axeX, axeX):
            color = px[x, y]
            if color == (248, 248, 248):
                return True
            else:
                return False

def ColorCheck(color):
    global count
    count = count + 1
    
    for y, row_colors in enumerate(color):
        for x, pixel_color in enumerate(row_colors):
            if pixel_color == (174, 49, 208): 
                # ⊙ Purple
                print(f"Detected: {Fore.MAGENTA}⊙ Purple{Fore.RESET} {pixel_color} at ({x}, {y}) ({count})")
                return " "
            elif pixel_color == (225, 50, 50): 
                # ⇑ Red
                print(f"Detected: {Fore.RED}⇑ Red{Fore.RESET} {pixel_color} at ({x}, {y}) ({count})")
                return "w"
            elif pixel_color == (52, 144, 246): 
                # ⇓ Blue
                print(f"Detected: {Fore.BLUE}⇓ Blue{Fore.RESET} {pixel_color} at ({x}, {y}) ({count})")
                return "s"
            elif pixel_color == (245, 197, 67): 
                # ⇐ Yellow
                print(f"Detected: {Fore.YELLOW}⇐ Yellow{Fore.RESET} {pixel_color} at ({x}, {y}) ({count})")
                return "a"
            elif pixel_color == (45, 235, 43): 
                # ⇒ Green
                print(f"Detected: {Fore.GREEN}⇒ Green{Fore.RESET} {pixel_color} at ({x}, {y}) ({count})")
                return "d"
    
    return "x"

def main():
    global time1
    # Capture region
    x1, y1, x2, y2 = 1177, 721, 1216, 797
    
    pixels = GetPixelColor(x1, y1, x2, y2)

    a = ColorCheck(pixels)
    
    if a == "x":
        time2 = time.time()
        if time1 < time2: # I want to add 4second to time 2
            print(f"{Fore.LIGHTRED_EX}Trying to go back to fishing...{Fore.RESET}", end='\r')
            statething = GetPixelWhiteState(999, 828)
            if statething == True:
                print(f"{Fore.CYAN}Going back to fishing..........{Fore.RESET}")
                pyautogui.keyDown("space")
                pyautogui.sleep(0.2)
                pyautogui.keyUp("space")
                time.sleep(2)
                pyautogui.keyDown("space")
                pyautogui.sleep(0.2)
                pyautogui.keyUp("space")
    else:
        pyautogui.keyDown(a)
        pyautogui.sleep(0.2)
        pyautogui.keyUp(a)
        time1 = time.time() + 4

def mainlogs():
    global time1
    # Capture region
    x1, y1, x2, y2 = 1177, 721, 1216, 797
    
    pixels = GetPixelColor(x1, y1, x2, y2)

    with open('logs.txt', 'a') as file:
        file.write(f'{pixels}\n')

    a = ColorCheck(pixels)
    
    if a == "x":
        time2 = time.time()
        if time1 < time2: # I want to add 4second to time 2
            print(f"{Fore.LIGHTRED_EX}Trying to go back to fishing...{Fore.RESET}", end='\r')
            statething = GetPixelWhiteState(999, 828)
            if statething == True:
                print(f"{Fore.CYAN}Going back to fishing..........{Fore.RESET}")
                pyautogui.keyDown("space")
                pyautogui.sleep(0.2)
                pyautogui.keyUp("space")
                time.sleep(2)
                pyautogui.keyDown("space")
                pyautogui.sleep(0.2)
                pyautogui.keyUp("space")
    else:
        pyautogui.keyDown(a)
        pyautogui.sleep(0.2)
        pyautogui.keyUp(a)
        time1 = time.time() + 4

time1 = time.time() + 500
print("\nWould you like to record logs to troubleshoot anything? (y/n)")
yesorno = input("> ")
if yesorno == "y":
    while True:
        mainlogs()
else:
    while True:
        main()
