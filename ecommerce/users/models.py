from django.db import models
from django.contrib.auth import models as auth_models


from ecommerce.addresses.models import Address,Country
from ecommerce.companies.models import CompagnyCategory


class User(auth_models.AbstractUser):
    """Utilisateur personnalisé pour l'application."""

class Client(auth_models.AbstractUser):
    """Utilisateur personnalisé pour l'application."""
    M= "Masculin"
    F= "Féminin"
    ROLE_CHOICES=((M,"Masculin"),
                  (F,"Féminin"))
    
    slug = models.SlugField(max_length=200)
    compagny = models.ForeignKey(CompagnyCategory,
                                    related_name='compagny',
                                    on_delete=models.CASCADE)
    civility = models.CharField(max_length=8,choices=ROLE_CHOICES)
    phone_mobile = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address,
                                    related_name='address',
                                    on_delete=models.CASCADE)
    city = models.ForeignKey(Country,
                                    related_name='country',
                                    on_delete=models.CASCADE)
    K_bis = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    
    
    
class UserDocument():
    identity_card = models.ImageField(upload_to='compagnycategory/%Y/%m/%d',
                                 blank=True)
  
        
class EmailConfirm():
    ...