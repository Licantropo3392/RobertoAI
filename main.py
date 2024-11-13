import RobertoAI
import time
import types

def Main(Lobby, WinCheck, Match):
    isPlaying = False

    lobby = Lobby(startPosition, startColor, endColor)
    winCheck = WinCheck(matchPosition, winColor, loseColor)
    matchLogic = Match()

    while True:
        time.sleep(1)

        check = lobby.Start()
        if check != None:
            isPlaying = check
        
        # winCheck.Win()
        # winCheck.Lose()

        matchLogic.Move(isPlaying)

if __name__ == "__main__":
    startPosition: dict[str, int] = {
        "x": 1335, 
        "y": 656
    }

    startColor: tuple[int, int, int] = (239, 198, 9)

    matchPosition: dict[str, int] = {
        "x": 624,
        "y": 332
    }

    winColor: tuple[int, int, int] = (9, 76, 240)
    loseColor: tuple[int, int, int] = (168, 14, 8)

    endColor: tuple[int, int, int] = (35, 115, 255)

    Main(RobertoAI.Lobby, RobertoAI.WinCheck, RobertoAI.Match_V2)