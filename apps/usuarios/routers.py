from rest_framework.routers import DefaultRouter
from . import viewset

router = DefaultRouter()

router.register(r'user', viewset.UserViewSet, basename="user")


urlpatterns = router.urls