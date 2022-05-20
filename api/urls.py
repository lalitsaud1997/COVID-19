from django.urls import path
from .views import CoronavirusListAPIView, CoronavirusDetailAPIView

urlpatterns = [
    path('api/', CoronavirusListAPIView.as_view()),
    path('<slug>', CoronavirusDetailAPIView.as_view()),
]