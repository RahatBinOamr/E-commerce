from django.urls import path
from .views import Register,LogOut,Profile,UpdateProfileForm
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',Register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogOut, name='logout'),
    path('profile/', Profile, name='profile'),
    path('update_profile/', UpdateProfileForm, name='update_profile'),
]
