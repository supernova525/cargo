from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Shipper(models.Model):
    name = models.CharField(max_length=10)
    #TODO: add more information if needed

    def __str__(self):
        return self.name


class Delivery(TimeStampedModel):
    tracking = models.CharField(max_length=100)
    observation = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="deliveries")
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE,  related_name="sh_deliveries")
    #TODO: add more information if needed

    class Meta:
        verbose_name='Delivery'
        verbose_name_plural = 'Deliveries'

    def __str__(self):
        return 'DELIVERY: {tracking}'.format(tracking=self.tracking)
