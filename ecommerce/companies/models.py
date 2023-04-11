from django.db import models


      
class CompagnyCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,
                            unique=True)
      
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'compagnycategory'
        verbose_name_plural = 'compagnycategories'

class compagny(models.Model):
     name = models.CharField(max_length=100)
     slug = models.SlugField(max_length=200,
                            unique=True)
     category = models.ForeignKey(CompagnyCategory,
                                    related_name='products',
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