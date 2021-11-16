
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

message = 'Berlin is the capital of great Germany '
alice_public = 197
alice_private = 199
bob_public = 151
bob_private = 157
alice = DH(alice_public, bob_public, alice_private)
bob = DH(alice_public, bob_public, bob_private)



if __name__ == "__main__":
    s_partial = alice.generate_partial_key()
    print(s_partial)  # 147

    m_partial = bob.generate_partial_key()
    print(m_partial)  # 66

    s_full = alice.generate_full_key(m_partial)
    print(s_full)  # 75

    m_full = bob.generate_full_key(s_partial)
    print(m_full)  # 75

    m_encrypted = bob.encrypt_message(message)
    print(m_encrypted)

    message_final = alice.decrypt_message(m_encrypted)
    print(message_final)

