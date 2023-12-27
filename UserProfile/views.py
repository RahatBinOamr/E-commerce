from django.shortcuts import redirect, render
from .forms import RegistrationForm, UpdateProfileForm, UpdateRegisterForm
from django.contrib.auth import logout
def Register(request):
    if request.method =='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form =RegistrationForm()
    return render(request, 'register.html',{'form':form})

def LogOut(request):
    logout(request)
    return redirect('login')

def Profile(request):
    return render(request, 'profile.html')




def updateProfile(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    profile_instance, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST, request.FILES, instance=profile_instance)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=profile_instance)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'updateProfile.html', context)