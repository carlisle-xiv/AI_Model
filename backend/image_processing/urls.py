from django.urls import path
from .views import process_image_view


urlpatterns = [
    path("image/predict/", process_image_view, name="predict_image"),
]
