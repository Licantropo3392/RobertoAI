import pyautogui as Screen
import random, time

class Match():
    def __init__(self) -> None:
        pass

    def Move(self, isPlaying):
        if isPlaying:
            key = random.randint(0,3)
            match key:
                case 0:
                    Screen.keyDown("w")
                    # print("Pressing W")

                    time.sleep(.5)
            
                    Screen.keyUp("w")
                    # print("Releasing W")
                case 1:
                    Screen.keyDown("a")
                    # print("Pressing A")

                    time.sleep(.5)
            
                    Screen.keyUp("a")
                    # print("Releasing A")
                case 2:
                    Screen.keyDown("s")
                    # print("Pressing S")

                    time.sleep(.5)
            
                    Screen.keyUp("s")
                    # print("Releasing s")
                case 3:
                    Screen.keyDown("d")
                    # print("Pressing D")

                    time.sleep(.5)
                    
                    Screen.keyUp("d")
                    # print("Releasing d")
            Screen.press('space')
            Screen.press('shift')