import math
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


def circle(x, y, radius):
    turtle.up()
    turtle.goto(x, y - radius)
    turtle.down()
    turtle.seth(0)
    turtle.circle(radius, steps=360)


def two_circles(x, y, radius, orientation):
    turtle.pensize(radius / 50)
    if orientation == 0:
        circle(x - radius / 2, y, radius)
        circle(x + radius / 2, y, radius)
    else:
        circle(x, y - radius / 2, radius)
        circle(x, y + radius / 2, radius)


def line(x, y, length, direction, pensize):
    turtle.up()
    turtle.pensize(pensize)
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(direction)
    turtle.fd(length)


def five_pointed_star(x, y, direction, r):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(direction)
    turtle.fd(r)
    turtle.right(180 - 18)
    turtle.down()
    length = r * math.sin(math.pi * 2 / 5) / (1 + math.sin(math.pi / 10))
    for _ in range(5):
        turtle.fd(length)
        turtle.left(72)
        turtle.fd(length)
        turtle.right(180 - 36)


def star(x, y, length, penc, fillcolor):
    turtle.up()
    turtle.goto(x, y)
    turtle.seth(90)
    turtle.fd(length)
    turtle.seth(180 + 36 / 2)
    L = length * math.sin(36 * math.pi / 180) / math.sin(54 * math.pi / 180)
    turtle.seth(180 + 72)
    turtle.down()
    turtle.fillcolor(fillcolor)
    turtle.pencolor(penc)
    turtle.begin_fill()
    for _ in range(5):
        turtle.fd(L)
        turtle.right(72)
        turtle.fd(L)
        turtle.left(144)
    turtle.end_fill()


def star_fractal(x, y, length, penc, fillcolor, n):
    if n == 0:
        star(x, y, length, penc, fillcolor)
        return
    length2 = length / (1 + (math.sin(18 * math.pi / 180) + 1) / math.sin(54 * math.pi / 180))
    length - length2 - length2 * math.sin(18 * math.pi / 180) / math.sin(54 * math.pi / 180)
    for i in range(5):
        star_fractal(x + math.cos((90 + i * 72) * math.pi / 180) * (length - length2),
                     y + math.sin((90 + i * 72) * math.pi / 180) * (length - length2),
                     length2, penc, fillcolor, n - 1)


def draw_cross(x, y, length, fillcolor, penc):
    turtle.up()
    turtle.goto(x - length / 2, y - length / 6)
    turtle.down()
    turtle.seth(0)
    turtle.fillcolor(fillcolor)
    turtle.pencolor(penc)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length / 3)
        turtle.right(90)
        turtle.fd(length / 3)
        turtle.left(90)
        turtle.fd(length / 3)
        turtle.left(90)
    turtle.end_fill()


def draw_stacked_squares(x, y, length, n, fillcolor, penc):
    def stacksquares(x, y, length, n, fillcolor, penc):
        if n == 0:
            return
        stacksquares(x - length / 2, y - length / 2, length / 2, n - 1, fillcolor, penc)
        stacksquares(x + length / 2, y + length / 2, length / 2, n - 1, fillcolor, penc)
        stacksquares(x - length / 2, y + length / 2, length / 2, n - 1, fillcolor, penc)
        stacksquares(x + length / 2, y - length / 2, length / 2, n - 1, fillcolor, penc)

        turtle.up()
        turtle.goto(x - length / 2, y - length / 2)
        turtle.down()
        turtle.seth(0)
        turtle.fillcolor(fillcolor)
        turtle.pencolor(penc)
        turtle.begin_fill()
        for _ in range(4):
            turtle.fd(length)
            turtle.left(90)
        turtle.end_fill()

    stacksquares(x, y, length, n, fillcolor, penc)


