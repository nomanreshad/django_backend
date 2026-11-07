from django.urls import path
from .views import get_notes

urlpatterns = [
    path('api/notes', get_notes, name='get_notes')
]