from utils import show_primes
import ecc

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

# TABELA COM OS VALORES DOS PRIMOS
show_primes(prime1, prime2, prime3, prime4, prime5)
