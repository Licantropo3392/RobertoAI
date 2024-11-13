import pyautogui as Screen

class WinCheck():
    def __init__(self, position: dict[int, int], win: tuple[int, int, int], lose: tuple[int, int, int]) -> None:
        self.position = position
        self.win = win
        self.lose = lose

    def Win(self):
        winned = Screen.pixelMatchesColor(self.position["x"], self.position["y"], self.win)

        if winned:
            print("Winned :)")
    
    def Lose(self):
        losed = Screen.pixelMatchesColor(self.position["x"], self.position["y"], self.lose)

        if losed:
            print("Losed :(")