import turtle



def recursSquare(turt, repeat, repeatTotal):
    #this terminates the recursive instance so it does not go on indefinetly
    if repeat > repeatTotal:
        return
    else:
        #drawing loop repeats four times to create a square, It simply makes a
        #circle followed by a line
        for i in range(4):
            #2 is raised to the power of repeat because the lines need to grow shorter
            #while the number of repeats increases.  The figures get smaller as repeats
            #bigger.  This is about the simplest formula to do so.
            #Raising to the 0th power returns 1, so the result will always be valid.
            #The basic figure is a circle followed by a line drawn out from
            #the beginning of the circle.
            turt.circle(90/(2**repeat))
            turt.forward(270/(2**repeat))
            #the loop goes biggest>middle>four smalls>middle>four smalls . . .
            #It makes one of each figure until the smallest, which makes a
            #complete set of four figures.
            #repeat increases by 1 for a new, smaller figure
            recursSquare(turt, repeat + 1, repeatTotal)
            #Changes angle so the figure continues in new direction
            turt.left(90)
    return

def draw_figure():
    window = turtle.Screen()
    window.bgcolor("yellow")
    bill = turtle.Turtle()
    bill.color("blue")
    bill.shape("arrow")
    bill.speed(1)
    recursSquare(bill, 0, 2)
    window.exitonclick()

draw_figure()
