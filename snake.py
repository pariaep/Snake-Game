from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEPS = 20
UP = 90
DOWN = -90
RIGHT = 0
LEFT = 180
class Snake:

    def __init__(self, ):
        self.cubes = []
        self.creat_snake()
        self.head = self.cubes[0]

    def creat_snake(self):
        for n in POSITIONS:
            self.add_cube(n)

    def add_cube(self, n):
        new_cube = Turtle("square")
        new_cube.color("white")
        new_cube.penup()
        new_cube.goto(n)
        self.cubes.append(new_cube)


    def extend(self):
        self.add_cube(self.cubes[-1].position())


    def move(self):
        for cube_number in range(len(self.cubes) - 1, 0, -1):
            new_x = self.cubes[cube_number - 1].xcor()
            new_y = self.cubes[cube_number - 1].ycor()
            self.cubes[cube_number].goto(new_x, new_y)
        self.head.fd(STEPS)

    def reset(self):
        for cube in self.cubes:
            cube.goto(1000, 1000)
        self.cubes.clear()
        self.creat_snake()
        self.head = self.cubes[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)