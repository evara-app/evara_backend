from kavenegar import *
from dotenv import dotenv_values

env_vars = dotenv_values()

sms = KavenegarAPI(env_vars.get("KAVENEGAR_TOKEN"))