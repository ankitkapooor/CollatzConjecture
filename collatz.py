import matplotlib.pyplot as plt
import networkx as nx

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

series = []
xaxis = []
daglist = []
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

def print_collatz(number):
    collatz(number)
    print(series)

def graph(number):
    collatz(number)
    for i in range(len(series)):
        xaxis.append(i)
    plt.plot(xaxis, series)
    #plt.show()

for number in range(1, 10001):
    print_collatz(number)
    #collatz(number)
    for i in range(len(series)):
        xaxis.append(i)
    plt.plot(xaxis, series)
    series = []
    xaxis =[]

plt.show()
#print(daglist)
