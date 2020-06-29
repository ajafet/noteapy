from main.models import *
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse 
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

def testing_load_base_page(request):
    return render(request, "main/home.html")
