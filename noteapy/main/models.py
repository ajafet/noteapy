from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Need This Class to Use Build In Admin Framework (Will Remove After Beta Testing)
from django.contrib.auth.models import PermissionsMixin
 
class CustomAccountManager(BaseUserManager):    

    def create_superuser(self, username, password, name): 
        user = self.model(username=username, password=password, name=name)
        user.set_password(password)

        # Need to Add These Fields to Use Built In Admin Framework (Will Remove After Beta Testing)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user 

    def create_user(self, username, password, name): 
        user = self.model(username=username, password=password, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user 
 
    def get_by_natural_key(self, username):
        return self.get(username=username)   
    
 
class User(AbstractBaseUser, PermissionsMixin):  

    username     = models.CharField(max_length=128, unique=True)
    name         = models.CharField(max_length=30)
    occupation   = models.CharField(max_length=128, blank=True, null=True) 

    # Need to Add These Fields to Use Built In Admin Framework (Will Remove After Beta Testing)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['name'] 
    USERNAME_FIELD = 'username' 
    objects = CustomAccountManager() 


class Categories(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = "Categories"

    
class Notes(models.Model):

    title    = models.CharField(max_length=30)
    content  = models.TextField()
    author   = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ForeignKey(Categories, on_delete=models.CASCADE) 
    num_of_favorites = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta: 
        verbose_name_plural = "Notes"

class Favorites(models.Model): 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE) 

    class Meta: 
        verbose_name_plural = "Favorites"
