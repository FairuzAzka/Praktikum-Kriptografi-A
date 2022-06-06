# "Encrypt" the number 12 using the exponent e = 65537 and the primes p = 17 and q = 23. What number do you get as the ciphertext?

# Get n
p = 17
q = 23
n = p * q

# Encrypt data
e = 65537
numberOfPlainText = 12
numbeOfChiperText = pow(numberOfPlainText, e, n)

# Print
print(numbeOfChiperText)
