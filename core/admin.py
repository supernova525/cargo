from django.contrib import admin
from core.models import (
    Delivery,
    Shipper,
    Prealert,
)

admin.site.register(Delivery)
admin.site.register(Shipper)
admin.site.register(Prealert)
