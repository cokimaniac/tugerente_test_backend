from django.urls import path
from rest_framework.routers import SimpleRouter

#views
from . import views

urlpatterns = []

router = SimpleRouter()
router.register("", views.RoomsViewset)

urlpatterns += router.urls