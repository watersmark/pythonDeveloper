# обычным циклом переберём кол-во раз сколько
# будет отскоков на уровне 1.5 meters
def bouncing_ball(h, bounce, window):
    if h > 0 and  0 < bounce < 1 and window < h:
        countS = 0
        while True:
            if window >= h:
                return countS - 1

            countS += 2
            h = h * bounce

    else:
        return -1

print(bouncing_ball(30, 0.75, 1.5))