# Generated by Django 4.2.4 on 2023-11-02 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lost',
            name='UPass',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]