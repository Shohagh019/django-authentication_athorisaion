from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate,login, logout, update_session_auth_hash
# Create your views here.
def home(request):
    return render (request, 'base.html')

def sign_up(request):
    if not request.user.is_authenticated:    
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Congratulations! Your Account Created Successfully!')
                form.save()
                # return redirect('home')
        else:
            form = RegisterForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return redirect('profile')
    
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request =request, data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_pass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form}) 
    else:
        return redirect('profile')
    
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return redirect('login')

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.method == 'POST':
        form = SetPasswordForm(user= request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'passchange.html', {'form':form})    

def pass_change_easy(request):
    if request.method == 'POST':
        form = SetPasswordForm(user= request.user, data= request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, 'passchange.html', {'form':form})    
