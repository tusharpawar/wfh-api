from rest_framework.serializers import(
	ModelSerializer,
	SerializerMethodField,
	HyperlinkedIdentityField,
	)

from team.models import TeamMember


'''
user = models.OneToOneField(User, on_delete=models.CASCADE)
	teamName = models.CharField(max_length=120)
	designation = models.CharField(max_length=150,blank=True)
	grade = models.CharField(max_length=50,blank=True)
	email = models.EmailField(max_length=50)
	phone = models.IntegerField(max_length=10, unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])  

'''


class TeamListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name="team-api:detail",
		lookup_field="id"
		)
	user=SerializerMethodField()
	class Meta:
		model=TeamMember
		fields=[
			'id',
			'user',
			'designation',
			'email',
			'url',
		]
	def get_user(self,obj):
		return obj.user.username

class TeamDetailSerializer(ModelSerializer):
	user=SerializerMethodField()
	class Meta:
		model = TeamMember
		fields = [
			'id',
			'user',
			'teamName',
			'designation',
			'grade',
			'email',
			'phone',
		]
	def get_user(self,obj):
		return obj.user.username
