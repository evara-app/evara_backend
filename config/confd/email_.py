from dotenv import dotenv_values
from config.settings.base import BASE_DIR

env_vars = dotenv_values()

DEFAULT_FROM_EMAIL = env_vars.get("DEFAULT_FROM_EMAIL")
EMAIL_BACKEND=env_vars.get("EMAIL_BACKEND")
EMAIL_HOST=env_vars.get("EMAIL_HOST")
EMAIL_PORT=int(env_vars.get("EMAIL_PORT"))
EMAIL_HOST_USER=env_vars.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=env_vars.get("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS=True