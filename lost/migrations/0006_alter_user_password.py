# Generated by Django 4.2.6 on 2023-11-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0005_alter_lost_upass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
