from rest_framework.views import APIView
from rest_framework.response import Response

from normalization.models import NormalizedRecord
from audit.models import AuditLog


class ReviewListView(APIView):

    def get(self, request):

        records = list(
            NormalizedRecord.objects.values()
        )

        return Response(records)


class ApproveRecordView(APIView):

    def post(self, request, pk):

        record = NormalizedRecord.objects.get(id=pk)

        previous_data = {
            'review_status': record.review_status
        }

        record.review_status = 'approved'

        record.save()

        AuditLog.objects.create(
            record=record,
            action='approved record',
            previous_value=previous_data,
            new_value={
                'review_status': 'approved'
            },
            changed_by='analyst'
        )

        return Response({
            'message': 'Record approved'
        })


class RejectRecordView(APIView):

    def post(self, request, pk):

        record = NormalizedRecord.objects.get(id=pk)

        previous_data = {
            'review_status': record.review_status
        }

        record.review_status = 'rejected'

        record.save()

        AuditLog.objects.create(
            record=record,
            action='rejected record',
            previous_value=previous_data,
            new_value={
                'review_status': 'rejected'
            },
            changed_by='analyst'
        )

        return Response({
            'message': 'Record rejected'
        })


class LockRecordView(APIView):

    def post(self, request, pk):

        record = NormalizedRecord.objects.get(id=pk)

        record.locked_for_audit = True

        record.review_status = 'locked'

        record.save()

        AuditLog.objects.create(
            record=record,
            action='locked for audit',
            changed_by='analyst'
        )

        return Response({
            'message': 'Record locked'
        })