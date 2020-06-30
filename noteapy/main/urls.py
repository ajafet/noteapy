from django.urls import include, path
from django.conf.urls import url
from . import views 

app_name = "main" 
urlpatterns = [

    path('', views.Login.as_view(), name="Login"), 
    path('home/', views.ManageNotes.as_view(), name="Notes"), 
    path('account/', views.load_admin_dashboard_account, name="Account"), 
    path('logout/', views.logout_admin_dashboard, name="Logout"), 

]
