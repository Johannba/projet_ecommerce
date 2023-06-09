from django.db import models
from django.contrib.auth import models as auth_models

from ecommerce.addresses.models import Address,Country
from ecommerce.companies.models import CompagnyCategory
from ecommerce.users.managers import CustomUserManager

class User(auth_models.AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['civility',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    
    """Utilisateur personnalisé pour l'application."""
    M= "Masculin"
    F= "Féminin"
    ROLE_CHOICES=((M,"Masculin"),
                  (F,"Féminin"))
    
    compagny = models.ForeignKey(CompagnyCategory,
                                    related_name='compagny',
                                    on_delete=models.CASCADE,null=True)
    civility = models.CharField(max_length=8,choices=ROLE_CHOICES)
    phone_mobile = models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.ForeignKey(Address,
                                    related_name='address',
                                    on_delete=models.CASCADE,null=True)
    city = models.ForeignKey(Country,
                                    related_name='country',
                                    on_delete=models.CASCADE,null=True)
    k_bis = models.CharField(max_length=100)

    
class UserDocument():
    identity_card = models.ImageField(upload_to='compagnycategory/%Y/%m/%d')
  
        
class EmailConfirm():
    ...