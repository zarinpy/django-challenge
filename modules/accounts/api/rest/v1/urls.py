from django.urls import path
from rest_framework.routers import DefaultRouter

from modules.accounts.api.rest.v1.views import LoginView, SignUpView

router = DefaultRouter()
router.register("register", SignUpView, basename="register")
router.register("login", LoginView, basename="login")

urlpatterns = router.urls
