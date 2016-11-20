from django.conf.urls import url
from django.contrib import admin

from .views import (
	WFHListAPIView,
	WFHDetailAPIView,
	WFHUpdateAPIView,
	WFHDeleteAPIView,
	#CreateUserAPIView,
	#CreateTeamMemberAPIView,
	)

urlpatterns = [
	url(r'^$', WFHListAPIView.as_view(), name='list'),
	url(r'^(?P<id>[\d-]+)/$', WFHDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<id>[\d-]+)/edit/$', WFHUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<id>[\d-]+)/delete/$', WFHDeleteAPIView.as_view(), name='delete'),
	#url(r'^$', CreateTeamMemberAPIView.as_view(), name='register'),
]