import turtle

list = [11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
list2 = [18, 9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
turt = turtle.Turtle()
turt.speed(0)
turtle.mode(mode = "logo")
turt.penup()
turt.setpos(-300,-300)
turt.pendown()
turt.width(3)
turtle.colormode(255)
turt.pencolor("blue")
turtle.Screen().bgcolor("cyan")


def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

#count = 0
series = []
def collatz(number):
    series.append(int(number))
    if is_even(number):
        number = number/2
        #series.append(int(number))
        collatz(number)
    elif not is_even(number) and number != 1:
        number = 3*number + 1
        #series.append(int(number))
        collatz(number)
    elif number == 1:
        pass

def draw(series):
    count = 0
    for number in series:
        if number%2 == 0:
            turt.right(15)
            turt.forward(20)
        else:
            turt.left(15)
            turt.forward(20)
        count+=1
    turt.penup()
    turt.goto(-300, -300)
    turt.setheading(0)
    turt.pendown()

for i in range(1, 20):
    collatz(i)
    draw(series)
    print(series)
    series = []

turtle.done()
