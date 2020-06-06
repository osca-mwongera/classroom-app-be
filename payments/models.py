from datetime import timedelta

from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from accounts.models import Profile
from properties.models import Property
from django.shortcuts import reverse


class LNMOnline(models.Model):
    checkout_request_id = models.CharField(max_length=99)
    merchant_request_id = models.CharField(max_length=99)
    result_code = models.IntegerField()
    result_desc = models.CharField(max_length=120)

    amount = models.FloatField(null=True)
    mpesa_receipt_number = models.CharField(max_length=18, null=True)
    phone_number = models.CharField(max_length=13, null=True)
    timestamp = models.DateTimeField(null=True)

    class Meta:
        ordering = ('timestamp',)
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        if self.mpesa_receipt_number:
            return 'Transaction %s' % self.mpesa_receipt_number
        return 'Transaction %s' % self.checkout_request_id


class PaymentType(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    amount = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s Payment' % self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PaymentType, self).save(*args, **kwargs)


class Payment(models.Model):
    payment_type = models.ForeignKey(PaymentType, on_delete=models.DO_NOTHING)
    transaction = models.OneToOneField(LNMOnline, null=True, on_delete=models.SET_NULL)
    property_item = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    client = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    merchant_request_id = models.CharField(max_length=99, null=True)
    checkout_request_id = models.CharField(max_length=99, null=True)

    valid_until = models.DateTimeField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, default='Pending')

    class Meta:
        ordering = ['-timestamp']
        get_latest_by = 'timestamp'

    def __str__(self):
        return '%s for %s' %(self.payment_type, self.client.fullname)

    @property
    def mpesa_amount(self):
        if self.transaction:
            return self.transaction.amount
        return None

    @property
    def receipt_number(self):
        if self.transaction:
            return self.transaction.mpesa_receipt_number
        return None

    @property
    def is_active(self):
        if self.valid_until:
            if timezone.now() < self.valid_until:
                return True
        return False

    @property
    def property_name(self):
        return self.property_item.name    

    def get_absolute_url(self):
        return reverse('payments:payment_sent')

    def save(self, *args, **kwargs):
        if self.transaction:
            self.valid_until = self.transaction.timestamp + timedelta(hours=3)
            if self.transaction.result_code == 0:
                self.status = 'Complete'
            else:
                self.status = 'Failed'
        super(Payment, self).save(*args, **kwargs)
