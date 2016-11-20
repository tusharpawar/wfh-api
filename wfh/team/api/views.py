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
	)

#pagination
from .permissions import IsOwner
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from team.models import TeamMember

from .serializers import (
	TeamListSerializer,
	TeamDetailSerializer,
	TeamCreateUpdateSerializer,
	#UserSerializer
	TeamMemberSerializer,
	)

class TeamListAPIView(ListAPIView):
	serializer_class = TeamListSerializer
	filter_backends=[SearchFilter]
	permission_classes = [IsAdminUser]
	search_fields = ["user__username","user__first_name","teamName","designation","grade"]
	#pagination_class
	def get_queryset(self,*args,**kwargs):
		queryset_list=TeamMember.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(designation__icontains=query)|
					Q(grade__icontains=query)|
					Q(teamName__icontains=query)|
					Q(user__username__icontains=query) |
					Q(user__first_name__icontains=query) |
					Q(user__last_name__icontains=query)
					).distinct()
		return queryset_list

class TeamDetailAPIView(RetrieveAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamDetailSerializer
	permission_classes = [IsAuthenticated]
	lookup_field = 'id'

class TeamUpdateAPIView(RetrieveUpdateAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamCreateUpdateSerializer
	lookup_field = 'id'
	permission_classes = [IsOwner]

	def perform_update(self,serializer):
		serializer.save(user=self.request.user)

class TeamCreateAPIView(CreateAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamCreateUpdateSerializer

	def perform_create(self,serializer):
		user = User.objects.create_user()
'''
class CreateUserAPIView(CreateAPIView):

    model = get_user_model()
    permission_classes = [AllowAny] # Or anon users can't register
    serializer_class = UserSerializer
'''
class CreateTeamMemberAPIView(CreateAPIView):
	queryset = TeamMember.objects.all()
	serializer_class = TeamMemberSerializer
	permission_classes = [AllowAny]