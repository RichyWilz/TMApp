from django.urls import path
from .views import *

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('password-reset/', password_reset, name='password_reset'),
    path('signup/', signup, name='register'),
]