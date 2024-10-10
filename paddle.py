from turtle import Turtle

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__(shape='square')
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.color('white')

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)

    def stop(self):
        pass
        