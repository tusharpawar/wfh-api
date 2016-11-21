from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model 


from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import(
	ListAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	CreateAPIView,
	DestroyAPIView,
	RetrieveDestroyAPIView
	)

#pagination
from .permissions import IsOwner
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from wfhapp.models import WFH

from .serializers import (
	WFHListSerializer,
	WFHDetailSerializer,
	WFHCreateUpdateSerializer,
	#TeamCreateUpdateSerializer,
	#UserSerializer
	#TeamMemberSerializer,
	)

class WFHListAPIView(ListAPIView):
	serializer_class = WFHListSerializer
	filter_backends=[SearchFilter]
	permission_classes = [IsAuthenticated]
	#search_fields = ["teamMember.user__username","user__first_name","teamName","designation","grade"]
	#pagination_class
	def get_queryset(self,*args,**kwargs):
		queryset_list=WFH.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(subject__icontains=query)|
					Q(task__icontains=query)|
					Q(comments__icontains=query)#|
					#Q(user__username__icontains=query) |
					#Q(user__first_name__icontains=query) |
					#Q(user__last_name__icontains=query)
					).distinct()
		return queryset_list

class WFHDetailAPIView(RetrieveAPIView):
	queryset = WFH.objects.all()
	serializer_class = WFHDetailSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'id'

class WFHUpdateAPIView(RetrieveUpdateAPIView):
	queryset = WFH.objects.all()
	serializer_class = WFHCreateUpdateSerializer
	permission_classes = [IsOwner]
	lookup_field = 'id'
	#send_email_confirmation

class WFHDeleteAPIView(RetrieveDestroyAPIView):
	queryset = WFH.objects.all()
	serializer_class = WFHDetailSerializer
	permission_classes = [IsOwner]
	allowed_methods = ['GET','DELETE']
	lookup_field = 'id'
