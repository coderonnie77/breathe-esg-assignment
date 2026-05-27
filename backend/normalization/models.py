from django.db import models

from tenants.models import Tenant
from ingestion.models import RawRecord


class NormalizedRecord(models.Model):

    REVIEW_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('locked', 'Locked')
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    category = models.CharField(max_length=100)

    scope = models.CharField(max_length=20)

    activity_type = models.CharField(max_length=255)

    quantity = models.FloatField()

    normalized_unit = models.CharField(max_length=50)

    original_quantity = models.FloatField()

    original_unit = models.CharField(max_length=50)

    source_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    suspicious_flag = models.BooleanField(default=False)

    review_status = models.CharField(
        max_length=50,
        choices=REVIEW_STATUS,
        default='pending'
    )

    locked_for_audit = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category} - {self.quantity}'