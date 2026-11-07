from models.payment import Payment # type: ignore
from models.enums import PaymentStatus # type: ignore


class PaymentGateway:


    def __init__(self, audit_logger):

        self.audit_logger = audit_logger



    def process_payment(
        self,
        payment,
        username
    ):

        try:

            payment.validate()

            payment.process_payment()


            self.audit_logger.log_event(
                username,
                "PAYMENT_PROCESSED",
                "SUCCESS"
            )


            return True


        except Exception:

            payment.status = PaymentStatus.FAILED


            self.audit_logger.log_event(
                username,
                "PAYMENT_FAILED",
                "DENIED"
            )


            return False