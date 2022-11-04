from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    
    return render(request, 'index.html',{})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
@login_required
def payment(request):
    return render(request, 'payment.html')
@login_required
def studentdashboard(request):
    return render(request, 'student.html')