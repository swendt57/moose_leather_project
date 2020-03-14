from django.urls import path
from .views import get_retail_items, get_consignment_items, render_consigned_item_upload, submit_consigned_item, get_item_details
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', get_retail_items, name='retail'),
    path('consigned', get_consignment_items, name='consigned'),
    path('upload_consigned', render_consigned_item_upload, name='upload_consigned'),
    path('submit_consigned', submit_consigned_item, name='submit_consigned'),
    path('details', get_item_details, name='details')
]

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
