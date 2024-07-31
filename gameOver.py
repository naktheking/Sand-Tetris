from cmu_graphics import *

def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 50)

    # drawOval(app.width/2, app.height/4, 150, 70, fill = 'white')
    drawLabel('GAME OVER', app.width/2, app.height/4, bold = True, font='monospace', 
               size = 24)


    drawRect(app.width/2, 3*app.height/5, 150, 40, align = 'center', fill = 'white')
    drawLabel('New Game', app.width/2, 3*app.height/5, bold = True, font='sacramento',
               size = 24)

def main():
    runApp()

main()