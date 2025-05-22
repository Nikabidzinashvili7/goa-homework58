from turtle import*
#drawing a house 
# step 1 draw a square 
speed(12)

width (5)


forward (200) 
left(90)

forward(200)
left (90)

forward (200)
left(90)
 
forward(200)
left(90)

#done
# step 2 draw a door
forward (70)
begin_fill()
color("green")

left (90)
forward (120) #size of the door
right(90)
forward(60)
right (90)
forward(120)
end_fill()
#done 
#step 3 draw a roof 
penup()
goto(200,200)
pendown() 


begin_fill()
right (150)
forward (200)
left(120)
forward(200)
end_fill()

#done
#last step  draw a windows 
penup()
goto(200,130)
pendown()
right(60)
forward (40)
left(90)
forward(40)
left(90)
forward (40)
left (90)
forward(40) 
left (90)
forward (20)
left(90)
forward (40)
left (90)
forward (20)
left(90)
forward(20)
left(90)
forward (40)

penup()
goto(200,200)
pendown()
right(90)
left(90)
forward(200)
left(90)
forward(110)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward (40)
left(180)
right(90)

forward(20)
left(90)
forward(40)
left(90)
forward(20)
left(90)
forward(20)
left(90)
forward(45)
# done here is the house.
exitonclick()