from django.db.models import Q

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import(
	ListAPIView,
	RetrieveAPIView,
	)

#pagination
#permission

from team.models import TeamMember

from .serializers import (
	TeamListSerializer,
	TeamDetailSerializer,
	)

class TeamListAPIView(ListAPIView):
	serializer_class = TeamListSerializer
	filter_backends=[SearchFilter]
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
	lookup_field = 'id'