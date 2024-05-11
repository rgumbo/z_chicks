# Generated by Django 5.0.3 on 2024-05-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0015_alter_packtype_options_alter_storeorder_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='oi_cs_num',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='oi_sn_code',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='oi_so_ord_date',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='oi_so_p_s',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='oi_so_type',
        ),
        migrations.AddField(
            model_name='storeorder',
            name='so_base_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Base Amnt', max_digits=15, null=True, verbose_name='Base Amnt'),
        ),
        migrations.AddField(
            model_name='storeorder',
            name='so_disc_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total Discount amnt', max_digits=15, null=True, verbose_name='Disc Amnt'),
        ),
        migrations.AddField(
            model_name='storeorder',
            name='so_tax_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total Tax amount', max_digits=15, null=True, verbose_name='Tax Amount'),
        ),
        migrations.AddField(
            model_name='storeorder',
            name='so_tot_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Total amount due', max_digits=15, null=True, verbose_name='Total Amnt'),
        ),
        migrations.AddField(
            model_name='storeorder',
            name='so_trans_amnt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Trans. Amnt', max_digits=15, null=True, verbose_name='Trans. Amnt'),
        ),
    ]
