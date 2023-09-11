import utils
import ec

def find_order_of_point(curve, P, q):
    m = int(q**0.25) + 1
    stored_points = {}

    jP = P
    for j in range(m + 1):
        stored_points[jP] = j
        jP = curve.add(jP, P)

    k = -m
    while True:
        candidate = curve.add(q, curve.mul(2 * m * k, P))
        if candidate in stored_points:
            j = stored_points[candidate]
            M = q + 1 + 2 * m * k - j
            return M

        k += 1

def find_private_key(order, q):
    private_key = q + 1 - order
    return private_key
