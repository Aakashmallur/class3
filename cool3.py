import pgzrun

WIDTH= 400
HEIGHT=400

def draw():
    #starting corner
    corner1=(0,0)
    corner2=(WIDTH,HEIGHT/2)
    rectangle=Rect(corner1,corner2)
    screen.draw.rect(rectangle, (0,0,255))

    corner3=(100,100)
    corner4=(WIDTH-200,50)
    rectangle2=Rect(corner3,corner4)
    screen.draw.filled_rect(rectangle2,(255,0,0))

pgzrun.go()