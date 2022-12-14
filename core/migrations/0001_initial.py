# Generated by Django 4.0.4 on 2022-09-24 14:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Application Category',
                'verbose_name_plural': 'Application Categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Image')),
                ('is_pin', models.BooleanField(default=False, verbose_name='Is Pin')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=200, verbose_name='Question')),
                ('question_en', models.CharField(max_length=200, null=True, verbose_name='Question')),
                ('question_az', models.CharField(max_length=200, null=True, verbose_name='Question')),
                ('question_ru', models.CharField(max_length=200, null=True, verbose_name='Question')),
                ('answer', models.TextField(max_length=10000, verbose_name='Answer')),
                ('answer_en', models.TextField(max_length=10000, null=True, verbose_name='Answer')),
                ('answer_az', models.TextField(max_length=10000, null=True, verbose_name='Answer')),
                ('answer_ru', models.TextField(max_length=10000, null=True, verbose_name='Answer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='finance/', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='hr/', verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='service/', verbose_name='Image')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('slogan', models.CharField(max_length=200, verbose_name='Slogan')),
                ('slogan_en', models.CharField(max_length=200, null=True, verbose_name='Slogan')),
                ('slogan_az', models.CharField(max_length=200, null=True, verbose_name='Slogan')),
                ('slogan_ru', models.CharField(max_length=200, null=True, verbose_name='Slogan')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logo/', verbose_name='Logo')),
                ('default_image', models.ImageField(blank=True, null=True, upload_to='default_image/', verbose_name='Default Image')),
                ('default_number', models.CharField(max_length=200, verbose_name='Default Number')),
                ('default_email', models.CharField(max_length=200, verbose_name='Default Email')),
                ('default_address', models.CharField(max_length=200, verbose_name='Default Address')),
                ('facebook', models.CharField(blank=True, max_length=200, verbose_name='Facebook')),
                ('whatsapp', models.CharField(blank=True, max_length=200, verbose_name='Whatsapp')),
                ('instagram', models.CharField(blank=True, max_length=200, verbose_name='Instagram')),
                ('linkedin', models.CharField(blank=True, max_length=200, verbose_name='Linkedin')),
                ('youtube', models.CharField(blank=True, max_length=200, verbose_name='Youtube')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=200, verbose_name='Email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_az', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_en', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_az', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='tax/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Tax',
                'verbose_name_plural': 'Taxes',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone Number')),
                ('message', models.TextField(verbose_name='Message')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='core.applicationcategory', verbose_name='Category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
