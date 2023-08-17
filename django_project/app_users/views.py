from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppUserRegisterForm


def register(request):
    if request.method == 'POST':
        form = AppUserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = AppUserRegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'app_users/register.html', context)
