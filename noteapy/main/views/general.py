from main.models import *
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Login(View):

    def get(self, request):
        if request.user.is_authenticated: 
            return redirect('main:Notes')
        else: 
            return render(request, "main/login.html")

    def post(self, request):
        
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user: 
            login(request, user)
            return redirect('main:Notes') 
        else:  
            return render(request, "main/login.html", {"error": "true"})


@login_required
def logout_admin_dashboard(request): 
    logout(request)    
    return redirect('main:Login') 


@login_required
def load_admin_dashboard_account(request): 
    return render(request, "main/account.html")
 