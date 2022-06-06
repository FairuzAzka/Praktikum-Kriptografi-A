# Data
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
# Question: What is the private key d?

# Get totient
tot = (p - 1) * (q - 1)

# Get private key
privateKey = pow(e, -1, tot) # This how to use mod inverse in python 3.8+

# Print
print(privateKey)
