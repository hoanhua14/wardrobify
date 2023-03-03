from django.urls import path
from accounts.views import user_log_in, user_log_out, signup_form

urlpatterns = [
    path("login/", user_log_in, name="login"),
    path("logout/", user_log_out, name="logout"),
    path("signup/", signup_form, name="signup"),
]
