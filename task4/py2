Accuracy = 10 ** (-4)

def f(x, y):
    x1 = ((y ** 2 - 1.98) / 2) ** (1/3)
    y1 = -x + 1.03 / x
    return x1, y1

def main():
    x = 1
    y = 2

    x1, y1 = f(x, y)
    counter = 1
    while(abs(x - x1) > Accuracy or abs(y - y1) > Accuracy):
        x = x1
        y = y1
        x2, y2 = f(x2, y2)
        counter += 1
    print(x2, y2, counter)

def print(x, y, counter):
    print('x = ', x, 'y = ', y)
    print('iteration_num = ', counter)

