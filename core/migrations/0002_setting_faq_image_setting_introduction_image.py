# Generated by Django 4.0.4 on 2022-09-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='faq_image',
            field=models.ImageField(blank=True, null=True, upload_to='faq_image/', verbose_name='FAQ Image'),
        ),
        migrations.AddField(
            model_name='setting',
            name='introduction_image',
            field=models.ImageField(blank=True, null=True, upload_to='introduction_image/', verbose_name='Introduction Image'),
        ),
    ]