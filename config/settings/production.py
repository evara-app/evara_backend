from .base import *

REST_FRAMEWORK.update(
    {
        "DEFAULT_RENDERER_CLASSES": "rest_framework.renderers.JSONRenderer",
    }
)
ALLOWED_HOSTS = ["*"]
