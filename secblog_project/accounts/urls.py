from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_page),
    path('signin/', views.signin_page),
    path('api/signup/', views.signup_api),
    path('api/signin/', views.signin_api),
    path('api/logout/', views.logout_api),
    path('api/check-auth/', views.check_auth_api),
]