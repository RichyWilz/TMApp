from django.db import models
from enum import UNIQUE
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
import uuid


class Role(models.Model):
    class Meta:
        ordering = ['-updated_at']

    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    slug = models.SlugField("Safe Url", unique=True, blank=True, null=True, max_length=200)

    def __str__(self):
        return f"{self.name}"
        

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}{uuid.uuid4()}")[:200]

        super().save(*args, **kwargs)


class User(AbstractUser):
    class Meta:
        ordering = ['-updated_at']

    STATUS_CHOICES = [
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Rejected', 'Rejected'),
        ]
    email = models.EmailField("user email", blank=True, null=True)
    role = models.ForeignKey("Role", on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Approved')
    image = models.ImageField(upload_to='accounts/user/', null=True, blank=True)
    slug = models.SlugField("Safe Url", unique=True, blank=True, null=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    
    def __str__(self):
        if not (self.first_name and self.last_name):
            return f"{self.username}"
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}{uuid.uuid4()}")[:200]
        super().save(*args, **kwargs)


    @property
    def name(self):
        if not (self.first_name and self.last_name):
            return f"{self.username}"
        return f"{self.first_name} {self.last_name}"