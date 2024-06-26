# Generated by Django 5.0.3 on 2024-04-27 07:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0007_currency_packtype_stockloc_alter_custorders_od_grade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='cu_base',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', help_text='Indicates whether the currency is the base currency', max_length=1, verbose_name='Base Currency ?'),
        ),
        migrations.AlterField(
            model_name='storename',
            name='sn_rg_code',
            field=models.ForeignKey(blank=True, help_text='Region', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='region', to='chicks.region', verbose_name='Region'),
        ),
    ]
