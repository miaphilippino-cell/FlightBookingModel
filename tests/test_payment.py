from models.payment import Payment # type: ignore


def test_payment():

    payment = Payment(
        250,
        "USD",
        "CreditCard"
    )

    assert payment.process_payment()

    assert payment.status.value == "COMPLETED"