# Generated by Django 5.0.3 on 2024-04-30 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0011_alter_currency_cu_base_alter_orderitem_oi_base_amnt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='io_cs_num',
            field=models.ForeignKey(default=1, help_text='Customer', on_delete=django.db.models.deletion.CASCADE, to='chicks.customer', verbose_name='Order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='io_so_ord_date',
            field=models.DateTimeField(blank=True, help_text='Date of Order', null=True, verbose_name='Order Date'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='io_so_p_s',
            field=models.CharField(default='C', help_text='Type of the Order', max_length=1, verbose_name='Purchase/Sales'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='io_so_type',
            field=models.CharField(default='C', help_text='Type of the Order', max_length=1, verbose_name='Order Type'),
        ),
    ]
