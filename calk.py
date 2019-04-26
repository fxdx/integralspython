import matplotlib.pyplot as plt
import numpy as np
import re


def fun(x):
    return eval(function)


def graph_plotting(limit1, limit2): #setting graph
    t = np.arange(limit1*1.5, limit2*1.5, 0.01)
    integr = np.arange(limit1, limit2, 0.01)
    plt.plot(t, fun(t))
    plt.fill_between(integr, fun(integr))
    plt.xlabel("x")
    plt.ylabel("y=f(x)")
    plt.title("graph")
    plt.grid(True)
    plt.show()

def rectangle_integral(limit1, limit2, precision): #at this point i don't know how to solve problem with calculating if we have functions like 1/x etc
    height = float((limit2 - limit1) / precision)
    sum = 0
    for i in range(0, precision+1):
        sum += fun(limit1 + i*height) * height
    print(sum)



def trapezium_integral(limit1, limit2, precision): #at this point i don't know how to solve problem with calculating if we have functions like 1/x etc
    height = float((limit2 - limit1) / precision)
    sum = 0
    for i in range(0, precision):
        sum += height / 2.0 * (fun(limit1+i*height) + fun(limit1+(i+1)*height))
    print(sum)


if __name__ == '__main__':
    global function
    function = input() #input function, style x^3 + 3* x etc
    function = re.sub(r'[a-zA-Z]', "x", function) #transcripting any variable to "x"
    function = re.sub(r'(\^)', "**", function)    #transcripting ^ to **
    limit1 = float(input()) #lower limit
    limit2 = float(input()) #higher limit
    precision = int(input()) #how many calculations
    trapezium_integral(limit1, limit2, precision)
    rectangle_integral(limit1, limit2, precision)
    graph_plotting(limit1, limit2)

