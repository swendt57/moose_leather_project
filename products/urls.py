from django.urls import path
from .views import get_retail_items, get_consignment_items, upload_consigned_item, submit_consigned_item
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', get_retail_items, name='retail'),
    path('consigned', get_consignment_items, name='consigned'),
    path('upload_consigned', upload_consigned_item, name='upload_consigned'),
    path('submit_consigned', submit_consigned_item, name='submit_consigned'),
] \

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
