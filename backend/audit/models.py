from django.db import models

from normalization.models import NormalizedRecord


class AuditLog(models.Model):

    record = models.ForeignKey(
        NormalizedRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=255)

    previous_value = models.JSONField(
        null=True,
        blank=True
    )

    new_value = models.JSONField(
        null=True,
        blank=True
    )

    changed_by = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action