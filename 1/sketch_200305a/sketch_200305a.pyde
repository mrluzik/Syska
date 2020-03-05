def setup():
    size(600,600)
    point(50,50)
def draw():
    rectMode(CENTER)
    rect(300,300,300,300)
    fill(100,100,100,100)
    print(height, width, mouseX, mouseY, mousePressed)
    line(height, width, mouseX, mouseY)
    if mousePressed:
            rect(mouseX,mouseY, mouseX, mouseY)
