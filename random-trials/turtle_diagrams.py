import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Spiral")

t = turtle.Turtle()
t.speed(-100)

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "violet"]

for i in range(1000):
    t.color(colors[i % len(colors)])
    t.forward(i * 0.5)
    t.right(91)

turtle.done()
