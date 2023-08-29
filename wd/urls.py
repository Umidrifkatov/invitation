from django.urls import path
from . import views

app_name = 'wd'

urlpatterns = [
    path('<str:unique_identifier>/', views.detail, name='detail'),
    # ... other URL patterns ...
]