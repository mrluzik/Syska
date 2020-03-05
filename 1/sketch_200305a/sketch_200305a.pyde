def setup():
    size(600,600)
    point(50,50)
    rectMode(CENTER)
    rect(300,300,300,300)
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    line(height, width, mouseX, mouseY)
    if mousePressed:
            rect(mouseX,mouseY, mouseX, mouseY)
