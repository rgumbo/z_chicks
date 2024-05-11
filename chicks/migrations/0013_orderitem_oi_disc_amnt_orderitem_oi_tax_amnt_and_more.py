# Generated by Django 5.0.3 on 2024-04-30 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0012_orderitem_io_cs_num_orderitem_io_so_ord_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='oi_disc_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total Discount amnt', max_digits=15, null=True, verbose_name='Disc Amnt'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='oi_tax_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total Tax amount', max_digits=15, null=True, verbose_name='Tax Amount'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='oi_tot_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total amount due', max_digits=15, null=True, verbose_name='Total Amnt'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='sl_sn_code',
            field=models.ForeignKey(blank=True, help_text='The Store', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='i_store', to='chicks.storename', verbose_name='Store'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='si_sn_code',
            field=models.ForeignKey(blank=True, help_text='The Store', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='si_store', to='chicks.storename', verbose_name='Store'),
        ),
        migrations.AddField(
            model_name='stocktype',
            name='st_sn_code',
            field=models.ForeignKey(blank=True, help_text='The Store', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='st_store', to='chicks.storename', verbose_name='Store'),
        ),
        migrations.AddField(
            model_name='storeorder',
            name='sl_sn_code',
            field=models.ForeignKey(blank=True, help_text='The Store', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='o_store', to='chicks.storename', verbose_name='Store'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='io_so_p_s',
            field=models.CharField(choices=[('P', 'Purchase Order'), ('S', 'Sales Order')], default='C', help_text='Type of the Order', max_length=1, verbose_name='Purchase/Sales'),
        ),
        migrations.AlterField(
            model_name='stockloc',
            name='sl_sn_code',
            field=models.ForeignKey(blank=True, help_text='The Store', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sl_store', to='chicks.storename', verbose_name='Store'),
        ),
    ]
