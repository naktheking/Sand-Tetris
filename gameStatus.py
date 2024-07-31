# Tried to use CS Academy to play sound but crashes every time
# playsound learned from https://www.geeksforgeeks.org/play-sound-in-python/ 
from playsound import playsound

def checkGameOver(app):
    for row, col, color in app.tetrinoPiece:
        if (row, col) in app.board:
            app.gameOver = True
            app.paused = True
            playsound(app.gameOverSound, True)
            return True
    return False