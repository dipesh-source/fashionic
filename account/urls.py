"""all  the URL's for the viewset"""
from django.urls import path
from . import viewset


urlpatterns = [
    path("sign-up/", viewset.RegistrationViewSet.as_view(), name="signup"),
    path("sign-in/", viewset.LoginViewSet.as_view(), name="signin"),
    path("user-profile/", viewset.UserProfile.as_view(), name="user-profile"),
]
