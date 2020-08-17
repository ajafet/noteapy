from django.contrib import admin
from main.models import User, Categories, Notes, Favorites


# Used to Hash Passwords After Being Updated in the Admin Consolde (Will Remove After Beta Testing)
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

class UserAdminClass(UserAdmin): 
    list_display = ('name', 'username', 'occupation', 'is_staff', 'is_superuser', 'is_active')
    exclude = ('email', 'date_joined', 'first_name', 'last_name')
    fieldsets = (
        (_('Authentication'), {'fields': ( 'username', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'occupation')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )


# Customizing Admin Models
class CategoriesAdmin(admin.ModelAdmin): 
    list_display = ('user', 'name')

class NotesAdmin(admin.ModelAdmin): 
    list_display = ('author', 'title', 'content', 'category', 'num_of_favorites')

class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('user', 'note')
    

# Registering Models to Admin Console
admin.site.register(User, UserAdminClass) 
admin.site.register(Categories, CategoriesAdmin) 
admin.site.register(Notes, NotesAdmin) 
admin.site.register(Favorites, FavoritesAdmin) 


# Changing Admin Console Apperance
admin.site.site_header = "Noteapy Admin Portal"
admin.site.site_title = "Noteapy Admin Portal"
admin.site.index_title = "Welcome to Noteapy Admin Portal"

