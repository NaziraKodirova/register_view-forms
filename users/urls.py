from django.urls import path

from .views import register, login_view, logout_view, change_password

urlpatterns = [
    path('register/', register, name='register_page'),
    path('login/', login_view, name='login_page'),
    path('logout/', logout_view, name='logout_page'),
    path('change-password/', change_password, name='change_password'),
]
