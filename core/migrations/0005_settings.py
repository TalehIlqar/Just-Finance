# Generated by Django 4.0.4 on 2022-09-19 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_applicationcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('base_models_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.base_models')),
                ('slogan', models.CharField(max_length=200, verbose_name='Slogan')),
                ('slogan_en', models.CharField(max_length=200, null=True, verbose_name='Slogan')),
                ('slogan_az', models.CharField(max_length=200, null=True, verbose_name='Slogan')),
                ('slogan_ru', models.CharField(max_length=200, null=True, verbose_name='Slogan')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Logo')),
                ('default_image', models.ImageField(blank=True, null=True, upload_to='default_image/', verbose_name='Default Image')),
                ('default_number', models.CharField(max_length=200, verbose_name='Default Number')),
                ('default_email', models.CharField(max_length=200, verbose_name='Default Email')),
                ('default_address', models.CharField(max_length=200, verbose_name='Default Address')),
                ('facebook', models.CharField(max_length=200, verbose_name='Facebook')),
                ('twitter', models.CharField(max_length=200, verbose_name='Twitter')),
                ('instagram', models.CharField(max_length=200, verbose_name='Instagram')),
                ('linkedin', models.CharField(max_length=200, verbose_name='Linkedin')),
                ('youtube', models.CharField(max_length=200, verbose_name='Youtube')),
            ],
            bases=('core.base_models',),
        ),
    ]
