import random

class DH():
    def __init__(self, public_key1, public_key2, private_key):
        self.public_key1 = public_key1
        self.public_key2 = public_key2
        self.private_key = private_key
        self.full_key = None

    def generate_partial_key(self):
        partial_key = pow(self.public_key1, self.private_key) % self.public_key2
        return partial_key

    def generate_full_key(self, partial_key_r):
        full_key = pow(partial_key_r, self.private_key) % self.public_key2
        self.full_key = full_key
        return full_key

    def encrypt_message(self, message):
        encrypted_message = ""
        key = self.full_key
        for c in message:
            encrypted_message += chr(ord(c) + key)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        decrypted_message = ""
        key = self.full_key
        for c in encrypted_message:
            decrypted_message += chr(ord(c) - key)
        return decrypted_message

def generate_primes(n):
    primes = [2]
    nextPrime = 3
    while nextPrime < n:
        isPrime = True
        i = 0
        squareRoot = int(nextPrime ** 0.5)
        while primes[i] <= squareRoot:
            if nextPrime % primes[i] == 0:
                isPrime = False
            i += 1
        if isPrime:
            primes.append(nextPrime)

        nextPrime += 1
    return primes

def get_prime():

    while True:
        num = random.randint(2, 1000)
        if num in generate_primes(1000):
            return num



message = 'Berlin is the capital of great Germany '

alice_public = get_prime()
alice_private = get_prime()
bob_public = get_prime()
bob_private = get_prime()
eva_private = get_prime()

alice = DH(alice_public, bob_public, alice_private)
bob = DH(alice_public, bob_public, bob_private)
eva = DH(alice_public, bob_public, eva_private)


alice_partial = alice.generate_partial_key()
bob_partial = bob.generate_partial_key()
eva_partial = eva.generate_partial_key()
alice_full = alice.generate_full_key(bob_partial)
bob_full = bob.generate_full_key(alice_partial)
eva_full = eva.generate_full_key(alice_partial)

bob_encrypted = bob.encrypt_message(message)
dec_message = alice.decrypt_message(bob_encrypted)


if __name__ == "__main__":
  print(f'??????????\n* '
        f'??????????????????: {str(alice_public)}\n* ????????????:  {str(alice_private)}\n* '
        f'??????????????????: {str(alice_partial)}\n* ????????????: {str(alice_full)}')
  print(f'??????\n* '
        f'??????????????????: {str(bob_public)}\n* ????????????:  {str(bob_private)}\n*'
        f' ??????????????????: {str(bob_partial)}\n* ????????????: {str(bob_full)}')
  print(f'??????\n* '
        f'????????????: {str(eva_private)}\n* ??????????????????:  {str(eva_partial)}\n* '
        f'????????????: {str(eva_full)}')

  print('?????????????????????????? ??????????????????: ' + bob_encrypted)
  print("???????????????????????????? ??????????????????: " + dec_message)