class Fractal:
    def __init__(self):
        self.edges = 6  # default number of edges (snowflake)
        self.direction = 90  # default direction (star)
        self.length = 2  # default max length (golden tree)
        self.points_nr = 100  # default number of points (fern)
        self.depth = 5  # default depth
        self.size = 700  # default size
        self.color = 'black'  # default color
        self.speed = 0  # default speed
        self.shape = 'triangle'  # default shape
        self.background = 'white'  # default background color
        self.fill = "false"  # default fill value
        self.instant = "false"  # not to draw in an instant by default
        self.ratio = '0.4'  # default ratio for Cesaro fractal

    def set_size(self, size):
        self.size = size

    def set_edges(self, edges):
        self.edges = edges

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

    def set_instant(self, instant):
        self.instant = instant

    def set_fill(self, fill):
        self.fill = fill

    def set_background(self, background):
        self.background = background

    def set_length(self, length):
        self.length = length

    def set_direction(self, direction):
        self.direction = direction

    def set_ratio(self, ratio):
        self.ratio = ratio

    def draw(self):
        turtle.setup(width=self.size, height=self.size)
        turtle.bgcolor(self.background)
        turtle.speed(self.speed)
        turtle.color(self.color)
        turtle.hideturtle()
        if self.instant == "true":
            turtle.tracer(0)

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
            self.draw_barnsley_fern(self.points_nr)
        elif self.shape == 'tree' or self.shape == 'golden tree':
            self.draw_golden_fractal_tree(90, self.size / 4, self.depth)
        elif self.shape == 'star':
            self.five_pointed_star_fractal(0, -40, self.direction, self.size / 2)
        elif self.shape == 'snowflake':
            self.snowflake(self.size / 3, self.depth, self.edges)
        elif self.shape == 'gardi' or self.shape == 'circle':
            start_at(0, 0)
            self.gardi_fractal(0, 0, self.size / 3, self.direction, self.depth)
        elif self.shape == 'spiral':
            start_at(0, 0)
            self.draw_spiral(self.size, self.direction)
        elif self.shape == 'star fractal':
            if self.fill == "true":
                star_fractal(0, 0, self.size / 2, self.color, self.color, self.depth)
            else:
                star_fractal(0, 0, self.size / 2, self.color, self.background, self.depth)
        elif self.shape == 'vicsek' or self.shape == 'cross':
            start_at(0, 0)
            if self.fill == "true":
                self.vicsek_fractal(0, 0, self.size, self.depth, self.color, self.color)
            else:
                self.vicsek_fractal(0, 0, self.size, self.depth, self.background, self.color)
        elif self.shape == 'cesaro' or self.shape == 'square':
            scale = 4
            start_at(-self.size / 2, -self.size / 2)
            self.Cesaro(-self.size / scale, -self.size / scale, -self.size / scale, self.size / scale, float(self.ratio))
            self.Cesaro(-self.size / scale, self.size / scale, self.size / scale, self.size / scale, float(self.ratio))
            self.Cesaro(self.size / scale, self.size / scale, self.size / scale, -self.size / scale, float(self.ratio))
            self.Cesaro(self.size / scale, -self.size / scale, -self.size / scale, -self.size / scale, float(self.ratio))
        elif self.shape == 'stacked squares':  # Add this block for the new shape
            if self.fill == "true":
                draw_stacked_squares(0, 0, self.size/2, self.depth, self.color, self.color)
            else:
                draw_stacked_squares(0, 0, self.size/2, self.depth, self.background, self.color)
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

    # Golden Fractal Tree
    def draw_golden_fractal_tree(self, direction, length, depths):
        golden_ratio = (1 + 5 ** 0.5) / 2
        turtle.speed(0)
        turtle.tracer(0, 0)

        def golden_fractal_tree(x, y, directions, lengths, depth):
            turtle.up()
            turtle.goto(x, y)
            turtle.seth(directions)
            turtle.pensize(int(math.log(lengths, 2) / 3))
            if lengths < depth:
                turtle.color('forest green')
            else:
                turtle.color(self.color)
            turtle.down()
            turtle.fd(lengths)
            if lengths < self.length:
                return
            cx, cy = turtle.xcor(), turtle.ycor()
            golden_fractal_tree(cx, cy, directions + 72, (2 - golden_ratio) * lengths, depth)
            golden_fractal_tree(cx, cy, directions - 72, (2 - golden_ratio) * lengths, depth)
            golden_fractal_tree(cx, cy, directions, (golden_ratio - 1) * lengths, depth)

        golden_fractal_tree(0, -self.size / 2, direction, length, depths)
        turtle.update()

    # Five Pointed Star Fractal
    def five_pointed_star_fractal(self, x, y, direction, r):
        five_pointed_star(x, y, direction, r)
        if r < 20:
            return
        self.five_pointed_star_fractal(x, y, 180 + direction, r * math.sin(math.pi / 10) / math.cos(math.pi / 5))

    # Snowflake function
    def snowflake(self, length, depth, edges):
        for i in range(edges):
            self.line_fractal(0, 0, length, i * 360 / edges, 3, depth)

    def line_fractal(self, x, y, length, direction, pensize, n):
        if n == 0:
            return
        line(x, y, length, direction, pensize)
        self.line_fractal(x + math.cos(direction * math.pi / 180) * length * 2 / 5,
                          y + math.sin(direction * math.pi / 180) * length * 2 / 5,
                          length * 3 / 5,
                          direction - 25,
                          pensize * 3 / 5,
                          n - 1)
        self.line_fractal(x + math.cos(direction * math.pi / 180) * length * 2 / 5,
                          y + math.sin(direction * math.pi / 180) * length * 2 / 5,
                          length * 3 / 5,
                          direction + 25,
                          pensize * 3 / 5,
                          n - 1)

    # Gardi Fractal
    def gardi_fractal(self, x, y, radius, orientation, n):
        if n == 0:
            return
        two_circles(x, y, radius, orientation)
        self.gardi_fractal(x, y, (4 - 7 ** 0.5) / 3 * radius, 1 - orientation, n - 1)

    # Spiral of Spirals
    def draw_spiral(self, length, direction):
        c = 0
        while length > 1 or c < 20:
            if length > 2:
                self.draw_spiral(length * 0.255, 160 + direction)
            turtle.up()
            turtle.seth(direction)
            turtle.goto(turtle.xcor(), turtle.ycor())
            if length <= 2:
                turtle.down()
            turtle.fd(length)
            length *= 0.93
            direction += 20
            c += 1

    # Cross fractal
    def vicsek_fractal(self, x, y, length, n, fillcolor, penc):
        if n == 0:
            draw_cross(x, y, length, fillcolor, penc)
            return

        self.vicsek_fractal(x, y, length / 3, n - 1, fillcolor, penc)
        self.vicsek_fractal(x + length / 3, y, length / 3, n - 1, fillcolor, penc)
        self.vicsek_fractal(x - length / 3, y, length / 3, n - 1, fillcolor, penc)
        self.vicsek_fractal(x, y + length / 3, length / 3, n - 1, fillcolor, penc)
        self.vicsek_fractal(x, y - length / 3, length / 3, n - 1, fillcolor, penc)

    # Cesaro fractal
    def Cesaro(self, x1, y1, x2, y2, ratio):
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if dist < 5:  # Adjust the threshold for stopping recursion
            turtle.goto(x2, y2)
            return
        direction = math.atan2(y2 - y1, x2 - x1)
        px1, py1 = x1 + dist * ratio * math.cos(direction), y1 + dist * ratio * math.sin(direction)
        px3, py3 = x1 + dist * (1 - ratio) * math.cos(direction), y1 + dist * (1 - ratio) * math.sin(direction)
        ptx, pty = (px1 + px3) / 2, (py1 + py3) / 2
        d = ((dist * ratio) ** 2 - (dist * (1 - 2 * ratio) / 2) ** 2) ** 0.5
        px2, py2 = ptx + d * math.cos(direction + math.radians(90)), pty + d * math.sin(direction + math.radians(90))

        self.Cesaro(x1, y1, px1, py1, ratio)
        self.Cesaro(px1, py1, px2, py2, ratio)
        self.Cesaro(px2, py2, px3, py3, ratio)
        self.Cesaro(px3, py3, x2, y2, ratio)
