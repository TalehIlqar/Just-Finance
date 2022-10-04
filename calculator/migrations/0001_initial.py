# Generated by Django 4.0.4 on 2022-10-02 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_number', models.IntegerField()),
                ('to_number', models.IntegerField()),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InsuranceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('fee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.insurancefee', verbose_name='Fee')),
            ],
            options={
                'verbose_name': 'Insurance Type',
                'verbose_name_plural': 'Insurance Types',
            },
        ),
        migrations.CreateModel(
            name='TaxType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('insurance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tax_types', to='calculator.insurancetype')),
            ],
        ),
        migrations.CreateModel(
            name='SectorType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tax_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_types', to='calculator.taxtype')),
            ],
        ),
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.sectortype')),
            ],
        ),
    ]