from cmu_graphics import *
def onAppStart(app):
    app.width = app.height = 700


def redrawAll(app):
    peru = rgb(205, 133, 63)
    chocolate = rgb(210, 105, 30)
    gray = rgb(43, 43, 40)

    drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, 
             app.boardHeight, fill = gray, opacity = 70)
    #Paused Text
    drawLabel('PAUSED',app.boardWidth/2 + app.leftBoardCoordinate, 
              app.boardHeight/4 + app.topBoardCoordinate, size = 24, 
              fill='white')

    #Resume Button
    drawRect(app.resumeXCoord, 
             app.resumeYCoord, app.resumeWidth, app.resumeHeight, 
             align = 'center', fill = peru)
    drawLabel('RESUME', app.resumeXCoord,
               app.resumeYCoord, bold = True, 
               font='monospace', size = 24)
    
    #New Game Button
    drawRect(app.newGameXCoord, 
             app.newGameYCoord,app.newGameWidth, app.newGameHeight, 
             align = 'center', fill = chocolate)
    drawLabel('NEW GAME', app.newGameXCoord, 
              app.newGameYCoord, bold = True, 
              font='monospace', size = 24)
    
    #Music Button
    

def main():
    runApp()

main()