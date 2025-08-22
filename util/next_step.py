import math


def next_step(src, dst):
    if src == dst:
        return src

    x1, y1 = src
    x2, y2 = dst

    # Calcola le differenze
    dx = x2 - x1
    dy = y2 - y1

    # Determina il numero di passi (distanza massima tra le coordinate)
    steps = max(abs(dx), abs(dy))

    if steps == 0:
        return src

    # Calcola gli incrementi reali per ogni passo
    x_increment = dx / steps
    y_increment = dy / steps

    # Coordinate reali correnti
    x_real = float(x1)
    y_real = float(y1)

    # Esegui il primo passo (per ottenere il prossimo punto)
    x_real += x_increment
    y_real += y_increment

    # Quantizza sulla griglia discreta
    next_x = round(x_real)
    next_y = round(y_real)

    return (next_x, next_y)
