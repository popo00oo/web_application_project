# Generated by Django 4.2.6 on 2023-11-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0004_alter_lost_upass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='UPass',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
