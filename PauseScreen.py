from cmu_graphics import *

def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 75)
    drawRect(app.width/2, 2*app.height/5, 120, 50, align = 'center', fill = 'gray')
    drawLabel('resume', app.width/2, 2*app.height/5, bold = True, font='monospace', 
               size = 24)
    drawRect(app.width/2, 3*app.height/5, 150, 50, align = 'center', fill = 'gray')
    drawLabel('new game', app.width/2, 3*app.height/5, bold = True, font='monospace', 
               size = 24)
    

def main():
    runApp()

main()