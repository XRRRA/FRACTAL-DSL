import turtle


class Fractal:
    def __init__(self):
        self.depth = 5  # default depth
        self.size = 700  # default size
        self.color = 'black'  # default color
        self.speed = 0  # default speed
        self.shape = 'triangle'  # default shape
        self.background = 'white'  # default background color

    def set_size(self, size):
        self.size = size

    def set_color(self, color):
        self.color = color

    def set_speed(self, speed):
        self.speed = speed

    def set_depth(self, depth):
        self.depth = depth

    def set_shape(self, shape):
        self.shape = shape

    def set_background(self, background):
        self.background = background

    def draw(self):
        turtle.setup(width=self.size, height=self.size)
        turtle.bgcolor(self.background)
        turtle.speed(self.speed)
        turtle.color(self.color)

        def start_at(x, y):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

        if self.shape == 'triangle':
            start_at(-self.size / 2, -self.size / 2)
            self.draw_sierpinski_triangle(self.size, self.depth)
        elif self.shape == 'snowflake':
            start_at(-self.size / 2, self.size / 4)
            self.draw_koch_snowflake(self.size, self.depth)
        elif self.shape == 'dragon':
            start_at(0, 0)
            self.draw_dragon_curve(self.size * 10, self.depth)
        elif self.shape == 'capital':
            start_at(0, 0)
            self.capital(self.size / 2, self.depth)

        turtle.done()

    # Fractal functions
    # Sierpinski triangle
    def draw_sierpinski_triangle(self, side_length, depth):
        if depth == 0:
            for _ in range(3):
                turtle.forward(side_length)
                turtle.left(120)
        else:
            self.draw_sierpinski_triangle(side_length / 2, depth - 1)
            turtle.forward(side_length / 2)
            self.draw_sierpinski_triangle(side_length / 2, depth - 1)
            turtle.backward(side_length / 2)
            turtle.left(60)
            turtle.forward(side_length / 2)
            turtle.right(60)
            self.draw_sierpinski_triangle(side_length / 2, depth - 1)
            turtle.left(60)
            turtle.backward(side_length / 2)
            turtle.right(60)

    # Koch snowflake
    def draw_koch_snowflake(self, side_length, depth):
        for _ in range(3):
            self.draw_koch_curve(side_length, depth)
            turtle.right(120)

    def draw_koch_curve(self, length, depth):
        if depth == 0:
            turtle.forward(length)
        else:
            self.draw_koch_curve(length / 3, depth - 1)
            turtle.left(60)
            self.draw_koch_curve(length / 3, depth - 1)
            turtle.right(120)
            self.draw_koch_curve(length / 3, depth - 1)
            turtle.left(60)
            self.draw_koch_curve(length / 3, depth - 1)

    # Dragon curve
    def draw_dragon_curve(self, length, depth):
        if depth == 0:
            turtle.forward(length)
        else:
            self.draw_dragon_curve(length / 2, depth - 1)
            turtle.right(90)

    # Capital I
    def capital(self, size, depth):
        def draw_capital_I(x, y, length, n):
            if n == 0:
                return
            turtle.penup()
            turtle.goto(x - length, y + length)
            turtle.pendown()
            turtle.setheading(0)
            turtle.forward(2 * length)
            turtle.penup()
            turtle.goto(x - length, y - length)
            turtle.pendown()
            turtle.forward(2 * length)
            turtle.penup()
            turtle.goto(x, y + length)
            turtle.pendown()
            turtle.setheading(270)
            turtle.forward(2 * length)

            draw_capital_I(x - length, y + length, length / 2, n - 1)
            draw_capital_I(x + length, y + length, length / 2, n - 1)
            draw_capital_I(x + length, y - length, length / 2, n - 1)
            draw_capital_I(x - length, y - length, length / 2, n - 1)

        draw_capital_I(0, 0, size / 2, depth)
