from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views, models

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=models.pic.objects.all().order_by("-postDate"), template_name="photos/photos.html"), name = 'photoSite'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=models.pic, template_name="photos/lightbox.html"))
]