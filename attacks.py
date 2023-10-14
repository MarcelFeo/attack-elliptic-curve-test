import random
from math import ceil, sqrt

INF_POINT = None

def baby_step_giant_step(a, g, p):
    # a^x ≅ g mod p

    m = ceil(sqrt(p))
    points = []

    # baby steps & giant steps
    baby_step = {}
    giant_step = {}

    for i in range(m):
        baby_step[i] = (a ** (m * i)) % p
        giant_step[i] = (g * (a ** (-i))) % p

    # procurando os valores iguais
    for j in range(m):
        for k in range(m):
            if baby_step[j] == giant_step[k]:
                points.append((j, baby_step[j]))
                points.append((k, giant_step[k]))

    key = (m * j + k) % p
    return key

def pollard_rho_discrete_log(curve, g, h):
    x = INF_POINT
    y = INF_POINT
    d = INF_POINT

    while d == INF_POINT:
        x = curve.add(x, curve.public_key(random.randint(1, curve.p - 1), g))
        y = curve.add(y, curve.public_key(random.randint(1, curve.p - 1), g))
        y = curve.add(y, curve.public_key(random.randint(1, curve.p - 1), g))
        d = curve.add(x, curve.add(y, curve.mul(-1, h)))

    return d
