# Generated by Django 4.2.7 on 2023-11-27 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200, verbose_name='公告内容')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': 'Announcement list',
                'db_table': 'notice',
            },
        ),
        migrations.CreateModel(
            name='Lost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20, verbose_name='丢失位置')),
                ('date', models.CharField(max_length=20, verbose_name='丢失时间')),
                ('category', models.CharField(max_length=20, verbose_name='物品分类')),
                ('upass', models.CharField(max_length=20, null=True)),
                ('desc', models.CharField(max_length=200, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='有效状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users', verbose_name='所属用户')),
            ],
            options={
                'verbose_name': 'List of lost property',
                'db_table': 'lost',
            },
        ),
    ]