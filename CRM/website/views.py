from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    #Checking for login 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged In!")
            return redirect('home')
        
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again.")
    return render(request, 'home.html', {})

# def login_user(request):
    # #Checking for login 
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     #Authenticate
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         messages.success(request, "You have been logged In!")
    #         return redirect('home')
        
    #     else:
    #         messages.success(request, "There Was An Error Logging In, Please Try Again.")
def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out.")
    return redirect('home') 

def register_user(request):
        return render(request, 'register.html', {})
