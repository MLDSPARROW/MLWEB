from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class DataSet(models.Model):
    dataset = models.FileField(upload_to='datasets/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class MLModel(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, null=False, blank=False)
    model_dataset = models.ForeignKey(
        DataSet, on_delete=models.PROTECT, null=False, blank=False)
    model_name = models.CharField(max_length=100, blank=False)
    model_async_id = models.CharField(max_length=255, blank=False)
    model_parameters = models.CharField(max_length=255, blank=True)
    model_param_values = models.CharField(max_length=255, blank=True)
    