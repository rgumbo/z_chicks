# Generated by Django 5.0.3 on 2024-05-03 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0016_remove_orderitem_oi_cs_num_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='oi_disc',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Discount', max_digits=15, null=True, verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='oi_tax',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Exch. Rate', max_digits=15, null=True, verbose_name='Tax Rate'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='si_disc',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Discount', max_digits=15, null=True, verbose_name='Discount'),
        ),
        migrations.AddField(
            model_name='stockitem',
            name='si_tax',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Exch. Rate', max_digits=15, null=True, verbose_name='Tax Rate'),
        ),
    ]
