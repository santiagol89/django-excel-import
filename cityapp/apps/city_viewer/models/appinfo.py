# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cityapp.apps.city_viewer.models import Area
from django_extensions.db.fields import CreationDateTimeField


class APPInfo(models.Model):
    class Meta:
        app_label = 'city_viewer'
        verbose_name = verbose_name_plural = _('城市APP')

    name = models.CharField(_('名称'), max_length=50, unique=True)
    icon = models.ImageField(_('Icon'), upload_to='uploads/appicons/')
    desc = models.TextField(_('App描述'), max_length=255)
    link = models.URLField(_('App Store链接'), blank=True)
    sell_date = models.DateField(_('上线时间'))
    latest_ver = models.CharField(_('最新版本'), max_length=3, default='1')
    area = models.ForeignKey(Area, verbose_name=_('城市'), blank=True, null=True, on_delete= models.SET_NULL)

    def __unicode__(self):
        return self.name

class APPDevice(models.Model):
    class Meta:
        app_label = 'city_viewer'
        verbose_name  = verbose_name_plural = _('安装设备')

    identifier = models.CharField(_('标示符'), max_length=255)
    system = models.CharField(_('系统'), max_length=100)
    platform = models.CharField(_('设备'), max_length=100)

    def __unicode__(self):
        return self.identifier

class APPLikeManager(models.Manager):
    def liked_num(self, area):
        return  self.filter(area=area).count()

class APPLike(models.Model):
    class Meta:
        app_label = 'city_viewer'
        verbose_name = verbose_name_plural = _('喜欢查看')

    area = models.ForeignKey(Area, verbose_name=_('城市'))
    device = models.ForeignKey(APPDevice, verbose_name=_('设备'))
    create_at = CreationDateTimeField()
    objects = APPLikeManager()

    def __unicode__(self):
        return self.area.zh_name

class APPInstall(models.Model):
    class Meta:
        app_label = 'city_viewer'
        verbose_name = verbose_name_plural = _('安装查看')

    area = models.ForeignKey(Area, verbose_name=_('城市'))
    device = models.ForeignKey(APPDevice, verbose_name=_('设备'))
    create_at = CreationDateTimeField()

    def __unicode__(self):
        return self.area.zh_name