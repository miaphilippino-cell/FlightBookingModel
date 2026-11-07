from security.encryption import EncryptionManager # type: ignore


class PaymentMethod:

    def __init__(
        self,
        card_number,
        expiry_date,
        cvv,
        account_name
    ):

        self.method_id = None

        self.encryption = EncryptionManager()

        # Never store raw card data
        self.card_number = self.encryption.encrypt(card_number)

        self.expiry_date = expiry_date

        # CVV should not be stored
        self.cvv = None

        self.account_name = account_name

        self.is_encrypted = True


    def verify_card(self):

        return self.is_encrypted


    def decrypt_card_number(self):

        return self.encryption.decrypt(
            self.card_number
        )


    def encrypt(self):

        self.is_encrypted = True