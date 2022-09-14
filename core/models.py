from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


from core.tools.base_models import Base_models

# Create your models here.

class Blog(Base_models):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title


class Service(Base_models):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='service/', blank=True, null=True)

    def __str__(self):
        return self.title


class Finance(Base_models):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='finance/', blank=True, null=True)

    def __str__(self):
        return self.title


class Tax(Base_models):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='tax/', blank=True, null=True)

    def __str__(self):
        return self.title


class HR(Base_models):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='hr/', blank=True, null=True)

    def __str__(self):
        return self.title


class About(Base_models):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    
    def __str__(self):
        return self.title


class Contact(Base_models):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FAQ(Base_models):
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=10000)

    def __str__(self):
        return self.question