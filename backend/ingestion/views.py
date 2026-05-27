import csv
import io

from rest_framework.views import APIView
from rest_framework.response import Response

from tenants.models import Tenant

from ingestion.models import DataSource
from ingestion.models import RawRecord

from normalization.models import NormalizedRecord

from normalization.services import normalize_unit
from normalization.scope_mapper import determine_scope
from normalization.anomaly import is_suspicious


class SAPUploadView(APIView):

    def post(self, request):

        file = request.FILES['file']

        decoded_file = file.read().decode('utf-8')

        io_string = io.StringIO(decoded_file)

        reader = csv.DictReader(io_string)

        tenant = Tenant.objects.first()

        if not tenant:
            tenant = Tenant.objects.create(
                name='Demo Company'
            )

        source = DataSource.objects.create(
            tenant=tenant,
            source_type='sap',
            source_name=file.name,
            uploaded_by='admin'
        )

        for row in reader:

            raw_record = RawRecord.objects.create(
                source=source,
                raw_payload=row,
                ingest_status='success'
            )

            quantity = float(row.get('Quantity', 0))

            unit = row.get('Unit', '')

            normalized_quantity, normalized_unit = normalize_unit(
                quantity,
                unit
            )

            category = row.get('Fuel Type', 'fuel')

            scope = determine_scope(category)

            suspicious = is_suspicious(
                quantity,
                unit
            )

            NormalizedRecord.objects.create(
                tenant=tenant,

                category=category,

                scope=scope,

                activity_type='fuel consumption',

                quantity=normalized_quantity,

                normalized_unit=normalized_unit,

                original_quantity=quantity,

                original_unit=unit,

                source_record=raw_record,

                suspicious_flag=suspicious
            )

        return Response({
            'message': 'SAP file uploaded successfully'
        })