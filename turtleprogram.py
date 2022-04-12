import turtle

turtle.shape('turtle')
turtle.speed(1)
counter=1

while counter <=36:
	for i in range(4):
		turtle.forward(200)
		turtle.right(90)
		turtle.left(10)
		counter+=1
		
		turtle.exitonclick
