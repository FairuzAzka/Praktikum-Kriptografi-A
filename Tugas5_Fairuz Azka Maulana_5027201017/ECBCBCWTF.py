<<<<<<< HEAD
from Crypto.Cipher import AES
import requests

def xor(a,b):
	a = bytes.fromhex(a)
	b = bytes.fromhex(b)
	return bytes(i ^ j for i,j in zip(a,b))

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}
        
cipher = requests.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
cipher = cipher.json()['ciphertext']

iv = cipher[:32]
cipher1 = cipher[32:64]
cipher2 = cipher[64:96]

decrypt2 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher2 + '/')
decrypt2 = decrypt2.json()['plaintext']
decrypt2 = xor(decrypt2,cipher1)

decrypt1 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher1 + '/')
decrypt1 = decrypt1.json()['plaintext']
decrypt1 = xor(decrypt1,iv)

=======
from Crypto.Cipher import AES
import requests

def xor(a,b):
	a = bytes.fromhex(a)
	b = bytes.fromhex(b)
	return bytes(i ^ j for i,j in zip(a,b))

def decrypt(ciphertext):
    ciphertext = bytes.fromhex(ciphertext)

    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}
        
cipher = requests.get('http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/')
cipher = cipher.json()['ciphertext']

iv = cipher[:32]
cipher1 = cipher[32:64]
cipher2 = cipher[64:96]

decrypt2 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher2 + '/')
decrypt2 = decrypt2.json()['plaintext']
decrypt2 = xor(decrypt2,cipher1)

decrypt1 = requests.get('http://aes.cryptohack.org/ecbcbcwtf/decrypt/' + cipher1 + '/')
decrypt1 = decrypt1.json()['plaintext']
decrypt1 = xor(decrypt1,iv)

>>>>>>> 333a5bbfb989e6c94cdad9f661c0417315018344
print(decrypt1+decrypt2)