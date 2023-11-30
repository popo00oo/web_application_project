from django.db import models


class Users(models.Model):
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User table'

    def __str__(self):
        return self.username

