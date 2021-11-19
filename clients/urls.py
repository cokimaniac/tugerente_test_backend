from django.urls import path

#views
from . import views

urlpatterns = [
    path(
        route="signup",
        name="signup",
        view=views.SignupClientView.as_view()
    ),
    path(
        route="signin",
        name="signin",
        view=views.LoginClientView.as_view()
    ),
]
