import hashlib


class PasswordHasher:


    @staticmethod
    def hash_password(password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()



    @staticmethod
    def verify_password(password, hashed):

        return (
            PasswordHasher.hash_password(password)
            == hashed
        )