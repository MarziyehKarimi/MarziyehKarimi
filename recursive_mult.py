def mult(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        if a < 0 and b > 0:
            return a + mult(a, b - 1)
        elif a < 0 and b < 0:
            return -b + mult(-a - 1, -b)
        else:
            return b + mult(a - 1, b)
