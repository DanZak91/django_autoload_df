# Generated by Django 4.2.3 on 2023-07-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadin_db', '0002_rename_grp_employ_grp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employ',
            name='resolution_po',
            field=models.TextField(null=True, verbose_name='Разрешение ПО'),
        ),
    ]
