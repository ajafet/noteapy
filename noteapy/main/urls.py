from django.urls import include, path
from django.conf.urls import url
from . import views 

app_name = "main" 
urlpatterns = [

    path('', views.Login.as_view(), name="Login"), 
    path('logout/', views.logout_admin_dashboard, name="Logout"), 

    
    path('home/', views.ManageNotes.as_view(), name="Notes"), 

    ## Categories ## 
    path('categories/', views.ManageCategories.as_view(), name="Categories"), 
    path('categories/new', views.NewCategory.as_view(), name="New_Category"), 

    
    ## Account ##
    path('account/', views.Account.as_view(), name="Account"), 
    path('account/update/', views.UpdateAccount.as_view(), name="Update_Account"),
    

]
