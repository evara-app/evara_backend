from dotenv import dotenv_values
from config.settings.base import BASE_DIR

env_vars = dotenv_values()

db_status = env_vars.get("DB_STATUS")


if db_status == "postgres":
    DATABASES = {
        "default": {
            "ENGINE": env_vars.get("db_engine"),
            "NAME": env_vars.get("db_name"),
            "USER": env_vars.get("db_user"),
            "PASSWORD": env_vars.get("db_password"),
            "HOST": env_vars.get("db_host"),
            "PORT": env_vars.get("db_port"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
