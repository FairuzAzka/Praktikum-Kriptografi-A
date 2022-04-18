<<<<<<< HEAD
import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

=======
import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

>>>>>>> 333a5bbfb989e6c94cdad9f661c0417315018344
print("flag", bytearray.fromhex(plaintext).decode())