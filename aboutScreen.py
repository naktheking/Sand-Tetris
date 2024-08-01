from cmu_graphics import *
from PIL import Image

def about_onAppStart(app):
    app.width = 700
    app.height = 700
    app.boardWidth = app.width/2
    app.boardHeight = app.height-20
    app.leftBoardCoordinate = app.width//2-(7*app.boardWidth//10)
    app.topBoardCoordinate = app.height//2-(app.boardHeight//2)

    app.homeButtonImage = CMUImage(Image.open('button.png'))

def about_redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'black')

    #Title
    drawLabel('Lauren Sands-Tris', app.width/2, 4*app.height/20, fill = 'white', 
               size = 30)
    drawLabel('Controls', app.width/2, 6*app.height/20, fill = 'white', 
               size = 20)
    
    
    #Move Right
    drawLabel('Move Left/Right/Down', app.width/4, 8*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('Left/Right/Down Arrow key', (2*app.width/4)+60, 8*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    
    #Rotating
    drawLabel('Rotate Clockwise', app.width/4, 9*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('Up Arrow Key', (2*app.width/4)+60, 9*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    
    #Instant Down
    drawLabel('Instant Down', app.width/4, 10*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('Space Bar', (2*app.width/4)+60, 10*app.height/20, fill = 'white', 
               size = 17, align = 'left')

    #Pause/unpause
    drawLabel('Pause/unpause', app.width/4, 11*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('p', (2*app.width/4)+60, 11*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    
    #Fast moving
    drawLabel('Move Sideways Faster:', app.width/4, 12*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('s', (2*app.width/4)+60, 12*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    

    #Credits
    drawLabel('Credits', app.width/2, 14*app.height/20, fill = 'white', 
               size = 25,  bold = True)
    
    #Creator
    drawLabel('Creator:', app.width/4, 15*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('Max Zhang', (2*app.width/4)+60, 15*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    
    #SFX
    drawLabel('Sound Effects:', app.width/4, 16*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('Oliver Zhang', (2*app.width/4)+60, 16*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    
    #BGM
    drawLabel('Background Music:', app.width/4, 17*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    drawLabel('King Wang', (2*app.width/4)+60, 17*app.height/20, fill = 'white', 
               size = 17, align = 'left')
    
    
    #Home Button
    drawImage(app.homeButtonImage, 80, 70, width = 50, height = 45, align = 'center')
    drawRect(80, 70, 50, 45, align = 'center', fill = None, border = 'white')

def about_onMousePress(app, mouseX, mouseY):
    #if button is in start button
    if ((55 < mouseX < 105) and 
        (45 < mouseY < 95)):
        setActiveScreen('startScreen')