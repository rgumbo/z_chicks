# Generated by Django 5.0.3 on 2024-04-27 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0008_alter_currency_cu_base_alter_storename_sn_rg_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='so_sn_code',
            new_name='cs_sn_code',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='oi_so_num',
            field=models.ForeignKey(default=1, help_text='Store Order', on_delete=django.db.models.deletion.CASCADE, to='chicks.storeorder', verbose_name='Store Order'),
        ),
    ]