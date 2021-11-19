from django.urls import path

#views
from . import views

urlpatterns = [
    path(
        route="signup",
        name="clients",
        view=views.SignupClientView.as_view()
    )
]
