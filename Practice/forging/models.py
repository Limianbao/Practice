# coding:utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class People(models.Model):
	name = models.CharField(max_length=20, verbose_name='名字')
	age = models.IntegerField(max_length=5, verbose_name='年龄')


	class Meta:
		abstract = True


class User(People):
	pwd = models.CharField(max_length=10, verbose_name='密码')
	email = models.EmailField(max_length=20, verbose_name='邮箱')
	phone = models.IntegerField(max_length=11, verbose_name='手机号')
	head_portrait = models.ImageField(verbose_name='头像', upload_to='images',blank=False)
	Introduction = models.TextField(verbose_name='简介')

	class Meta(People.Meta):
		db_table = 'user'
		verbose_name = '用户'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name


class Game(models.Model):
	name = models.CharField(max_length=20, verbose_name='名字')
	user = models.ForeignKey('User', verbose_name='购买者')

	class Meta:
		db_table = 'game'
		verbose_name = '游戏'
		verbose_name_plural = verbose_name

	def __unicode__(self):
		return self.name
