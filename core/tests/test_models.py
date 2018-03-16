from django.test import TestCase

from  model_mommy import mommy

from core.models import (
    Delivery,
    Prealert,
    Shipper,
)


class DeliveryTest(TestCase):
    def setUp(self):
        self.delivery = mommy.make(Delivery, tracking='USP-12345')

    def test_str_delivery(self):
        expected = 'DELIVERY: USP-12345'
        self.assertEquals(str(self.delivery), expected)
