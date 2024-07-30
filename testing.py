from cmu_graphics import *

def redrawAll(app):
    drawLabel('Score: 7', 5*app.width/7, 13*app.width/70, fill = 'black',
               size = 24, bold = True)

def main():
    runApp()

main()