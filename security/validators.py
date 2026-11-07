class Validators:

    @staticmethod
    def validate_email(email):

        return (
            "@" in email
            and "." in email
        )


    @staticmethod
    def validate_age(age):

        return (
            age >= 1
            and age <= 100
        )


    @staticmethod
    def validate_flight_times(departure, arrival):

        return departure < arrival


    @staticmethod
    def validate_payment_amount(amount):

        return amount > 0


    @staticmethod
    def validate_seat_count(requested, capacity):

        return (
            requested <= capacity
            and requested >= 0
        )


    @staticmethod
    def validate_required_fields(data):

        for field in data:

            if data[field] is None:
                return False

        return True