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
        