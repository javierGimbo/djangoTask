from django.conf import settings
from django.db import models
from django.utils import timezone

class Task(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.title