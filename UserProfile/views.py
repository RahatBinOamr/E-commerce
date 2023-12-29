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




def UpdateProfile(request):
    if request.method == 'POST':
        u_form = UpdateRegisterForm(request.POST, instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form =  UpdateRegisterForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)

    context = {

        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'update_profile.html', context)