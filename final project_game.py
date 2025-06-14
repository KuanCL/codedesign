import turtle
import random

def draw_rounded_rectangle(turtle , width , height , radius, color , posx , posy ) :
    turtle.penup()
    turtle.goto(posx, posy)
    turtle.setheading(0)
    turtle.forward(width/2)
    turtle.right(90)
    turtle.forward(height/2-radius)
    turtle.setheading(90)
    turtle.pendown()

    turtle.color(color, color)
    turtle.begin_fill()
    turtle.forward(height-radius*2)
    turtle.circle(radius, 90)
    turtle.forward(width-radius*2)
    turtle.circle(radius, 90)
    turtle.forward(height-radius*2)
    turtle.circle(radius, 90)
    turtle.forward(width-radius*2)
    turtle.circle(radius, 90)
    turtle.end_fill()

    return None

def func1(x1, y1):
    global x0, y0
    x0, y0 = x1, y1

def q():
    global _time
    _time = False

def create_grid(size, r, g, b):
    a.clear()
    x_spacing = 600 / size
    y_spacing = 600 / size
    l = x_spacing - 10  # Define 'l' here within the function
    target_index = random.randint(1, size * size)
    current_index = 1
    target_x, target_y = 0, 0

    for row in range(size):
        for col in range(size):
            x = -300 + x_spacing / 2 + col * x_spacing
            y = 300 - y_spacing / 2 - row * y_spacing
            if current_index == target_index:
                r0 = r + 20 if r < 235 else r - 20
                g0 = g + 20 if g < 235 else g - 20
                b0 = b + 20 if b < 235 else b - 20
                target_x, target_y = x, y
                draw_rounded_rectangle(a, l, l, 10, (r0, g0, b0), x, y)
            else:
                draw_rounded_rectangle(a, l, l, 10, (r, g, b), x, y)
            current_index += 1

    return target_x, target_y, l

# Initialize
a = turtle.Turtle()
a.hideturtle()
s = turtle.Screen()
s.colormode(255)
s.setup(610, 610)
s.tracer(0)
s.onclick(func1)
s.ontimer(q, t=15 * 1000)

x0, y0 = -500, -500
_time = True
Lv = 0
size = 2

# Game loop
while _time:
    r, g, b = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)
    X, Y,l = create_grid(size, r, g, b)  # Call create_grid function
    while _time:
        s.update()
        if X - l / 2 < x0 < X + l / 2 and Y - l / 2 < y0 < Y + l / 2:  # Access 'l' within the correct scope
            Lv += 1
            size += 1
            x0, y0 = -500, -500
            break

print('Score：', Lv)