from django.urls import path
from django.urls import path, include
from . import views


urlpatterns = [
    path('signup/', views.signup),

]
