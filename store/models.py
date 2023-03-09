from django.db import models
from django.urls import reverse


class Clothes(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True, verbose_name='content')
    price = models.IntegerField(blank=True, verbose_name='price')
    image = models.ImageField(upload_to='store/images', verbose_name='image')
    is_published = models.BooleanField(default=True, verbose_name='is_published')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('clothes', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes_model'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name_plural = 'Categories'
