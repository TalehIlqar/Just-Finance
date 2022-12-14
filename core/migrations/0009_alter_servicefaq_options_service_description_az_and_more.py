# Generated by Django 4.0.4 on 2022-10-26 21:36

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_service_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicefaq',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='service',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='service',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Description'),
        ),
    ]
