# views.py
from django.shortcuts import render,redirect,get_object_or_404
from UserProfile.models import UserProfile
from UserProfile.forms import UserProfileForm
from product.models import CartItem

def profile(request):
    user_profile = get_object_or_404(UserProfile,user=request.user)
    count = CartItem.objects.filter(user=request.user).count()
    return render(request, 'profile.html', {'user_profile': user_profile,'count': count})

def update_profile(request):
    user_profile = get_object_or_404(UserProfile,user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'update_profile.html', {'form': form})
