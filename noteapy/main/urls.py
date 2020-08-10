from django.urls import include, path
from django.conf.urls import url
from . import views 

app_name = "main" 
urlpatterns = [

    path('', views.Login.as_view(), name="Login"), 
    path('logout/', views.logout_admin_dashboard, name="Logout"), 

    ## Notes ## 
    path('notes/', views.ManageNotes.as_view(), name="Notes"), 
    path('notes/new', views.NewNote.as_view(), name="New_Note"), 
    path('notes/update/<int:id>/', views.UpdateNote.as_view(), name="Update_Note"),
    path('notes/delete/<int:id>/', views.DeleteNote.as_view(), name="Delete_Note"),

    ## Categories ## 
    path('categories/', views.ManageCategories.as_view(), name="Categories"), 
    path('categories/new', views.NewCategory.as_view(), name="New_Category"), 
    path('categories/view/<int:id>/', views.ViewCategory.as_view(), name="View_Category"),
    path('categories/update/<int:id>/', views.UpdateCategory.as_view(), name="Update_Category"),
    path('categories/delete/<int:id>/', views.DeleteCategory.as_view(), name="Delete_Category"),

    ## Favorites ##
    
    ## Search Notes ##
    path('search/', views.SearchNotes.as_view(), name="Search"), 

    ## Account ##
    path('account/', views.Account.as_view(), name="Account"), 
    path('account/update/', views.UpdateAccount.as_view(), name="Update_Account"),
    

]
