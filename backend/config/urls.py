from django.contrib import admin
from django.urls import path

from ingestion.views import SAPUploadView

from review.views import (
    ReviewListView,
    ApproveRecordView,
    RejectRecordView,
    LockRecordView
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path(
        'api/upload/sap/',
        SAPUploadView.as_view()
    ),

    path(
        'api/review/',
        ReviewListView.as_view()
    ),

    path(
        'api/review/<int:pk>/approve/',
        ApproveRecordView.as_view()
    ),

    path(
        'api/review/<int:pk>/reject/',
        RejectRecordView.as_view()
    ),

    path(
        'api/review/<int:pk>/lock/',
        LockRecordView.as_view()
    ),

]