from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsOwner(BasePermission):
	message = "You have no rights to change WFH of other TeamMember"

	def has_object_permission(self,request,view,obj):
		if request.method in SAFE_METHODS:
			return True
		return obj.teamMember.user == request.user