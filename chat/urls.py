from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index_view, name='chat-index'),
    path('<str:room_name>/', views.room_view, name='chat-room'),
    path('image/send',views.Imagesend,name='imagesend'),
    # path('upload/img/',views.UploadImage,name='image_upload')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

