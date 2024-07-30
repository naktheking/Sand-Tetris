def checkGameOver(app):
    for row, col, color in app.tetrinoPiece:
        if (row, col) in app.board:
            app.gameOver = True
            app.paused = True
            # app.gameOverSound.play()
            return True
    return False