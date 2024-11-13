import pyautogui as Screen
import random, time

class Match_V2():
    def __init__(self) -> None:
        self.key: int = 0
        self.keys: dict[int, str] = {
            0: "w",
            1: "a",
            2: "s",
            3: "d",
            4: "wa",
            5: "wd",
            6: "aw",
            # 7: "as",
            # 8: "sa",
            # 9: "sd",
            # 10: "ds",
            7: "dw",
        }

    def Move(self, isPlaying: bool) -> None:
        if isPlaying:
            key = random.randint(0,(len(self.keys) - 1))

            if key == self.key:
                return

            for i in self.keys[self.key]:
                Screen.keyUp(i)

            self.key = key

            for i in self.keys[self.key]:
                Screen.keyDown(i)

            Screen.press("space")
            Screen.press("shift")

if __name__ == "__main__":
    time.sleep(1)

    match_logic = Match_V2()

    while True:
        match_logic.Move(True)