from django.urls import path
from .views import ListMenu
urlpatterns = [
    path('', ListMenu.as_view()),
]