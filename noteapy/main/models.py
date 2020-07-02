from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
 
class CustomAccountManager(BaseUserManager):    

    def create_superuser(self, username, password, name): 
        user = self.model(username=username, password=password, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_user(self, username, password, name): 
        user = self.model(username=username, password=password, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user 
 
    def get_by_natural_key(self, username):
        return self.get(username=username)   
    
 
class User(AbstractBaseUser):  

    username     = models.CharField(max_length=128, unique=True)
    name         = models.CharField(max_length=30)
    occupation   = models.CharField(max_length=128, blank=True, null=True) 

    REQUIRED_FIELDS = ['name'] 
    USERNAME_FIELD = 'username' 
    objects = CustomAccountManager() 


class Categories(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    
class Notes(models.Model):

    title    = models.CharField(max_length=30)
    content  = models.TextField()
    author   = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ForeignKey(Categories, on_delete=models.CASCADE) 
    num_of_favorites = models.IntegerField()

class Favorites(models.Model): 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE) 
