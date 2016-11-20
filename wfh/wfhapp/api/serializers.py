from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User


from rest_framework.serializers import(
	ModelSerializer,
	SerializerMethodField,
	HyperlinkedIdentityField,
	CharField,
	)

from wfhapp.models import WFH
'''
onDate = models.DateField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	subject = models.CharField(max_length=150,default="<WFH:Today>",blank=True)
	tasks = models.TextField()
	comments = models.CharField(max_length=120,blank=True)
'''

class WFHListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name="wfh-api:detail",
		lookup_field="id"
		)
	user=SerializerMethodField()
	class Meta:
		model=WFH
		fields=[
			'id',
			'user',
			'onDate',
			'url',
		]
	def get_user(self,obj):
		return obj.teamMember.user.username

class WFHDetailSerializer(ModelSerializer):
	user=SerializerMethodField()
	class Meta:
		model = WFH
		fields = [
			'id',
			'user',
			'onDate',
			'updated',
			'subject',
			'tasks',
			'comments',
		]
	def get_user(self,obj):
		return obj.teamMember.user.username

class WFHCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = WFH
		fields = [
			'onDate',
			'subject',
			'tasks',
			'comments',
		]