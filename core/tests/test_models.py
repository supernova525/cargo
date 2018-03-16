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


class PrealertTest(TestCase):
    def setUp(self):
        self.prealert = mommy.make(Prealert, tracking="12345")

    def test_str(self):
        expected = "Prealert: 00001"
        self.assertEquals(str(self.prealert), expected)

class ShipperTest(TestCase):
    def setUp(self):
        self.shipper = mommy.make(Shipper, name="UPS")
    
    def test_str(self):
        self.assertEquals(str(self.shipper), "UPS")

