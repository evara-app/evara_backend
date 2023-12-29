from uuid import uuid4
import string
from random import randint, choice
from django.conf import settings
from kavenegar import APIException, HTTPException
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from apps.utilities.email import send_email
from apps.utilities.messages import CommonMessages, UserMessages
from apps.utilities.extends import Extends
from apps.auths.models import Otp, User, Profile


def login_register(data: dict):
    email_or_phone = check_email_or_phone(data=data)
    uuid_token = send_otp_code(data=email_or_phone)
    if uuid_token != False:
        return {"uuid_token": uuid_token}, status.HTTP_200_OK
    return CommonMessages.server_down.value


def check_email_or_phone(data: dict) -> dict:
    if isd := data.get("isd"):
        return {"phone_number": data.get("phone_number"), "isd": isd}
    if email := data.get("email"):
        return {"email": email}
    return CommonMessages.data_not_valid.value


def create_user():
    pass


def check_exists_otp_data(data: dict) -> None:
    """
    if otp object old exists delete that
    """
    if email := data.get("email"):
        result = Extends.get_or_none(klass=Otp, filter={"email": email})
        if result:
            result.delete()
    elif phone_number := data.get("phone_number"):
        result = Extends.get_or_none(klass=Otp, filter={"phone_number": phone_number})
        if result:
            result.delete()


def normalize_phone_number(phone_number: str):
    if phone_number is None:
        return None
    if phone_number.startswith("0"):
        return phone_number[1:]
    return phone_number


def create_otp_data(data: dict):
    check_exists_otp_data(data=data)
    result = Otp.objects.create(
        uuid_token=str(uuid4()),
        password=randint(11111, 99999),
        email=data.get("email"),
        phone_number=normalize_phone_number(phone_number=data.get("phone_number")),
        isd=data.get("isd"),
    )

    return result


def send_otp_code(data: dict):
    if email := data.get("email"):
        return send_otp_email(email)
    return send_otp_phone(data=data)


def send_otp_email(email=str):
    result = create_otp_data(data={"email": email})
    email_status = send_email(
        receiver_email=result.email,
        subject="Evara Team",
        message=f"Welcome To Evara Here is the Code Please Enter In App\n {result.password}",
    )
    if email_status != 1:
        return result.uuid_token
    return False


def send_otp_phone(data: dict):
    result = create_otp_data(data=data)
    # when system is ok uncomment
    # receptor = f"00{result.isd}{result.phone_number}"
    # params = {
    #     "sender":"122",
    #     "receptor":receptor,
    #     "message":f"Welcome To Evara Here is the Code Please Enter In App\n {result.password}"
    # }
    # try:
    #     settings.sms.verify_lookup(params)
    # except APIException as e:
    #     return False
    # except HTTPException as e:
    #     return False
    # else:
    #     return result.uuid_token
    return result.uuid_token


def check_password_otp(data: object, sended_password=str):
    if data.password == sended_password:
        return data
    return False


def create_random_username():
    username = ""
    for _ in range(50):
        username += choice(string.ascii_letters)

    return username


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


def login_user(data: object):
    if data.email:
        profile = Profile.objects.filter(email=data.email)
        if profile:
            user = profile.first()
        else:
            random_user_name = create_random_username()
            user = User.objects.create(username=random_user_name)
            profile = Profile.objects.create(
                user=user, phone_number=None, isd=None, email=data.email, role=1
            )

    elif data.phone_number:
        profile = Profile.objects.filter(phone_number=data.phone_number)
        if profile:
            user = profile.first()
        else:
            random_user_name = create_random_username()
            user = User.objects.create(username=random_user_name)
            profile = Profile.objects.create(
                user=user,
                phone_number=data.phone_number,
                isd=data.isd,
                email=None,
                role=1,
            )

    data.delete()
    return get_tokens_for_user(user=user), status.HTTP_200_OK


def verify_login_register(data: dict):
    uuid_token = data.get("uuid_token")
    result = Otp.objects.filter(uuid_token=uuid_token)
    if result:
        sended_password = data.get("password")
        otp_obj = result.first()
        if check_password_otp(data=otp_obj, sended_password=sended_password):
            return login_user(data=otp_obj)
        return UserMessages.password_wrong.value
    return CommonMessages.data_not_valid.value
