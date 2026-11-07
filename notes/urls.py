from django.urls import path
from .views import get_notes, health_check

urlpatterns = [
    path('api/notes/', get_notes, name='get_notes'),
    path('api/health/', health_check, name='health_check'),
]