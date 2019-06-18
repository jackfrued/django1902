from django.db import models


class User(models.Model):
    """用户"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    username = models.CharField(max_length=20, unique=True, verbose_name='用户名')
    password = models.CharField(max_length=32, verbose_name='用户密码')
    email = models.CharField(max_length=255, default='', blank=True, verbose_name='邮箱')
    tel = models.CharField(max_length=11, verbose_name='手机号')

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Subject(models.Model):
    """学科"""
    no = models.IntegerField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='名称')
    intro = models.CharField(max_length=511, default='', verbose_name='介绍')
    create_date = models.DateField(null=True, verbose_name='成立日期')
    is_hot = models.BooleanField(default=False, verbose_name='是否热门')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_subject'
        verbose_name = '学科'
        verbose_name_plural = '学科'


class Teacher(models.Model):
    """老师"""
    no = models.AutoField(primary_key=True, verbose_name='编号')
    name = models.CharField(max_length=20, verbose_name='姓名')
    detail = models.CharField(max_length=1023, default='', blank=True, verbose_name='详情')
    photo = models.CharField(max_length=1023, default='', verbose_name='照片')
    good_count = models.IntegerField(default=0, verbose_name='好评数')
    bad_count = models.IntegerField(default=0, verbose_name='差评数')
    subject = models.ForeignKey(to=Subject, on_delete=models.PROTECT, db_column='sno', verbose_name='所属学科')

    class Meta:
        db_table = 'tb_teacher'
        verbose_name = '老师'
        verbose_name_plural = '老师'
