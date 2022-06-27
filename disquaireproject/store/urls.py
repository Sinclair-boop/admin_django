from django.urls import include, path
# from django.urls import path

# from disquaireproject.store import views
from . import views

urlpatterns = [
    path('home/<name>', views.home, name='home'),
]
