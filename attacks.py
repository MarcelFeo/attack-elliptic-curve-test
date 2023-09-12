from math import ceil, sqrt

def baby_step_giant_step(a, g, p):
    # a^x ≅ g mod p

    m = ceil(sqrt(p))
    print("m = ", m)
    points = []

    # baby steps & giant steps
    baby_step = {}
    giant_step = {}

    for i in range(m):
        # baby_step.append((i, a ** (m * i) % p))
        # giant_step.append((i, g * (a ** -i) % p))
        baby_step[i] = (a ** (m * i)) % p
        giant_step[i] = (g * (a ** (-i))) % p
        print("\n i = " + str(i) + "\n")
        print("valor baby = " + str(baby_step[i]))
        print("valor giant = " + str(giant_step[i]))

    # procurando os valores iguais
    for j in range(m):
        for k in range(m):
            # print("valor baby = " + str(baby_step[j]))
            # print("valor giant = " + str(giant_step[k]))

            if baby_step[j] == giant_step[k]:
                points.append((j, baby_step[j]))
                points.append((k, giant_step[k]))
                # print("Dentro do if")
                # print("valor baby = " + str(baby_step[j]))
                # print("valor giant = " + str(giant_step[k]))

    key = (m * j + k) % p
    return key
