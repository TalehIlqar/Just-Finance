from datetime import datetime
import email

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from just_finance.utils.base_model import BaseModel


class Blog(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    image = models.ImageField(
        upload_to="blog/", blank=True, null=True, verbose_name=_("Image")
    )
    is_pin = models.BooleanField(default=False, verbose_name=_("Is Pin"))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_("Slug"))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.slug = slugify(self.title + "-" + str(now.strftime("%Y%m%d%H%M%S")))
        super(Blog, self).save(*args, **kwargs)


class Service(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    image = models.ImageField(
        upload_to="service/", blank=True, null=True, verbose_name=_("Image")
    )

    slug = models.SlugField(max_length=200, unique=True, verbose_name=_("Slug"))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        now = datetime.now()
        self.slug = slugify(self.title + "-" + str(now.strftime("%Y%m%d%H%M%S")))
        super(Service, self).save(*args, **kwargs)


class ServiceFAQ(BaseModel):
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, verbose_name=_("Service")
    )
    question = models.CharField(max_length=200, verbose_name=_("Question"))
    answer = models.TextField(verbose_name=_("Answer"))
    # ordering = ["-id"]
    def __str__(self):
        return self.question


class Finance(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    image = models.ImageField(
        upload_to="finance/", blank=True, null=True, verbose_name=_("Image")
    )

    def __str__(self):
        return self.title


class Tax(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    image = models.ImageField(
        upload_to="tax/", blank=True, null=True, verbose_name=_("Image")
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Tax")
        verbose_name_plural = _("Taxes")


class HR(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    image = models.ImageField(
        upload_to="hr/", blank=True, null=True, verbose_name=_("Image")
    )

    def __str__(self):
        return self.title


class About(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = RichTextField(verbose_name=_("Description"))
    image = models.ImageField(
        upload_to="about/", blank=True, null=True, verbose_name=_("Image")
    )

    def __str__(self):
        return self.title


class Contact(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    phone_number = models.CharField(
        max_length=200, blank=True, null=True, verbose_name=_("Phone Number")
    )
    category = models.ForeignKey(
        "ApplicationCategory",
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="contacts",
    )
    message = models.TextField(verbose_name=_("Message"))

    def __str__(self):
        return self.name


class FAQ(BaseModel):
    question = models.CharField(max_length=200, verbose_name=_("Question"))
    answer = models.TextField(max_length=10000, verbose_name=_("Answer"))

    def __str__(self):
        return self.question


class ApplicationCategory(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Application Category")
        verbose_name_plural = _("Application Categories")


class Subscriber(BaseModel):
    email = models.EmailField(max_length=200, verbose_name=_("Email"))

    def __str__(self):
        return self.email


class Excell_template(BaseModel):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    file = models.FileField(upload_to="excell/", verbose_name=_("File"))
    category = models.ForeignKey(
        "ApplicationCategory",
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="excell_templates",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Excell Template")
        verbose_name_plural = _("Excell Templates")


class Setting(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    slogan = models.CharField(max_length=200, verbose_name=_("Slogan"))
    logo = models.ImageField(
        upload_to="logo/", blank=True, null=True, verbose_name=_("Logo")
    )
    default_image = models.ImageField(
        upload_to="default_image/",
        blank=True,
        null=True,
        verbose_name=_("Default Image"),
    )
    default_number = models.CharField(max_length=200, verbose_name=_("Default Number"))
    default_email = models.CharField(max_length=200, verbose_name=_("Default Email"))
    default_address = models.CharField(
        max_length=200, verbose_name=_("Default Address")
    )
    faq_image = models.ImageField(
        upload_to="faq_image/", blank=True, null=True, verbose_name=_("FAQ Image")
    )
    introduction_image = models.ImageField(
        upload_to="introduction_image/",
        blank=True,
        null=True,
        verbose_name=_("Introduction Image"),
    )
    keywords = models.CharField(max_length=200, verbose_name=_("Keywords (SEO)"))
    description = models.CharField(max_length=200, verbose_name=_("Description (SEO)"))
    facebook = models.CharField(max_length=200, verbose_name=_("Facebook"), blank=True)
    whatsapp = models.CharField(max_length=200, verbose_name=_("Whatsapp"), blank=True)
    instagram = models.CharField(max_length=200, verbose_name=_("Instagram"), blank=True)
    linkedin = models.CharField(max_length=200, verbose_name=_("Linkedin"), blank=True)
    youtube = models.CharField(max_length=200, verbose_name=_("Youtube"), blank=True)
    email_address = models.CharField(max_length=200, verbose_name=_("Email Address"), blank=True, null=True)
    telegram = models.CharField(max_length=200, verbose_name=_("Telegram"), blank=True, null=True)

    def __str__(self):
        return "Settings"
