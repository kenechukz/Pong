
from turtle import Turtle, shape
STARTING_POSITION = (0,0)

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('white')
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.pu()


    def move(self):
        
        self.x = self.xcor() + self.x_move
        self.y = self.ycor() + self.y_move
        self.goto(self.x,self.y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1
        self.bounce_x()


