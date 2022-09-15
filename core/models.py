from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


from core.tools.base_models import Base_models

# Create your models here.

class Blog(Base_models):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.title


class Service(Base_models):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='service/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.title


class Finance(Base_models):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='finance/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.title


class Tax(Base_models):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='tax/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.title


class HR(Base_models):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='hr/', blank=True, null=True, verbose_name=_('Image'))

    def __str__(self):
        return self.title


class About(Base_models):
    title = models.CharField(max_length=200, verbose_name=_('Title'))
    description = RichTextField(verbose_name=_('Description'))
    image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name=_('Image'))
    
    def __str__(self):
        return self.title


class Contact(Base_models):
    name = models.CharField(max_length=200, verbose_name=_('Name'))
    number = models.CharField(max_length=200, verbose_name=_('Number'))
    subject = models.CharField(max_length=200, verbose_name=_('Subject'))

    def __str__(self):
        return self.name


class FAQ(Base_models):
    question = models.CharField(max_length=200, verbose_name=_('Question'))
    answer = models.TextField(max_length=10000, verbose_name=_('Answer'))

    def __str__(self):
        return self.question