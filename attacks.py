import random
from math import ceil, sqrt

INF_POINT = None

# Baby Step Giant Step
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

# Pollard Rho
def cycle_detect_floyd(f, x0, matchfunc=None, include_count=False):
    u = x0
    v = x0
    k = 0
    if matchfunc is None:
        matchfunc = lambda u,v: u == v
    while True:
        k += 1
        u = f(u)
        v = f(f(v))
        if matchfunc(u,v):
            result = (u, v, k, 2*k)
            return result + (3*k,) if include_count else result

def cycle_detect_brent(f, x0, matchfunc=None, include_count=False):
    u = x0
    v = x0
    ku = 0
    kv = 0
    if matchfunc is None:
        matchfunc = lambda u,v: u == v
    kpow2 = 1
    while True:
        kv += 1
        v = f(v)
        if matchfunc(u,v):
            result = u, v, ku, kv
            return result + (kv,) if include_count else result
        if kv == kpow2:
            ku = kv
            u = v
            kpow2 *= 2

def blankinship(a,b, verbose=False):
    arow = [a,1,0]
    brow = [b,0,1]
    if verbose:
        print(arow)
    while brow[0] != 0:
        q,r = divmod(arow[0], brow[0])
        if verbose:
            print(brow, q)
        if r == 0:
            break
        rrow =[r, arow[1]-q*brow[1], arow[2]-q*brow[2]]
        arow = brow
        brow = rrow
    return brow[0], brow[1], brow[2]

def log_rho(y, g, p, hashfunc, cycle_detector, verbose=False):
    """ Executes Pollard's rho algorithm for determining discrete logarithm.
    The generator g must have order p.
    """
    assert g ** (p+1) == g
    def f(uab):
        u, a, b = uab
        h = hashfunc(u)
        if h == 0:
            u *= g
            a += 1
        elif h == 1:
            u *= u
            a *= 2
            b *= 2
        elif h == 2:
            u *= y
            b += 1
        else:
            raise ValueError("Expected hash value 0, 1, 2")
        return u, a, b
    def matchfunc(uab, vab):
        return uab[0] == vab[0]
    uab0 = (g, 1, 0)
    uab, vab, ku, kv, nf = cycle_detector(f, uab0, matchfunc, include_count=True)
    if verbose:
        if verbose is True:
            print("Found cycle in %d function evaluations" % nf)
        else:
            # allow verbose to be a function
            verbose(evaluation_count=nf)
    _, ai, bi = uab
    _, aj, bj = vab
    delta_a = ai-aj
    delta_b = bj-bi
    gcd, c, _ = blankinship(delta_b, p)
    assert gcd == 1
    return (c*delta_a) % p

def simple_hash(y):
    return (y.coeffs & 255) % 3
