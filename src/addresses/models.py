from django.db import models

from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    address_type  = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city  = models.CharField(max_length=120, null=True, blank=True)
    country  = models.CharField(max_length=120, default= "Philippines")
    state  = models.CharField(max_length=120, null=True, blank=True)
    postal_code  = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.billing_profile}"

    def get_address(self):
        address_2 = self.address_line_2 or ""
        return f"{self.address_line_1}\n{address_2}\n{self.state}, {self.postal_code}\n{self.country}"
