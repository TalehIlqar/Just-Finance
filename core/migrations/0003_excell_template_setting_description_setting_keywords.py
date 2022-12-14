# Generated by Django 4.0.4 on 2022-09-30 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_setting_faq_image_setting_introduction_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Excell_template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('file', models.FileField(upload_to='excell/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Excell Template',
                'verbose_name_plural': 'Excell Templates',
            },
        ),
        migrations.AddField(
            model_name='setting',
            name='description',
            field=models.CharField(default='', max_length=200, verbose_name='Description (SEO)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='setting',
            name='keywords',
            field=models.CharField(default=' ', max_length=200, verbose_name='Keywords (SEO)'),
            preserve_default=False,
        ),
    ]
