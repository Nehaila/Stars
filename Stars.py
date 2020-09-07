import turtle
stars= turtle.Turtle()
stars.getscreen().bgcolor("yellow")
stars.setheading(180)
def starz(size):
	if size < 10: 
		return 
	else: 
		for j in range(5):
			stars.left(144)
			stars.forward(size)
			starz(size/3)
starz(500)
turtle.done()