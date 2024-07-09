from django.db import models
from django.forms import ModelForm

# Create your models here.


class Pins(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} - {self.author}"
