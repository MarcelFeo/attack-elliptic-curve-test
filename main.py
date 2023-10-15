import utils
import ec
import attacks

# PRIMOS UTILIZADOS NO EXPERIMENTO

# (1) 192 bits: 2^192 - 2^64 - 1
prime1 = 2**192 - 2**64 - 1

# (2) 224 bits: 2^224 - 2^96 + 1
prime2 = 2**224 - 2**96 + 1

# (3) 256 bits: 2^256 - 2^224 + 2^192 + 2^96 - 1
prime3 = 2**256 - 2**224 + 2**192 + 2^96 - 1

# (4) 384 bits: 2^384 - 2^128 - 2^96 + 2^32 - 1
prime4 = 2**384 - 2**128 - 2^96 + 2^32 - 1

# (5) 521 bits: 2^521 - 1
prime5 = 2**521 - 1

# CURVAS ELÍPTICAS UTILIZADOS NO EXPERIMENTO

# (1) DUAL_EC_DRBG "P-384" CURVE
num384 = utils.generate_random_number(384)
p384 = ec.EllipticCurve(-3, num384, 17) # point: (0, 3)

generator_point = (0, 3)
pk = p384.public_key(2, generator_point) # public key = (13, 12)

# TABELA COM OS VALORES DOS PRIMOS
print("<< PRIMES >>")
utils.show_primes(prime1, prime2, prime3, prime4, prime5)
print("<< CURVES >>")
utils.show_curves(p384)
