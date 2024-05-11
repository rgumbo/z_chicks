# Generated by Django 5.0.3 on 2024-03-31 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mm_co_code',
            field=models.ForeignKey(blank=True, help_text='Country\tto which the member belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.country', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_code',
            field=models.CharField(blank=True, help_text='A number/code by whhich member is identified by', max_length=100, null=True, verbose_name='Assigned Number'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_comm_date',
            field=models.DateTimeField(blank=True, help_text='Date member commenced operations', null=True, verbose_name='Commencement Date'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_contact',
            field=models.CharField(blank=True, help_text='First contact person', max_length=100, null=True, verbose_name='Contact Person1'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_dt_code',
            field=models.ForeignKey(blank=True, help_text='District to which the member belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.district', verbose_name='District'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_email',
            field=models.EmailField(blank=True, help_text='member s email address', max_length=100, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_mobile',
            field=models.IntegerField(blank=True, help_text='member s mobile phone number', null=True, verbose_name='Mobile Phone'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_paddress1',
            field=models.CharField(blank=True, help_text='The member s Physical Address line 1', max_length=200, null=True, verbose_name='Physical Address'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_paddress2',
            field=models.CharField(blank=True, help_text='The member s Physical Address line 2', max_length=200, null=True, verbose_name='Physical Address'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_phone',
            field=models.IntegerField(blank=True, help_text='member s phone number', null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_phone1',
            field=models.IntegerField(blank=True, help_text='First contact person phone number', null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_reg_date',
            field=models.DateTimeField(blank=True, help_text='Date member was registered with institution', null=True, verbose_name='Date of Registration'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_rg_code',
            field=models.ForeignKey(blank=True, help_text='Region to which the member belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.region', verbose_name='Region'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_to_code',
            field=models.ForeignKey(blank=True, help_text='Town to which the member belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.town', verbose_name='Town'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_vg_code',
            field=models.ForeignKey(blank=True, help_text='Village to which the member belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.village', verbose_name='Village'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_wd_code',
            field=models.ForeignKey(blank=True, help_text='Ward to which the member belongs', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.ward', verbose_name='Ward'),
        ),
        migrations.AlterField(
            model_name='member',
            name='mm_wsite',
            field=models.CharField(blank=True, help_text='member s website', max_length=200, null=True, verbose_name='Website'),
        ),
    ]
