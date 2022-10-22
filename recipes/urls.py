from django.urls import path
from calculator.views import recipe_handler

urlpatterns = [
    path('<str:recipe>/', recipe_handler)
]
