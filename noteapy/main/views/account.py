from main.models import *
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from main.forms import UpdateUserForm
from django.contrib import messages


class Account(LoginRequiredMixin, View): 

    def get(self, request): 
        return render(request, "main/account/account.html")


class UpdateAccount(LoginRequiredMixin, View): 

    def get(self, request):

        data = {
            "username": request.user.username, 
            "name": request.user.name, 
            "occupation": request.user.occupation,
        }

        form = UpdateUserForm(initial=data, instance=request.user)
        context = {
            "form": form,
        }

        return render(request, "main/account/update_account.html", context)

    def post(self, request):
        form = UpdateUserForm(request.POST, instance=request.user) 
        context = {
            "form": form,
        }
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Account Has Been Updated")  
            return redirect('main:Account')
        else: 
            return render(request, "main/account/update_account.html", context)

