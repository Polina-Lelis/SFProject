from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

from faceapp.views import SortView, AnswerView
from faceapp.models import Photo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SortView.as_view()),
    path('result/<int:pk>', AnswerView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


