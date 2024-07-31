from cmu_graphics import *

def startScreen_onAppStart(app):
    #Screen dimentions
    app.width = 700
    app.height = 700
    
    #Start button information
    app.startButtonX = app.width/3
    app.startButtonY = app.height*2/3
    app.startButtonWidth = 3*app.width/14
    app.startButtonHeight = 3*app.height/35

    #About button information
    app.aboutButtonX = app.aboutButtonY = app.width*2/3
    app.aboutButtonWidth = 3*app.width/14
    app.aboutButtonHeight = 3*app.height/35

    #Music button information
    app.musicButtonX = app.width*9/10
    app.musicButtonY = app.height/5
    app.musicButtonWidth = app.width/10
    app.musicButtonHeight = 3*app.height/70

    #music
    app.music = False

def startScreen_redrawAll(app):
    #Background
    drawRect(0, 0, app.width, app.height, fill = 'black')
    
    #Title
    drawLabel('Lauren', app.width/2, app.height/4, font = 'monospace', size = 18, 
              fill = 'white')
    drawLabel('SANDS-TRIS', app.width/2, app.height/3, font='monospace', size = 40, 
              fill = 'white')
    
    #start button
    drawRect(app.startButtonX, app.startButtonY, app.startButtonWidth, 
             app.startButtonHeight, border='white', align = 'center', fill= None)
    drawLabel('START', app.startButtonX, app.startButtonY, font='orbitron', size=40, 
              fill = 'white')
    
    #About button
    drawRect(app.aboutButtonX, app.aboutButtonY, app.aboutButtonWidth, 
             app.aboutButtonHeight, border='white', align = 'center', fill= None)
    drawLabel('ABOUT', app.aboutButtonX, app.aboutButtonY, font='orbitron', size=40,
              fill = 'white')
    
    #Music button
    drawLabel('MUSIC', app.musicButtonX, app.musicButtonY, font='caveat', size = 14,
              fill = 'white')
    if not app.music:
        drawLine(app.width*9/10+35, app.height/5-15, app.width*9/10-35, 
                 app.height/5+15, fill = 'red')
    drawRect(app.musicButtonX, app.musicButtonY, app.musicButtonWidth, 
             app.musicButtonHeight, align = 'center', fill = None, 
             border = 'white')
        
def startScreen_onMousePress(app, mouseX, mouseY):
    #if button is in start button
    if (((app.width/3)-75 < mouseX < (app.width/3+75)) and 
    ((app.height*2/3)-30 < mouseY < (app.height*2/3)+30)):
        setActiveScreen('game')

    #if button is in about button
    elif ((app.width*2/3)-75 < mouseX < (app.width*2/3)+75 and 
        ((app.height*2/3)-30 < mouseY < (app.height*2/3)+30)):
        setActiveScreen('about')
    
    #if button is in music button
    elif ((app.musicButtonX - app.musicButtonWidth/2) < mouseX < 
          (app.musicButtonX + app.musicButtonWidth/2) and 
          (app.musicButtonY - app.musicButtonHeight/2) < mouseY <
          (app.musicButtonY + app.musicButtonHeight/2)):
        app.music = not app.music
