from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import AppUserRegisterForm


def register(request):
    if request.method == 'POST':
        form = AppUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = AppUserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'app_users/register.html', context)


@login_required
def profile(request):
    return render(request, 'app_users/profile.html')
