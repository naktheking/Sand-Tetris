from cmu_graphics import *

def startScreen_onAppStart(app):
    # Screen dimensions
    app.width = 700
    app.height = 700
    
    # Start button information
    app.startButtonX = app.width / 3
    app.startButtonY = app.height * 2 / 3
    app.startButtonWidth = 3 * app.width / 14
    app.startButtonHeight = 3 * app.height / 35

    # About button information
    app.aboutButtonX = app.aboutButtonY = app.width * 2 / 3
    app.aboutButtonWidth = 3 * app.width / 14
    app.aboutButtonHeight = 3 * app.height / 35


def startScreen_redrawAll(app):
    # Background
    drawRect(0, 0, app.width, app.height, fill=rgb(46, 46, 46))
    
    # Title
    drawLabel('Lauren', app.width / 2, app.height / 4, font='monospace', size=18, 
              fill='white')
    drawLabel('SANDS-TRIS', app.width / 2, app.height / 3, font='monospace', size=40, 
              fill='white')
    
    # Start button shadow
    drawRect(app.startButtonX, app.height * 2 / 3 + 10, app.startButtonWidth, 
             app.startButtonHeight, align='center', fill=rgb(28, 28, 28))
    
    # Start button
    drawRect(app.startButtonX, app.startButtonY, app.startButtonWidth, 
             app.startButtonHeight, border=rgb(0, 255, 0), align='center', fill=rgb(50, 50, 50))
    
    drawLabel('START', app.startButtonX, app.startButtonY, font='orbitron', size=40, 
              fill=rgb(0, 255, 0))
    
    # About button shadow
    drawRect(app.aboutButtonX, app.width * 2 / 3 + 10, app.aboutButtonWidth, 
             app.aboutButtonHeight, align='center', fill=rgb(28, 28, 28))
    
    # About button
    drawRect(app.aboutButtonX, app.aboutButtonY, app.aboutButtonWidth, 
             app.aboutButtonHeight, border=rgb(0, 255, 0), align='center', fill=rgb(50, 50, 50))
    
    drawLabel('ABOUT', app.aboutButtonX, app.aboutButtonY, font='orbitron', size=40,
              fill=rgb(0, 255, 0))
        
def startScreen_onMousePress(app, mouseX, mouseY):
    # If button is in start button
    if (((app.width / 3) - 75 < mouseX < (app.width / 3 + 75)) and 
    ((app.height * 2 / 3) - 30 < mouseY < (app.height * 2 / 3) + 30)):
        setActiveScreen('game')

    # If button is in about button
    elif ((app.width * 2 / 3) - 75 < mouseX < (app.width * 2 / 3) + 75 and 
        ((app.height * 2 / 3) - 30 < mouseY < (app.height * 2 / 3) + 30)):
        setActiveScreen('about')
    

def startScreen_onMouseMove(app, mouseX, mouseY):
    # If mouse is over start button, move everything down
    if (((app.width / 3) - 75 < mouseX < (app.width / 3 + 75)) and 
        ((app.height * 2 / 3) - 30 < mouseY < (app.height * 2 / 3) + 30)):
        app.startButtonY = app.height * 2 / 3 + 5

    #if mouse is over about button
    elif ((app.width * 2 / 3) - 75 < mouseX < (app.width * 2 / 3) + 75 and 
        ((app.height * 2 / 3) - 30 < mouseY < (app.height * 2 / 3) + 30)):
        app.aboutButtonY = app.width * 2 / 3 + 5
    
    #not on either button
    else:
        app.startButtonY = app.height * 2 / 3
        app.aboutButtonY = app.width * 2 / 3