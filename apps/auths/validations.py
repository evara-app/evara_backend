from apps.auths.models import User


class UserValidation:
    @staticmethod
    def check_email_exists(email: str):
        if email is None:
            return False
        if User.objects.filter(email=email):
            return True
        return False

    @staticmethod
    def check_phone_exists(phone_number: str):
        if phone_number is None:
            return False
        if User.objects.filter(phone_number=phone_number):
            return True
        return False
