from django.db import models
from users.models import Users


class Lost(models.Model):
    location = models.CharField(max_length=20, verbose_name='lost location')
    date = models.CharField(max_length=20, verbose_name='lost time')
    category = models.CharField(max_length=20, verbose_name='category')
    # optional enter
    upass = models.CharField(max_length=20, null=True)
    desc = models.CharField(max_length=200, verbose_name='description')
    status = models.BooleanField(default=True, verbose_name='status')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'lost'
        verbose_name = 'List of lost property'

    def __str__(self):
        return self.category


class Notice(models.Model):
    user = models.ForeignKey(to=Users, to_field='id', on_delete=models.CASCADE, verbose_name='所属用户')
    content = models.CharField(max_length=200, verbose_name='公告内容')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notice'
        verbose_name = 'Announcement list'

    def __str__(self):
        return self.user.username
