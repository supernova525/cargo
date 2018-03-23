from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel
from django.db.models.signals import pre_save 
from django.dispatch import receiver


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

@receiver(pre_save, sender=Delivery)
def fetch_prealert_delivery_on_save(sender, instance, **kwargs):
    """
        This method will be triggered when someone try to save
        a new delivery. If the tracking exists, it will automatically
        bind the user to the delivery.
        We are using Django Signals for this approach.
    """
    try:
        prealert = Prealert.objects.get(tracking=instance.tracking)
    except Prealert.DoesNotExist:
        prealert = None

    if prealert:
        instance.user = prealert.user

class Prealert(models.Model):
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    tracking = models.CharField(max_length=100)
    delivery_date = models.DateField()
    provider = models.CharField(max_length=50, help_text="Ex: Amazon, Ebay, etc.")
    price = models.DecimalField(decimal_places=2, max_digits=6)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #TODO: Add support for attachments (bills, etc.)

    def __str__(self):
        return "Prealert: {0:05d}".format(self.id)

class Contact(models.Model):
    sender = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField()