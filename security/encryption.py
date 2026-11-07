from cryptography.fernet import Fernet


class EncryptionManager:


    def __init__(self):

        self.key = Fernet.generate_key()

        self.cipher = Fernet(self.key)



    def encrypt(self, data):

        return self.cipher.encrypt(
            data.encode()
        )



    def decrypt(self, encrypted):

        return self.cipher.decrypt(
            encrypted
        ).decode()