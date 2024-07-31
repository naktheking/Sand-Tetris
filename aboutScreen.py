from cmu_graphics import *

def startScreen_onAppStart(app):
    app.width = 700
    app.height = 700
    app.boardWidth = app.width/2
    app.boardHeight = app.height-20
    app.leftBoardCoordinate = app.width//2-(7*app.boardWidth//10)
    app.topBoardCoordinate = app.height//2-(app.boardHeight//2)
    app.music = False

def startScreen_redrawAll(app):
    # drawRect(app.leftBoardCoordinate, app.topBoardCoordinate, app.boardWidth, app.boardHeight,
    #          fill = None, border = 'gray', borderWidth = 2)
    drawRect(0, 0, app.width, app.height, fill = 'black')
    drawLabel('Lauren', app.width/2, app.height/4, font = 'monospace', size = 18, 
              fill = 'white')
    drawLabel('SANDS-TRIS', app.width/2, app.height/3, font='monospace', size = 40, 
              fill = 'white')
    #start button
    drawRect(app.width/3, app.height*2/3, 150, 60, border='white', 
             align = 'center', fill= None)
    drawLabel('Start', app.width/3, app.height*2/3, font='orbitron', size=40, 
              fill = 'white')
    #About button
    drawRect(app.width*2/3, app.height*2/3, 150, 60, border='white', 
             align = 'center', fill= None)
    drawLabel('About', app.width*2/3, app.height*2/3, font='orbitron', size=40,
              fill = 'white')
    #music button
    drawRect(app.width*9/10, app.height/5, 70, 30, align = 'center', fill = None, 
             border = 'white')
    drawLabel('Music', app.width*9/10, app.height/5, font='caveat', size = 14,
              fill = 'white')
    if not app.music:
        drawLine(app.width*9/10+35, app.height/5-15, app.width*9/10-35, 
                 app.height/5+15, fill = 'red')
        
def startScreen_onMousePress(app, mouseX, mouseY):
    #if button is in start button
    if (((app.width/3)-75 < mouseX < (app.width/3+75)) and 
    ((app.height*2/3)-30 < mouseY < (app.height*2/3)+30)):
        setActiveScreen('game')

    #if button is in about button
    elif ((app.width*2/3)-75 < mouseX < (app.width*2/3)+75 and 
        ((app.height*2/3)-30 < mouseY < (app.height*2/3)+30)):
        setActiveScreen('about')
