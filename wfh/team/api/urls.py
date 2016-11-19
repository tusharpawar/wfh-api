from django.conf.urls import url
from django.contrib import admin

from .views import (
	TeamListAPIView,
	TeamDetailAPIView,
	)

urlpatterns = [
	url(r'^$', TeamListAPIView.as_view(), name='list'),
	url(r'^(?P<id>[\d-]+)/$', TeamDetailAPIView.as_view(), name='detail'),
]