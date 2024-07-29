from cmu_graphics import *

def redrawAll(app):
    peru = rgb(205, 133, 63)
    chocolate = rgb(210, 105, 30)
    gray = rgb(43, 43, 40)


    drawRect(0, 0, app.width, app.height, fill = gray, opacity = 50)
    
    drawLabel('PAUSED',app.width/2, app.height/5, size = 24)

    drawRect(app.width/2, 2*app.height/5, 120, 50, align = 'center', fill = peru)
    drawLabel('RESUME', app.width/2, 2*app.height/5, bold = True, font='monospace', 
               size = 24)
    

    drawRect(app.width/2, 3*app.height/5, 150, 50, align = 'center', fill = chocolate)
    drawLabel('NEW GAME', app.width/2, 3*app.height/5, bold = True, font='monospace', 
               size = 24)
    

def main():
    runApp()

main()