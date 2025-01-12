from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Logged in successfully')
                else :
                    return HttpResponse('User account is disabled')
            else :
                return HttpResponse('Username and password are incorrect')
    else :
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def dashboard_view(request):
    user = request.user
    context = {'user': user}
    return render(request, 'pages/user_profile.html', context)

def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            context={'new_user': new_user}
            return render(request, 'account/register_done.html', context)
        else:
            return HttpResponse("Ro'yxatdan o'tishda xatolik . Iltimos tekshirib qaytadan ro'yxatdan o'ting")
    else :
        user_form = UserRegistrationForm()
        context = {'user_form': user_form}
        return render(request, 'account/register.html',context)

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'account/register.html'










