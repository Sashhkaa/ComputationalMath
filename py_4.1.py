import math
def solve_system(x_0, y_0, tol):
    x, y = x_0, y_0
    i = 0
    while True and i < 1e10:
        if 1 - y * y > 0:
            x_tmp = math.atan(y)
            y_tmp = math.sqrt(1 - x_tmp*x_tmp)
            if abs(x - x_tmp) < tol and abs(y - y_tmp) < tol:
                return (x_tmp, y_tmp)
            x, y = x_tmp, y_tmp
        i += 1


x1, y1 = solve_system(0.5, 0.5, 1e-6)
print(f"Solution: x = {x1}, y = {y1}")