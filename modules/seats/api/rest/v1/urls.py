
from django.urls import path
from rest_framework.routers import DefaultRouter

from modules.seats.api.rest.v1.views import ReserveApiView, SeatViewSet

router = DefaultRouter()
router.register("", SeatViewSet, basename="seats")

urlpatterns = [
    path("reserve/<int:match_id>", ReserveApiView.as_view())
]
urlpatterns += router.urls
