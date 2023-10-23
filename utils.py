from tabulate import tabulate
import random
import hashlib
import base58

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

    table = tabulate(data, headers=header, tablefmt="fancy_grid")
    print(table)

def show_curves(c1):

    data = [
        ["P-384", "y^2 = x^3 - 3x + b", c1.points[:10]]
    ]

    header = ["Name", "Expression", "Some Points"]



    table = tabulate(data, headers=header, tablefmt="fancy_grid", disable_numparse=True)
    print(table)

# Função para gerar endereço Bitcoin fictício
def generate_address(private_key):
    private_key_bytes = private_key.to_bytes(32, byteorder='big')
    public_key_hex = hashlib.sha256(private_key_bytes).hexdigest()
    address_hex = hashlib.new('ripemd160', bytes.fromhex(public_key_hex)).hexdigest()
    address_with_prefix = '00' + address_hex
    checksum = hashlib.sha256(hashlib.sha256(bytes.fromhex(address_with_prefix)).digest()).hexdigest()[:8]
    address_binary = bytes.fromhex(address_with_prefix + checksum)
    bitcoin_address = base58.b58encode(address_binary)
    return bitcoin_address
