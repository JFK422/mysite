from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views, models

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=models.post.objects.all().order_by("-date"), template_name="contributions/contribution.html"), name = 'contSite'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=models.post, template_name="contributions/cntDetail.html"))
]