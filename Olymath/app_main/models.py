from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30,default='')
    password = models.CharField(max_length=255,default='')
    wx_openid = models.CharField(max_length=255,default='',unique=True)
    nickName = models.CharField(max_length=100,default='')
    phone = models.CharField(max_length=30,default='')
    avatarUrl = models.CharField(max_length=255,default='')
    gender = models.CharField(max_length=2,default='')
    language = models.CharField(max_length=10,default='')
    city = models.CharField(max_length=10,default='')
    province = models.CharField(max_length=10,default='')
    country = models.CharField(max_length=15,default='')
    session_key = models.CharField(max_length=255,default='')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class trip_info(models.Model):
    wx_openid = models.CharField(max_length=255,default='')
    from_address = models.CharField(max_length=30,default='')
    des_address = models.CharField(max_length=30,default='')
    leave_time = models.DateTimeField(null=True)
    seats_count = models.PositiveIntegerField(default=0,max_length=10)
    demo = models.TextField(default='')
    status = models.CharField(max_length=20,default='')
    contact_phone = models.CharField(max_length=30,default='')
    contact_wechat_account = models.CharField(max_length=50,default='')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

