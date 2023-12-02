
from rest_framework.routers import DefaultRouter
from django.urls import path
from modules.seats.api.rest.v1.views import SeatViewSet, ReserveApiView

router = DefaultRouter()
router.register("", SeatViewSet, basename="seats")
# router.register("reserve", ReserveApiView, basename="reserve")

urlpatterns = [
    path("reserve/<int:match_id>", ReserveApiView.as_view())
]
urlpatterns += router.urls
