# Generated by Django 4.0.4 on 2022-10-13 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_insurancetypename_taxtypename_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurancetype',
            name='fees',
        ),
        migrations.RemoveField(
            model_name='sectortype',
            name='tax_types',
        ),
        migrations.RemoveField(
            model_name='taxtype',
            name='insurance_types',
        ),
        migrations.AddField(
            model_name='insurancefee',
            name='insurance_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fees', to='calculator.insurancetype'),
        ),
        migrations.AddField(
            model_name='insurancetype',
            name='tax_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='insurance_types', to='calculator.taxtype'),
        ),
        migrations.AddField(
            model_name='taxtype',
            name='sector_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tax_types', to='calculator.sectortype'),
        ),
        migrations.AlterField(
            model_name='insurancetype',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='taxtype',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='InsuranceTypeName',
        ),
        migrations.DeleteModel(
            name='TaxTypeName',
        ),
    ]
