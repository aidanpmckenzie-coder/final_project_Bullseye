import turtle

class Button:
    def __init__(self, x, y, text, pen):
        self.x = x
        self.y = y
        self.text = text
        self.pen = pen 

    def draw(self):
        self.pen.goto(self.x - 60, self.y - 20)
        self.pen.pendown()
        for _ in range(2):
            self.pen.forward(120)
            self.pen.left(90)
            self.pen.forward(40)
            self.pen.left(90)
        self.pen.penup()

        self.pen.goto(self.x, self.y - 10)
        self.pen.write(self.text, align="center", font=("Arial", 14))

    def clicked(self, x, y):
        return (self.x - 60 < x < self.x + 60 and
                self.y - 20 < y < self.y + 20)