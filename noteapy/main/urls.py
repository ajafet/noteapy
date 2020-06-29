from django.urls import include, path
from django.conf.urls import url
from . import views 

app_name = "main" 
urlpatterns = [

    # path('', views.Login.as_view(), name="Login"), 
    # path('home/', views.load_admin_dashboard_home, name="Admin"), 

    path('', views.testing_load_base_page, name="Home"), 

]
