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


        # Check If Updating Password
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        
        if new_password: 
            if len(new_password) < 8: 
                context["new_password_error"] = "Must be at Least 8 Characters"
            else: 
                if new_password != confirm_password: 
                    context["confirm_password_error"] = "Must Match New Password"
                # else: 
                    #passwords match then save new password as password 


        if form.is_valid() and "new_password_error" not in context and "confirm_password_error" not in context:
            form.save()
            return redirect("main:Account")
        else: 
            return render(request, "main/account/update_account.html", context)

