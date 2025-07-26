import another_module as am

print(am.another_variable)

#import turtle

#timmy = turtle.Turtle()

from turtle import Turtle,Screen

timmy = Turtle()

print(timmy)
timmy.shape("turtle")

timmy.color("green")

timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



from prettytable import PrettyTable

table = PrettyTable()



table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align["Pokemon"] = "l"
table.align["Type"]="r"
print(table)