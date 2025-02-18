from django.db import models
from django.utils.text import slugify
import uuid
from accounts.models import User

# Create your models here.

class Task(models.Model):
    class Meta:
        ordering = ['-updated_at']

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField("Safe Url", unique=True, blank=True, null=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}{uuid.uuid4()}")[:200]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name