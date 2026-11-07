from datetime import datetime
import uuid

from models.enums import PaymentStatus # type: ignore


class Payment:

    def __init__(
        self,
        amount,
        currency,
        processor
    ):

        self.payment_id = str(uuid.uuid4())

        self.amount = amount
        self.currency = currency

        self.timestamp = datetime.now()

        self.processor = processor

        self.status = PaymentStatus.PENDING


    def validate(self):

        if self.amount <= 0:
            raise ValueError(
                "Payment amount must be greater than zero"
            )

        return True


    def process_payment(self):

        self.validate()

        self.status = PaymentStatus.COMPLETED

        return True


    def refund(self):

        if self.status != PaymentStatus.COMPLETED:
            raise Exception(
                "Cannot refund incomplete payment"
            )

        self.status = PaymentStatus.REFUNDED

        return True