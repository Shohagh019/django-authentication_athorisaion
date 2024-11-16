from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('change_password/', views.pass_change, name='pass_change'),
    path('change_password_easy/', views.pass_change_easy, name='pass_change_easy'),
]