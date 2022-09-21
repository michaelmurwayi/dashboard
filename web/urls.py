from django.urls import path
from .views import DashboardView

urlpatterns = [
    path('home/', DashboardView.as_view()),

]