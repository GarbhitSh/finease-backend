from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from chequeml import views

urlpatterns = [
    path("",views.simple_upload,name='Cheque'),
   #path("chequeupdate",views.chequeupdate,name='chequeupdate'),
    
    # Project url patterns...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)