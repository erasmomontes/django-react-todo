from django.db import models
from django.urls import reverse

# Create your models here.

class Todo(models.Model):
    
    title = models.CharField(max_length=50)
    description = models.TextField()
    complete = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Todo_detail", kwargs={"pk": self.pk})
