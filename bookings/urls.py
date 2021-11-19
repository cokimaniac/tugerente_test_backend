from django.urls import path

#views
from . import views

urlpatterns = [
    path(
        route="",
        view=views.RegisterBookingView.as_view(),
        name="register"
    ),
    path(
        route="list",
        view=views.BookingListView.as_view(),
        name="list"
    )
]
