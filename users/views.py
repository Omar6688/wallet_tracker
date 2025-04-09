from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        messages.success(self.request, f"Welcome back, {username}!")
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')
