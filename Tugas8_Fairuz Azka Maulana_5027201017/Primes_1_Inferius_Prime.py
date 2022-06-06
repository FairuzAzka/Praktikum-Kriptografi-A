from Crypto.Util.number import long_to_bytes

# Data
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

# Factor the n by the Primes_1_Factoring
p = 986369682585281993933185289261
q = 752708788837165590355094155871

# Get the private key (d)
totient = (p - 1) * (q - 1)
d = pow(e, -1, totient)

# Decrypt
pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)

print(decrypted)
