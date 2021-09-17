from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
 url(r'^$', views.first_view, name='first_view'),
 url(r'^dface/$', views.dface, name='dface'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
