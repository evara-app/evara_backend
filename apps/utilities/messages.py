from enum import Enum
from rest_framework import status

class CommonMessages(Enum):
    data_not_valid = {"fa":"داده نا معتبر است", "en":"user exists!", "ar":"", "ru":"", "tr":""}, status.HTTP_400_BAD_REQUEST
    server_down = {"fa":"در حال حاضر سرویس فعال نمیباشد", "en":"", "ar":"", "ru":"", "tr":"", }, status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

class UserMessages(Enum):
    user_exists = {"fa":"", "en":"user exists!", "ar":"", "ru":"", "tr":""}, status.HTTP_400_BAD_REQUEST
    password_wrong = {"fa":"رمز اشتباه می باشد", "en":"user exists!", "ar":"", "ru":"", "tr":""}, status.HTTP_401_UNAUTHORIZED
    login_successful = {"fa":"با موفقیت وارد شدید", "en":"user exists!", "ar":"", "ru":"", "tr":""}, status.HTTP_200_OK
