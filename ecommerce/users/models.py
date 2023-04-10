from django.db import models
from django.contrib.auth import models as auth_models


from ecommerce.companies.models import CompagnyCategory

class User(auth_models.AbstractUser):
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
    addresses = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)
    K_bis = models.CharField(max_length=100)
    category = models.ForeignKey(CompagnyCategory,
                                    related_name='compagnycategory',
                                    on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['category']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['category']),
            models.Index(fields=['-created']),
    ]
    def __str__(self):
        return self.name
                

    
class UserDocument():
    identity_card = models.ImageField(upload_to='compagnycategory/%Y/%m/%d',
                                 blank=True)
    
class email():
    ...