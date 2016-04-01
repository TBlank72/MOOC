import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("darkgrey")
	#Create turtle Todd
	todd = turtle.Turtle()
	todd.shape("turtle")
	todd.color("darkblue")
	todd.speed(0)
	todd.width(2)
	#Create turtle Kyle
	kyle = turtle.Turtle()
	kyle.shape("arrow")
	kyle.color("red")
	kyle.speed(0)
	kyle.width(2)
	#Create turtle Tim
	tim = turtle.Turtle()
	tim.color("yellow")
	tim.speed(0)
	tim.width(2)
	
	for i in range(36):
		todd.forward(100)
		todd.right(90)
		todd.forward(100)
		todd.right(90)
		todd.forward(100)
		todd.right(90)
		todd.forward(100)
		todd.right(90)
		todd.right(10)
		for i in range(3):
			tim. forward(150)
			tim.left(120)
		tim.left(10)
		kyle.circle(100)
		kyle.left(10)
	
	
	
	window.exitonclick()
	

	
draw_shapes()