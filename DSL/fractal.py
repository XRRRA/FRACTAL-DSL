import random
import turtle


def capital(size, depth):
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


class Fractal:
    def __init__(self):
        self.points_nr = 100  # default number of points (fern)
        self.depth = 5  # default depth
        self.size = 700  # default size
        self.color = 'black'  # default color
        self.speed = 0  # default speed
        self.shape = 'triangle'  # default shape
        self.background = 'white'  # default background color

    def set_size(self, size):
        self.size = size

    def set_points_nr(self, points_nr):
        self.points_nr = points_nr

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
        turtle.hideturtle()

        def start_at(x, y):
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

        if self.shape == 'triangle':
            start_at(-self.size / 2, -self.size / 2.5)
            self.draw_sierpinski_triangle(self.size, self.depth)
        elif self.shape == 'koch' or self.shape == 'koch snowflake':
            start_at(-self.size / 2.5, self.size / 4)
            self.draw_koch_snowflake(self.size / 1.25, self.depth)
        elif self.shape == 'dragon':
            start_at(0, 0)
            self.draw_dragon_curve(self.size * 10, self.depth)
        elif self.shape == 'capital':
            start_at(0, 0)
            capital(self.size / 2, self.depth)
        elif self.shape == 'fern' or self.shape == 'barnsley fern':
            start_at(0, -self.size)
            self.draw_barnsley_fern(self.points_nr)

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
            self.draw_inverse_dragon_curve(length / 2, depth - 1)

    def draw_inverse_dragon_curve(self, length, depth):
        if depth == 0:
            turtle.forward(length)
        else:
            self.draw_dragon_curve(length / 2, depth - 1)
            turtle.left(90)
            self.draw_inverse_dragon_curve(length / 2, depth - 1)

    def draw_barnsley_fern(self, points_nr):
        turtle.tracer(0, 0)

        p = (0, 0)
        turtle.up()
        turtle.hideturtle()
        for i in range(points_nr):
            turtle.goto(p[0] * self.size / 10, p[1] * self.size / 10 - (self.size / 2))
            turtle.dot(2, self.color)
            r = random.uniform(0, 1)
            if r < 0.01:
                p = (0, 0.16 * p[1])
            elif r < 0.86:
                p = (0.85 * p[0] + 0.04 * p[1], -0.04 * p[0] + 0.85 * p[1] + 1.6)
            elif r < 0.93:
                p = (0.2 * p[0] - 0.26 * p[1], 0.23 * p[0] + 0.22 * p[1] + 1.6)
            else:
                p = (-0.15 * p[0] + 0.28 * p[1], 0.26 * p[0] + 0.24 * p[1] + 0.44)

            if i % 1000 == 0:
                turtle.up()
                turtle.hideturtle()
                turtle.update()
