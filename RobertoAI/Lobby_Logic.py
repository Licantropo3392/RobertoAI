import pyautogui as Screen

class Lobby():
    def __init__(self, position: dict[int, int], startColor: tuple[int, int, int], endColor: tuple[int, int, int]) -> None:
        self.position = position
        self.startColor = startColor
        self.endColor = endColor

    def Start(self) -> bool:
        inLobby = Screen.pixelMatchesColor(self.position["x"], self.position["y"], self.startColor)
        
        if inLobby:
            Screen.press("f")
            print("Started succesfully!")
            return True
        
        isEnded = Screen.pixelMatchesColor(self.position["x"], self.position["y"], self.endColor)  
        
        if isEnded: 
            Screen.press("f")
            print("Match finished!")
            return False