from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="home_log"),
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('magic_link_login_request/', views.magic_link_login_request_view, name="magic-link-login-request"),
    path('magic_link_login/<uidb64>/<token>/', views.magic_link_login_view, name="magic-link-login"),
    


]