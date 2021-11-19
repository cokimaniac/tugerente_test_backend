from django.urls import path

#views
from . import views

urlpatterns = [
    path(
        name="create",
        route="",
        view=views.CreateInvoiceView.as_view()
    )
]
