from django.contrib import admin
from core.models import (
    Delivery,
    Shipper,
)

admin.site.register(Delivery)
admin.site.register(Shipper)
