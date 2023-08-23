from tabulate import tabulate
import random

def generate_random_number(bits):
    num = random.getrandbits(bits)
    return num

def show_primes(p1, p2, p3, p4, p5):
    data = [
        ["192 bits", "2^192 - 2^64 - 1", "{:.5e}".format(p1)],
        ["224 bits", "2^224 - 2^96 + 1", "{:.5e}".format(p2)],
        ["256 bits", "2^256 - 2^224 + 2^192 + 2^96 - 1", "{:.5e}".format(p3)],
        ["384 bits", "2^384 - 2^128 - 2^96 + 2^32 - 1", "{:.5e}".format(p4)],
        ["521 bits", "2^521 - 1", "{:.5e}".format(p5)]
    ]

    header = ["Name", "Expression", "Value"]

    table = tabulate(data, headers=header, tablefmt="grid")
    print(table)
