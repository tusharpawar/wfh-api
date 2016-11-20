from django.conf.urls import url
from django.contrib import admin

from .views import (
	TeamListAPIView,
	TeamDetailAPIView,
	TeamUpdateAPIView,
	#CreateUserAPIView,
	CreateTeamMemberAPIView,
	)

urlpatterns = [
	url(r'^$', TeamListAPIView.as_view(), name='list'),
	url(r'^(?P<id>[\d-]+)/$', TeamDetailAPIView.as_view(), name='detail'),
	url(r'^(?P<id>[\d-]+)/edit/$', TeamUpdateAPIView.as_view(), name='update'),
	#url(r'^$', CreateTeamMemberAPIView.as_view(), name='register'),
]