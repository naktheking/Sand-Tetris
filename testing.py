from cmu_graphics import *
def screen1_onAppStart(app):
    app.title = 'skibo'

def screen1_redrawAll(app):
    drawLabel(app.title, app.width/2, app.height/2, size = 40)

def change(app):
    app.title = 'skibo changed'

def screen2_onAppStart(app):
    app.title = 'skibo2'

def screen2_redrawAll(app):
    drawLabel(app.title, app.width/2, app.height/2, size = 40)










def main():
    runAppWithScreens(initialScreen='screen1', width=800, height=800)

main()






# def redrawAll(app):
#     drawLabel('Arial font (default)', 200, 50, font='arial', size=20)
#     drawLabel('Monospace font', 200, 90, font='monospace', size=20)
#     drawLabel('Caveat font', 200, 130, font='caveat', size=20)
#     drawLabel('Cinzel font', 200, 170, font='cinzel', size=20)
#     drawLabel('Montserrat font', 200, 210, font='montserrat', size=20)
#     drawLabel('Grenze font', 200, 250, font='grenze', size=20)
#     drawLabel('Sacramento font', 200, 290, font='sacramento', size=20)
#     drawLabel('Orbitron font', 200, 330, font='orbitron', size=20)

# def main():
#     runApp()

# main()