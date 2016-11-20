from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message = "You have no rights to change details of other User"

	def has_object_permission(self,request,view,obj):
		if obj.user == request.user :
			print "yes"
		return obj.user == request.user