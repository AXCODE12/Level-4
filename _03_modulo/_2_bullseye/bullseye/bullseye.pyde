def setup():
    # Set the size of your sketch
    
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    
    # Use an if statement and modulo to alternate the color of your rings
    
    
    pass
def setup():
    # Set the size of your sketch
    size(300,300)

    pass

def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    for i in range(8):
    # Use an if statement and modulo to alternate the color of your ring
        if i % 2 ==0:
            fill(200,0,0)
            ellipse(145,140,152-15*(i+1),152-15*(i+1))

        else:
            fill(0,0,0)
            ellipse(145,140,152-15*(i+1),152-15*(i+1))