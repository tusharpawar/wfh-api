from django.contrib.auth import get_user_model 
from django.contrib.auth.models import User


from rest_framework.serializers import(
	ModelSerializer,
	SerializerMethodField,
	HyperlinkedIdentityField,
	CharField,
	)

from team.models import TeamMember

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

class TeamCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = TeamMember
		fields =[
			'teamName',
			'designation',
			'grade',
			'email',
			'phone',
		]


UserModel = get_user_model()

'''
class UserSerializer(ModelSerializer):

    password = CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = UserModel

'''
'''
username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    password = serializers.CharField(source='user.password')
    ban_status = serializers.Field(source='ban_status')

    class Meta:
        model = AppUser
        fields = ('id', 'username', 'email', 'password', 'ban_status')

    def restore_object(self, attrs, instance=None):
        """
        Given a dictionary of deserialized field values, either update
        an existing model instance, or create a new model instance.
        """
        if instance is not None:
            instance.user.email = attrs.get('user.email', instance.user.email)
            instance.ban_status = attrs.get('ban_status', instance.ban_status)
            instance.user.password = attrs.get('user.password', instance.user.password)
            return instance

        user = User.objects.create_user(username=attrs.get('user.username'), email= attrs.get('user.email'), password=attrs.get('user.password'))
        return AppUser(user=user)
'''

class TeamMemberSerializer(ModelSerializer):
	username = CharField(source='user.username')
	password = CharField(source='user.password')
	user=SerializerMethodField()

	class Meta:
		model = TeamMember
		fields =[
			'id',
			'user',
			'username',
			'email',
			'password',
			'teamName',
			'designation',
			'grade',
			'phone',
		]
	def get_user(self,obj):
		return obj.user.username

	def update(self, instance, validated_data):
		instance.user.username = validated_data.get('user.username',instance.user.username)
		instance.user.password = validated_data.get('user.password',instance.user.password)
		instance.email = validated_data.get('email',instance.email)
		instance.teamName = validated_data.get('teamName',instance.teamName)
		instance.designation = validated_data.get('designation',instance.designation)
		instance.grade = validated_data.get('grade',instance.grade)
		instance.phone = validated_data.get('phone',instance.phone)
		instance.save()
		return instance

	def create(self,instance, validated_data):
		user = User.objects.create_user(username='default_username4',password=validated_data.get('user.password'))
		email = validated_data.get('email',instance.email)
		teamName = validated_data.get('teamName',instance.teamName)
		designation = validated_data.get('designation',instance.designation)
		grade = validated_data.get('grade',instance.grade)
		phone = validated_data.get('phone',instance.phone)
		return TeamMember(user=user,email=email,teamName=teamName,designation=designation,grade=grade,phone=phone)



