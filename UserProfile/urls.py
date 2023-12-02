from django.urls import path
from UserProfile.views import profile,update_profile
urlpatterns = [
    path('profile/', profile, name='profile'),
    path('update-profile/', update_profile, name='update_profile'),
]
