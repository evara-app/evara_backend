from django.urls import path
from apps.auths.views import LoginRegisterApiView, VerifyLoginRegisterApiView


app_name = "auth"
urlpatterns = [
    path("login_register/", LoginRegisterApiView.as_view(), name="login_register"),
    path(
        "verify_login_register/",
        VerifyLoginRegisterApiView.as_view(),
        name="verify_login_register",
    ),
]
