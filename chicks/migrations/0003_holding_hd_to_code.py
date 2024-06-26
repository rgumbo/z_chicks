# Generated by Django 5.0.3 on 2024-03-31 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicks', '0002_alter_member_mm_co_code_alter_member_mm_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holding',
            name='hd_to_code',
            field=models.ForeignKey(blank=True, help_text='Town where the holding is found', null=True, on_delete=django.db.models.deletion.CASCADE, to='chicks.town', verbose_name='Town'),
        ),
    ]
